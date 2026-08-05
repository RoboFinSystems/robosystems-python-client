from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerMappingCoverage(BaseModel):
  mapping_coverage: Optional["GetLedgerMappingCoverageMappingCoverage"] = Field(
    alias="mappingCoverage"
  )


class GetLedgerMappingCoverageMappingCoverage(BaseModel):
  mapping_id: str = Field(alias="mappingId")
  total_coa_elements: int = Field(alias="totalCoaElements")
  mapped_count: int = Field(alias="mappedCount")
  unmapped_count: int = Field(alias="unmappedCount")
  coverage_percent: float = Field(alias="coveragePercent")
  high_confidence: int = Field(alias="highConfidence")
  medium_confidence: int = Field(alias="mediumConfidence")
  low_confidence: int = Field(alias="lowConfidence")


GetLedgerMappingCoverage.model_rebuild()
