from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerAccountTree(BaseModel):
  account_tree: Optional["GetLedgerAccountTreeAccountTree"] = Field(alias="accountTree")


class GetLedgerAccountTreeAccountTree(BaseModel):
  total_accounts: int = Field(alias="totalAccounts")
  roots: list["GetLedgerAccountTreeAccountTreeRoots"]


class GetLedgerAccountTreeAccountTreeRoots(BaseModel):
  id: str
  code: Optional[str]
  name: str
  trait: Optional[str]
  account_type: Optional[str] = Field(alias="accountType")
  balance_type: str = Field(alias="balanceType")
  depth: int
  is_active: bool = Field(alias="isActive")
  children: list["GetLedgerAccountTreeAccountTreeRootsChildren"]


class GetLedgerAccountTreeAccountTreeRootsChildren(BaseModel):
  id: str
  code: Optional[str]
  name: str
  trait: Optional[str]
  account_type: Optional[str] = Field(alias="accountType")
  balance_type: str = Field(alias="balanceType")
  depth: int
  is_active: bool = Field(alias="isActive")
  children: list["GetLedgerAccountTreeAccountTreeRootsChildrenChildren"]


class GetLedgerAccountTreeAccountTreeRootsChildrenChildren(BaseModel):
  id: str
  code: Optional[str]
  name: str
  trait: Optional[str]
  account_type: Optional[str] = Field(alias="accountType")
  balance_type: str = Field(alias="balanceType")
  depth: int
  is_active: bool = Field(alias="isActive")
  children: list["GetLedgerAccountTreeAccountTreeRootsChildrenChildrenChildren"]


class GetLedgerAccountTreeAccountTreeRootsChildrenChildrenChildren(BaseModel):
  id: str
  code: Optional[str]
  name: str
  trait: Optional[str]
  account_type: Optional[str] = Field(alias="accountType")
  balance_type: str = Field(alias="balanceType")
  depth: int
  is_active: bool = Field(alias="isActive")


GetLedgerAccountTree.model_rebuild()
GetLedgerAccountTreeAccountTree.model_rebuild()
GetLedgerAccountTreeAccountTreeRoots.model_rebuild()
GetLedgerAccountTreeAccountTreeRootsChildren.model_rebuild()
GetLedgerAccountTreeAccountTreeRootsChildrenChildren.model_rebuild()
