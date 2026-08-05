from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerPublishLists(BaseModel):
  publish_lists: Optional["ListLedgerPublishListsPublishLists"] = Field(
    alias="publishLists"
  )


class ListLedgerPublishListsPublishLists(BaseModel):
  publish_lists: list["ListLedgerPublishListsPublishListsPublishLists"] = Field(
    alias="publishLists"
  )
  pagination: "ListLedgerPublishListsPublishListsPagination"


class ListLedgerPublishListsPublishListsPublishLists(BaseModel):
  id: str
  name: str
  description: Optional[str]
  member_count: int = Field(alias="memberCount")
  created_by: str = Field(alias="createdBy")
  created_at: str = Field(alias="createdAt")
  updated_at: str = Field(alias="updatedAt")


class ListLedgerPublishListsPublishListsPagination(BaseModel):
  total: int
  limit: int
  offset: int
  has_more: bool = Field(alias="hasMore")


ListLedgerPublishLists.model_rebuild()
ListLedgerPublishListsPublishLists.model_rebuild()
