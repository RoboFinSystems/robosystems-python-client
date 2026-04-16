from enum import Enum


class UpdateElementRequestPeriodTypeType0(str, Enum):
  DURATION = "duration"
  INSTANT = "instant"

  def __str__(self) -> str:
    return str(self.value)
