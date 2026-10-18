from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.worksheet_column_kind import WorksheetColumnKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorksheetColumn")


@_attrs_define
class WorksheetColumn:
  """One column of the consolidation worksheet.

  Attributes:
      key (str): The entity id for an entity's column; `combined` and `consolidated` for the two totals.
      label (str): The entity's name, or the total's.
      kind (WorksheetColumnKind): `member`: the parent or a member consolidated in full. `combined`: the members' sum,
          nothing eliminated. `adjustments`: the consolidation entity's entries. `consolidated`: combined plus the
          adjustments. `not_summed`: an equity-method or cost member, shown beside the sum and never in it.
      in_sum (bool): Whether the column is part of the consolidated total.
      entity_id (None | str | Unset): The entity the column reads; null on a total.
      consolidation_method (None | str | Unset): The entity's `consolidation_method`; null on a total.
      ownership_pct (float | None | Unset): The parent's share of the entity, where it has one.
  """

  key: str
  label: str
  kind: WorksheetColumnKind
  in_sum: bool
  entity_id: None | str | Unset = UNSET
  consolidation_method: None | str | Unset = UNSET
  ownership_pct: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    key = self.key

    label = self.label

    kind = self.kind.value

    in_sum = self.in_sum

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    consolidation_method: None | str | Unset
    if isinstance(self.consolidation_method, Unset):
      consolidation_method = UNSET
    else:
      consolidation_method = self.consolidation_method

    ownership_pct: float | None | Unset
    if isinstance(self.ownership_pct, Unset):
      ownership_pct = UNSET
    else:
      ownership_pct = self.ownership_pct

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "key": key,
        "label": label,
        "kind": kind,
        "in_sum": in_sum,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if consolidation_method is not UNSET:
      field_dict["consolidation_method"] = consolidation_method
    if ownership_pct is not UNSET:
      field_dict["ownership_pct"] = ownership_pct

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    key = d.pop("key")

    label = d.pop("label")

    kind = WorksheetColumnKind(d.pop("kind"))

    in_sum = d.pop("in_sum")

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_consolidation_method(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    consolidation_method = _parse_consolidation_method(
      d.pop("consolidation_method", UNSET)
    )

    def _parse_ownership_pct(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    ownership_pct = _parse_ownership_pct(d.pop("ownership_pct", UNSET))

    worksheet_column = cls(
      key=key,
      label=label,
      kind=kind,
      in_sum=in_sum,
      entity_id=entity_id,
      consolidation_method=consolidation_method,
      ownership_pct=ownership_pct,
    )

    worksheet_column.additional_properties = d
    return worksheet_column

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
