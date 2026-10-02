from enum import Enum


class ReconciliationMechanicsScope(str, Enum):
  ACCOUNT = "account"
  LEDGER = "ledger"

  def __str__(self) -> str:
    return str(self.value)
