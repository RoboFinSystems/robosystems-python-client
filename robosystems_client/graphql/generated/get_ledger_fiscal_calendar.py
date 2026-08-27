from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerFiscalCalendar(BaseModel):
  fiscal_calendar: Optional["GetLedgerFiscalCalendarFiscalCalendar"] = Field(
    alias="fiscalCalendar"
  )


class GetLedgerFiscalCalendarFiscalCalendar(BaseModel):
  graph_id: str = Field(alias="graphId")
  fiscal_year_start_month: int = Field(alias="fiscalYearStartMonth")
  closed_through: Optional[str] = Field(alias="closedThrough")
  close_target: Optional[str] = Field(alias="closeTarget")
  gap_periods: int = Field(alias="gapPeriods")
  catch_up_sequence: list[str] = Field(alias="catchUpSequence")
  closeable_now: bool = Field(alias="closeableNow")
  blockers: list[str]
  pending_obligation_count: int = Field(alias="pendingObligationCount")
  pending_obligation_sample: list[
    "GetLedgerFiscalCalendarFiscalCalendarPendingObligationSample"
  ] = Field(alias="pendingObligationSample")
  earliest_pending_period: Optional[str] = Field(alias="earliestPendingPeriod")
  stranded_obligation_count: int = Field(alias="strandedObligationCount")
  stranded_obligation_sample: list[
    "GetLedgerFiscalCalendarFiscalCalendarStrandedObligationSample"
  ] = Field(alias="strandedObligationSample")
  reconciling_item_count: int = Field(alias="reconcilingItemCount")
  reconciling_item_sample: list[str] = Field(alias="reconcilingItemSample")
  sync_stale_days: Optional[int] = Field(alias="syncStaleDays")
  last_close_at: Optional[str] = Field(alias="lastCloseAt")
  initialized_at: Optional[str] = Field(alias="initializedAt")
  last_sync_at: Optional[str] = Field(alias="lastSyncAt")
  periods: list["GetLedgerFiscalCalendarFiscalCalendarPeriods"]


class GetLedgerFiscalCalendarFiscalCalendarPendingObligationSample(BaseModel):
  event_id: str = Field(alias="eventId")
  schedule_id: Optional[str] = Field(alias="scheduleId")
  schedule_name: Optional[str] = Field(alias="scheduleName")
  period: str


class GetLedgerFiscalCalendarFiscalCalendarStrandedObligationSample(BaseModel):
  event_id: str = Field(alias="eventId")
  schedule_id: Optional[str] = Field(alias="scheduleId")
  schedule_name: Optional[str] = Field(alias="scheduleName")
  period: str


class GetLedgerFiscalCalendarFiscalCalendarPeriods(BaseModel):
  name: str
  start_date: str = Field(alias="startDate")
  end_date: str = Field(alias="endDate")
  status: str
  closed_at: Optional[str] = Field(alias="closedAt")


GetLedgerFiscalCalendar.model_rebuild()
GetLedgerFiscalCalendarFiscalCalendar.model_rebuild()
