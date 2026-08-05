from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLibraryElementEquivalents(BaseModel):
  library_element_equivalents: Optional[
    "GetLibraryElementEquivalentsLibraryElementEquivalents"
  ] = Field(alias="libraryElementEquivalents")


class GetLibraryElementEquivalentsLibraryElementEquivalents(BaseModel):
  element: "GetLibraryElementEquivalentsLibraryElementEquivalentsElement"
  equivalents: list["GetLibraryElementEquivalentsLibraryElementEquivalentsEquivalents"]


class GetLibraryElementEquivalentsLibraryElementEquivalentsElement(BaseModel):
  id: str
  qname: str
  name: str
  trait: Optional[str]
  source: str


class GetLibraryElementEquivalentsLibraryElementEquivalentsEquivalents(BaseModel):
  id: str
  qname: str
  name: str
  trait: Optional[str]
  source: str


GetLibraryElementEquivalents.model_rebuild()
GetLibraryElementEquivalentsLibraryElementEquivalents.model_rebuild()
