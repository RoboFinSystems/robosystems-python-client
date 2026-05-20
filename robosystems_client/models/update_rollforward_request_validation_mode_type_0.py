from enum import Enum


class UpdateRollforwardRequestValidationModeType0(str, Enum):
  RESIDUAL_AS_DEFAULT = "residual_as_default"
  STRICT = "strict"
  WARN_ONLY = "warn_only"

  def __str__(self) -> str:
    return str(self.value)
