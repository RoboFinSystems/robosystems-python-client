from enum import Enum


class CreateElementRequestPeriodType(str, Enum):
  DURATION = "duration"
  INSTANT = "instant"

  def __str__(self) -> str:
    return str(self.value)
