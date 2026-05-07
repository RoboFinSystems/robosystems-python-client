from enum import Enum


class TaxonomyBlockElementOrigin(str, Enum):
  LIBRARY = "library"
  TENANT = "tenant"

  def __str__(self) -> str:
    return str(self.value)
