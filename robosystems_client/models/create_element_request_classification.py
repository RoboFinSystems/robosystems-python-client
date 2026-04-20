from enum import Enum


class CreateElementRequestClassification(str, Enum):
  ASSET = "asset"
  CASHFLOW = "cashflow"
  EQUITY = "equity"
  INFLOW = "inflow"
  LIABILITY = "liability"
  OUTFLOW = "outflow"

  def __str__(self) -> str:
    return str(self.value)
