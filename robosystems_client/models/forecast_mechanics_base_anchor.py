from enum import Enum


class ForecastMechanicsBaseAnchor(str, Enum):
  FIXED = "fixed"
  SEAM = "seam"

  def __str__(self) -> str:
    return str(self.value)
