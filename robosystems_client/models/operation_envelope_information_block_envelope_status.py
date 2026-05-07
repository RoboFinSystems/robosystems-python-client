from enum import Enum


class OperationEnvelopeInformationBlockEnvelopeStatus(str, Enum):
  COMPLETED = "completed"
  FAILED = "failed"
  PENDING = "pending"

  def __str__(self) -> str:
    return str(self.value)
