from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerEntities(BaseModel):
  entities: list["ListLedgerEntitiesEntities"]


class ListLedgerEntitiesEntities(BaseModel):
  id: str
  name: str
  legal_name: Optional[str] = Field(alias="legalName")
  ticker: Optional[str]
  cik: Optional[str]
  industry: Optional[str]
  entity_type: Optional[str] = Field(alias="entityType")
  status: str
  is_parent: bool = Field(alias="isParent")
  parent_entity_id: Optional[str] = Field(alias="parentEntityId")
  source: str
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  connection_id: Optional[str] = Field(alias="connectionId")
  created_at: Optional[str] = Field(alias="createdAt")
  updated_at: Optional[str] = Field(alias="updatedAt")


ListLedgerEntities.model_rebuild()
