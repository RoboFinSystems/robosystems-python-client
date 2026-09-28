from enum import Enum


class MutationAuditEntrySurface(str, Enum):
  API = "api"
  MCP = "mcp"
  OPERATOR = "operator"

  def __str__(self) -> str:
    return str(self.value)
