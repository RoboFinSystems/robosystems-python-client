from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class SearchLibraryElements(BaseModel):
  search_library_elements: list["SearchLibraryElementsSearchLibraryElements"] = Field(
    alias="searchLibraryElements"
  )


class SearchLibraryElementsSearchLibraryElements(BaseModel):
  id: str
  qname: str
  namespace: Optional[str]
  name: str
  trait: Optional[str]
  balance_type: str = Field(alias="balanceType")
  period_type: str = Field(alias="periodType")
  is_abstract: bool = Field(alias="isAbstract")
  is_monetary: bool = Field(alias="isMonetary")
  element_type: str = Field(alias="elementType")
  source: str
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  parent_id: Optional[str] = Field(alias="parentId")
  labels: list["SearchLibraryElementsSearchLibraryElementsLabels"]
  references: list["SearchLibraryElementsSearchLibraryElementsReferences"]


class SearchLibraryElementsSearchLibraryElementsLabels(BaseModel):
  role: str
  language: str
  text: str


class SearchLibraryElementsSearchLibraryElementsReferences(BaseModel):
  ref_type: Optional[str] = Field(alias="refType")
  citation: str
  uri: Optional[str]


SearchLibraryElements.model_rebuild()
SearchLibraryElementsSearchLibraryElements.model_rebuild()
