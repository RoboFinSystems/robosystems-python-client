from enum import Enum


class ScheduleRollForwardRowScope(str, Enum):
  HISTORICAL = "historical"
  IN_SCOPE = "in_scope"

  def __str__(self) -> str:
    return str(self.value)
