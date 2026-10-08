from enum import Enum


class SetWritePolicyRequestWritePolicy(str, Enum):
  QB_AUTHORITATIVE = "qb_authoritative"
  SHADOW = "shadow"

  def __str__(self) -> str:
    return str(self.value)
