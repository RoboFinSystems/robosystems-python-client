from enum import Enum


class GraphRole(str, Enum):
  ADMIN = "admin"
  MEMBER = "member"
  VIEWER = "viewer"

  def __str__(self) -> str:
    return str(self.value)
