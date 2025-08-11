from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.account_info import AccountInfo


T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
  """User information response model.

  Example:
      {'accounts': [{'provider': 'github', 'provider_account_id': '12345', 'provider_type': 'oauth'}, {'provider':
          'google', 'provider_account_id': '67890', 'provider_type': 'oauth'}], 'email': 'john@example.com', 'id':
          'user-123', 'name': 'johndoe'}

  Attributes:
      id (str): Unique identifier for the user
      name (Union[None, Unset, str]): User's display name
      email (Union[None, Unset, str]): User's email address
      accounts (Union[Unset, list['AccountInfo']]): User's authentication accounts
  """

  id: str
  name: Union[None, Unset, str] = UNSET
  email: Union[None, Unset, str] = UNSET
  accounts: Union[Unset, list["AccountInfo"]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name: Union[None, Unset, str]
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    email: Union[None, Unset, str]
    if isinstance(self.email, Unset):
      email = UNSET
    else:
      email = self.email

    accounts: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(self.accounts, Unset):
      accounts = []
      for accounts_item_data in self.accounts:
        accounts_item = accounts_item_data.to_dict()
        accounts.append(accounts_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if email is not UNSET:
      field_dict["email"] = email
    if accounts is not UNSET:
      field_dict["accounts"] = accounts

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.account_info import AccountInfo

    d = dict(src_dict)
    id = d.pop("id")

    def _parse_name(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_email(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    email = _parse_email(d.pop("email", UNSET))

    accounts = []
    _accounts = d.pop("accounts", UNSET)
    for accounts_item_data in _accounts or []:
      accounts_item = AccountInfo.from_dict(accounts_item_data)

      accounts.append(accounts_item)

    user_response = cls(
      id=id,
      name=name,
      email=email,
      accounts=accounts,
    )

    user_response.additional_properties = d
    return user_response

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
