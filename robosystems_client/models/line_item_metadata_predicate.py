from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemMetadataPredicate")


@_attrs_define
class LineItemMetadataPredicate:
  """Filter ledger LineItems by flow concept.

  The single predicate kind shipped to date. ``values`` are flow-concept
  qnames — mini's ``TransactionDescriptionCode`` values, rs-gaap flow
  concepts (what the enrichment classifier emits for QuickBooks data),
  future XBRL GL ``GenericFlowCategory`` codes. The engine resolves them
  to element_ids and matches the first-class ``LineItem.flow_element_id``
  FK; matched lines aggregate signed into the attributed fact for the
  period.

  ``field`` is **legacy and ignored** — the flow tag used to live in
  ``line_items.metadata[field]`` but has been promoted to the typed
  ``flow_element_id`` FK. Retained for wire-compatibility; the engine no
  longer reads it.

      Attributes:
          values (list[str]): Flow-concept qnames that route to this filter's target concept. A LineItem matches when its
              ``flow_element_id`` is one of the elements named here AND the line falls within the rollforward's period.
          kind (Literal['line_item_metadata_field'] | Unset): Discriminator value selecting this predicate shape. Default:
              'line_item_metadata_field'.
          field (str | Unset): Legacy/ignored. The flow tag now lives in the typed ``flow_element_id`` FK, not JSONB
              metadata; the engine no longer reads this. Retained for wire-compatibility. Default:
              'transaction_description_code'.
  """

  values: list[str]
  kind: Literal["line_item_metadata_field"] | Unset = "line_item_metadata_field"
  field: str | Unset = "transaction_description_code"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    values = self.values

    kind = self.kind

    field = self.field

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "values": values,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if field is not UNSET:
      field_dict["field"] = field

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    values = cast(list[str], d.pop("values"))

    kind = cast(Literal["line_item_metadata_field"] | Unset, d.pop("kind", UNSET))
    if kind != "line_item_metadata_field" and not isinstance(kind, Unset):
      raise ValueError(
        f"kind must match const 'line_item_metadata_field', got '{kind}'"
      )

    field = d.pop("field", UNSET)

    line_item_metadata_predicate = cls(
      values=values,
      kind=kind,
      field=field,
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
