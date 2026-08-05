from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerSummary(BaseModel):
  summary: Optional["GetLedgerSummarySummary"]


class GetLedgerSummarySummary(BaseModel):
  graph_id: str = Field(alias="graphId")
  account_count: int = Field(alias="accountCount")
  transaction_count: int = Field(alias="transactionCount")
  entry_count: int = Field(alias="entryCount")
  line_item_count: int = Field(alias="lineItemCount")
  earliest_transaction_date: Optional[str] = Field(alias="earliestTransactionDate")
  latest_transaction_date: Optional[str] = Field(alias="latestTransactionDate")
  connection_count: int = Field(alias="connectionCount")
  last_sync_at: Optional[str] = Field(alias="lastSyncAt")


GetLedgerSummary.model_rebuild()
