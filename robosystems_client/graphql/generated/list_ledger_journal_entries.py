from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerJournalEntries(BaseModel):
  journal_entries: Optional["ListLedgerJournalEntriesJournalEntries"] = Field(
    alias="journalEntries"
  )


class ListLedgerJournalEntriesJournalEntries(BaseModel):
  entries: list["ListLedgerJournalEntriesJournalEntriesEntries"]
  pagination: "ListLedgerJournalEntriesJournalEntriesPagination"


class ListLedgerJournalEntriesJournalEntriesEntries(BaseModel):
  id: str
  number: Optional[str]
  transaction_id: Optional[str] = Field(alias="transactionId")
  type_: str = Field(alias="type")
  status: str
  posting_date: str = Field(alias="postingDate")
  memo: Optional[str]
  provenance: Optional[str]
  source_structure_id: Optional[str] = Field(alias="sourceStructureId")
  source_structure_name: Optional[str] = Field(alias="sourceStructureName")
  triggered_by_event_id: Optional[str] = Field(alias="triggeredByEventId")
  reversal_of: Optional[str] = Field(alias="reversalOf")
  posted_at: Optional[str] = Field(alias="postedAt")
  total_debit: float = Field(alias="totalDebit")
  total_credit: float = Field(alias="totalCredit")
  balanced: bool
  line_items: list["ListLedgerJournalEntriesJournalEntriesEntriesLineItems"] = Field(
    alias="lineItems"
  )


class ListLedgerJournalEntriesJournalEntriesEntriesLineItems(BaseModel):
  id: str
  account_id: str = Field(alias="accountId")
  account_name: Optional[str] = Field(alias="accountName")
  account_code: Optional[str] = Field(alias="accountCode")
  debit_amount: float = Field(alias="debitAmount")
  credit_amount: float = Field(alias="creditAmount")
  description: Optional[str]
  line_order: int = Field(alias="lineOrder")


class ListLedgerJournalEntriesJournalEntriesPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerJournalEntries.model_rebuild()
ListLedgerJournalEntriesJournalEntries.model_rebuild()
ListLedgerJournalEntriesJournalEntriesEntries.model_rebuild()
