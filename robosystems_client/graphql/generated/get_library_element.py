from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLibraryElement(BaseModel):
  library_element: Optional["GetLibraryElementLibraryElement"] = Field(
    alias="libraryElement"
  )


class GetLibraryElementLibraryElement(BaseModel):
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
  labels: list["GetLibraryElementLibraryElementLabels"]
  references: list["GetLibraryElementLibraryElementReferences"]


class GetLibraryElementLibraryElementLabels(BaseModel):
  role: str
  language: str
  text: str


class GetLibraryElementLibraryElementReferences(BaseModel):
  ref_type: Optional[str] = Field(alias="refType")
  citation: str
  uri: Optional[str]


GetLibraryElement.model_rebuild()
GetLibraryElementLibraryElement.model_rebuild()
