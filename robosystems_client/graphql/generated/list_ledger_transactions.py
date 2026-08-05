from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerTransactions(BaseModel):
  transactions: Optional["ListLedgerTransactionsTransactions"]


class ListLedgerTransactionsTransactions(BaseModel):
  transactions: list["ListLedgerTransactionsTransactionsTransactions"]
  pagination: "ListLedgerTransactionsTransactionsPagination"


class ListLedgerTransactionsTransactionsTransactions(BaseModel):
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
  status: str


class ListLedgerTransactionsTransactionsPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerTransactions.model_rebuild()
ListLedgerTransactionsTransactions.model_rebuild()
