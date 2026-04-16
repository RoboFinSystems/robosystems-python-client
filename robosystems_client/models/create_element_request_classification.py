from enum import Enum


class CreateElementRequestClassification(str, Enum):
  ASSET = "asset"
  EQUITY = "equity"
  EXPENSE = "expense"
  LIABILITY = "liability"
  REVENUE = "revenue"

  def __str__(self) -> str:
    return str(self.value)
