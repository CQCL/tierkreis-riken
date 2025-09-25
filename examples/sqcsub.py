from typing import Literal
from uuid import UUID
from tierkreis import run_graph
from tierkreis.builder import GraphBuilder
from tierkreis.models import EmptyModel, TKR
from tierkreis.controller.data.models import OpaqueType
from tierkreis.storage import FileStorage, read_outputs  # type: ignore
from tierkreis.executor import ShellExecutor, UvExecutor, MultipleExecutor
from tierkreis.controller.data.types import ptype_from_bytes
from pytket.backends.backendresult import BackendResult

from workers.consts import WORKERS_DIR
from workers.examples_worker.stubs import to_qasm, ghz, parse_sqcsub_output
from workers.tkr_sqcsub.stubs import submit


# BackendResult = Literal[OpaqueType["pytket.backends.backendresult.BackendResult"]]
Circuit = OpaqueType["pytket._tket.circuit.Circuit"]
storage = FileStorage(UUID(int=106), do_cleanup=True)
uv_executor = UvExecutor(WORKERS_DIR, storage.logs_path)
shell_executor = ShellExecutor(WORKERS_DIR, storage.logs_path.parent, timeout=300)  # 5m
executor = MultipleExecutor(
    uv_executor, {"shell": shell_executor}, {"tkr_sqcsub": "shell"}
)


def convert_and_submit() -> GraphBuilder[TKR[Circuit], TKR[BackendResult]]:
    g = GraphBuilder(TKR[Circuit], TKR[BackendResult])
    circuit_bytes = g.task(to_qasm(g.inputs))
    res = g.task(
        submit(
            g.const(2),
            g.const(10),
            circuit_bytes,
            g.const("qasm"),
            g.const("raw"),
            g.const("reimei-simulator"),
        ),
    )
    out = g.task(parse_sqcsub_output(res))
    g.outputs(out)
    return g


def graph():
    g = GraphBuilder(TKR[int], TKR[list[BackendResult]])  # type: ignore
    circuits = g.task(ghz(g.inputs))
    results = g.map(
        convert_and_submit(),
        circuits,
    )
    g.outputs(results)
    return g


if __name__ == "__main__":
    run_graph(
        storage, executor, graph().get_data(), {"value": 2}, polling_interval_seconds=1
    )

    for out in read_outputs(graph().get_data(), storage):  # type: ignore
        print(BackendResult.from_dict(out).get_counts())
