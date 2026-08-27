from enum import Enum


class ResolveReconcilingItemRequestDispositionType0(str, Enum):
  ACKNOWLEDGE = "acknowledge"
  CATCH_UP = "catch_up"
  RESTATE = "restate"

  def __str__(self) -> str:
    return str(self.value)
