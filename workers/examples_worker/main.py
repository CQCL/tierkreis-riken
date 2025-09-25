from pathlib import Path
from sys import argv
from tierkreis import Worker
from pytket._tket.circuit import Circuit
from pytket.backends.backendresult import BackendResult
from pytket.qasm.qasm import circuit_from_qasm, circuit_to_qasm_str


import ast
import re
from pytket._tket.unit_id import Bit
from pytket.utils.outcomearray import OutcomeArray


worker = Worker("examples_worker")


@worker.task()
def example_circuit_list() -> list[Circuit]:
    circ1 = Circuit(4)
    circ1.X(0)
    circ1.CX(1, 3)
    circ1.Z(3)

    # circ2 = circuit_from_qasm(Path(__file__).parent / "circuit.qasm")

    return [circ1]


@worker.task()
def ghz(x: int) -> list[Circuit]:
    circ1 = Circuit(2)
    circ1.H(0)
    circ1.CX(0, 1)
    circ1.measure_all()
    return [circ1 for _ in range(x)]


@worker.task()
def to_qasm(circuit: Circuit) -> bytes:
    return circuit_to_qasm_str(circuit).encode()


@worker.task()
def parse_sqcsub_output(sqcsub_output: bytes) -> BackendResult:
    return parse_sqcsub_outputs(sqcsub_output.decode())


def parse_sqcsub_outputs(
    sqc_output: str,
) -> BackendResult:
    """Parse the sqsub backend result."""
    return parse_qsubmit(sqc_output)


def parse_qsubmit(input_str: str) -> BackendResult:
    blocks = re.findall(r"\{\s*\n(.*?)\n\s*\}", input_str, re.DOTALL)
    processed_data = [
        _parse_block(block) for block in blocks
    ]  # can block have multiple lines?
    readouts, all_bits_configs = zip(*processed_data)
    if len(set(all_bits_configs)) != 1:
        raise ValueError("Inconsistent bit configurations found in results.")
    return BackendResult(
        shots=OutcomeArray.from_readouts(readouts), c_bits=all_bits_configs[0]
    )


def _parse_block(line: str) -> tuple[list[int], tuple[Bit, ...]]:
    regname, bits_str = map(str.strip, line.split(":", 1))
    bits = [int(i) for i in ast.literal_eval(bits_str)]
    bit_register = [Bit(regname, i) for i in range(len(bits))]
    if not bit_register:
        return [], ()
    sorted_pairs = sorted(zip(bits, bit_register), key=lambda pair: str(pair[1]))
    sorted_readout, sorted_bits = zip(*sorted_pairs)
    return list(sorted_readout), sorted_bits


if __name__ == "__main__":
    worker.app(argv)
