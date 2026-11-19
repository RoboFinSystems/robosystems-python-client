from enum import Enum


class ReportDepartureKind(str, Enum):
  MOVED = "moved"
  OWN_LAYOUT = "own_layout"
  OWN_SUBTOTAL = "own_subtotal"
  PLACED = "placed"

  def __str__(self) -> str:
    return str(self.value)
