from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerPeriodDrafts(BaseModel):
  period_drafts: Optional["GetLedgerPeriodDraftsPeriodDrafts"] = Field(
    alias="periodDrafts"
  )


class GetLedgerPeriodDraftsPeriodDrafts(BaseModel):
  period: str
  period_start: str = Field(alias="periodStart")
  period_end: str = Field(alias="periodEnd")
  draft_count: int = Field(alias="draftCount")
  total_debit: int = Field(alias="totalDebit")
  total_credit: int = Field(alias="totalCredit")
  all_balanced: bool = Field(alias="allBalanced")
  qb_writeback_connection_id: Optional[str] = Field(alias="qbWritebackConnectionId")
  qb_write_policy: Optional[str] = Field(alias="qbWritePolicy")
  qb_publish_count: int = Field(alias="qbPublishCount")
  local_only_count: int = Field(alias="localOnlyCount")
  drafts: list["GetLedgerPeriodDraftsPeriodDraftsDrafts"]


class GetLedgerPeriodDraftsPeriodDraftsDrafts(BaseModel):
  entry_id: str = Field(alias="entryId")
  posting_date: str = Field(alias="postingDate")
  type_: str = Field(alias="type")
  memo: Optional[str]
  provenance: Optional[str]
  source_structure_id: Optional[str] = Field(alias="sourceStructureId")
  source_structure_name: Optional[str] = Field(alias="sourceStructureName")
  total_debit: int = Field(alias="totalDebit")
  total_credit: int = Field(alias="totalCredit")
  balanced: bool
  will_publish_to_qb: bool = Field(alias="willPublishToQb")
  line_items: list["GetLedgerPeriodDraftsPeriodDraftsDraftsLineItems"] = Field(
    alias="lineItems"
  )


class GetLedgerPeriodDraftsPeriodDraftsDraftsLineItems(BaseModel):
  line_item_id: str = Field(alias="lineItemId")
  element_id: str = Field(alias="elementId")
  element_code: Optional[str] = Field(alias="elementCode")
  element_name: str = Field(alias="elementName")
  debit_amount: int = Field(alias="debitAmount")
  credit_amount: int = Field(alias="creditAmount")
  description: Optional[str]


GetLedgerPeriodDrafts.model_rebuild()
GetLedgerPeriodDraftsPeriodDrafts.model_rebuild()
GetLedgerPeriodDraftsPeriodDraftsDrafts.model_rebuild()
