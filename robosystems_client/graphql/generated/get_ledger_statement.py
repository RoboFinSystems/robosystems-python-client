from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerStatement(BaseModel):
  statement: Optional["GetLedgerStatementStatement"]


class GetLedgerStatementStatement(BaseModel):
  report_id: str = Field(alias="reportId")
  structure_id: str = Field(alias="structureId")
  structure_name: str = Field(alias="structureName")
  block_type: str = Field(alias="blockType")
  unmapped_count: int = Field(alias="unmappedCount")
  periods: list["GetLedgerStatementStatementPeriods"]
  rows: list["GetLedgerStatementStatementRows"]
  validation: Optional["GetLedgerStatementStatementValidation"]


class GetLedgerStatementStatementPeriods(BaseModel):
  start: str
  end: str
  label: str


class GetLedgerStatementStatementRows(BaseModel):
  element_id: str = Field(alias="elementId")
  element_qname: str = Field(alias="elementQname")
  element_name: str = Field(alias="elementName")
  trait: Optional[str]
  values: list[Optional[float]]
  is_subtotal: bool = Field(alias="isSubtotal")
  depth: int


class GetLedgerStatementStatementValidation(BaseModel):
  passed: bool
  checks: list[str]
  failures: list[str]
  warnings: list[str]


GetLedgerStatement.model_rebuild()
GetLedgerStatementStatement.model_rebuild()
