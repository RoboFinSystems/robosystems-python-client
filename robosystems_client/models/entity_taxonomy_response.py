from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityTaxonomyResponse")


@_attrs_define
class EntityTaxonomyResponse:
  """Result of `link-entity-taxonomy` — the ENTITY_HAS_TAXONOMY edge.

  Attributes:
      entity_id (str): The entity that was linked.
      taxonomy_id (str): The taxonomy that was linked.
      basis (str): Linkage role (see request).
      is_primary (bool): Whether this is the primary linkage.
      adoption_context (None | str | Unset): Adoption context recorded at link time.
  """

  entity_id: str
  taxonomy_id: str
  basis: str
  is_primary: bool
  adoption_context: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    taxonomy_id = self.taxonomy_id

    basis = self.basis

    is_primary = self.is_primary

    adoption_context: None | str | Unset
    if isinstance(self.adoption_context, Unset):
      adoption_context = UNSET
    else:
      adoption_context = self.adoption_context

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "taxonomy_id": taxonomy_id,
        "basis": basis,
        "is_primary": is_primary,
      }
    )
    if adoption_context is not UNSET:
      field_dict["adoption_context"] = adoption_context

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    taxonomy_id = d.pop("taxonomy_id")

    basis = d.pop("basis")

    is_primary = d.pop("is_primary")

    def _parse_adoption_context(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    adoption_context = _parse_adoption_context(d.pop("adoption_context", UNSET))

    entity_taxonomy_response = cls(
      entity_id=entity_id,
      taxonomy_id=taxonomy_id,
      basis=basis,
      is_primary=is_primary,
      adoption_context=adoption_context,
    )

    entity_taxonomy_response.additional_properties = d
    return entity_taxonomy_response

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
