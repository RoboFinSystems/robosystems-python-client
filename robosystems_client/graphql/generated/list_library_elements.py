from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLibraryElements(BaseModel):
  library_elements: list["ListLibraryElementsLibraryElements"] = Field(
    alias="libraryElements"
  )


class ListLibraryElementsLibraryElements(BaseModel):
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
  labels: Optional[list["ListLibraryElementsLibraryElementsLabels"]] = None
  references: Optional[list["ListLibraryElementsLibraryElementsReferences"]] = None


class ListLibraryElementsLibraryElementsLabels(BaseModel):
  role: str
  language: str
  text: str


class ListLibraryElementsLibraryElementsReferences(BaseModel):
  ref_type: Optional[str] = Field(alias="refType")
  citation: str
  uri: Optional[str]


ListLibraryElements.model_rebuild()
ListLibraryElementsLibraryElements.model_rebuild()
