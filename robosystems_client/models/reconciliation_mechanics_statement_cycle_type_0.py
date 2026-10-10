from enum import Enum


class ReconciliationMechanicsStatementCycleType0(str, Enum):
  ANNUAL = "annual"
  MONTHLY = "monthly"
  QUARTERLY = "quarterly"

  def __str__(self) -> str:
    return str(self.value)
