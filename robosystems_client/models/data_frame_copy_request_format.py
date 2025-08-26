from enum import Enum


class DataFrameCopyRequestFormat(str, Enum):
  ARROW = "arrow"
  PANDAS = "pandas"
  POLARS = "polars"

  def __str__(self) -> str:
    return str(self.value)
