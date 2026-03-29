from enum import Enum


class CreateStructureRequestStructureType(str, Enum):
  BALANCE_SHEET = "balance_sheet"
  CASH_FLOW_STATEMENT = "cash_flow_statement"
  CHART_OF_ACCOUNTS = "chart_of_accounts"
  COA_MAPPING = "coa_mapping"
  CUSTOM = "custom"
  EQUITY_STATEMENT = "equity_statement"
  INCOME_STATEMENT = "income_statement"

  def __str__(self) -> str:
    return str(self.value)
