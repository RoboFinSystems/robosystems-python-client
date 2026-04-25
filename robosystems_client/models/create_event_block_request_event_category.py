from enum import Enum


class CreateEventBlockRequestEventCategory(str, Enum):
  ADJUSTMENT = "adjustment"
  APPROVAL = "approval"
  CONTROL = "control"
  FINANCING = "financing"
  INQUIRY = "inquiry"
  OTHER = "other"
  PAYROLL = "payroll"
  PURCHASE = "purchase"
  RECOGNITION = "recognition"
  RECONCILIATION = "reconciliation"
  SALES = "sales"
  TREASURY = "treasury"

  def __str__(self) -> str:
    return str(self.value)
