from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ClassificationStats(BaseModel):
  classification_stats: Optional["ClassificationStatsClassificationStats"] = Field(
    alias="classificationStats"
  )


class ClassificationStatsClassificationStats(BaseModel):
  period: str
  entity_id: Optional[str] = Field(alias="entityId")
  lines: int
  accepted: int
  overridden: int
  unsuggested: int
  split: int
  unstamped: int
  human_choice_share: Optional[float] = Field(alias="humanChoiceShare")
  open_lines: int = Field(alias="openLines")
  by_source: list["ClassificationStatsClassificationStatsBySource"] = Field(
    alias="bySource"
  )


class ClassificationStatsClassificationStatsBySource(BaseModel):
  source: str
  lines: int
  accepted: int
  overridden: int
  unsuggested: int
  split: int


ClassificationStats.model_rebuild()
ClassificationStatsClassificationStats.model_rebuild()
