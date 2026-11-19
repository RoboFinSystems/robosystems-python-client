from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_sync_request_status import ReportSyncRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.report_sync_request_counts import ReportSyncRequestCounts


T = TypeVar("T", bound="ReportSyncRequest")


@_attrs_define
class ReportSyncRequest:
  """An external integration's report of a run it just finished.

  The platform runs no sync for an external source, so the integration says
  when its last run was: a successful report is the connection's
  `last_sync`, which a period close reads to tell whether the books it
  mirrors are current.

      Attributes:
          status (ReportSyncRequestStatus): 'succeeded' moves `last_sync` to now. 'failed' records the outcome and leaves
              `last_sync` where it was.
          counts (ReportSyncRequestCounts | Unset): What the run did, as the integration counts it (for example
              `entries_sent`, `entries_replaced`, `entries_withdrawn`). Shown with the connection; nothing reads the names.
          message (None | str | Unset): A line about the run: the window it covered, or why it failed.
  """

  status: ReportSyncRequestStatus
  counts: ReportSyncRequestCounts | Unset = UNSET
  message: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status.value

    counts: dict[str, Any] | Unset = UNSET
    if not isinstance(self.counts, Unset):
      counts = self.counts.to_dict()

    message: None | str | Unset
    if isinstance(self.message, Unset):
      message = UNSET
    else:
      message = self.message

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
      }
    )
    if counts is not UNSET:
      field_dict["counts"] = counts
    if message is not UNSET:
      field_dict["message"] = message

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.report_sync_request_counts import ReportSyncRequestCounts

    d = dict(src_dict)
    status = ReportSyncRequestStatus(d.pop("status"))

    _counts = d.pop("counts", UNSET)
    counts: ReportSyncRequestCounts | Unset
    if isinstance(_counts, Unset):
      counts = UNSET
    else:
      counts = ReportSyncRequestCounts.from_dict(_counts)

    def _parse_message(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    message = _parse_message(d.pop("message", UNSET))

    report_sync_request = cls(
      status=status,
      counts=counts,
      message=message,
    )

    report_sync_request.additional_properties = d
    return report_sync_request

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
