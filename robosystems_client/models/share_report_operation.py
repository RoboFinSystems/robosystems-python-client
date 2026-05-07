from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ShareReportOperation")


@_attrs_define
class ShareReportOperation:
  """Share a published Report to every member of a publish list.

  Attributes:
      publish_list_id (str): Publish list whose members will receive the report. Created via `create-publish-list`.
      report_id (str): The published Report to share.
  """

  publish_list_id: str
  report_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    publish_list_id = self.publish_list_id

    report_id = self.report_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "publish_list_id": publish_list_id,
        "report_id": report_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    publish_list_id = d.pop("publish_list_id")

    report_id = d.pop("report_id")

    share_report_operation = cls(
      publish_list_id=publish_list_id,
      report_id=report_id,
    )

    share_report_operation.additional_properties = d
    return share_report_operation

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
