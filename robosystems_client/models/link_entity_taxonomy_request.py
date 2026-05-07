from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.link_entity_taxonomy_request_basis import LinkEntityTaxonomyRequestBasis
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkEntityTaxonomyRequest")


@_attrs_define
class LinkEntityTaxonomyRequest:
  """Link an entity to a taxonomy (creates the ENTITY_HAS_TAXONOMY edge).

  This is how a graph declares "this entity reports under this taxonomy."
  For ``chart_of_accounts`` taxonomies, this tells the platform which CoA
  the entity uses. For reporting taxonomies, which standard (us-gaap,
  ifrs). Idempotent — re-linking returns the existing edge unchanged.

  CoA blocks auto-link at create time; use this to switch the primary
  CoA, link a reporting extension, or attach a custom ontology
  explicitly.

      Attributes:
          taxonomy_id (str): The taxonomy to link to.
          basis (LinkEntityTaxonomyRequestBasis | Unset): Linkage role: `chart_of_accounts` (the entity's CoA),
              `reporting` (reporting standard like us-gaap), `mapping` (CoA→reporting rollup), `schedule` (schedule
              structure). Default: LinkEntityTaxonomyRequestBasis.CHART_OF_ACCOUNTS.
          is_primary (bool | Unset): Mark this as the primary linkage for the basis. False allows secondary attachments
              (e.g. parallel reporting standards). Default: True.
          adoption_context (None | str | Unset): Why the entity is reporting under this taxonomy (e.g. 'voluntary',
              'regulatory', 'lender_requirement'). Default: 'voluntary'.
  """

  taxonomy_id: str
  basis: LinkEntityTaxonomyRequestBasis | Unset = (
    LinkEntityTaxonomyRequestBasis.CHART_OF_ACCOUNTS
  )
  is_primary: bool | Unset = True
  adoption_context: None | str | Unset = "voluntary"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

    basis: str | Unset = UNSET
    if not isinstance(self.basis, Unset):
      basis = self.basis.value

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
        "taxonomy_id": taxonomy_id,
      }
    )
    if basis is not UNSET:
      field_dict["basis"] = basis
    if is_primary is not UNSET:
      field_dict["is_primary"] = is_primary
    if adoption_context is not UNSET:
      field_dict["adoption_context"] = adoption_context

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

    _basis = d.pop("basis", UNSET)
    basis: LinkEntityTaxonomyRequestBasis | Unset
    if isinstance(_basis, Unset):
      basis = UNSET
    else:
      basis = LinkEntityTaxonomyRequestBasis(_basis)

    is_primary = d.pop("is_primary", UNSET)

    def _parse_adoption_context(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    adoption_context = _parse_adoption_context(d.pop("adoption_context", UNSET))

    link_entity_taxonomy_request = cls(
      taxonomy_id=taxonomy_id,
      basis=basis,
      is_primary=is_primary,
      adoption_context=adoption_context,
    )

    link_entity_taxonomy_request.additional_properties = d
    return link_entity_taxonomy_request

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
