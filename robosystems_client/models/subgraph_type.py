from enum import Enum


class SubgraphType(str, Enum):
  EMPTY = "empty"
  KNOWLEDGE = "knowledge"
  STATIC = "static"

  def __str__(self) -> str:
    return str(self.value)
