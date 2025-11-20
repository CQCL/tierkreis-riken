import qnexus as qnx
from pytket.circuit import OpType
from tierkreis.exceptions import TierkreisError


def qnexus_quantinuum_device_by_name(device_name: str) -> qnx.models.Device:
    devices = list(
        filter(
            lambda d: d.device_name == device_name,
            qnx.devices.get_all([qnx.models.IssuerEnum.QUANTINUUM]),
        )
    )
    if len(devices) != 1:
        raise TierkreisError(f"Could not find device '{device_name}'")
    return devices[0]


REIMEI_OPS = {
    OpType.Barrier,
    OpType.WASM,
    OpType.SetBits,
    OpType.CopyBits,
    OpType.RangePredicate,
    OpType.ExplicitPredicate,
    OpType.ExplicitModifier,
    OpType.MultiBit,
    OpType.Rz,
    OpType.TK2,
    OpType.Measure,
    OpType.Reset,
    OpType.PhasedX,
    OpType.ZZMax,
    OpType.ZZPhase,
    OpType.ClExpr,
    OpType.RNGSeed,
    OpType.RNGBound,
    OpType.RNGIndex,
    OpType.RNGNum,
    OpType.JobShotNum,
}
