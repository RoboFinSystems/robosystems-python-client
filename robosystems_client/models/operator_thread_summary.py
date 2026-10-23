from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operator_thread_summary_last_status import OperatorThreadSummaryLastStatus

T = TypeVar("T", bound="OperatorThreadSummary")


@_attrs_define
class OperatorThreadSummary:
  """One console conversation: the runs that share a thread id.

  Attributes:
      thread_id (str): The thread id the runs were made under
      user_id (str): The user whose conversation it is
      title (str): The conversation's first question, clipped
      run_count (int): Runs in the thread
      first_run_at (datetime.datetime): When the first run started
      last_run_at (datetime.datetime): When the latest run started
      last_operator_type (str): The operator the latest run used
      last_status (OperatorThreadSummaryLastStatus): How the latest run ended
  """

  thread_id: str
  user_id: str
  title: str
  run_count: int
  first_run_at: datetime.datetime
  last_run_at: datetime.datetime
  last_operator_type: str
  last_status: OperatorThreadSummaryLastStatus
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    thread_id = self.thread_id

    user_id = self.user_id

    title = self.title

    run_count = self.run_count

    first_run_at = self.first_run_at.isoformat()

    last_run_at = self.last_run_at.isoformat()

    last_operator_type = self.last_operator_type

    last_status = self.last_status.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "thread_id": thread_id,
        "user_id": user_id,
        "title": title,
        "run_count": run_count,
        "first_run_at": first_run_at,
        "last_run_at": last_run_at,
        "last_operator_type": last_operator_type,
        "last_status": last_status,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    thread_id = d.pop("thread_id")

    user_id = d.pop("user_id")

    title = d.pop("title")

    run_count = d.pop("run_count")

    first_run_at = datetime.datetime.fromisoformat(d.pop("first_run_at"))

    last_run_at = datetime.datetime.fromisoformat(d.pop("last_run_at"))

    last_operator_type = d.pop("last_operator_type")

    last_status = OperatorThreadSummaryLastStatus(d.pop("last_status"))

    operator_thread_summary = cls(
      thread_id=thread_id,
      user_id=user_id,
      title=title,
      run_count=run_count,
      first_run_at=first_run_at,
      last_run_at=last_run_at,
      last_operator_type=last_operator_type,
      last_status=last_status,
    )

    operator_thread_summary.additional_properties = d
    return operator_thread_summary

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
