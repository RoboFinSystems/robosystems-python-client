from enum import Enum


class CreateTaxonomyBlockRequestTaxonomyType(str, Enum):
  CHART_OF_ACCOUNTS = "chart_of_accounts"
  CUSTOM_ONTOLOGY = "custom_ontology"
  REPORTING_EXTENSION = "reporting_extension"
  REPORTING_STANDARD = "reporting_standard"
  SCHEDULE = "schedule"

  def __str__(self) -> str:
    return str(self.value)
