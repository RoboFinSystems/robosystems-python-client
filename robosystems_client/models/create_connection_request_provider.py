from enum import Enum


class CreateConnectionRequestProvider(str, Enum):
  EXTERNAL = "external"
  MERCURY = "mercury"
  PLAID = "plaid"
  QUICKBOOKS = "quickbooks"

  def __str__(self) -> str:
    return str(self.value)
