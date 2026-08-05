from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLibraryElementClassifications(BaseModel):
  library_element_classifications: list[
    "GetLibraryElementClassificationsLibraryElementClassifications"
  ] = Field(alias="libraryElementClassifications")


class GetLibraryElementClassificationsLibraryElementClassifications(BaseModel):
  category: str
  identifier: str
  name: Optional[str]
  is_primary: bool = Field(alias="isPrimary")


GetLibraryElementClassifications.model_rebuild()
