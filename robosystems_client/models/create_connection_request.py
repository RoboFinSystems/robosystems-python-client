from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_connection_request_provider import CreateConnectionRequestProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.plaid_connection_config import PlaidConnectionConfig
  from ..models.quick_books_connection_config import QuickBooksConnectionConfig
  from ..models.sec_connection_config import SECConnectionConfig


T = TypeVar("T", bound="CreateConnectionRequest")


@_attrs_define
class CreateConnectionRequest:
  """Request to create a new connection.

  Attributes:
      provider (CreateConnectionRequestProvider): Connection provider type
      entity_id (str): Entity identifier
      sec_config (Union['SECConnectionConfig', None, Unset]):
      quickbooks_config (Union['QuickBooksConnectionConfig', None, Unset]):
      plaid_config (Union['PlaidConnectionConfig', None, Unset]):
  """

  provider: CreateConnectionRequestProvider
  entity_id: str
  sec_config: Union["SECConnectionConfig", None, Unset] = UNSET
  quickbooks_config: Union["QuickBooksConnectionConfig", None, Unset] = UNSET
  plaid_config: Union["PlaidConnectionConfig", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.plaid_connection_config import PlaidConnectionConfig
    from ..models.quick_books_connection_config import QuickBooksConnectionConfig
    from ..models.sec_connection_config import SECConnectionConfig

    provider = self.provider.value

    entity_id = self.entity_id

    sec_config: Union[None, Unset, dict[str, Any]]
    if isinstance(self.sec_config, Unset):
      sec_config = UNSET
    elif isinstance(self.sec_config, SECConnectionConfig):
      sec_config = self.sec_config.to_dict()
    else:
      sec_config = self.sec_config

    quickbooks_config: Union[None, Unset, dict[str, Any]]
    if isinstance(self.quickbooks_config, Unset):
      quickbooks_config = UNSET
    elif isinstance(self.quickbooks_config, QuickBooksConnectionConfig):
      quickbooks_config = self.quickbooks_config.to_dict()
    else:
      quickbooks_config = self.quickbooks_config

    plaid_config: Union[None, Unset, dict[str, Any]]
    if isinstance(self.plaid_config, Unset):
      plaid_config = UNSET
    elif isinstance(self.plaid_config, PlaidConnectionConfig):
      plaid_config = self.plaid_config.to_dict()
    else:
      plaid_config = self.plaid_config

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "provider": provider,
        "entity_id": entity_id,
      }
    )
    if sec_config is not UNSET:
      field_dict["sec_config"] = sec_config
    if quickbooks_config is not UNSET:
      field_dict["quickbooks_config"] = quickbooks_config
    if plaid_config is not UNSET:
      field_dict["plaid_config"] = plaid_config

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.plaid_connection_config import PlaidConnectionConfig
    from ..models.quick_books_connection_config import QuickBooksConnectionConfig
    from ..models.sec_connection_config import SECConnectionConfig

    d = dict(src_dict)
    provider = CreateConnectionRequestProvider(d.pop("provider"))

    entity_id = d.pop("entity_id")

    def _parse_sec_config(data: object) -> Union["SECConnectionConfig", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        sec_config_type_0 = SECConnectionConfig.from_dict(data)

        return sec_config_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SECConnectionConfig", None, Unset], data)

    sec_config = _parse_sec_config(d.pop("sec_config", UNSET))

    def _parse_quickbooks_config(
      data: object,
    ) -> Union["QuickBooksConnectionConfig", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        quickbooks_config_type_0 = QuickBooksConnectionConfig.from_dict(data)

        return quickbooks_config_type_0
      except:  # noqa: E722
        pass
      return cast(Union["QuickBooksConnectionConfig", None, Unset], data)

    quickbooks_config = _parse_quickbooks_config(d.pop("quickbooks_config", UNSET))

    def _parse_plaid_config(
      data: object,
    ) -> Union["PlaidConnectionConfig", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        plaid_config_type_0 = PlaidConnectionConfig.from_dict(data)

        return plaid_config_type_0
      except:  # noqa: E722
        pass
      return cast(Union["PlaidConnectionConfig", None, Unset], data)

    plaid_config = _parse_plaid_config(d.pop("plaid_config", UNSET))

    create_connection_request = cls(
      provider=provider,
      entity_id=entity_id,
      sec_config=sec_config,
      quickbooks_config=quickbooks_config,
      plaid_config=plaid_config,
    )

    create_connection_request.additional_properties = d
    return create_connection_request

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
