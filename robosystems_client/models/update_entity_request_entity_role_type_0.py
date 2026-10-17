from enum import Enum


class UpdateEntityRequestEntityRoleType0(str, Enum):
  CONSOLIDATION = "consolidation"
  OPERATING = "operating"

  def __str__(self) -> str:
    return str(self.value)
