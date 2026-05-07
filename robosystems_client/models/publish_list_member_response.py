from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishListMemberResponse")


@_attrs_define
class PublishListMemberResponse:
  """One recipient graph in a publish list.

  Attributes:
      id (str): Membership row identifier (ULID).
      target_graph_id (str): Recipient graph ID.
      added_by (str): User ID that added this member.
      added_at (datetime.datetime): When the member was added.
      target_graph_name (None | str | Unset): Display name of the recipient graph (if known).
      target_org_name (None | str | Unset): Display name of the org that owns the recipient graph.
  """

  id: str
  target_graph_id: str
  added_by: str
  added_at: datetime.datetime
  target_graph_name: None | str | Unset = UNSET
  target_org_name: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    target_graph_id = self.target_graph_id

    added_by = self.added_by

    added_at = self.added_at.isoformat()

    target_graph_name: None | str | Unset
    if isinstance(self.target_graph_name, Unset):
      target_graph_name = UNSET
    else:
      target_graph_name = self.target_graph_name

    target_org_name: None | str | Unset
    if isinstance(self.target_org_name, Unset):
      target_org_name = UNSET
    else:
      target_org_name = self.target_org_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "target_graph_id": target_graph_id,
        "added_by": added_by,
        "added_at": added_at,
      }
    )
    if target_graph_name is not UNSET:
      field_dict["target_graph_name"] = target_graph_name
    if target_org_name is not UNSET:
      field_dict["target_org_name"] = target_org_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    target_graph_id = d.pop("target_graph_id")

    added_by = d.pop("added_by")

    added_at = isoparse(d.pop("added_at"))

    def _parse_target_graph_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_graph_name = _parse_target_graph_name(d.pop("target_graph_name", UNSET))

    def _parse_target_org_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_org_name = _parse_target_org_name(d.pop("target_org_name", UNSET))

    publish_list_member_response = cls(
      id=id,
      target_graph_id=target_graph_id,
      added_by=added_by,
      added_at=added_at,
      target_graph_name=target_graph_name,
      target_org_name=target_org_name,
    )

    publish_list_member_response.additional_properties = d
    return publish_list_member_response

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
