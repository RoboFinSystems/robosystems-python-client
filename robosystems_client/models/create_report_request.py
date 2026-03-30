from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReportRequest")


@_attrs_define
class CreateReportRequest:
  """
  Attributes:
      name (str): Report name
      mapping_id (str): Mapping structure ID for CoA→GAAP rollup
      period_start (datetime.date): Period start date (inclusive)
      period_end (datetime.date): Period end date (inclusive)
      taxonomy_id (str | Unset): Taxonomy ID — determines which structures are available Default:
          'tax_usgaap_reporting'.
      period_type (str | Unset): Period type: monthly, quarterly, annual Default: 'quarterly'.
      comparative (bool | Unset): Include prior period comparison Default: True.
  """

  name: str
  mapping_id: str
  period_start: datetime.date
  period_end: datetime.date
  taxonomy_id: str | Unset = "tax_usgaap_reporting"
  period_type: str | Unset = "quarterly"
  comparative: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    mapping_id = self.mapping_id

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    taxonomy_id = self.taxonomy_id

    period_type = self.period_type

    comparative = self.comparative

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

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    mapping_id = d.pop("mapping_id")

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    taxonomy_id = d.pop("taxonomy_id", UNSET)

    period_type = d.pop("period_type", UNSET)

    comparative = d.pop("comparative", UNSET)

    create_report_request = cls(
      name=name,
      mapping_id=mapping_id,
      period_start=period_start,
      period_end=period_end,
      taxonomy_id=taxonomy_id,
      period_type=period_type,
      comparative=comparative,
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
