from enum import Enum


class CreateEventHandlerRequestOrigin(str, Enum):
  HUB = "hub"
  TENANT = "tenant"

  def __str__(self) -> str:
    return str(self.value)
