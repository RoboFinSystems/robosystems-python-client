from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLibraryStructures(BaseModel):
  library_structures: list["ListLibraryStructuresLibraryStructures"] = Field(
    alias="libraryStructures"
  )


class ListLibraryStructuresLibraryStructures(BaseModel):
  id: str
  name: str
  block_type: str = Field(alias="blockType")
  taxonomy_id: str = Field(alias="taxonomyId")
  role_uri: Optional[str] = Field(alias="roleUri")
  is_active: bool = Field(alias="isActive")


ListLibraryStructures.model_rebuild()
