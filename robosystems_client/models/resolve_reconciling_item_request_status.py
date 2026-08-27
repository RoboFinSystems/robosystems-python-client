from enum import Enum


class ResolveReconcilingItemRequestStatus(str, Enum):
  DRAFT = "draft"
  POSTED = "posted"

  def __str__(self) -> str:
    return str(self.value)
