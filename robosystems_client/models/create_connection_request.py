from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_connection_request_provider import CreateConnectionRequestProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.quick_books_connection_config import QuickBooksConnectionConfig
  from ..models.sec_connection_config import SECConnectionConfig


T = TypeVar("T", bound="CreateConnectionRequest")


@_attrs_define
class CreateConnectionRequest:
  """Request to create a new connection.

  Attributes:
      provider (CreateConnectionRequestProvider): Connection provider type
      entity_id (None | str | Unset): Entity identifier. Required for QuickBooks, optional for SEC (SEC creates the
          entity from filing data).
      sec_config (None | SECConnectionConfig | Unset):
      quickbooks_config (None | QuickBooksConnectionConfig | Unset):
  """

  provider: CreateConnectionRequestProvider
  entity_id: None | str | Unset = UNSET
  sec_config: None | SECConnectionConfig | Unset = UNSET
  quickbooks_config: None | QuickBooksConnectionConfig | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.quick_books_connection_config import QuickBooksConnectionConfig
    from ..models.sec_connection_config import SECConnectionConfig

    provider = self.provider.value

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    sec_config: dict[str, Any] | None | Unset
    if isinstance(self.sec_config, Unset):
      sec_config = UNSET
    elif isinstance(self.sec_config, SECConnectionConfig):
      sec_config = self.sec_config.to_dict()
    else:
      sec_config = self.sec_config

    quickbooks_config: dict[str, Any] | None | Unset
    if isinstance(self.quickbooks_config, Unset):
      quickbooks_config = UNSET
    elif isinstance(self.quickbooks_config, QuickBooksConnectionConfig):
      quickbooks_config = self.quickbooks_config.to_dict()
    else:
      quickbooks_config = self.quickbooks_config

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "provider": provider,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if sec_config is not UNSET:
      field_dict["sec_config"] = sec_config
    if quickbooks_config is not UNSET:
      field_dict["quickbooks_config"] = quickbooks_config

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.quick_books_connection_config import QuickBooksConnectionConfig
    from ..models.sec_connection_config import SECConnectionConfig

    d = dict(src_dict)
    provider = CreateConnectionRequestProvider(d.pop("provider"))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_sec_config(data: object) -> None | SECConnectionConfig | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        sec_config_type_0 = SECConnectionConfig.from_dict(data)

        return sec_config_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | SECConnectionConfig | Unset, data)

    sec_config = _parse_sec_config(d.pop("sec_config", UNSET))

    def _parse_quickbooks_config(
      data: object,
    ) -> None | QuickBooksConnectionConfig | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        quickbooks_config_type_0 = QuickBooksConnectionConfig.from_dict(data)

        return quickbooks_config_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | QuickBooksConnectionConfig | Unset, data)

    quickbooks_config = _parse_quickbooks_config(d.pop("quickbooks_config", UNSET))

    create_connection_request = cls(
      provider=provider,
      entity_id=entity_id,
      sec_config=sec_config,
      quickbooks_config=quickbooks_config,
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
