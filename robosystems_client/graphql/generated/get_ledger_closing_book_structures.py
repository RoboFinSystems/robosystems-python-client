from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerClosingBookStructures(BaseModel):
  closing_book_structures: Optional[
    "GetLedgerClosingBookStructuresClosingBookStructures"
  ] = Field(alias="closingBookStructures")


class GetLedgerClosingBookStructuresClosingBookStructures(BaseModel):
  has_data: bool = Field(alias="hasData")
  categories: list["GetLedgerClosingBookStructuresClosingBookStructuresCategories"]


class GetLedgerClosingBookStructuresClosingBookStructuresCategories(BaseModel):
  label: str
  items: list["GetLedgerClosingBookStructuresClosingBookStructuresCategoriesItems"]


class GetLedgerClosingBookStructuresClosingBookStructuresCategoriesItems(BaseModel):
  id: str
  name: str
  item_type: str = Field(alias="itemType")
  block_type: Optional[str] = Field(alias="blockType")
  report_id: Optional[str] = Field(alias="reportId")
  status: Optional[str]


GetLedgerClosingBookStructures.model_rebuild()
GetLedgerClosingBookStructuresClosingBookStructures.model_rebuild()
GetLedgerClosingBookStructuresClosingBookStructuresCategories.model_rebuild()
