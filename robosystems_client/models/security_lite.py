from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entity_lite import EntityLite


T = TypeVar("T", bound="SecurityLite")


@_attrs_define
class SecurityLite:
  """Lightweight security projection for embedding in position
  envelopes. Skips `terms`, `outstanding_shares`, etc. — fetch the
  full `SecurityResponse` when those are needed.

      Attributes:
          id (str): Security ID (`sec_*` ULID).
          name (str): Display name of the security.
          security_type (str): Instrument family (e.g. `common_stock`, `preferred_stock`, `warrant`).
          is_active (bool): `true` when the security is in active status.
          security_subtype (None | str | Unset): Optional subtype refinement (e.g. `class_a`).
          issuer (EntityLite | None | Unset): Embedded issuer entity, when one is linked. `null` for pre-issuer
              securities.
          source_graph_id (None | str | Unset): Tenant graph the security is pre-associated to, if any.
  """

  id: str
  name: str
  security_type: str
  is_active: bool
  security_subtype: None | str | Unset = UNSET
  issuer: EntityLite | None | Unset = UNSET
  source_graph_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.entity_lite import EntityLite

    id = self.id

    name = self.name

    security_type = self.security_type

    is_active = self.is_active

    security_subtype: None | str | Unset
    if isinstance(self.security_subtype, Unset):
      security_subtype = UNSET
    else:
      security_subtype = self.security_subtype

    issuer: dict[str, Any] | None | Unset
    if isinstance(self.issuer, Unset):
      issuer = UNSET
    elif isinstance(self.issuer, EntityLite):
      issuer = self.issuer.to_dict()
    else:
      issuer = self.issuer

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
        "security_type": security_type,
        "is_active": is_active,
      }
    )
    if security_subtype is not UNSET:
      field_dict["security_subtype"] = security_subtype
    if issuer is not UNSET:
      field_dict["issuer"] = issuer
    if source_graph_id is not UNSET:
      field_dict["source_graph_id"] = source_graph_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entity_lite import EntityLite

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    security_type = d.pop("security_type")

    is_active = d.pop("is_active")

    def _parse_security_subtype(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    security_subtype = _parse_security_subtype(d.pop("security_subtype", UNSET))

    def _parse_issuer(data: object) -> EntityLite | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        issuer_type_0 = EntityLite.from_dict(data)

        return issuer_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EntityLite | None | Unset, data)

    issuer = _parse_issuer(d.pop("issuer", UNSET))

    def _parse_source_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_id = _parse_source_graph_id(d.pop("source_graph_id", UNSET))

    security_lite = cls(
      id=id,
      name=name,
      security_type=security_type,
      is_active=is_active,
      security_subtype=security_subtype,
      issuer=issuer,
      source_graph_id=source_graph_id,
    )

    security_lite.additional_properties = d
    return security_lite

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
