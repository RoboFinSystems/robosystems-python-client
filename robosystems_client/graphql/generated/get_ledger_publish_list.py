from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerPublishList(BaseModel):
  publish_list: Optional["GetLedgerPublishListPublishList"] = Field(alias="publishList")


class GetLedgerPublishListPublishList(BaseModel):
  id: str
  name: str
  description: Optional[str]
  member_count: int = Field(alias="memberCount")
  created_by: str = Field(alias="createdBy")
  created_at: str = Field(alias="createdAt")
  updated_at: str = Field(alias="updatedAt")
  members: list["GetLedgerPublishListPublishListMembers"]


class GetLedgerPublishListPublishListMembers(BaseModel):
  id: str
  target_graph_id: str = Field(alias="targetGraphId")
  target_graph_name: Optional[str] = Field(alias="targetGraphName")
  target_org_name: Optional[str] = Field(alias="targetOrgName")
  added_by: str = Field(alias="addedBy")
  added_at: str = Field(alias="addedAt")


GetLedgerPublishList.model_rebuild()
GetLedgerPublishListPublishList.model_rebuild()
