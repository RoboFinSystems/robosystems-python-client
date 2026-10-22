from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerAllocationOverrides(BaseModel):
  allocation_overrides: Optional["ListLedgerAllocationOverridesAllocationOverrides"] = (
    Field(alias="allocationOverrides")
  )


class ListLedgerAllocationOverridesAllocationOverrides(BaseModel):
  entity_id: str = Field(alias="entityId")
  overrides: list["ListLedgerAllocationOverridesAllocationOverridesOverrides"]


class ListLedgerAllocationOverridesAllocationOverridesOverrides(BaseModel):
  period: str
  amount: Optional[int]
  percentage: Optional[float]
  basis: Optional[str]
  set_by: Optional[str] = Field(alias="setBy")


ListLedgerAllocationOverrides.model_rebuild()
ListLedgerAllocationOverridesAllocationOverrides.model_rebuild()
