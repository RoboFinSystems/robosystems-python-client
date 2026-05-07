from enum import Enum


class UpdateLegacyArmBlockType(str, Enum):
  BALANCE_SHEET = "balance_sheet"
  CASH_FLOW_STATEMENT = "cash_flow_statement"
  EQUITY_STATEMENT = "equity_statement"
  INCOME_STATEMENT = "income_statement"
  METRIC = "metric"

  def __str__(self) -> str:
    return str(self.value)
