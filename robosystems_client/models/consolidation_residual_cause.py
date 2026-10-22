from enum import Enum


class ConsolidationResidualCause(str, Enum):
  PRE_ACQUISITION = "pre_acquisition"
  UNEXPLAINED = "unexplained"

  def __str__(self) -> str:
    return str(self.value)
