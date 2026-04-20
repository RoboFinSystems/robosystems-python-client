from enum import Enum


class CreateElementRequestClassification(str, Enum):
  ASSET = "asset"
  COMPREHENSIVEINCOME = "comprehensiveIncome"
  CONTRAASSET = "contraAsset"
  CONTRAEQUITY = "contraEquity"
  CONTRALIABILITY = "contraLiability"
  DISTRIBUTIONTOOWNERS = "distributionToOwners"
  EQUITY = "equity"
  EXPENSE = "expense"
  EXPENSEREVERSAL = "expenseReversal"
  GAIN = "gain"
  INVESTMENTBYOWNERS = "investmentByOwners"
  LIABILITY = "liability"
  LOSS = "loss"
  REVENUE = "revenue"
  TEMPORARYEQUITY = "temporaryEquity"

  def __str__(self) -> str:
    return str(self.value)
