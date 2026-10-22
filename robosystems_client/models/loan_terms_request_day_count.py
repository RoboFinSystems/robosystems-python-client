from enum import Enum


class LoanTermsRequestDayCount(str, Enum):
  ACTUAL360 = "actual/360"
  ACTUAL365 = "actual/365"
  VALUE_0 = "30/360"

  def __str__(self) -> str:
    return str(self.value)
