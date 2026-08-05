from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerReport(BaseModel):
  report: Optional["GetLedgerReportReport"]


class GetLedgerReportReport(BaseModel):
  id: str
  name: str
  taxonomy_id: str = Field(alias="taxonomyId")
  generation_status: str = Field(alias="generationStatus")
  period_type: str = Field(alias="periodType")
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: Optional[str] = Field(alias="periodEnd")
  comparative: bool
  mapping_id: Optional[str] = Field(alias="mappingId")
  ai_generated: bool = Field(alias="aiGenerated")
  created_at: str = Field(alias="createdAt")
  last_generated: Optional[str] = Field(alias="lastGenerated")
  entity_name: Optional[str] = Field(alias="entityName")
  filing_status: str = Field(alias="filingStatus")
  filed_at: Optional[str] = Field(alias="filedAt")
  filed_by: Optional[str] = Field(alias="filedBy")
  supersedes_id: Optional[str] = Field(alias="supersedesId")
  superseded_by_id: Optional[str] = Field(alias="supersededById")
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  source_report_id: Optional[str] = Field(alias="sourceReportId")
  shared_at: Optional[str] = Field(alias="sharedAt")
  periods: Optional[list["GetLedgerReportReportPeriods"]]
  structures: list["GetLedgerReportReportStructures"]


class GetLedgerReportReportPeriods(BaseModel):
  start: str
  end: str
  label: str


class GetLedgerReportReportStructures(BaseModel):
  id: str
  name: str
  block_type: str = Field(alias="blockType")


GetLedgerReport.model_rebuild()
GetLedgerReportReport.model_rebuild()
