from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.pagination_info import PaginationInfo
  from ..models.publish_list_response import PublishListResponse


T = TypeVar("T", bound="PublishListListResponse")


@_attrs_define
class PublishListListResponse:
  """
  Attributes:
      publish_lists (list[PublishListResponse]):
      pagination (PaginationInfo): Pagination information for list responses. Example: {'has_more': True, 'limit': 20,
          'offset': 0, 'total': 100}.
  """

  publish_lists: list[PublishListResponse]
  pagination: PaginationInfo
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    publish_lists = []
    for publish_lists_item_data in self.publish_lists:
      publish_lists_item = publish_lists_item_data.to_dict()
      publish_lists.append(publish_lists_item)

    pagination = self.pagination.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "publish_lists": publish_lists,
        "pagination": pagination,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.pagination_info import PaginationInfo
    from ..models.publish_list_response import PublishListResponse

    d = dict(src_dict)
    publish_lists = []
    _publish_lists = d.pop("publish_lists")
    for publish_lists_item_data in _publish_lists:
      publish_lists_item = PublishListResponse.from_dict(publish_lists_item_data)

      publish_lists.append(publish_lists_item)

    pagination = PaginationInfo.from_dict(d.pop("pagination"))

    publish_list_list_response = cls(
      publish_lists=publish_lists,
      pagination=pagination,
    )

    publish_list_list_response.additional_properties = d
    return publish_list_list_response

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
