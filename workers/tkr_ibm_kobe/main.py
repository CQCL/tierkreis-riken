from tierkreis import Worker

from tkr_sqcsub import TranspileInfo, get_transpile_info_inner


worker = Worker("tkr_ibm_kobe")


@worker.task()
def get_transpile_info() -> TranspileInfo:
    return get_transpile_info_inner()
