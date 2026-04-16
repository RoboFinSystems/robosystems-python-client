from enum import Enum


class UpdateElementRequestBalanceTypeType0(str, Enum):
  CREDIT = "credit"
  DEBIT = "debit"

  def __str__(self) -> str:
    return str(self.value)
