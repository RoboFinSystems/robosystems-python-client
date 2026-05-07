from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderingRowLite")


@_attrs_define
class RenderingRowLite:
  """One row of a server-side rendered statement.

  Mirrors :class:`FactRow` from the legacy
  :mod:`robosystems.operations.roboledger.reports.fact_grid` but lives at
  the API boundary so envelope consumers don't depend on the
  fact-grid module. ``values`` is one entry per period column in
  :class:`RenderingLite.periods`.

      Attributes:
          element_id (str):
          element_name (str):
          element_qname (None | str | Unset):
          classification (None | str | Unset): FASB elementsOfFinancialStatements trait identifier — 'asset', 'liability',
              'equity', 'revenue', 'expense'. Surfaced so the viewer can color-code or group rows without a follow-up trait
              lookup.
          balance_type (None | str | Unset):
          values (list[float | None] | Unset):
          is_subtotal (bool | Unset):  Default: False.
          depth (int | Unset):  Default: 0.
  """

  element_id: str
  element_name: str
  element_qname: None | str | Unset = UNSET
  classification: None | str | Unset = UNSET
  balance_type: None | str | Unset = UNSET
  values: list[float | None] | Unset = UNSET
  is_subtotal: bool | Unset = False
  depth: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    element_name = self.element_name

    element_qname: None | str | Unset
    if isinstance(self.element_qname, Unset):
      element_qname = UNSET
    else:
      element_qname = self.element_qname

    classification: None | str | Unset
    if isinstance(self.classification, Unset):
      classification = UNSET
    else:
      classification = self.classification

    balance_type: None | str | Unset
    if isinstance(self.balance_type, Unset):
      balance_type = UNSET
    else:
      balance_type = self.balance_type

    values: list[float | None] | Unset = UNSET
    if not isinstance(self.values, Unset):
      values = []
      for values_item_data in self.values:
        values_item: float | None
        values_item = values_item_data
        values.append(values_item)

    is_subtotal = self.is_subtotal

    depth = self.depth

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "element_name": element_name,
      }
    )
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if classification is not UNSET:
      field_dict["classification"] = classification
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if values is not UNSET:
      field_dict["values"] = values
    if is_subtotal is not UNSET:
      field_dict["is_subtotal"] = is_subtotal
    if depth is not UNSET:
      field_dict["depth"] = depth

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    element_name = d.pop("element_name")

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    def _parse_classification(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    classification = _parse_classification(d.pop("classification", UNSET))

    def _parse_balance_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    balance_type = _parse_balance_type(d.pop("balance_type", UNSET))

    _values = d.pop("values", UNSET)
    values: list[float | None] | Unset = UNSET
    if _values is not UNSET:
      values = []
      for values_item_data in _values:

        def _parse_values_item(data: object) -> float | None:
          if data is None:
            return data
          return cast(float | None, data)

        values_item = _parse_values_item(values_item_data)

        values.append(values_item)

    is_subtotal = d.pop("is_subtotal", UNSET)

    depth = d.pop("depth", UNSET)

    rendering_row_lite = cls(
      element_id=element_id,
      element_name=element_name,
      element_qname=element_qname,
      classification=classification,
      balance_type=balance_type,
      values=values,
      is_subtotal=is_subtotal,
      depth=depth,
    )

    rendering_row_lite.additional_properties = d
    return rendering_row_lite

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
