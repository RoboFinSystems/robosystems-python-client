from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerDimensions(BaseModel):
  dimensions: Optional["ListLedgerDimensionsDimensions"]


class ListLedgerDimensionsDimensions(BaseModel):
  types: list[str]
  dimensions: list["ListLedgerDimensionsDimensionsDimensions"]


class ListLedgerDimensionsDimensionsDimensions(BaseModel):
  id: str
  dimension_type: str = Field(alias="dimensionType")
  name: str
  value: str
  source: str
  is_active: bool = Field(alias="isActive")
  line_count: int = Field(alias="lineCount")
  created_at: Optional[str] = Field(alias="createdAt")


ListLedgerDimensions.model_rebuild()
ListLedgerDimensionsDimensions.model_rebuild()
