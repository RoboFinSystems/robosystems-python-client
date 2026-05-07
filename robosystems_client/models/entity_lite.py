from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityLite")


@_attrs_define
class EntityLite:
  """Lightweight entity projection for embedding in portfolio-block /
  position envelopes. Carries identity-only fields; full entity data
  lives behind the Master Data entity APIs.

      Attributes:
          id (str): Entity ID (`ent_*` ULID).
          name (str): Display name of the entity.
          source_graph_id (None | str | Unset): Tenant graph this entity is anchored to, when known. `null` for entities
              not yet linked to a graph.
  """

  id: str
  name: str
  source_graph_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    source_graph_id: None | str | Unset
    if isinstance(self.source_graph_id, Unset):
      source_graph_id = UNSET
    else:
      source_graph_id = self.source_graph_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
      }
    )
    if source_graph_id is not UNSET:
      field_dict["source_graph_id"] = source_graph_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    def _parse_source_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_id = _parse_source_graph_id(d.pop("source_graph_id", UNSET))

    entity_lite = cls(
      id=id,
      name=name,
      source_graph_id=source_graph_id,
    )

    entity_lite.additional_properties = d
    return entity_lite

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
