from enum import Enum


class UpdateAgentRequestClassificationModeType0(str, Enum):
  ALWAYS_ASK = "always_ask"
  SUGGEST = "suggest"

  def __str__(self) -> str:
    return str(self.value)
