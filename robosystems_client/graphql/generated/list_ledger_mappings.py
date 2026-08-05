from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerMappings(BaseModel):
  mappings: Optional["ListLedgerMappingsMappings"]


class ListLedgerMappingsMappings(BaseModel):
  structures: list["ListLedgerMappingsMappingsStructures"]


class ListLedgerMappingsMappingsStructures(BaseModel):
  id: str
  name: str
  description: Optional[str]
  block_type: str = Field(alias="blockType")
  taxonomy_id: str = Field(alias="taxonomyId")
  is_active: bool = Field(alias="isActive")


ListLedgerMappings.model_rebuild()
ListLedgerMappingsMappings.model_rebuild()
