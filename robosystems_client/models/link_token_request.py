from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.link_token_request_provider_type_0 import LinkTokenRequestProviderType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.link_token_request_options_type_0 import LinkTokenRequestOptionsType0


T = TypeVar("T", bound="LinkTokenRequest")


@_attrs_define
class LinkTokenRequest:
  """Request to create a link token for embedded authentication.

  Attributes:
      entity_id (str): Entity identifier
      user_id (str): User identifier
      provider (Union[LinkTokenRequestProviderType0, None, Unset]): Provider type (defaults based on connection)
      products (Union[None, Unset, list[str]]): Data products to request (provider-specific)
      options (Union['LinkTokenRequestOptionsType0', None, Unset]): Provider-specific options
  """

  entity_id: str
  user_id: str
  provider: Union[LinkTokenRequestProviderType0, None, Unset] = UNSET
  products: Union[None, Unset, list[str]] = UNSET
  options: Union["LinkTokenRequestOptionsType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.link_token_request_options_type_0 import LinkTokenRequestOptionsType0

    entity_id = self.entity_id

    user_id = self.user_id

    provider: Union[None, Unset, str]
    if isinstance(self.provider, Unset):
      provider = UNSET
    elif isinstance(self.provider, LinkTokenRequestProviderType0):
      provider = self.provider.value
    else:
      provider = self.provider

    products: Union[None, Unset, list[str]]
    if isinstance(self.products, Unset):
      products = UNSET
    elif isinstance(self.products, list):
      products = self.products

    else:
      products = self.products

    options: Union[None, Unset, dict[str, Any]]
    if isinstance(self.options, Unset):
      options = UNSET
    elif isinstance(self.options, LinkTokenRequestOptionsType0):
      options = self.options.to_dict()
    else:
      options = self.options

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "user_id": user_id,
      }
    )
    if provider is not UNSET:
      field_dict["provider"] = provider
    if products is not UNSET:
      field_dict["products"] = products
    if options is not UNSET:
      field_dict["options"] = options

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.link_token_request_options_type_0 import LinkTokenRequestOptionsType0

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    user_id = d.pop("user_id")

    def _parse_provider(
      data: object,
    ) -> Union[LinkTokenRequestProviderType0, None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        provider_type_0 = LinkTokenRequestProviderType0(data)

        return provider_type_0
      except:  # noqa: E722
        pass
      return cast(Union[LinkTokenRequestProviderType0, None, Unset], data)

    provider = _parse_provider(d.pop("provider", UNSET))

    def _parse_products(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        products_type_0 = cast(list[str], data)

        return products_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    products = _parse_products(d.pop("products", UNSET))

    def _parse_options(
      data: object,
    ) -> Union["LinkTokenRequestOptionsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        options_type_0 = LinkTokenRequestOptionsType0.from_dict(data)

        return options_type_0
      except:  # noqa: E722
        pass
      return cast(Union["LinkTokenRequestOptionsType0", None, Unset], data)

    options = _parse_options(d.pop("options", UNSET))

    link_token_request = cls(
      entity_id=entity_id,
      user_id=user_id,
      provider=provider,
      products=products,
      options=options,
    )

    link_token_request.additional_properties = d
    return link_token_request

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
