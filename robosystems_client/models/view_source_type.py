from enum import Enum


class ViewSourceType(str, Enum):
  FACT_SET = "fact_set"
  TRANSACTIONS = "transactions"

  def __str__(self) -> str:
    return str(self.value)
