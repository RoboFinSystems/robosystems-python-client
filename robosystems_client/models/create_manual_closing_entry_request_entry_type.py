from enum import Enum


class CreateManualClosingEntryRequestEntryType(str, Enum):
  ADJUSTING = "adjusting"
  CLOSING = "closing"
  REVERSING = "reversing"
  STANDARD = "standard"

  def __str__(self) -> str:
    return str(self.value)
