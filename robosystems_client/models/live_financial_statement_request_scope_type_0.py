from enum import Enum


class LiveFinancialStatementRequestScopeType0(str, Enum):
  COMBINED = "combined"
  CONSOLIDATED = "consolidated"
  ENTITY = "entity"

  def __str__(self) -> str:
    return str(self.value)
