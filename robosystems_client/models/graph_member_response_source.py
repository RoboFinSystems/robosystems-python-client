from enum import Enum


class GraphMemberResponseSource(str, Enum):
  EXPLICIT = "explicit"
  ORG_ROLE = "org_role"

  def __str__(self) -> str:
    return str(self.value)
