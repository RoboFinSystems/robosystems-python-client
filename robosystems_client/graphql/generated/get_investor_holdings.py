from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetInvestorHoldings(BaseModel):
  holdings: Optional["GetInvestorHoldingsHoldings"]


class GetInvestorHoldingsHoldings(BaseModel):
  total_entities: int = Field(alias="totalEntities")
  total_positions: int = Field(alias="totalPositions")
  holdings: list["GetInvestorHoldingsHoldingsHoldings"]


class GetInvestorHoldingsHoldingsHoldings(BaseModel):
  entity_id: str = Field(alias="entityId")
  entity_name: str = Field(alias="entityName")
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  total_cost_basis_dollars: float = Field(alias="totalCostBasisDollars")
  total_current_value_dollars: Optional[float] = Field(alias="totalCurrentValueDollars")
  position_count: int = Field(alias="positionCount")
  securities: list["GetInvestorHoldingsHoldingsHoldingsSecurities"]


class GetInvestorHoldingsHoldingsHoldingsSecurities(BaseModel):
  security_id: str = Field(alias="securityId")
  security_name: str = Field(alias="securityName")
  security_type: str = Field(alias="securityType")
  quantity: float
  quantity_type: str = Field(alias="quantityType")
  cost_basis_dollars: float = Field(alias="costBasisDollars")
  current_value_dollars: Optional[float] = Field(alias="currentValueDollars")


GetInvestorHoldings.model_rebuild()
GetInvestorHoldingsHoldings.model_rebuild()
GetInvestorHoldingsHoldingsHoldings.model_rebuild()
