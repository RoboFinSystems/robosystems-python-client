from enum import Enum


class ConnectionProviderInfoAuthType(str, Enum):
  API_KEY = "api_key"
  LINK = "link"
  NONE = "none"
  OAUTH = "oauth"

  def __str__(self) -> str:
    return str(self.value)
