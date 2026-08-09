from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RevokeReportShareResponse")


@_attrs_define
class RevokeReportShareResponse:
  """Outcome of withdrawing a shared report from one recipient.

  Attributes:
      report_id (str): The report whose share was revoked.
      target_graph_id (str): Recipient the copy was pulled from.
      revoked_at (datetime.datetime): When the share was revoked.
      copy_deleted (bool): True when a copy was found and deleted in the recipient's schema. False when the recipient
          had already deleted it themselves — the share is still marked revoked.
  """

  report_id: str
  target_graph_id: str
  revoked_at: datetime.datetime
  copy_deleted: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    report_id = self.report_id

    target_graph_id = self.target_graph_id

    revoked_at = self.revoked_at.isoformat()

    copy_deleted = self.copy_deleted

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_id": report_id,
        "target_graph_id": target_graph_id,
        "revoked_at": revoked_at,
        "copy_deleted": copy_deleted,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    report_id = d.pop("report_id")

    target_graph_id = d.pop("target_graph_id")

    revoked_at = datetime.datetime.fromisoformat(d.pop("revoked_at"))

    copy_deleted = d.pop("copy_deleted")

    revoke_report_share_response = cls(
      report_id=report_id,
      target_graph_id=target_graph_id,
      revoked_at=revoked_at,
      copy_deleted=copy_deleted,
    )

    revoke_report_share_response.additional_properties = d
    return revoke_report_share_response

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
