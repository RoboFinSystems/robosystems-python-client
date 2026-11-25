from enum import Enum


class InitialEntityDataEntityTypeType0(str, Enum):
  CORPORATION = "corporation"
  LLC = "llc"
  NON_PROFIT = "non_profit"
  PARTNERSHIP = "partnership"
  SOLE_PROPRIETORSHIP = "sole_proprietorship"

  def __str__(self) -> str:
    return str(self.value)
