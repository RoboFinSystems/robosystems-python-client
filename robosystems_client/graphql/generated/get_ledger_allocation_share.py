from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerAllocationShare(BaseModel):
  allocation_share: Optional["GetLedgerAllocationShareAllocationShare"] = Field(
    alias="allocationShare"
  )


class GetLedgerAllocationShareAllocationShare(BaseModel):
  entity_id: str = Field(alias="entityId")
  entity_name: str = Field(alias="entityName")
  period: str
  consolidation_method: str = Field(alias="consolidationMethod")
  ownership_pct: Optional[float] = Field(alias="ownershipPct")
  outside_pct: float = Field(alias="outsidePct")
  month_result: int = Field(alias="monthResult")
  pro_rata_amount: int = Field(alias="proRataAmount")
  override: Optional["GetLedgerAllocationShareAllocationShareOverride"]
  effective_amount: int = Field(alias="effectiveAmount")
  closed: bool


class GetLedgerAllocationShareAllocationShareOverride(BaseModel):
  period: str
  amount: Optional[int]
  percentage: Optional[float]
  basis: Optional[str]
  set_by: Optional[str] = Field(alias="setBy")


GetLedgerAllocationShare.model_rebuild()
GetLedgerAllocationShareAllocationShare.model_rebuild()
