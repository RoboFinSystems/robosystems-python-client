from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerBankAccounts(BaseModel):
  bank_accounts: Optional["ListLedgerBankAccountsBankAccounts"] = Field(
    alias="bankAccounts"
  )


class ListLedgerBankAccountsBankAccounts(BaseModel):
  total: int
  accounts: list["ListLedgerBankAccountsBankAccountsAccounts"]


class ListLedgerBankAccountsBankAccountsAccounts(BaseModel):
  id: str
  code: Optional[str]
  name: str
  kind: str
  balance_type: str = Field(alias="balanceType")
  is_active: bool = Field(alias="isActive")
  entity_id: Optional[str] = Field(alias="entityId")
  entity_name: Optional[str] = Field(alias="entityName")
  source: Optional[str]
  connection_id: Optional[str] = Field(alias="connectionId")
  institution: Optional[str]
  feed_account_id: Optional[str] = Field(alias="feedAccountId")
  feed_account_name: Optional[str] = Field(alias="feedAccountName")
  feed_account_kind: Optional[str] = Field(alias="feedAccountKind")
  connection_status: Optional[str] = Field(alias="connectionStatus")
  last_sync_at: Optional[str] = Field(alias="lastSyncAt")
  last_sync_status: Optional[str] = Field(alias="lastSyncStatus")


ListLedgerBankAccounts.model_rebuild()
ListLedgerBankAccountsBankAccounts.model_rebuild()
