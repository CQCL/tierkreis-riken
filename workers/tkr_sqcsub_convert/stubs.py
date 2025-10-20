"""Code generated from tkr_sqcsub_convert namespace. Please do not edit."""

from typing import NamedTuple, Union
from tierkreis.controller.data.models import TKR, OpaqueType


class SubmissionData(NamedTuple):
    qasm: TKR[bytes]  # noqa: F821 # fmt: skip
    qpu: TKR[str]  # noqa: F821 # fmt: skip


class prepare_submission(NamedTuple):
    config: TKR[Union[OpaqueType["quantinuum_schemas.models.backend_config.AerConfig"], OpaqueType["quantinuum_schemas.models.backend_config.AerStateConfig"], OpaqueType["quantinuum_schemas.models.backend_config.AerUnitaryConfig"], OpaqueType["quantinuum_schemas.models.backend_config.BraketConfig"], OpaqueType["quantinuum_schemas.models.backend_config.QuantinuumConfig"], OpaqueType["quantinuum_schemas.models.backend_config.IBMQConfig"], OpaqueType["quantinuum_schemas.models.backend_config.IBMQEmulatorConfig"], OpaqueType["quantinuum_schemas.models.backend_config.QulacsConfig"], OpaqueType["quantinuum_schemas.models.backend_config.SeleneConfig"], OpaqueType["quantinuum_schemas.models.backend_config.SelenePlusConfig"]]]  # noqa: F821 # fmt: skip
    circuit: TKR[OpaqueType["pytket._tket.circuit.Circuit"]]  # noqa: F821 # fmt: skip

    @staticmethod
    def out() -> type[SubmissionData]:  # noqa: F821 # fmt: skip
        return SubmissionData  # noqa: F821 # fmt: skip

    @property
    def namespace(self) -> str:
        return "tkr_sqcsub_convert"
