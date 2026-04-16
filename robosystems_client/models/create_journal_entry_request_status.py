from enum import Enum


class CreateJournalEntryRequestStatus(str, Enum):
  DRAFT = "draft"
  POSTED = "posted"

  def __str__(self) -> str:
    return str(self.value)
