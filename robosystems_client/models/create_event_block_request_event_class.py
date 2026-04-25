from enum import Enum


class CreateEventBlockRequestEventClass(str, Enum):
  ECONOMIC = "economic"
  SUPPORT = "support"

  def __str__(self) -> str:
    return str(self.value)
