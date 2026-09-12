from pydantic import Field

from .base_model import BaseModel


class ListChartTemplates(BaseModel):
  chart_templates: list["ListChartTemplatesChartTemplates"] = Field(
    alias="chartTemplates"
  )


class ListChartTemplatesChartTemplates(BaseModel):
  key: str
  display_name: str = Field(alias="displayName")
  description: str
  account_count: int = Field(alias="accountCount")


ListChartTemplates.model_rebuild()
