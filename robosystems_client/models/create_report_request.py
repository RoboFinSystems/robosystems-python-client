from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.period_spec import PeriodSpec


T = TypeVar("T", bound="CreateReportRequest")


@_attrs_define
class CreateReportRequest:
  """Generate report facts from the ledger and publish a Report definition.

  The report is materialized synchronously: we resolve the taxonomy +
  CoA mapping, roll up GL facts into reportable concepts, attach them
  to a fresh ``Report`` row, evaluate any reporting-rule structures
  (cell-level checks), and stamp ``generation_status='published'``.
  Subsequent ``regenerate-report`` calls re-run the same pipeline against
  the latest ledger state without creating a new Report row.

  ``period_start``/``period_end``/``comparative`` is the simple path
  (auto-derives current + prior period). For multi-column reports
  (YTD-by-quarter, multi-year) supply ``periods`` explicitly — when
  set, ``period_start``/``period_end``/``comparative`` are ignored as
  inputs to period generation.

      Attributes:
          name (str): Human-readable report name shown in lists and headers.
          mapping_id (str): Mapping structure that rolls up the tenant's chart of accounts to the taxonomy's reporting
              concepts. Created via `create-mapping-association` / `auto-map-elements`.
          period_start (datetime.date): Current-period start (inclusive). Ignored when `periods` is supplied.
          period_end (datetime.date): Current-period end (inclusive). Must be >= `period_start`. Ignored when `periods` is
              supplied.
          taxonomy_id (str | Unset): Taxonomy that defines the structures (BS / IS / CF / Equity / Schedules) this report
              can render. Defaults to the platform US GAAP reporting taxonomy. Default: 'tax_usgaap_reporting'.
          period_type (str | Unset): Period cadence: `monthly`, `quarterly`, or `annual`. Default: 'quarterly'.
          comparative (bool | Unset): When true, automatically generates a prior-period column (same length as the current
              period). Ignored when `periods` is supplied. Default: True.
          periods (list[PeriodSpec] | None | Unset): Explicit period columns. When set, overrides
              `period_start`/`period_end`/`comparative`. Use for multi-period layouts (YTD-by-quarter, multi-year, custom
              rolling windows).
  """

  name: str
  mapping_id: str
  period_start: datetime.date
  period_end: datetime.date
  taxonomy_id: str | Unset = "tax_usgaap_reporting"
  period_type: str | Unset = "quarterly"
  comparative: bool | Unset = True
  periods: list[PeriodSpec] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    mapping_id = self.mapping_id

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    taxonomy_id = self.taxonomy_id

    period_type = self.period_type

    comparative = self.comparative

    periods: list[dict[str, Any]] | None | Unset
    if isinstance(self.periods, Unset):
      periods = UNSET
    elif isinstance(self.periods, list):
      periods = []
      for periods_type_0_item_data in self.periods:
        periods_type_0_item = periods_type_0_item_data.to_dict()
        periods.append(periods_type_0_item)

    else:
      periods = self.periods

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "mapping_id": mapping_id,
        "period_start": period_start,
        "period_end": period_end,
      }
    )
    if taxonomy_id is not UNSET:
      field_dict["taxonomy_id"] = taxonomy_id
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if comparative is not UNSET:
      field_dict["comparative"] = comparative
    if periods is not UNSET:
      field_dict["periods"] = periods

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.period_spec import PeriodSpec

    d = dict(src_dict)
    name = d.pop("name")

    mapping_id = d.pop("mapping_id")

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    taxonomy_id = d.pop("taxonomy_id", UNSET)

    period_type = d.pop("period_type", UNSET)

    comparative = d.pop("comparative", UNSET)

    def _parse_periods(data: object) -> list[PeriodSpec] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        periods_type_0 = []
        _periods_type_0 = data
        for periods_type_0_item_data in _periods_type_0:
          periods_type_0_item = PeriodSpec.from_dict(periods_type_0_item_data)

          periods_type_0.append(periods_type_0_item)

        return periods_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[PeriodSpec] | None | Unset, data)

    periods = _parse_periods(d.pop("periods", UNSET))

    create_report_request = cls(
      name=name,
      mapping_id=mapping_id,
      period_start=period_start,
      period_end=period_end,
      taxonomy_id=taxonomy_id,
      period_type=period_type,
      comparative=comparative,
      periods=periods,
    )

    create_report_request.additional_properties = d
    return create_report_request

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
