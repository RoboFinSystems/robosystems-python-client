from enum import Enum


class CreateConnectionRequestProvider(str, Enum):
  EXTERNAL = "external"
  QUICKBOOKS = "quickbooks"

  def __str__(self) -> str:
    return str(self.value)
