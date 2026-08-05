from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLibraryTaxonomyArcs(BaseModel):
  library_taxonomy_arc_count: int = Field(alias="libraryTaxonomyArcCount")
  library_taxonomy_arcs: list["ListLibraryTaxonomyArcsLibraryTaxonomyArcs"] = Field(
    alias="libraryTaxonomyArcs"
  )


class ListLibraryTaxonomyArcsLibraryTaxonomyArcs(BaseModel):
  id: str
  structure_id: str = Field(alias="structureId")
  structure_name: Optional[str] = Field(alias="structureName")
  from_element_id: str = Field(alias="fromElementId")
  from_element_qname: Optional[str] = Field(alias="fromElementQname")
  from_element_name: Optional[str] = Field(alias="fromElementName")
  from_element_trait: Optional[str] = Field(alias="fromElementTrait")
  from_element_is_abstract: Optional[bool] = Field(alias="fromElementIsAbstract")
  to_element_id: str = Field(alias="toElementId")
  to_element_qname: Optional[str] = Field(alias="toElementQname")
  to_element_name: Optional[str] = Field(alias="toElementName")
  to_element_trait: Optional[str] = Field(alias="toElementTrait")
  to_element_is_abstract: Optional[bool] = Field(alias="toElementIsAbstract")
  association_type: str = Field(alias="associationType")
  arcrole: Optional[str]
  order_value: Optional[float] = Field(alias="orderValue")
  weight: Optional[float]


ListLibraryTaxonomyArcs.model_rebuild()
