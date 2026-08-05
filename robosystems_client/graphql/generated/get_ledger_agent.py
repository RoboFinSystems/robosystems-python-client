from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerAgent(BaseModel):
  agent: Optional["GetLedgerAgentAgent"]


class GetLedgerAgentAgent(BaseModel):
  id: str
  agent_type: str = Field(alias="agentType")
  name: str
  legal_name: Optional[str] = Field(alias="legalName")
  tax_id: Optional[str] = Field(alias="taxId")
  registration_number: Optional[str] = Field(alias="registrationNumber")
  duns: Optional[str]
  lei: Optional[str]
  email: Optional[str]
  phone: Optional[str]
  address: Optional[Any]
  source: str
  external_id: Optional[str] = Field(alias="externalId")
  is_active: bool = Field(alias="isActive")
  is_1099_recipient: bool = Field(alias="is1099Recipient")
  created_at: Optional[str] = Field(alias="createdAt")
  updated_at: Optional[str] = Field(alias="updatedAt")
  created_by: Optional[str] = Field(alias="createdBy")


GetLedgerAgent.model_rebuild()
