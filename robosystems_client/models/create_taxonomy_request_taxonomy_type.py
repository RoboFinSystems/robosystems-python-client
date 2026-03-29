from enum import Enum


class CreateTaxonomyRequestTaxonomyType(str, Enum):
  CHART_OF_ACCOUNTS = "chart_of_accounts"
  MAPPING = "mapping"
  REPORTING = "reporting"

  def __str__(self) -> str:
    return str(self.value)
