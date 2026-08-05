from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerTrialBalance(BaseModel):
  trial_balance: Optional["GetLedgerTrialBalanceTrialBalance"] = Field(
    alias="trialBalance"
  )


class GetLedgerTrialBalanceTrialBalance(BaseModel):
  total_debits: float = Field(alias="totalDebits")
  total_credits: float = Field(alias="totalCredits")
  rows: list["GetLedgerTrialBalanceTrialBalanceRows"]


class GetLedgerTrialBalanceTrialBalanceRows(BaseModel):
  account_id: str = Field(alias="accountId")
  account_code: str = Field(alias="accountCode")
  account_name: str = Field(alias="accountName")
  trait: Optional[str]
  account_type: Optional[str] = Field(alias="accountType")
  total_debits: float = Field(alias="totalDebits")
  total_credits: float = Field(alias="totalCredits")
  net_balance: float = Field(alias="netBalance")


GetLedgerTrialBalance.model_rebuild()
GetLedgerTrialBalanceTrialBalance.model_rebuild()
