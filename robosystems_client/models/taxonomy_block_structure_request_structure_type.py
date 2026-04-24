from enum import Enum


class TaxonomyBlockStructureRequestStructureType(str, Enum):
  BALANCE_SHEET = "balance_sheet"
  CASH_FLOW_STATEMENT = "cash_flow_statement"
  CHART_OF_ACCOUNTS = "chart_of_accounts"
  COA_MAPPING = "coa_mapping"
  CUSTOM = "custom"
  EQUITY_STATEMENT = "equity_statement"
  INCOME_STATEMENT = "income_statement"
  METRIC = "metric"
  POLICY = "policy"
  RECONCILIATION = "reconciliation"
  ROLLFORWARD = "rollforward"
  SCHEDULE = "schedule"

  def __str__(self) -> str:
    return str(self.value)
