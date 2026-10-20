from enum import Enum


class LiveStatementFactRowOriginType0(str, Enum):
  ACCOUNTS = "accounts"
  COMPUTED = "computed"
  SUBTOTAL = "subtotal"

  def __str__(self) -> str:
    return str(self.value)
