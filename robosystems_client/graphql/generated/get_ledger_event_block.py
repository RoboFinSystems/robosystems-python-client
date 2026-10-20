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
  document_id: Optional[str] = Field(alias="documentId")
  created_at: str = Field(alias="createdAt")
  created_by: str = Field(alias="createdBy")
  triggered_entries: list["GetLedgerEventBlockEventBlockTriggeredEntries"] = Field(
    alias="triggeredEntries"
  )


class GetLedgerEventBlockEventBlockTriggeredEntries(BaseModel):
  id: str
  number: Optional[str]
  type_: str = Field(alias="type")
  status: str
  posting_date: str = Field(alias="postingDate")
  memo: Optional[str]
  provenance: Optional[str]
  total_debit: float = Field(alias="totalDebit")
  total_credit: float = Field(alias="totalCredit")
  line_items: list["GetLedgerEventBlockEventBlockTriggeredEntriesLineItems"] = Field(
    alias="lineItems"
  )


class GetLedgerEventBlockEventBlockTriggeredEntriesLineItems(BaseModel):
  id: str
  account_id: str = Field(alias="accountId")
  account_name: Optional[str] = Field(alias="accountName")
  account_code: Optional[str] = Field(alias="accountCode")
  debit_amount: float = Field(alias="debitAmount")
  credit_amount: float = Field(alias="creditAmount")
  description: Optional[str]
  line_order: int = Field(alias="lineOrder")


GetLedgerEventBlock.model_rebuild()
GetLedgerEventBlockEventBlock.model_rebuild()
GetLedgerEventBlockEventBlockTriggeredEntries.model_rebuild()
