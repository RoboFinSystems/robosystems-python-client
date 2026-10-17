from enum import Enum


class UpdateEntityRequestConsolidationMethodType0(str, Enum):
  COST = "cost"
  EQUITY = "equity"
  FULL = "full"
  NONE = "none"

  def __str__(self) -> str:
    return str(self.value)
