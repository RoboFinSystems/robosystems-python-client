from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerificationResultLite")


@_attrs_define
class VerificationResultLite:
  """Persisted outcome of one Rule evaluation.

  One row per ``public.verification_results`` entry the rule engine
  writes. The envelope surfaces them so the block viewer's
  "Verification Results" tab and MCP ``list-verification-failures``
  tool can render + aggregate without a second round-trip.

      Attributes:
          id (str):
          rule_id (str):
          status (str): 'pass' | 'fail' | 'error' | 'skipped'. Enum closure enforced by the
              ``public.verification_results`` CHECK constraint.
          structure_id (None | str | Unset):
          fact_set_id (None | str | Unset):
          message (None | str | Unset):
          period_start (datetime.date | None | Unset):
          period_end (datetime.date | None | Unset):
          evaluated_at (datetime.datetime | None | Unset):
  """

  id: str
  rule_id: str
  status: str
  structure_id: None | str | Unset = UNSET
  fact_set_id: None | str | Unset = UNSET
  message: None | str | Unset = UNSET
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  evaluated_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    rule_id = self.rule_id

    status = self.status

    structure_id: None | str | Unset
    if isinstance(self.structure_id, Unset):
      structure_id = UNSET
    else:
      structure_id = self.structure_id

    fact_set_id: None | str | Unset
    if isinstance(self.fact_set_id, Unset):
      fact_set_id = UNSET
    else:
      fact_set_id = self.fact_set_id

    message: None | str | Unset
    if isinstance(self.message, Unset):
      message = UNSET
    else:
      message = self.message

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    elif isinstance(self.period_end, datetime.date):
      period_end = self.period_end.isoformat()
    else:
      period_end = self.period_end

    evaluated_at: None | str | Unset
    if isinstance(self.evaluated_at, Unset):
      evaluated_at = UNSET
    elif isinstance(self.evaluated_at, datetime.datetime):
      evaluated_at = self.evaluated_at.isoformat()
    else:
      evaluated_at = self.evaluated_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "rule_id": rule_id,
        "status": status,
      }
    )
    if structure_id is not UNSET:
      field_dict["structure_id"] = structure_id
    if fact_set_id is not UNSET:
      field_dict["fact_set_id"] = fact_set_id
    if message is not UNSET:
      field_dict["message"] = message
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if evaluated_at is not UNSET:
      field_dict["evaluated_at"] = evaluated_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    rule_id = d.pop("rule_id")

    status = d.pop("status")

    def _parse_structure_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    structure_id = _parse_structure_id(d.pop("structure_id", UNSET))

    def _parse_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fact_set_id = _parse_fact_set_id(d.pop("fact_set_id", UNSET))

    def _parse_message(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    message = _parse_message(d.pop("message", UNSET))

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = isoparse(data).date()

        return period_start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_end_type_0 = isoparse(data).date()

        return period_end_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_evaluated_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        evaluated_at_type_0 = isoparse(data)

        return evaluated_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    evaluated_at = _parse_evaluated_at(d.pop("evaluated_at", UNSET))

    verification_result_lite = cls(
      id=id,
      rule_id=rule_id,
      status=status,
      structure_id=structure_id,
      fact_set_id=fact_set_id,
      message=message,
      period_start=period_start,
      period_end=period_end,
      evaluated_at=evaluated_at,
    )

    verification_result_lite.additional_properties = d
    return verification_result_lite

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
