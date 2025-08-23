from enum import Enum


class SubgraphType(str, Enum):
  MEMORY = "memory"
  STATIC = "static"
  TEMPORAL = "temporal"
  VERSIONED = "versioned"

  def __str__(self) -> str:
    return str(self.value)
