from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerMapping(BaseModel):
  mapping: Optional["GetLedgerMappingMapping"]


class GetLedgerMappingMapping(BaseModel):
  id: str
  name: str
  block_type: str = Field(alias="blockType")
  taxonomy_id: str = Field(alias="taxonomyId")
  total_associations: int = Field(alias="totalAssociations")
  associations: list["GetLedgerMappingMappingAssociations"]


class GetLedgerMappingMappingAssociations(BaseModel):
  id: str
  structure_id: str = Field(alias="structureId")
  from_element_id: str = Field(alias="fromElementId")
  from_element_name: Optional[str] = Field(alias="fromElementName")
  from_element_qname: Optional[str] = Field(alias="fromElementQname")
  to_element_id: str = Field(alias="toElementId")
  to_element_name: Optional[str] = Field(alias="toElementName")
  to_element_qname: Optional[str] = Field(alias="toElementQname")
  association_type: str = Field(alias="associationType")
  order_value: Optional[float] = Field(alias="orderValue")
  weight: Optional[float]
  confidence: Optional[float]
  suggested_by: Optional[str] = Field(alias="suggestedBy")
  approved_by: Optional[str] = Field(alias="approvedBy")


GetLedgerMapping.model_rebuild()
GetLedgerMappingMapping.model_rebuild()
