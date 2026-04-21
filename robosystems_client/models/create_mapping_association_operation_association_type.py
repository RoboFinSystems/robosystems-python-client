from enum import Enum


class CreateMappingAssociationOperationAssociationType(str, Enum):
  CALCULATION = "calculation"
  EQUIVALENCE = "equivalence"
  MAPPING = "mapping"
  PRESENTATION = "presentation"

  def __str__(self) -> str:
    return str(self.value)
