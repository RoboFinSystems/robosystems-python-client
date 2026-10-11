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
  classification: Optional["GetLedgerAgentAgentClassification"]


class GetLedgerAgentAgentClassification(BaseModel):
  element_id: str = Field(alias="elementId")
  account_name: Optional[str] = Field(alias="accountName")
  mode: str
  confirmations: int
  overrides: int
  set_by: Optional[str] = Field(alias="setBy")
  set_at: Optional[str] = Field(alias="setAt")
  learned_from: Optional[str] = Field(alias="learnedFrom")


GetLedgerAgent.model_rebuild()
GetLedgerAgentAgent.model_rebuild()
