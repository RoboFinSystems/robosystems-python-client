from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerReportingTaxonomy(BaseModel):
  reporting_taxonomy: Optional["GetLedgerReportingTaxonomyReportingTaxonomy"] = Field(
    alias="reportingTaxonomy"
  )


class GetLedgerReportingTaxonomyReportingTaxonomy(BaseModel):
  id: str
  name: str
  description: Optional[str]
  taxonomy_type: str = Field(alias="taxonomyType")
  version: Optional[str]
  standard: Optional[str]
  namespace_uri: Optional[str] = Field(alias="namespaceUri")
  is_shared: bool = Field(alias="isShared")
  is_active: bool = Field(alias="isActive")
  is_locked: bool = Field(alias="isLocked")
  source_taxonomy_id: Optional[str] = Field(alias="sourceTaxonomyId")
  target_taxonomy_id: Optional[str] = Field(alias="targetTaxonomyId")


GetLedgerReportingTaxonomy.model_rebuild()
