from enum import Enum


class ScheduleLegRequestAmountSource(str, Enum):
  INTEREST = "interest"
  INTEREST_PAID = "interest_paid"
  PAYMENT = "payment"
  PRINCIPAL = "principal"

  def __str__(self) -> str:
    return str(self.value)
