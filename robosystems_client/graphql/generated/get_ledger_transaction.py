from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerTransaction(BaseModel):
  transaction: Optional["GetLedgerTransactionTransaction"]


class GetLedgerTransactionTransaction(BaseModel):
  id: str
  number: Optional[str]
  type_: str = Field(alias="type")
  category: Optional[str]
  amount: float
  currency: str
  date: str
  due_date: Optional[str] = Field(alias="dueDate")
  merchant_name: Optional[str] = Field(alias="merchantName")
  reference_number: Optional[str] = Field(alias="referenceNumber")
  description: Optional[str]
  source: str
  source_id: Optional[str] = Field(alias="sourceId")
  status: str
  posted_at: Optional[str] = Field(alias="postedAt")
  entries: list["GetLedgerTransactionTransactionEntries"]


class GetLedgerTransactionTransactionEntries(BaseModel):
  id: str
  number: Optional[str]
  type_: str = Field(alias="type")
  posting_date: str = Field(alias="postingDate")
  memo: Optional[str]
  status: str
  posted_at: Optional[str] = Field(alias="postedAt")
  line_items: list["GetLedgerTransactionTransactionEntriesLineItems"] = Field(
    alias="lineItems"
  )


class GetLedgerTransactionTransactionEntriesLineItems(BaseModel):
  id: str
  account_id: str = Field(alias="accountId")
  account_name: Optional[str] = Field(alias="accountName")
  account_code: Optional[str] = Field(alias="accountCode")
  debit_amount: float = Field(alias="debitAmount")
  credit_amount: float = Field(alias="creditAmount")
  description: Optional[str]
  line_order: int = Field(alias="lineOrder")


GetLedgerTransaction.model_rebuild()
GetLedgerTransactionTransaction.model_rebuild()
GetLedgerTransactionTransactionEntries.model_rebuild()
