from enum import Enum


class ListGraphMutationsSurfaceType0(str, Enum):
  API = "api"
  MCP = "mcp"
  OPERATOR = "operator"

  def __str__(self) -> str:
    return str(self.value)
