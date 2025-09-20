from enum import Enum


class AgentMode(str, Enum):
  EXTENDED = "extended"
  QUICK = "quick"
  STANDARD = "standard"
  STREAMING = "streaming"

  def __str__(self) -> str:
    return str(self.value)
