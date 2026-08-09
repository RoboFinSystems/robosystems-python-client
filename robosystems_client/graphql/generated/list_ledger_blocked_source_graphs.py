from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerBlockedSourceGraphs(BaseModel):
  blocked_source_graphs: Optional[
    "ListLedgerBlockedSourceGraphsBlockedSourceGraphs"
  ] = Field(alias="blockedSourceGraphs")


class ListLedgerBlockedSourceGraphsBlockedSourceGraphs(BaseModel):
  blocked_source_graphs: list[
    "ListLedgerBlockedSourceGraphsBlockedSourceGraphsBlockedSourceGraphs"
  ] = Field(alias="blockedSourceGraphs")
  pagination: "ListLedgerBlockedSourceGraphsBlockedSourceGraphsPagination"


class ListLedgerBlockedSourceGraphsBlockedSourceGraphsBlockedSourceGraphs(BaseModel):
  id: str
  source_graph_id: str = Field(alias="sourceGraphId")
  source_graph_name: Optional[str] = Field(alias="sourceGraphName")
  blocked_by: str = Field(alias="blockedBy")
  blocked_at: str = Field(alias="blockedAt")
  reason: Optional[str]


class ListLedgerBlockedSourceGraphsBlockedSourceGraphsPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerBlockedSourceGraphs.model_rebuild()
ListLedgerBlockedSourceGraphsBlockedSourceGraphs.model_rebuild()
