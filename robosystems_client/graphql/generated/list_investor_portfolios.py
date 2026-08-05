from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListInvestorPortfolios(BaseModel):
  portfolios: Optional["ListInvestorPortfoliosPortfolios"]


class ListInvestorPortfoliosPortfolios(BaseModel):
  portfolios: list["ListInvestorPortfoliosPortfoliosPortfolios"]
  pagination: "ListInvestorPortfoliosPortfoliosPagination"


class ListInvestorPortfoliosPortfoliosPortfolios(BaseModel):
  id: str
  name: str
  description: Optional[str]
  strategy: Optional[str]
  inception_date: Optional[str] = Field(alias="inceptionDate")
  base_currency: str = Field(alias="baseCurrency")
  created_at: str = Field(alias="createdAt")
  updated_at: str = Field(alias="updatedAt")


class ListInvestorPortfoliosPortfoliosPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListInvestorPortfolios.model_rebuild()
ListInvestorPortfoliosPortfolios.model_rebuild()
