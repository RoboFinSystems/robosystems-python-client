from enum import Enum


class S3CopyRequestFileFormat(str, Enum):
  CSV = "csv"
  DELTA = "delta"
  ICEBERG = "iceberg"
  JSON = "json"
  PARQUET = "parquet"

  def __str__(self) -> str:
    return str(self.value)
