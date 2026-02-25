from enum import Enum


class CreateConnectionRequestProvider(str, Enum):
  PLAID = "plaid"
  QUICKBOOKS = "quickbooks"
  SEC = "sec"

  def __str__(self) -> str:
    return str(self.value)
