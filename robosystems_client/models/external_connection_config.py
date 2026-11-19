from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalConnectionConfig")


@_attrs_define
class ExternalConnectionConfig:
  """External-integration connection configuration.

  Registers a source namespace for an integration the platform does not
  run: the connection is registration + telemetry, not execution config.
  The platform holds no credentials for the external source — the
  integration authenticates to its own source and writes here through
  the public API, stamping `source_name` on everything it emits.

      Attributes:
          source_name (str): Source slug the integration stamps on the events it emits (lowercase letters, digits, '-',
              '_'; must start with a letter). Unique per graph among live connections.
          display_name (None | str | Unset): Human-readable label for the connections UI.
          ledger (bool | Unset): The source is the general ledger that keeps an entity's books. The connection becomes
              that entity's ledger of record in `shadow`: the journal entries the source sends land posted, nothing else posts
              to those books, nothing is written back, and the close stamps the period without posting. Refused (409) when
              another ledger already keeps the entity's books or the entity has books of its own. Default: False.
          entity_id (None | str | Unset): With `ledger`, the entity whose books the source keeps: a subsidiary's id, or
              omit for the group parent. One source keeps one entity's books; register a source per entity.
  """

  source_name: str
  display_name: None | str | Unset = UNSET
  ledger: bool | Unset = False
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    source_name = self.source_name

    display_name: None | str | Unset
    if isinstance(self.display_name, Unset):
      display_name = UNSET
    else:
      display_name = self.display_name

    ledger = self.ledger

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "source_name": source_name,
      }
    )
    if display_name is not UNSET:
      field_dict["display_name"] = display_name
    if ledger is not UNSET:
      field_dict["ledger"] = ledger
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    source_name = d.pop("source_name")

    def _parse_display_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    display_name = _parse_display_name(d.pop("display_name", UNSET))

    ledger = d.pop("ledger", UNSET)

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    external_connection_config = cls(
      source_name=source_name,
      display_name=display_name,
      ledger=ledger,
      entity_id=entity_id,
    )

    external_connection_config.additional_properties = d
    return external_connection_config

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
