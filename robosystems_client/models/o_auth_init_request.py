from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.o_auth_init_request_additional_params_type_0 import (
    OAuthInitRequestAdditionalParamsType0,
  )


T = TypeVar("T", bound="OAuthInitRequest")


@_attrs_define
class OAuthInitRequest:
  """Request to initiate OAuth flow.

  Attributes:
      connection_id (str): Connection ID to link OAuth to
      redirect_uri (Union[None, Unset, str]): Override default redirect URI
      additional_params (Union['OAuthInitRequestAdditionalParamsType0', None, Unset]): Provider-specific parameters
  """

  connection_id: str
  redirect_uri: Union[None, Unset, str] = UNSET
  additional_params: Union["OAuthInitRequestAdditionalParamsType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.o_auth_init_request_additional_params_type_0 import (
      OAuthInitRequestAdditionalParamsType0,
    )

    connection_id = self.connection_id

    redirect_uri: Union[None, Unset, str]
    if isinstance(self.redirect_uri, Unset):
      redirect_uri = UNSET
    else:
      redirect_uri = self.redirect_uri

    additional_params: Union[None, Unset, dict[str, Any]]
    if isinstance(self.additional_params, Unset):
      additional_params = UNSET
    elif isinstance(self.additional_params, OAuthInitRequestAdditionalParamsType0):
      additional_params = self.additional_params.to_dict()
    else:
      additional_params = self.additional_params

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "connection_id": connection_id,
      }
    )
    if redirect_uri is not UNSET:
      field_dict["redirect_uri"] = redirect_uri
    if additional_params is not UNSET:
      field_dict["additional_params"] = additional_params

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.o_auth_init_request_additional_params_type_0 import (
      OAuthInitRequestAdditionalParamsType0,
    )

    d = dict(src_dict)
    connection_id = d.pop("connection_id")

    def _parse_redirect_uri(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    redirect_uri = _parse_redirect_uri(d.pop("redirect_uri", UNSET))

    def _parse_additional_params(
      data: object,
    ) -> Union["OAuthInitRequestAdditionalParamsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        additional_params_type_0 = OAuthInitRequestAdditionalParamsType0.from_dict(data)

        return additional_params_type_0
      except:  # noqa: E722
        pass
      return cast(Union["OAuthInitRequestAdditionalParamsType0", None, Unset], data)

    additional_params = _parse_additional_params(d.pop("additional_params", UNSET))

    o_auth_init_request = cls(
      connection_id=connection_id,
      redirect_uri=redirect_uri,
      additional_params=additional_params,
    )

    o_auth_init_request.additional_properties = d
    return o_auth_init_request

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
