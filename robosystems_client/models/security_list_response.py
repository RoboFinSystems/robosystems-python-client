from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.pagination_info import PaginationInfo
  from ..models.security_response import SecurityResponse


T = TypeVar("T", bound="SecurityListResponse")


@_attrs_define
class SecurityListResponse:
  """
  Attributes:
      securities (list[SecurityResponse]):
      pagination (PaginationInfo): Pagination information for list responses. Example: {'has_more': True, 'limit': 20,
          'offset': 0, 'total': 100}.
  """

  securities: list[SecurityResponse]
  pagination: PaginationInfo
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    securities = []
    for securities_item_data in self.securities:
      securities_item = securities_item_data.to_dict()
      securities.append(securities_item)

    pagination = self.pagination.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "securities": securities,
        "pagination": pagination,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.pagination_info import PaginationInfo
    from ..models.security_response import SecurityResponse

    d = dict(src_dict)
    securities = []
    _securities = d.pop("securities")
    for securities_item_data in _securities:
      securities_item = SecurityResponse.from_dict(securities_item_data)

      securities.append(securities_item)

    pagination = PaginationInfo.from_dict(d.pop("pagination"))

    security_list_response = cls(
      securities=securities,
      pagination=pagination,
    )

    security_list_response.additional_properties = d
    return security_list_response

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
