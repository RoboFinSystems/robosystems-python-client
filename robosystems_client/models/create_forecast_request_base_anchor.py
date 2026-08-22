from enum import Enum


class CreateForecastRequestBaseAnchor(str, Enum):
  FIXED = "fixed"
  SEAM = "seam"

  def __str__(self) -> str:
    return str(self.value)
