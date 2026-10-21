from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerReportShares(BaseModel):
  report_shares: Optional["ListLedgerReportSharesReportShares"] = Field(
    alias="reportShares"
  )


class ListLedgerReportSharesReportShares(BaseModel):
  report_shares: list["ListLedgerReportSharesReportSharesReportShares"] = Field(
    alias="reportShares"
  )
  pagination: "ListLedgerReportSharesReportSharesPagination"


class ListLedgerReportSharesReportSharesReportShares(BaseModel):
  id: str
  report_id: str = Field(alias="reportId")
  target_graph_id: str = Field(alias="targetGraphId")
  target_graph_name: Optional[str] = Field(alias="targetGraphName")
  shared_by: str = Field(alias="sharedBy")
  shared_at: str = Field(alias="sharedAt")
  revoked_at: Optional[str] = Field(alias="revokedAt")
  fact_count: int = Field(alias="factCount")


class ListLedgerReportSharesReportSharesPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerReportShares.model_rebuild()
ListLedgerReportSharesReportShares.model_rebuild()
