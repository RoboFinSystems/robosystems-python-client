from enum import Enum


class ListConnectionsProviderType0(str, Enum):
  EXTERNAL = "external"
  MERCURY = "mercury"
  QUICKBOOKS = "quickbooks"

  def __str__(self) -> str:
    return str(self.value)
