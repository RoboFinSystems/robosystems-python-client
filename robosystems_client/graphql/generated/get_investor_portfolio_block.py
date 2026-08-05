from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetInvestorPortfolioBlock(BaseModel):
  portfolio_block: Optional["GetInvestorPortfolioBlockPortfolioBlock"] = Field(
    alias="portfolioBlock"
  )


class GetInvestorPortfolioBlockPortfolioBlock(BaseModel):
  id: str
  name: str
  description: Optional[str]
  strategy: Optional[str]
  inception_date: Optional[str] = Field(alias="inceptionDate")
  base_currency: str = Field(alias="baseCurrency")
  owner: Optional["GetInvestorPortfolioBlockPortfolioBlockOwner"]
  positions: list["GetInvestorPortfolioBlockPortfolioBlockPositions"]
  total_cost_basis_dollars: float = Field(alias="totalCostBasisDollars")
  total_current_value_dollars: Optional[float] = Field(alias="totalCurrentValueDollars")
  active_position_count: int = Field(alias="activePositionCount")
  created_at: str = Field(alias="createdAt")
  updated_at: str = Field(alias="updatedAt")


class GetInvestorPortfolioBlockPortfolioBlockOwner(BaseModel):
  id: str
  name: str
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")


class GetInvestorPortfolioBlockPortfolioBlockPositions(BaseModel):
  id: str
  quantity: float
  quantity_type: str = Field(alias="quantityType")
  cost_basis_dollars: float = Field(alias="costBasisDollars")
  current_value_dollars: Optional[float] = Field(alias="currentValueDollars")
  valuation_date: Optional[str] = Field(alias="valuationDate")
  valuation_source: Optional[str] = Field(alias="valuationSource")
  acquisition_date: Optional[str] = Field(alias="acquisitionDate")
  status: str
  notes: Optional[str]
  security: "GetInvestorPortfolioBlockPortfolioBlockPositionsSecurity"


class GetInvestorPortfolioBlockPortfolioBlockPositionsSecurity(BaseModel):
  id: str
  name: str
  security_type: str = Field(alias="securityType")
  security_subtype: Optional[str] = Field(alias="securitySubtype")
  is_active: bool = Field(alias="isActive")
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  issuer: Optional["GetInvestorPortfolioBlockPortfolioBlockPositionsSecurityIssuer"]


class GetInvestorPortfolioBlockPortfolioBlockPositionsSecurityIssuer(BaseModel):
  id: str
  name: str
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")


GetInvestorPortfolioBlock.model_rebuild()
GetInvestorPortfolioBlockPortfolioBlock.model_rebuild()
GetInvestorPortfolioBlockPortfolioBlockPositions.model_rebuild()
GetInvestorPortfolioBlockPortfolioBlockPositionsSecurity.model_rebuild()
