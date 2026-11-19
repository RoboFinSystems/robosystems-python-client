from enum import Enum


class ReportSectionRowLayoutType0(str, Enum):
  GIVEN = "given"
  LIBRARY = "library"

  def __str__(self) -> str:
    return str(self.value)
