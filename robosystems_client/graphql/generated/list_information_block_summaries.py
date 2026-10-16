from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListInformationBlockSummaries(BaseModel):
  information_block_summaries: list[
    "ListInformationBlockSummariesInformationBlockSummaries"
  ] = Field(alias="informationBlockSummaries")


class ListInformationBlockSummariesInformationBlockSummaries(BaseModel):
  id: str
  block_type: str = Field(alias="blockType")
  name: str
  display_name: str = Field(alias="displayName")
  category: str
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  taxonomy_name: Optional[str] = Field(alias="taxonomyName")
  entity_id: Optional[str] = Field(alias="entityId")
  fact_count: int = Field(alias="factCount")
  connection_count: int = Field(alias="connectionCount")


ListInformationBlockSummaries.model_rebuild()
