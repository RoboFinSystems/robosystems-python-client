from enum import Enum


class ConsolidationProposalAdjustmentKind(str, Enum):
  ACQUISITION = "acquisition"
  DECONSOLIDATION = "deconsolidation"
  ELIMINATION_INTERCOMPANY = "elimination_intercompany"
  ELIMINATION_INVESTMENT = "elimination_investment"
  ELIMINATION_UNREALIZED_PROFIT = "elimination_unrealized_profit"
  EQUITY_METHOD_DISTRIBUTION = "equity_method_distribution"
  EQUITY_METHOD_PICKUP = "equity_method_pickup"
  MANUAL = "manual"
  NCI_ALLOCATION = "nci_allocation"
  NCI_DISTRIBUTION = "nci_distribution"
  TRANSLATION = "translation"

  def __str__(self) -> str:
    return str(self.value)
