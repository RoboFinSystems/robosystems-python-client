from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemMetadataPredicate")


@_attrs_define
class LineItemMetadataPredicate:
  """Filter ledger LineItems whose ``metadata_[field]`` is in ``values``.

  The single predicate kind shipped in Phase 2 MVP. Sufficient for any
  source taxonomy that stamps a flow-tag column on each transaction
  line — mini's ``TransactionDescriptionCode``, future XBRL GL
  ``GenericFlowCategory`` columns, custom tenant tags.

  ``field`` is the JSONB key under ``line_items.metadata`` (e.g.
  ``"transaction_description_code"``). ``values`` is the set of values
  that route to the filter's target concept; matched LineItems aggregate
  signed into the attributed fact for the period.

      Attributes:
          field (str): JSONB key under ``line_items.metadata`` to match against — e.g. ``transaction_description_code``.
              The renderer performs an exact-string comparison on the JSONB-extracted text value.
          values (list[str]): Metadata values that route to this filter's target concept. A LineItem matches when
              ``metadata[field] ∈ values`` AND the line falls within the rollforward's period.
          kind (Literal['line_item_metadata_field'] | Unset): Discriminator value selecting this predicate shape. Default:
              'line_item_metadata_field'.
  """

  field: str
  values: list[str]
  kind: Literal["line_item_metadata_field"] | Unset = "line_item_metadata_field"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    field = self.field

    values = self.values

    kind = self.kind

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "field": field,
        "values": values,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    field = d.pop("field")

    values = cast(list[str], d.pop("values"))

    kind = cast(Literal["line_item_metadata_field"] | Unset, d.pop("kind", UNSET))
    if kind != "line_item_metadata_field" and not isinstance(kind, Unset):
      raise ValueError(
        f"kind must match const 'line_item_metadata_field', got '{kind}'"
      )

    line_item_metadata_predicate = cls(
      field=field,
      values=values,
      kind=kind,
    )

    line_item_metadata_predicate.additional_properties = d
    return line_item_metadata_predicate

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
