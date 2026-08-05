from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerStructures(BaseModel):
  structures: Optional["ListLedgerStructuresStructures"]


class ListLedgerStructuresStructures(BaseModel):
  structures: list["ListLedgerStructuresStructuresStructures"]


class ListLedgerStructuresStructuresStructures(BaseModel):
  id: str
  name: str
  description: Optional[str]
  block_type: str = Field(alias="blockType")
  taxonomy_id: str = Field(alias="taxonomyId")
  is_active: bool = Field(alias="isActive")


ListLedgerStructures.model_rebuild()
ListLedgerStructuresStructures.model_rebuild()
