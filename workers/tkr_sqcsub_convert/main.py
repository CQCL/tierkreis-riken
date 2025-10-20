from sys import argv
from typing import NamedTuple

from pytket._tket.circuit import Circuit
from pytket.extensions.qiskit.qiskit_convert import tk_to_qiskit
from pytket.qasm.qasm import circuit_to_qasm_str
from quantinuum_schemas.models.backend_config import (
    BackendConfig,
    IBMQConfig,
    QuantinuumConfig,
)
import qiskit.qasm3  # type: ignore
from tierkreis import Worker
from tierkreis.worker.worker import TierkreisWorkerError
from tierkreis.models import portmapping

worker = Worker("tkr_sqcsub_convert")


@portmapping
class SubmissionData(NamedTuple):
    qasm: bytes
    qpu: str


@worker.task()
def prepare_submission(config: BackendConfig, circuit: Circuit) -> SubmissionData:
    match config:
        case IBMQConfig():
            qc = tk_to_qiskit(circuit)
            qasm = qiskit.qasm3.dumps(qc)  # type: ignore
            return SubmissionData(qasm.encode(), "ibm_kobe")
        case QuantinuumConfig():
            return SubmissionData(circuit_to_qasm_str(circuit).encode(), "reimei")
        case _:
            raise TierkreisWorkerError(f"Unsupported config {config}")


if __name__ == "__main__":
    worker.app(argv)
