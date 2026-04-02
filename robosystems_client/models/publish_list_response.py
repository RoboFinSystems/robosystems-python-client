from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishListResponse")


@_attrs_define
class PublishListResponse:
  """
  Attributes:
      id (str):
      name (str):
      created_by (str):
      created_at (datetime.datetime):
      updated_at (datetime.datetime):
      description (None | str | Unset):
      member_count (int | Unset):  Default: 0.
  """

  id: str
  name: str
  created_by: str
  created_at: datetime.datetime
  updated_at: datetime.datetime
  description: None | str | Unset = UNSET
  member_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    created_by = self.created_by

    created_at = self.created_at.isoformat()

    updated_at = self.updated_at.isoformat()

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    member_count = self.member_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "created_by": created_by,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if member_count is not UNSET:
      field_dict["member_count"] = member_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    created_by = d.pop("created_by")

    created_at = isoparse(d.pop("created_at"))

    updated_at = isoparse(d.pop("updated_at"))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    member_count = d.pop("member_count", UNSET)

    publish_list_response = cls(
      id=id,
      name=name,
      created_by=created_by,
      created_at=created_at,
      updated_at=updated_at,
      description=description,
      member_count=member_count,
    )

    publish_list_response.additional_properties = d
    return publish_list_response

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
