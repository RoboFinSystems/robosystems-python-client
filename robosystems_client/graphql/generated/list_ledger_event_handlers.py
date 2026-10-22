from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerEventHandlers(BaseModel):
  event_handlers: Optional["ListLedgerEventHandlersEventHandlers"] = Field(
    alias="eventHandlers"
  )


class ListLedgerEventHandlersEventHandlers(BaseModel):
  event_handlers: list["ListLedgerEventHandlersEventHandlersEventHandlers"] = Field(
    alias="eventHandlers"
  )
  pagination: "ListLedgerEventHandlersEventHandlersPagination"


class ListLedgerEventHandlersEventHandlersEventHandlers(BaseModel):
  id: str
  name: str
  description: Optional[str]
  event_type: str = Field(alias="eventType")
  event_category: Optional[str] = Field(alias="eventCategory")
  match_source: Optional[str] = Field(alias="matchSource")
  match_agent_type: Optional[str] = Field(alias="matchAgentType")
  match_resource_type: Optional[str] = Field(alias="matchResourceType")
  match_metadata_expression: Optional[Any] = Field(alias="matchMetadataExpression")
  transaction_template: Any = Field(alias="transactionTemplate")
  priority: int
  is_active: bool = Field(alias="isActive")
  origin: str
  suggested_by: Optional[str] = Field(alias="suggestedBy")
  confidence: Optional[float]
  approved_by: Optional[str] = Field(alias="approvedBy")
  approved_at: Optional[str] = Field(alias="approvedAt")
  awaiting_approval: bool = Field(alias="awaitingApproval")
  created_at: Optional[str] = Field(alias="createdAt")
  updated_at: Optional[str] = Field(alias="updatedAt")
  created_by: Optional[str] = Field(alias="createdBy")


class ListLedgerEventHandlersEventHandlersPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerEventHandlers.model_rebuild()
ListLedgerEventHandlersEventHandlers.model_rebuild()
