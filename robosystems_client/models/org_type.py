from enum import Enum


class OrgType(str, Enum):
  ENTERPRISE = "enterprise"
  PERSONAL = "personal"
  TEAM = "team"

  def __str__(self) -> str:
    return str(self.value)
