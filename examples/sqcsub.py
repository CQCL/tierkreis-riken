from typing import Literal
from uuid import UUID
from tierkreis import run_graph
from tierkreis.builder import GraphBuilder
from tierkreis.models import EmptyModel, TKR
from tierkreis.controller.data.models import OpaqueType
from tierkreis.storage import FileStorage, read_outputs  # type: ignore
from tierkreis.executor import ShellExecutor, UvExecutor, MultipleExecutor

from workers.consts import WORKERS_DIR
from workers.examples_worker.stubs import example_circuit_list, to_qasm
from workers.tkr_sqcsub.stubs import submit

BackendResult = Literal[OpaqueType["pytket.backends.backendresult.BackendResult"]]
Circuit = OpaqueType["pytket._tket.circuit.Circuit"]
storage = FileStorage(UUID(int=106), do_cleanup=True)
uv_executor = UvExecutor(WORKERS_DIR, storage.logs_path)
shell_executor = ShellExecutor(WORKERS_DIR, storage.logs_path.parent)
executor = MultipleExecutor(
    uv_executor, {"shell": shell_executor}, {"tkr_sqcsub": "shell"}
)


def convert_and_submit() -> GraphBuilder[TKR[Circuit], TKR[bytes]]:
    g = GraphBuilder(TKR[Circuit], submit.out())
    circuit_bytes = g.task(to_qasm(g.inputs))
    out = g.task(
        submit(
            g.const(4),
            g.const(30),
            circuit_bytes,
            g.const("qasm"),
            g.const("raw"),
            g.const("reimei-simulator"),
        ),
    )
    g.outputs(out)
    return g


def graph():
    g = GraphBuilder(EmptyModel, TKR[list[bytes]])  # type: ignore
    circuits = g.task(example_circuit_list())
    results = g.map(
        convert_and_submit(),
        circuits,
    )
    g.outputs(results)
    return g


if __name__ == "__main__":
    run_graph(storage, executor, graph().get_data(), {}, polling_interval_seconds=0.1)
    print(len(read_outputs(graph().get_data(), storage)))  # type: ignore
