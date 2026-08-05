from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLibraryElementArcs(BaseModel):
  library_element_arcs: list["GetLibraryElementArcsLibraryElementArcs"] = Field(
    alias="libraryElementArcs"
  )


class GetLibraryElementArcsLibraryElementArcs(BaseModel):
  id: str
  direction: str
  association_type: str = Field(alias="associationType")
  arcrole: Optional[str]
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  taxonomy_standard: Optional[str] = Field(alias="taxonomyStandard")
  taxonomy_name: Optional[str] = Field(alias="taxonomyName")
  structure_id: Optional[str] = Field(alias="structureId")
  structure_name: Optional[str] = Field(alias="structureName")
  peer: "GetLibraryElementArcsLibraryElementArcsPeer"


class GetLibraryElementArcsLibraryElementArcsPeer(BaseModel):
  id: str
  qname: str
  name: str
  trait: Optional[str]
  source: str


GetLibraryElementArcs.model_rebuild()
GetLibraryElementArcsLibraryElementArcs.model_rebuild()
