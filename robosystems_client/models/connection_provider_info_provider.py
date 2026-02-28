from enum import Enum


class ConnectionProviderInfoProvider(str, Enum):
  QUICKBOOKS = "quickbooks"
  SEC = "sec"

  def __str__(self) -> str:
    return str(self.value)
