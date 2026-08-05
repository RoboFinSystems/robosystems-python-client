from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class ListInvestorSecurities(BaseModel):
  securities: Optional["ListInvestorSecuritiesSecurities"]


class ListInvestorSecuritiesSecurities(BaseModel):
  securities: list["ListInvestorSecuritiesSecuritiesSecurities"]
  pagination: "ListInvestorSecuritiesSecuritiesPagination"


class ListInvestorSecuritiesSecuritiesSecurities(BaseModel):
  id: str
  entity_id: Optional[str] = Field(alias="entityId")
  entity_name: Optional[str] = Field(alias="entityName")
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  name: str
  security_type: str = Field(alias="securityType")
  security_subtype: Optional[str] = Field(alias="securitySubtype")
  terms: Any
  is_active: bool = Field(alias="isActive")
  authorized_shares: Optional[int] = Field(alias="authorizedShares")
  outstanding_shares: Optional[int] = Field(alias="outstandingShares")
  created_at: str = Field(alias="createdAt")
  updated_at: str = Field(alias="updatedAt")


class ListInvestorSecuritiesSecuritiesPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListInvestorSecurities.model_rebuild()
ListInvestorSecuritiesSecurities.model_rebuild()
