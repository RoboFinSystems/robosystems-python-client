from enum import Enum


class SetWritePolicyRequestWritePolicy(str, Enum):
  NATIVE = "native"
  QB_AUTHORITATIVE = "qb_authoritative"

  def __str__(self) -> str:
    return str(self.value)
