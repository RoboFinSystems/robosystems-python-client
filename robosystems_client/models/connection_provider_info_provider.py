from enum import Enum


class ConnectionProviderInfoProvider(str, Enum):
  EXTERNAL = "external"
  MERCURY = "mercury"
  PLAID = "plaid"
  QUICKBOOKS = "quickbooks"

  def __str__(self) -> str:
    return str(self.value)
