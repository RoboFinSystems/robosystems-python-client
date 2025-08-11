from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_provider_info_auth_type import ConnectionProviderInfoAuthType
from ..models.connection_provider_info_provider import ConnectionProviderInfoProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionProviderInfo")


@_attrs_define
class ConnectionProviderInfo:
  """Information about a connection provider.

  Attributes:
      provider (ConnectionProviderInfoProvider): Provider identifier
      display_name (str): Human-readable provider name
      description (str): Provider description
      auth_type (ConnectionProviderInfoAuthType): Authentication type
      required_config (list[str]): Required configuration fields
      features (list[str]): Supported features
      data_types (list[str]): Types of data available
      auth_flow (Union[None, Unset, str]): Description of authentication flow
      optional_config (Union[Unset, list[str]]): Optional configuration fields
      sync_frequency (Union[None, Unset, str]): Typical sync frequency
      setup_instructions (Union[None, Unset, str]): Setup instructions
      documentation_url (Union[None, Unset, str]): Link to documentation
  """

  provider: ConnectionProviderInfoProvider
  display_name: str
  description: str
  auth_type: ConnectionProviderInfoAuthType
  required_config: list[str]
  features: list[str]
  data_types: list[str]
  auth_flow: Union[None, Unset, str] = UNSET
  optional_config: Union[Unset, list[str]] = UNSET
  sync_frequency: Union[None, Unset, str] = UNSET
  setup_instructions: Union[None, Unset, str] = UNSET
  documentation_url: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    provider = self.provider.value

    display_name = self.display_name

    description = self.description

    auth_type = self.auth_type.value

    required_config = self.required_config

    features = self.features

    data_types = self.data_types

    auth_flow: Union[None, Unset, str]
    if isinstance(self.auth_flow, Unset):
      auth_flow = UNSET
    else:
      auth_flow = self.auth_flow

    optional_config: Union[Unset, list[str]] = UNSET
    if not isinstance(self.optional_config, Unset):
      optional_config = self.optional_config

    sync_frequency: Union[None, Unset, str]
    if isinstance(self.sync_frequency, Unset):
      sync_frequency = UNSET
    else:
      sync_frequency = self.sync_frequency

    setup_instructions: Union[None, Unset, str]
    if isinstance(self.setup_instructions, Unset):
      setup_instructions = UNSET
    else:
      setup_instructions = self.setup_instructions

    documentation_url: Union[None, Unset, str]
    if isinstance(self.documentation_url, Unset):
      documentation_url = UNSET
    else:
      documentation_url = self.documentation_url

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "provider": provider,
        "display_name": display_name,
        "description": description,
        "auth_type": auth_type,
        "required_config": required_config,
        "features": features,
        "data_types": data_types,
      }
    )
    if auth_flow is not UNSET:
      field_dict["auth_flow"] = auth_flow
    if optional_config is not UNSET:
      field_dict["optional_config"] = optional_config
    if sync_frequency is not UNSET:
      field_dict["sync_frequency"] = sync_frequency
    if setup_instructions is not UNSET:
      field_dict["setup_instructions"] = setup_instructions
    if documentation_url is not UNSET:
      field_dict["documentation_url"] = documentation_url

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    provider = ConnectionProviderInfoProvider(d.pop("provider"))

    display_name = d.pop("display_name")

    description = d.pop("description")

    auth_type = ConnectionProviderInfoAuthType(d.pop("auth_type"))

    required_config = cast(list[str], d.pop("required_config"))

    features = cast(list[str], d.pop("features"))

    data_types = cast(list[str], d.pop("data_types"))

    def _parse_auth_flow(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    auth_flow = _parse_auth_flow(d.pop("auth_flow", UNSET))

    optional_config = cast(list[str], d.pop("optional_config", UNSET))

    def _parse_sync_frequency(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    sync_frequency = _parse_sync_frequency(d.pop("sync_frequency", UNSET))

    def _parse_setup_instructions(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    setup_instructions = _parse_setup_instructions(d.pop("setup_instructions", UNSET))

    def _parse_documentation_url(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

    connection_provider_info = cls(
      provider=provider,
      display_name=display_name,
      description=description,
      auth_type=auth_type,
      required_config=required_config,
      features=features,
      data_types=data_types,
      auth_flow=auth_flow,
      optional_config=optional_config,
      sync_frequency=sync_frequency,
      setup_instructions=setup_instructions,
      documentation_url=documentation_url,
    )

    connection_provider_info.additional_properties = d
    return connection_provider_info

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
