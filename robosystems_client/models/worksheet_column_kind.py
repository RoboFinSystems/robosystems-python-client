from enum import Enum


class WorksheetColumnKind(str, Enum):
  ADJUSTMENTS = "adjustments"
  COMBINED = "combined"
  CONSOLIDATED = "consolidated"
  MEMBER = "member"
  NOT_SUMMED = "not_summed"

  def __str__(self) -> str:
    return str(self.value)
