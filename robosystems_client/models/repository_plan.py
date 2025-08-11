from enum import Enum


class RepositoryPlan(str, Enum):
  ADVANCED = "advanced"
  STARTER = "starter"
  UNLIMITED = "unlimited"

  def __str__(self) -> str:
    return str(self.value)
