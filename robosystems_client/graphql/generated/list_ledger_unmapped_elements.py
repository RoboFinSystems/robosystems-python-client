from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerUnmappedElements(BaseModel):
  unmapped_elements: list["ListLedgerUnmappedElementsUnmappedElements"] = Field(
    alias="unmappedElements"
  )


class ListLedgerUnmappedElementsUnmappedElements(BaseModel):
  id: str
  code: Optional[str]
  name: str
  trait: Optional[str]
  balance_type: str = Field(alias="balanceType")
  external_source: Optional[str] = Field(alias="externalSource")
  suggested_targets: list[
    "ListLedgerUnmappedElementsUnmappedElementsSuggestedTargets"
  ] = Field(alias="suggestedTargets")


class ListLedgerUnmappedElementsUnmappedElementsSuggestedTargets(BaseModel):
  element_id: str = Field(alias="elementId")
  qname: str
  name: str
  confidence: Optional[float]


ListLedgerUnmappedElements.model_rebuild()
ListLedgerUnmappedElementsUnmappedElements.model_rebuild()
