from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.account_response import AccountResponse
  from ..models.pagination_info import PaginationInfo


T = TypeVar("T", bound="AccountListResponse")


@_attrs_define
class AccountListResponse:
  """
  Attributes:
      accounts (list[AccountResponse]):
      pagination (PaginationInfo): Pagination information for list responses. Example: {'has_more': True, 'limit': 20,
          'offset': 0, 'total': 100}.
  """

  accounts: list[AccountResponse]
  pagination: PaginationInfo
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    accounts = []
    for accounts_item_data in self.accounts:
      accounts_item = accounts_item_data.to_dict()
      accounts.append(accounts_item)

    pagination = self.pagination.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "accounts": accounts,
        "pagination": pagination,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.account_response import AccountResponse
    from ..models.pagination_info import PaginationInfo

    d = dict(src_dict)
    accounts = []
    _accounts = d.pop("accounts")
    for accounts_item_data in _accounts:
      accounts_item = AccountResponse.from_dict(accounts_item_data)

      accounts.append(accounts_item)

    pagination = PaginationInfo.from_dict(d.pop("pagination"))

    account_list_response = cls(
      accounts=accounts,
      pagination=pagination,
    )

    account_list_response.additional_properties = d
    return account_list_response

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
