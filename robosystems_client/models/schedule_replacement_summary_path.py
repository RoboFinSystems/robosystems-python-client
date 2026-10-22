from enum import Enum


class ScheduleReplacementSummaryPath(str, Enum):
  REBUILD = "rebuild"
  TERMINATE_AND_SUCCEED = "terminate_and_succeed"

  def __str__(self) -> str:
    return str(self.value)
