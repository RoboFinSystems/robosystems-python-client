from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerMappedTrialBalance(BaseModel):
  mapped_trial_balance: Optional["GetLedgerMappedTrialBalanceMappedTrialBalance"] = (
    Field(alias="mappedTrialBalance")
  )


class GetLedgerMappedTrialBalanceMappedTrialBalance(BaseModel):
  mapping_id: str = Field(alias="mappingId")
  rows: list["GetLedgerMappedTrialBalanceMappedTrialBalanceRows"]


class GetLedgerMappedTrialBalanceMappedTrialBalanceRows(BaseModel):
  reporting_element_id: str = Field(alias="reportingElementId")
  qname: str
  reporting_name: str = Field(alias="reportingName")
  trait: Optional[str]
  balance_type: Optional[str] = Field(alias="balanceType")
  total_debits: float = Field(alias="totalDebits")
  total_credits: float = Field(alias="totalCredits")
  net_balance: float = Field(alias="netBalance")


GetLedgerMappedTrialBalance.model_rebuild()
GetLedgerMappedTrialBalanceMappedTrialBalance.model_rebuild()
