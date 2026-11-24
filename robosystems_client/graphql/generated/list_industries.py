from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListIndustries(BaseModel):
  industries: list["ListIndustriesIndustries"]


class ListIndustriesIndustries(BaseModel):
  id: str
  parent_id: Optional[str] = Field(alias="parentId")
  level: str
  label: str
  path: list[str]
  carried: bool
  replaced_by: Optional[str] = Field(alias="replacedBy")


ListIndustries.model_rebuild()
