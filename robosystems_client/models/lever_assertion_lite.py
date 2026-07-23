from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.lever_assertion_lite_values_by_period import (
    LeverAssertionLiteValuesByPeriod,
  )


T = TypeVar("T", bound="LeverAssertionLite")


@_attrs_define
class LeverAssertionLite:
  """One lever's persisted assertion inside ``ForecastMechanics``.

  The create handler expands the wire-level assertion (uniform ``value``
  + per-month overrides) into the explicit ``values_by_period`` map so
  compute never interpolates — every asserted month is stated. The
  values are duplicated as authored facts in the scenario's lever
  FactSet (rules for mechanics, **facts for values** — the facts are
  what ``compute-forecast`` binds); this mechanics copy is the
  operator-legible round-trip shape.

      Attributes:
          qname (str): rs-driver lever element qname.
          element_id (str): Resolved tenant element id.
          values_by_period (LeverAssertionLiteValuesByPeriod): Expanded per-month assertions keyed by ``YYYY-MM``.
          item_type (None | str | Unset): Format family from the catalog (percent | days | ...).
  """

  qname: str
  element_id: str
  values_by_period: LeverAssertionLiteValuesByPeriod
  item_type: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    element_id = self.element_id

    values_by_period = self.values_by_period.to_dict()

    item_type: None | str | Unset
    if isinstance(self.item_type, Unset):
      item_type = UNSET
    else:
      item_type = self.item_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
        "element_id": element_id,
        "values_by_period": values_by_period,
      }
    )
    if item_type is not UNSET:
      field_dict["item_type"] = item_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.lever_assertion_lite_values_by_period import (
      LeverAssertionLiteValuesByPeriod,
    )

    d = dict(src_dict)
    qname = d.pop("qname")

    element_id = d.pop("element_id")

    values_by_period = LeverAssertionLiteValuesByPeriod.from_dict(
      d.pop("values_by_period")
    )

    def _parse_item_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    item_type = _parse_item_type(d.pop("item_type", UNSET))

    lever_assertion_lite = cls(
      qname=qname,
      element_id=element_id,
      values_by_period=values_by_period,
      item_type=item_type,
    )

    lever_assertion_lite.additional_properties = d
    return lever_assertion_lite

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
