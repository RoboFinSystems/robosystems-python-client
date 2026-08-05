from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerEntity(BaseModel):
  entity: Optional["GetLedgerEntityEntity"]


class GetLedgerEntityEntity(BaseModel):
  id: str
  name: str
  legal_name: Optional[str] = Field(alias="legalName")
  uri: Optional[str]
  cik: Optional[str]
  ticker: Optional[str]
  exchange: Optional[str]
  sic: Optional[str]
  sic_description: Optional[str] = Field(alias="sicDescription")
  category: Optional[str]
  state_of_incorporation: Optional[str] = Field(alias="stateOfIncorporation")
  fiscal_year_end: Optional[str] = Field(alias="fiscalYearEnd")
  tax_id: Optional[str] = Field(alias="taxId")
  lei: Optional[str]
  industry: Optional[str]
  entity_type: Optional[str] = Field(alias="entityType")
  phone: Optional[str]
  website: Optional[str]
  status: str
  is_parent: bool = Field(alias="isParent")
  parent_entity_id: Optional[str] = Field(alias="parentEntityId")
  source: str
  source_id: Optional[str] = Field(alias="sourceId")
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  connection_id: Optional[str] = Field(alias="connectionId")
  address_line_1: Optional[str] = Field(alias="addressLine1")
  address_city: Optional[str] = Field(alias="addressCity")
  address_state: Optional[str] = Field(alias="addressState")
  address_postal_code: Optional[str] = Field(alias="addressPostalCode")
  address_country: Optional[str] = Field(alias="addressCountry")
  created_at: Optional[str] = Field(alias="createdAt")
  updated_at: Optional[str] = Field(alias="updatedAt")


GetLedgerEntity.model_rebuild()
