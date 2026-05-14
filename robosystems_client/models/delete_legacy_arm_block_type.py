from enum import Enum


class DeleteLegacyArmBlockType(str, Enum):
  BALANCE_SHEET = "balance_sheet"
  CASH_FLOW_STATEMENT = "cash_flow_statement"
  COMPREHENSIVE_INCOME = "comprehensive_income"
  EQUITY_STATEMENT = "equity_statement"
  INCOME_STATEMENT = "income_statement"
  METRIC = "metric"

  def __str__(self) -> str:
    return str(self.value)
