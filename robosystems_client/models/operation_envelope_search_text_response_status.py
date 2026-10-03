from enum import Enum


class OperationEnvelopeSearchTextResponseStatus(str, Enum):
  COMPLETED = "completed"
  FAILED = "failed"
  PENDING = "pending"

  def __str__(self) -> str:
    return str(self.value)
