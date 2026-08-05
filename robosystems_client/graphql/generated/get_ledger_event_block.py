from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerEventBlock(BaseModel):
  event_block: Optional["GetLedgerEventBlockEventBlock"] = Field(alias="eventBlock")


class GetLedgerEventBlockEventBlock(BaseModel):
  id: str
  event_type: str = Field(alias="eventType")
  event_category: str = Field(alias="eventCategory")
  event_class: str = Field(alias="eventClass")
  status: str
  occurred_at: str = Field(alias="occurredAt")
  effective_at: Optional[str] = Field(alias="effectiveAt")
  source: str
  external_id: Optional[str] = Field(alias="externalId")
  external_url: Optional[str] = Field(alias="externalUrl")
  amount: Optional[int]
  currency: str
  description: Optional[str]
  metadata: Any
  dimension_ids: list[str] = Field(alias="dimensionIds")
  agent_id: Optional[str] = Field(alias="agentId")
  resource_type: Optional[str] = Field(alias="resourceType")
  resource_element_id: Optional[str] = Field(alias="resourceElementId")
  replaced_by_event_id: Optional[str] = Field(alias="replacedByEventId")
  replaces_event_id: Optional[str] = Field(alias="replacesEventId")
  obligated_by_event_id: Optional[str] = Field(alias="obligatedByEventId")
  discharges_event_id: Optional[str] = Field(alias="dischargesEventId")
  created_at: str = Field(alias="createdAt")
  created_by: str = Field(alias="createdBy")


GetLedgerEventBlock.model_rebuild()
