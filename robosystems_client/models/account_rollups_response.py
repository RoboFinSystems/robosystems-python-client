from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.account_rollup_group import AccountRollupGroup


T = TypeVar("T", bound="AccountRollupsResponse")


@_attrs_define
class AccountRollupsResponse:
  """
  Attributes:
      mapping_id (str):
      mapping_name (str):
      groups (list[AccountRollupGroup]):
      total_mapped (int):
      total_unmapped (int):
  """

  mapping_id: str
  mapping_name: str
  groups: list[AccountRollupGroup]
  total_mapped: int
  total_unmapped: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    mapping_id = self.mapping_id

    mapping_name = self.mapping_name

    groups = []
    for groups_item_data in self.groups:
      groups_item = groups_item_data.to_dict()
      groups.append(groups_item)

    total_mapped = self.total_mapped

    total_unmapped = self.total_unmapped

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "mapping_id": mapping_id,
        "mapping_name": mapping_name,
        "groups": groups,
        "total_mapped": total_mapped,
        "total_unmapped": total_unmapped,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.account_rollup_group import AccountRollupGroup

    d = dict(src_dict)
    mapping_id = d.pop("mapping_id")

    mapping_name = d.pop("mapping_name")

    groups = []
    _groups = d.pop("groups")
    for groups_item_data in _groups:
      groups_item = AccountRollupGroup.from_dict(groups_item_data)

      groups.append(groups_item)

    total_mapped = d.pop("total_mapped")

    total_unmapped = d.pop("total_unmapped")

    account_rollups_response = cls(
      mapping_id=mapping_id,
      mapping_name=mapping_name,
      groups=groups,
      total_mapped=total_mapped,
      total_unmapped=total_unmapped,
    )

    account_rollups_response.additional_properties = d
    return account_rollups_response

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
