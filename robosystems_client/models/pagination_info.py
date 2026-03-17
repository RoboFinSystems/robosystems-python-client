from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationInfo")


@_attrs_define
class PaginationInfo:
  """Pagination information for list responses.

  Example:
      {'has_more': True, 'limit': 20, 'offset': 0, 'total': 100}

  Attributes:
      total (int): Total number of items available
      limit (int): Maximum number of items returned in this response
      offset (int): Number of items skipped
      has_more (bool): Whether more items are available
  """

  total: int
  limit: int
  offset: int
  has_more: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total = self.total

    limit = self.limit

    offset = self.offset

    has_more = self.has_more

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total": total,
        "limit": limit,
        "offset": offset,
        "has_more": has_more,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    total = d.pop("total")

    limit = d.pop("limit")

    offset = d.pop("offset")

    has_more = d.pop("has_more")

    pagination_info = cls(
      total=total,
      limit=limit,
      offset=offset,
      has_more=has_more,
    )

    pagination_info.additional_properties = d
    return pagination_info

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
