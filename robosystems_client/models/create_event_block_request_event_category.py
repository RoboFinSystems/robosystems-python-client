from enum import Enum


class CreateEventBlockRequestEventCategory(str, Enum):
  ADJUSTMENT = "adjustment"
  FINANCING = "financing"
  OTHER = "other"
  PAYROLL = "payroll"
  PURCHASE = "purchase"
  RECOGNITION = "recognition"
  SALES = "sales"
  TREASURY = "treasury"

  def __str__(self) -> str:
    return str(self.value)
