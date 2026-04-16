from enum import Enum


class CreateElementRequestElementType(str, Enum):
  ABSTRACT = "abstract"
  AXIS = "axis"
  CONCEPT = "concept"
  HYPERCUBE = "hypercube"
  MEMBER = "member"

  def __str__(self) -> str:
    return str(self.value)
