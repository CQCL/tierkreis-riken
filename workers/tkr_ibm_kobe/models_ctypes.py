import ctypes
from pathlib import Path


class CTranspileInformation(ctypes.Structure):
    _fields_ = [
        ("configuration", ctypes.c_char_p),
        ("properties", ctypes.c_char_p),
    ]


c_tkr_sqcsub = ctypes.CDLL(Path(__file__).parent / "build" / "tkr_sqcsub.so")
c_tkr_sqcsub.get_transpile_info.argtypes = ()
c_tkr_sqcsub.get_transpile_info.restype = CTranspileInformation
