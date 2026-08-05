from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetInvestorPosition(BaseModel):
  position: Optional["GetInvestorPositionPosition"]


class GetInvestorPositionPosition(BaseModel):
  id: str
  portfolio_id: str = Field(alias="portfolioId")
  security_id: str = Field(alias="securityId")
  security_name: Optional[str] = Field(alias="securityName")
  entity_name: Optional[str] = Field(alias="entityName")
  quantity: float
  quantity_type: str = Field(alias="quantityType")
  cost_basis: int = Field(alias="costBasis")
  cost_basis_dollars: float = Field(alias="costBasisDollars")
  currency: str
  current_value: Optional[int] = Field(alias="currentValue")
  current_value_dollars: Optional[float] = Field(alias="currentValueDollars")
  valuation_date: Optional[str] = Field(alias="valuationDate")
  valuation_source: Optional[str] = Field(alias="valuationSource")
  acquisition_date: Optional[str] = Field(alias="acquisitionDate")
  disposition_date: Optional[str] = Field(alias="dispositionDate")
  status: str
  notes: Optional[str]
  created_at: str = Field(alias="createdAt")
  updated_at: str = Field(alias="updatedAt")


GetInvestorPosition.model_rebuild()
