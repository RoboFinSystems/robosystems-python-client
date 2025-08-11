from enum import Enum


class RepositoryType(str, Enum):
  ECONOMIC = "economic"
  INDUSTRY = "industry"
  SEC = "sec"

  def __str__(self) -> str:
    return str(self.value)
