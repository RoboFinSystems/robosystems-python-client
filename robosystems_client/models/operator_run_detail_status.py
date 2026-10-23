from enum import Enum


class OperatorRunDetailStatus(str, Enum):
  CANCELLED = "cancelled"
  COMPLETED = "completed"
  FAILED = "failed"

  def __str__(self) -> str:
    return str(self.value)
