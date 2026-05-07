from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileReportRequest")


@_attrs_define
class FileReportRequest:
  """Transition a Report to ``filed`` — locks the package.

  Acceptable from ``draft`` or ``under_review``. ``filed_by`` and
  ``filed_at`` are stamped from the auth context + server clock; the
  request itself carries no fields today (kept as a model for OpenAPI
  shape consistency and to avoid breaking changes if we add fields).
  Use ``transition-filing-status`` for the non-file legs of the
  lifecycle (`draft ↔ under_review`, `filed → archived`).

      Attributes:
          report_id (str): The Report to file.
  """

  report_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    report_id = self.report_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_id": report_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    report_id = d.pop("report_id")

    file_report_request = cls(
      report_id=report_id,
    )

    file_report_request.additional_properties = d
    return file_report_request

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
