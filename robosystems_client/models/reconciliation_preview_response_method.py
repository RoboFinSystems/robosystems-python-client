from enum import Enum


class ReconciliationPreviewResponseMethod(str, Enum):
  SCHEDULE_REGISTER = "schedule_register"
  SOURCE_LEDGER = "source_ledger"
  STATEMENT = "statement"

  def __str__(self) -> str:
    return str(self.value)
