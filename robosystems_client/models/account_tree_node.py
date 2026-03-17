from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountTreeNode")


@_attrs_define
class AccountTreeNode:
  """
  Attributes:
      id (str):
      code (str):
      name (str):
      classification (str):
      balance_type (str):
      depth (int):
      is_active (bool):
      children (list[AccountTreeNode] | Unset):
  """

  id: str
  code: str
  name: str
  classification: str
  balance_type: str
  depth: int
  is_active: bool
  children: list[AccountTreeNode] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    code = self.code

    name = self.name

    classification = self.classification

    balance_type = self.balance_type

    depth = self.depth

    is_active = self.is_active

    children: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.children, Unset):
      children = []
      for children_item_data in self.children:
        children_item = children_item_data.to_dict()
        children.append(children_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "code": code,
        "name": name,
        "classification": classification,
        "balance_type": balance_type,
        "depth": depth,
        "is_active": is_active,
      }
    )
    if children is not UNSET:
      field_dict["children"] = children

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    code = d.pop("code")

    name = d.pop("name")

    classification = d.pop("classification")

    balance_type = d.pop("balance_type")

    depth = d.pop("depth")

    is_active = d.pop("is_active")

    _children = d.pop("children", UNSET)
    children: list[AccountTreeNode] | Unset = UNSET
    if _children is not UNSET:
      children = []
      for children_item_data in _children:
        children_item = AccountTreeNode.from_dict(children_item_data)

        children.append(children_item)

    account_tree_node = cls(
      id=id,
      code=code,
      name=name,
      classification=classification,
      balance_type=balance_type,
      depth=depth,
      is_active=is_active,
      children=children,
    )

    account_tree_node.additional_properties = d
    return account_tree_node

  @property
  def additional_keys(self) -> list[str]:
    return list(self.additional_properties.keys())

  def __getitem__(self, key: str) -> Any:
    return self.additional_properties[key]

  def __setitem__(self, key: str, value: Any) -> None:
    self.additional_properties[key] = value

  def __delitem__(self, key: str) -> None:
    del self.additional_properties[key]

  def __contains__(self, key: str) -> bool:
    return key in self.additional_properties
