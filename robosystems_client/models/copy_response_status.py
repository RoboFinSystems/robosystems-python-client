from enum import Enum


class CopyResponseStatus(str, Enum):
  ACCEPTED = "accepted"
  COMPLETED = "completed"
  FAILED = "failed"
  PARTIAL = "partial"

  def __str__(self) -> str:
    return str(self.value)
