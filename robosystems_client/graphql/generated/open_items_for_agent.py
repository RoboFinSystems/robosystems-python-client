from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class OpenItemsForAgent(BaseModel):
  open_items_for_agent: list["OpenItemsForAgentOpenItemsForAgent"] = Field(
    alias="openItemsForAgent"
  )


class OpenItemsForAgentOpenItemsForAgent(BaseModel):
  event_id: str = Field(alias="eventId")
  entity_id: str = Field(alias="entityId")
  agent_id: Optional[str] = Field(alias="agentId")
  occurred_on: str = Field(alias="occurredOn")
  document_number: Optional[str] = Field(alias="documentNumber")
  description: Optional[str]
  original_cents: int = Field(alias="originalCents")
  settled_cents: int = Field(alias="settledCents")
  open_cents: int = Field(alias="openCents")
  currency: str
  due_date: str = Field(alias="dueDate")
  due_date_basis: str = Field(alias="dueDateBasis")
  days_past_due: int = Field(alias="daysPastDue")
  bucket: str


OpenItemsForAgent.model_rebuild()
