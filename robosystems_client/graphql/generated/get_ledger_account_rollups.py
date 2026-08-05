from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerAccountRollups(BaseModel):
  account_rollups: Optional["GetLedgerAccountRollupsAccountRollups"] = Field(
    alias="accountRollups"
  )


class GetLedgerAccountRollupsAccountRollups(BaseModel):
  mapping_id: str = Field(alias="mappingId")
  mapping_name: str = Field(alias="mappingName")
  total_mapped: int = Field(alias="totalMapped")
  total_unmapped: int = Field(alias="totalUnmapped")
  groups: list["GetLedgerAccountRollupsAccountRollupsGroups"]


class GetLedgerAccountRollupsAccountRollupsGroups(BaseModel):
  reporting_element_id: str = Field(alias="reportingElementId")
  reporting_name: str = Field(alias="reportingName")
  reporting_qname: str = Field(alias="reportingQname")
  trait: str
  balance_type: str = Field(alias="balanceType")
  total: float
  accounts: list["GetLedgerAccountRollupsAccountRollupsGroupsAccounts"]


class GetLedgerAccountRollupsAccountRollupsGroupsAccounts(BaseModel):
  element_id: str = Field(alias="elementId")
  account_name: str = Field(alias="accountName")
  account_code: Optional[str] = Field(alias="accountCode")
  total_debits: float = Field(alias="totalDebits")
  total_credits: float = Field(alias="totalCredits")
  net_balance: float = Field(alias="netBalance")


GetLedgerAccountRollups.model_rebuild()
GetLedgerAccountRollupsAccountRollups.model_rebuild()
GetLedgerAccountRollupsAccountRollupsGroups.model_rebuild()
