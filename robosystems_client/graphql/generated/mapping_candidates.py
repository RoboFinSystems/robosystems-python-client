from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class MappingCandidates(BaseModel):
  mapping_candidates: list["MappingCandidatesMappingCandidates"] = Field(
    alias="mappingCandidates"
  )


class MappingCandidatesMappingCandidates(BaseModel):
  id: str
  name: str
  qname: Optional[str]
  trait: Optional[str]


MappingCandidates.model_rebuild()
