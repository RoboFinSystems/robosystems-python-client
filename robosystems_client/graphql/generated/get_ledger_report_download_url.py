from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerReportDownloadUrl(BaseModel):
  report_download_url: Optional["GetLedgerReportDownloadUrlReportDownloadUrl"] = Field(
    alias="reportDownloadUrl"
  )


class GetLedgerReportDownloadUrlReportDownloadUrl(BaseModel):
  download_url: str = Field(alias="downloadUrl")
  expires_at: str = Field(alias="expiresAt")
  content_type: str = Field(alias="contentType")
  format: str
  generation_count: int = Field(alias="generationCount")


GetLedgerReportDownloadUrl.model_rebuild()
