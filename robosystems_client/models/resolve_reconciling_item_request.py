from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resolve_reconciling_item_request_disposition_type_0 import (
  ResolveReconcilingItemRequestDispositionType0,
)
from ..models.resolve_reconciling_item_request_status import (
  ResolveReconcilingItemRequestStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveReconcilingItemRequest")


@_attrs_define
class ResolveReconcilingItemRequest:
  """Dispose of one reconciling item and clear its flag.

  Attributes:
      event_id (str): Event id (evt_ prefixed) to resolve
      disposition (None | ResolveReconcilingItemRequestDispositionType0 | Unset): How to dispose of the difference.
          Omit to take the default the preview reports: restate when every period the event touches is open, catch_up when
          any is closed.
      posting_date (datetime.date | None | Unset): catch_up only: when to post the catch-up entry. Defaults to the end
          of the earliest open period.
      status (ResolveReconcilingItemRequestStatus | Unset): catch_up only: whether the catch-up entry is drafted for
          review at close (default) or posted immediately. A draft appears in list-period-drafts and posts locally when
          the period closes. Default: ResolveReconcilingItemRequestStatus.DRAFT.
      note (None | str | Unset): Why this disposition. Required for acknowledge, where it is the only record of what
          was done instead.
      reference_event_id (None | str | Unset): acknowledge only: the event that already handled this difference (e.g.
          an alignment entry authored by hand), recorded on the trail.
  """

  event_id: str
  disposition: None | ResolveReconcilingItemRequestDispositionType0 | Unset = UNSET
  posting_date: datetime.date | None | Unset = UNSET
  status: ResolveReconcilingItemRequestStatus | Unset = (
    ResolveReconcilingItemRequestStatus.DRAFT
  )
  note: None | str | Unset = UNSET
  reference_event_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    disposition: None | str | Unset
    if isinstance(self.disposition, Unset):
      disposition = UNSET
    elif isinstance(self.disposition, ResolveReconcilingItemRequestDispositionType0):
      disposition = self.disposition.value
    else:
      disposition = self.disposition

    posting_date: None | str | Unset
    if isinstance(self.posting_date, Unset):
      posting_date = UNSET
    elif isinstance(self.posting_date, datetime.date):
      posting_date = self.posting_date.isoformat()
    else:
      posting_date = self.posting_date

    status: str | Unset = UNSET
    if not isinstance(self.status, Unset):
      status = self.status.value

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    reference_event_id: None | str | Unset
    if isinstance(self.reference_event_id, Unset):
      reference_event_id = UNSET
    else:
      reference_event_id = self.reference_event_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
      }
    )
    if disposition is not UNSET:
      field_dict["disposition"] = disposition
    if posting_date is not UNSET:
      field_dict["posting_date"] = posting_date
    if status is not UNSET:
      field_dict["status"] = status
    if note is not UNSET:
      field_dict["note"] = note
    if reference_event_id is not UNSET:
      field_dict["reference_event_id"] = reference_event_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    def _parse_disposition(
      data: object,
    ) -> None | ResolveReconcilingItemRequestDispositionType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        disposition_type_0 = ResolveReconcilingItemRequestDispositionType0(data)

        return disposition_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ResolveReconcilingItemRequestDispositionType0 | Unset, data)

    disposition = _parse_disposition(d.pop("disposition", UNSET))

    def _parse_posting_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        posting_date_type_0 = datetime.date.fromisoformat(data)

        return posting_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    posting_date = _parse_posting_date(d.pop("posting_date", UNSET))

    _status = d.pop("status", UNSET)
    status: ResolveReconcilingItemRequestStatus | Unset
    if isinstance(_status, Unset):
      status = UNSET
    else:
      status = ResolveReconcilingItemRequestStatus(_status)

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    def _parse_reference_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reference_event_id = _parse_reference_event_id(d.pop("reference_event_id", UNSET))

    resolve_reconciling_item_request = cls(
      event_id=event_id,
      disposition=disposition,
      posting_date=posting_date,
      status=status,
      note=note,
      reference_event_id=reference_event_id,
    )

    resolve_reconciling_item_request.additional_properties = d
    return resolve_reconciling_item_request

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
