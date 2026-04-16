from enum import Enum


class CreateTransactionRequestStatus(str, Enum):
  PENDING = "pending"
  POSTED = "posted"

  def __str__(self) -> str:
    return str(self.value)
