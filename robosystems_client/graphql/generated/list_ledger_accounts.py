from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerAccounts(BaseModel):
  accounts: Optional["ListLedgerAccountsAccounts"]


class ListLedgerAccountsAccounts(BaseModel):
  accounts: list["ListLedgerAccountsAccountsAccounts"]
  pagination: "ListLedgerAccountsAccountsPagination"


class ListLedgerAccountsAccountsAccounts(BaseModel):
  id: str
  code: Optional[str]
  name: str
  description: Optional[str]
  trait: Optional[str]
  sub_classification: Optional[str] = Field(alias="subClassification")
  balance_type: str = Field(alias="balanceType")
  parent_id: Optional[str] = Field(alias="parentId")
  depth: int
  currency: str
  is_active: bool = Field(alias="isActive")
  is_placeholder: bool = Field(alias="isPlaceholder")
  account_type: Optional[str] = Field(alias="accountType")
  external_id: Optional[str] = Field(alias="externalId")
  external_source: Optional[str] = Field(alias="externalSource")


class ListLedgerAccountsAccountsPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerAccounts.model_rebuild()
ListLedgerAccountsAccounts.model_rebuild()
