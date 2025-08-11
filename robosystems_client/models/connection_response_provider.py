from enum import Enum


class ConnectionResponseProvider(str, Enum):
  PLAID = "plaid"
  QUICKBOOKS = "quickbooks"
  SEC = "sec"

  def __str__(self) -> str:
    return str(self.value)
