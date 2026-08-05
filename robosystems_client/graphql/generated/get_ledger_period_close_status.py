from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerPeriodCloseStatus(BaseModel):
  period_close_status: Optional["GetLedgerPeriodCloseStatusPeriodCloseStatus"] = Field(
    alias="periodCloseStatus"
  )


class GetLedgerPeriodCloseStatusPeriodCloseStatus(BaseModel):
  fiscal_period_start: str = Field(alias="fiscalPeriodStart")
  fiscal_period_end: str = Field(alias="fiscalPeriodEnd")
  period_status: str = Field(alias="periodStatus")
  total_draft: int = Field(alias="totalDraft")
  total_posted: int = Field(alias="totalPosted")
  schedules: list["GetLedgerPeriodCloseStatusPeriodCloseStatusSchedules"]


class GetLedgerPeriodCloseStatusPeriodCloseStatusSchedules(BaseModel):
  structure_id: str = Field(alias="structureId")
  structure_name: str = Field(alias="structureName")
  amount: float
  status: str
  entry_id: Optional[str] = Field(alias="entryId")
  reversal_entry_id: Optional[str] = Field(alias="reversalEntryId")
  reversal_status: Optional[str] = Field(alias="reversalStatus")


GetLedgerPeriodCloseStatus.model_rebuild()
GetLedgerPeriodCloseStatusPeriodCloseStatus.model_rebuild()
