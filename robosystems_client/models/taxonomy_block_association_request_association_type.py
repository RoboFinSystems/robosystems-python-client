from enum import Enum


class TaxonomyBlockAssociationRequestAssociationType(str, Enum):
  CALCULATION = "calculation"
  EQUIVALENCE = "equivalence"
  ESSENCE_ALIAS = "essence-alias"
  GENERAL_SPECIAL = "general-special"
  MAPPING = "mapping"
  PRESENTATION = "presentation"

  def __str__(self) -> str:
    return str(self.value)
