from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.fact_row_response import FactRowResponse
  from ..models.validation_check_response import ValidationCheckResponse


T = TypeVar("T", bound="StatementResponse")


@_attrs_define
class StatementResponse:
  """Rendered financial statement — facts viewed through a structure.

  Attributes:
      report_id (str):
      structure_id (str):
      structure_name (str):
      structure_type (str):
      period_start (datetime.date):
      period_end (datetime.date):
      comparative_period_start (datetime.date | None | Unset):
      comparative_period_end (datetime.date | None | Unset):
      rows (list[FactRowResponse] | Unset):
      validation (None | Unset | ValidationCheckResponse):
      unmapped_count (int | Unset):  Default: 0.
  """

  report_id: str
  structure_id: str
  structure_name: str
  structure_type: str
  period_start: datetime.date
  period_end: datetime.date
  comparative_period_start: datetime.date | None | Unset = UNSET
  comparative_period_end: datetime.date | None | Unset = UNSET
  rows: list[FactRowResponse] | Unset = UNSET
  validation: None | Unset | ValidationCheckResponse = UNSET
  unmapped_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.validation_check_response import ValidationCheckResponse

    report_id = self.report_id

    structure_id = self.structure_id

    structure_name = self.structure_name

    structure_type = self.structure_type

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    comparative_period_start: None | str | Unset
    if isinstance(self.comparative_period_start, Unset):
      comparative_period_start = UNSET
    elif isinstance(self.comparative_period_start, datetime.date):
      comparative_period_start = self.comparative_period_start.isoformat()
    else:
      comparative_period_start = self.comparative_period_start

    comparative_period_end: None | str | Unset
    if isinstance(self.comparative_period_end, Unset):
      comparative_period_end = UNSET
    elif isinstance(self.comparative_period_end, datetime.date):
      comparative_period_end = self.comparative_period_end.isoformat()
    else:
      comparative_period_end = self.comparative_period_end

    rows: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rows, Unset):
      rows = []
      for rows_item_data in self.rows:
        rows_item = rows_item_data.to_dict()
        rows.append(rows_item)

    validation: dict[str, Any] | None | Unset
    if isinstance(self.validation, Unset):
      validation = UNSET
    elif isinstance(self.validation, ValidationCheckResponse):
      validation = self.validation.to_dict()
    else:
      validation = self.validation

    unmapped_count = self.unmapped_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_id": report_id,
        "structure_id": structure_id,
        "structure_name": structure_name,
        "structure_type": structure_type,
        "period_start": period_start,
        "period_end": period_end,
      }
    )
    if comparative_period_start is not UNSET:
      field_dict["comparative_period_start"] = comparative_period_start
    if comparative_period_end is not UNSET:
      field_dict["comparative_period_end"] = comparative_period_end
    if rows is not UNSET:
      field_dict["rows"] = rows
    if validation is not UNSET:
      field_dict["validation"] = validation
    if unmapped_count is not UNSET:
      field_dict["unmapped_count"] = unmapped_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.fact_row_response import FactRowResponse
    from ..models.validation_check_response import ValidationCheckResponse

    d = dict(src_dict)
    report_id = d.pop("report_id")

    structure_id = d.pop("structure_id")

    structure_name = d.pop("structure_name")

    structure_type = d.pop("structure_type")

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    def _parse_comparative_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        comparative_period_start_type_0 = isoparse(data).date()

        return comparative_period_start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    comparative_period_start = _parse_comparative_period_start(
      d.pop("comparative_period_start", UNSET)
    )

    def _parse_comparative_period_end(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        comparative_period_end_type_0 = isoparse(data).date()

        return comparative_period_end_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    comparative_period_end = _parse_comparative_period_end(
      d.pop("comparative_period_end", UNSET)
    )

    _rows = d.pop("rows", UNSET)
    rows: list[FactRowResponse] | Unset = UNSET
    if _rows is not UNSET:
      rows = []
      for rows_item_data in _rows:
        rows_item = FactRowResponse.from_dict(rows_item_data)

        rows.append(rows_item)

    def _parse_validation(data: object) -> None | Unset | ValidationCheckResponse:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        validation_type_0 = ValidationCheckResponse.from_dict(data)

        return validation_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | ValidationCheckResponse, data)

    validation = _parse_validation(d.pop("validation", UNSET))

    unmapped_count = d.pop("unmapped_count", UNSET)

    statement_response = cls(
      report_id=report_id,
      structure_id=structure_id,
      structure_name=structure_name,
      structure_type=structure_type,
      period_start=period_start,
      period_end=period_end,
      comparative_period_start=comparative_period_start,
      comparative_period_end=comparative_period_end,
      rows=rows,
      validation=validation,
      unmapped_count=unmapped_count,
    )

    statement_response.additional_properties = d
    return statement_response

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
