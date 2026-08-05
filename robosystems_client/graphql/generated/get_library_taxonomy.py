from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLibraryTaxonomy(BaseModel):
  library_taxonomy: Optional["GetLibraryTaxonomyLibraryTaxonomy"] = Field(
    alias="libraryTaxonomy"
  )


class GetLibraryTaxonomyLibraryTaxonomy(BaseModel):
  id: str
  name: str
  description: Optional[str]
  standard: Optional[str]
  version: Optional[str]
  namespace_uri: Optional[str] = Field(alias="namespaceUri")
  taxonomy_type: str = Field(alias="taxonomyType")
  is_shared: bool = Field(alias="isShared")
  is_active: bool = Field(alias="isActive")
  is_locked: bool = Field(alias="isLocked")
  element_count: Optional[int] = Field(alias="elementCount")


GetLibraryTaxonomy.model_rebuild()
