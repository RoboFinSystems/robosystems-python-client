from enum import Enum


class ReportSyncRequestStatus(str, Enum):
  FAILED = "failed"
  SUCCEEDED = "succeeded"

  def __str__(self) -> str:
    return str(self.value)
