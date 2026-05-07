from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransitionFilingStatusRequest")


@_attrs_define
class TransitionFilingStatusRequest:
  """Generic filing-status transition — escape hatch for non-file moves.

  Used for ``draft → under_review`` (submit for review) and
  ``filed → archived`` (supersede / retire). Filing the package goes
  through :class:`FileReportRequest` so ``filed_at`` / ``filed_by``
  audit fields land cleanly.

      Attributes:
          report_id (str): The Report to transition.
          target_status (str): Target lifecycle state: `under_review` (submit a draft for review) or `archived` (supersede
              / retire a filed report). Reaching `filed` goes through `file-report` so audit fields land cleanly.
  """

  report_id: str
  target_status: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    report_id = self.report_id

    target_status = self.target_status

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_id": report_id,
        "target_status": target_status,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    report_id = d.pop("report_id")

    target_status = d.pop("target_status")

    transition_filing_status_request = cls(
      report_id=report_id,
      target_status=target_status,
    )

    transition_filing_status_request.additional_properties = d
    return transition_filing_status_request

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
