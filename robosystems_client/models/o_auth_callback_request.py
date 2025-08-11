from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthCallbackRequest")


@_attrs_define
class OAuthCallbackRequest:
  """OAuth callback parameters.

  Attributes:
      code (str): Authorization code from OAuth provider
      state (str): OAuth state for verification
      realm_id (Union[None, Unset, str]): QuickBooks-specific realm ID
      error (Union[None, Unset, str]): OAuth error if authorization failed
      error_description (Union[None, Unset, str]): OAuth error details
  """

  code: str
  state: str
  realm_id: Union[None, Unset, str] = UNSET
  error: Union[None, Unset, str] = UNSET
  error_description: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    code = self.code

    state = self.state

    realm_id: Union[None, Unset, str]
    if isinstance(self.realm_id, Unset):
      realm_id = UNSET
    else:
      realm_id = self.realm_id

    error: Union[None, Unset, str]
    if isinstance(self.error, Unset):
      error = UNSET
    else:
      error = self.error

    error_description: Union[None, Unset, str]
    if isinstance(self.error_description, Unset):
      error_description = UNSET
    else:
      error_description = self.error_description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "code": code,
        "state": state,
      }
    )
    if realm_id is not UNSET:
      field_dict["realm_id"] = realm_id
    if error is not UNSET:
      field_dict["error"] = error
    if error_description is not UNSET:
      field_dict["error_description"] = error_description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    code = d.pop("code")

    state = d.pop("state")

    def _parse_realm_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    realm_id = _parse_realm_id(d.pop("realm_id", UNSET))

    def _parse_error(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    error = _parse_error(d.pop("error", UNSET))

    def _parse_error_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    error_description = _parse_error_description(d.pop("error_description", UNSET))

    o_auth_callback_request = cls(
      code=code,
      state=state,
      realm_id=realm_id,
      error=error,
      error_description=error_description,
    )

    o_auth_callback_request.additional_properties = d
    return o_auth_callback_request

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
