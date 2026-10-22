from enum import Enum


class LoanTermsRequestPaymentFrequency(str, Enum):
  ANNUAL = "annual"
  AT_MATURITY = "at_maturity"
  MONTHLY = "monthly"
  QUARTERLY = "quarterly"

  def __str__(self) -> str:
    return str(self.value)
