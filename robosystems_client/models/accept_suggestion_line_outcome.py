from enum import Enum


class AcceptSuggestionLineOutcome(str, Enum):
  CLASSIFIED = "classified"
  COMMITTED = "committed"
  SKIPPED = "skipped"

  def __str__(self) -> str:
    return str(self.value)
