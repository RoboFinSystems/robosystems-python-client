from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerElements(BaseModel):
  elements: Optional["ListLedgerElementsElements"]


class ListLedgerElementsElements(BaseModel):
  elements: list["ListLedgerElementsElementsElements"]
  pagination: "ListLedgerElementsElementsPagination"


class ListLedgerElementsElementsElements(BaseModel):
  id: str
  code: Optional[str]
  name: str
  description: Optional[str]
  qname: Optional[str]
  namespace: Optional[str]
  trait: Optional[str]
  sub_classification: Optional[str] = Field(alias="subClassification")
  balance_type: str = Field(alias="balanceType")
  period_type: str = Field(alias="periodType")
  is_abstract: bool = Field(alias="isAbstract")
  element_type: str = Field(alias="elementType")
  source: str
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  parent_id: Optional[str] = Field(alias="parentId")
  depth: int
  is_active: bool = Field(alias="isActive")
  external_id: Optional[str] = Field(alias="externalId")
  external_source: Optional[str] = Field(alias="externalSource")


class ListLedgerElementsElementsPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerElements.model_rebuild()
ListLedgerElementsElements.model_rebuild()
