from pydantic import Field

from .base_model import BaseModel


class FlowCandidates(BaseModel):
  flow_candidates: list["FlowCandidatesFlowCandidates"] = Field(alias="flowCandidates")


class FlowCandidatesFlowCandidates(BaseModel):
  element_id: str = Field(alias="elementId")
  qname: str
  name: str
  activity: str


FlowCandidates.model_rebuild()
