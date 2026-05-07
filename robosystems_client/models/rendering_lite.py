from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.rendering_period_lite import RenderingPeriodLite
  from ..models.rendering_row_lite import RenderingRowLite
  from ..models.validation_lite import ValidationLite


T = TypeVar("T", bound="RenderingLite")


@_attrs_define
class RenderingLite:
  """Pre-computed rendering projection of an Information Block.

  Computed server-side at envelope-build time for blocks where rendering
  is deterministic (the statement family today; future block types add
  their own rendering builders). The frontend's ``BlockView``
  ``Rendering`` projection consumes this directly — no client-side
  rollup, depth computation, or calculation walk needed.

      Attributes:
          rows (list[RenderingRowLite] | Unset):
          periods (list[RenderingPeriodLite] | Unset):
          validation (None | Unset | ValidationLite):
          unmapped_count (int | Unset):  Default: 0.
  """

  rows: list[RenderingRowLite] | Unset = UNSET
  periods: list[RenderingPeriodLite] | Unset = UNSET
  validation: None | Unset | ValidationLite = UNSET
  unmapped_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.validation_lite import ValidationLite

    rows: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rows, Unset):
      rows = []
      for rows_item_data in self.rows:
        rows_item = rows_item_data.to_dict()
        rows.append(rows_item)

    periods: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.periods, Unset):
      periods = []
      for periods_item_data in self.periods:
        periods_item = periods_item_data.to_dict()
        periods.append(periods_item)

    validation: dict[str, Any] | None | Unset
    if isinstance(self.validation, Unset):
      validation = UNSET
    elif isinstance(self.validation, ValidationLite):
      validation = self.validation.to_dict()
    else:
      validation = self.validation

    unmapped_count = self.unmapped_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if rows is not UNSET:
      field_dict["rows"] = rows
    if periods is not UNSET:
      field_dict["periods"] = periods
    if validation is not UNSET:
      field_dict["validation"] = validation
    if unmapped_count is not UNSET:
      field_dict["unmapped_count"] = unmapped_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.rendering_period_lite import RenderingPeriodLite
    from ..models.rendering_row_lite import RenderingRowLite
    from ..models.validation_lite import ValidationLite

    d = dict(src_dict)
    _rows = d.pop("rows", UNSET)
    rows: list[RenderingRowLite] | Unset = UNSET
    if _rows is not UNSET:
      rows = []
      for rows_item_data in _rows:
        rows_item = RenderingRowLite.from_dict(rows_item_data)

        rows.append(rows_item)

    _periods = d.pop("periods", UNSET)
    periods: list[RenderingPeriodLite] | Unset = UNSET
    if _periods is not UNSET:
      periods = []
      for periods_item_data in _periods:
        periods_item = RenderingPeriodLite.from_dict(periods_item_data)

        periods.append(periods_item)

    def _parse_validation(data: object) -> None | Unset | ValidationLite:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        validation_type_0 = ValidationLite.from_dict(data)

        return validation_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | ValidationLite, data)

    validation = _parse_validation(d.pop("validation", UNSET))

    unmapped_count = d.pop("unmapped_count", UNSET)

    rendering_lite = cls(
      rows=rows,
      periods=periods,
      validation=validation,
      unmapped_count=unmapped_count,
    )

    rendering_lite.additional_properties = d
    return rendering_lite

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
