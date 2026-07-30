from enum import Enum


class DimensionType(str, Enum):
  ELEMENT = "element"
  ENTITY = "entity"
  PERIOD = "period"

  def __str__(self) -> str:
    return str(self.value)
