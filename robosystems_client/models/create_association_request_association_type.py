from enum import Enum


class CreateAssociationRequestAssociationType(str, Enum):
  CALCULATION = "calculation"
  MAPPING = "mapping"
  PRESENTATION = "presentation"

  def __str__(self) -> str:
    return str(self.value)
