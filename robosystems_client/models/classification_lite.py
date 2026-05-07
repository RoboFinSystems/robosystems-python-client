from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClassificationLite")


@_attrs_define
class ClassificationLite:
  """Classification projection — one row per `association_classifications`
  junction entry.

  Association-side only: concept_arrangement, member_arrangement,
  named_disclosure. Element-side FASB metamodel traits (asset, current,
  operating, …) live in `TraitLite` via `element_traits`.

  Carries enough for the envelope caller to render / filter by category +
  identifier without a follow-up lookup. The full `public.classifications`
  vocabulary catalog (name / description / metadata) is available via the
  library GraphQL surface when callers need the details.

      Attributes:
          id (str): Classification vocabulary row id.
          category (str): One of the 3 association-level categories in the `public.classifications` CHECK constraint:
              'concept_arrangement', 'member_arrangement', or 'named_disclosure'.
          identifier (str): Vocabulary identifier within the category — e.g. 'RollUp', 'aggregation', 'AssetsRollUp'.
          is_primary (bool | Unset): Whether this is the canonical classification for the (association|element, category)
              pair. Non-primary rows capture alternates / AI suggestions alongside the chosen primary. Default: True.
          confidence (float | None | Unset): AI/adapter-supplied confidence (0.0-1.0). Null for deterministic library-
              seeded rows.
          source (None | str | Unset): Provenance — 'arcrole_analysis', 'disclosure_mechanics', 'us-gaap-metamodel',
              adapter name, etc.
  """

  id: str
  category: str
  identifier: str
  is_primary: bool | Unset = True
  confidence: float | None | Unset = UNSET
  source: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    category = self.category

    identifier = self.identifier

    is_primary = self.is_primary

    confidence: float | None | Unset
    if isinstance(self.confidence, Unset):
      confidence = UNSET
    else:
      confidence = self.confidence

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "category": category,
        "identifier": identifier,
      }
    )
    if is_primary is not UNSET:
      field_dict["is_primary"] = is_primary
    if confidence is not UNSET:
      field_dict["confidence"] = confidence
    if source is not UNSET:
      field_dict["source"] = source

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    category = d.pop("category")

    identifier = d.pop("identifier")

    is_primary = d.pop("is_primary", UNSET)

    def _parse_confidence(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    confidence = _parse_confidence(d.pop("confidence", UNSET))

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    classification_lite = cls(
      id=id,
      category=category,
      identifier=identifier,
      is_primary=is_primary,
      confidence=confidence,
      source=source,
    )

    classification_lite.additional_properties = d
    return classification_lite

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
