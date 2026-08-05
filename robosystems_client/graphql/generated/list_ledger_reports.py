from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerReports(BaseModel):
  reports: Optional["ListLedgerReportsReports"]


class ListLedgerReportsReports(BaseModel):
  reports: list["ListLedgerReportsReportsReports"]


class ListLedgerReportsReportsReports(BaseModel):
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
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  source_report_id: Optional[str] = Field(alias="sourceReportId")
  shared_at: Optional[str] = Field(alias="sharedAt")
  periods: Optional[list["ListLedgerReportsReportsReportsPeriods"]]
  structures: list["ListLedgerReportsReportsReportsStructures"]


class ListLedgerReportsReportsReportsPeriods(BaseModel):
  start: str
  end: str
  label: str


class ListLedgerReportsReportsReportsStructures(BaseModel):
  id: str
  name: str
  block_type: str = Field(alias="blockType")


ListLedgerReports.model_rebuild()
ListLedgerReportsReports.model_rebuild()
ListLedgerReportsReportsReports.model_rebuild()
