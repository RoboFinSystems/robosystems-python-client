from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operator_run_summary_status import OperatorRunSummaryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorRunSummary")


@_attrs_define
class OperatorRunSummary:
  """One in-app AI operator run: what it was asked and what it answered.

  Attributes:
      operation_id (str): The run's operation id; every mutation audit entry the run made carries it as `operation_id`
      user_id (str): The user the run ran as
      operator_type (str): The operator that ran
      mode (str): The execution mode the run used
      status (OperatorRunSummaryStatus): How the run ended
      question (str): The message the run was given
      started_at (datetime.datetime): When the run started on the worker
      finished_at (datetime.datetime): When the run ended
      duration_ms (float): How long the run took
      thread_id (None | str | Unset): The conversation the run belongs to, when the caller threaded it; null for a
          standalone API call
      answer (None | str | Unset): The operator's answer; null when the run did not reach one
      error (None | str | Unset): Why a failed run failed
      credits_consumed (float | Unset): Credits the run's model calls cost Default: 0.0.
      call_count (int | Unset): Model calls the run made Default: 0.
      tools_called (list[str] | Unset): The tools the run called, each named once
      write_count (int | Unset): Writes the run made to the graph Default: 0.
  """

  operation_id: str
  user_id: str
  operator_type: str
  mode: str
  status: OperatorRunSummaryStatus
  question: str
  started_at: datetime.datetime
  finished_at: datetime.datetime
  duration_ms: float
  thread_id: None | str | Unset = UNSET
  answer: None | str | Unset = UNSET
  error: None | str | Unset = UNSET
  credits_consumed: float | Unset = 0.0
  call_count: int | Unset = 0
  tools_called: list[str] | Unset = UNSET
  write_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    operation_id = self.operation_id

    user_id = self.user_id

    operator_type = self.operator_type

    mode = self.mode

    status = self.status.value

    question = self.question

    started_at = self.started_at.isoformat()

    finished_at = self.finished_at.isoformat()

    duration_ms = self.duration_ms

    thread_id: None | str | Unset
    if isinstance(self.thread_id, Unset):
      thread_id = UNSET
    else:
      thread_id = self.thread_id

    answer: None | str | Unset
    if isinstance(self.answer, Unset):
      answer = UNSET
    else:
      answer = self.answer

    error: None | str | Unset
    if isinstance(self.error, Unset):
      error = UNSET
    else:
      error = self.error

    credits_consumed = self.credits_consumed

    call_count = self.call_count

    tools_called: list[str] | Unset = UNSET
    if not isinstance(self.tools_called, Unset):
      tools_called = self.tools_called

    write_count = self.write_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "operation_id": operation_id,
        "user_id": user_id,
        "operator_type": operator_type,
        "mode": mode,
        "status": status,
        "question": question,
        "started_at": started_at,
        "finished_at": finished_at,
        "duration_ms": duration_ms,
      }
    )
    if thread_id is not UNSET:
      field_dict["thread_id"] = thread_id
    if answer is not UNSET:
      field_dict["answer"] = answer
    if error is not UNSET:
      field_dict["error"] = error
    if credits_consumed is not UNSET:
      field_dict["credits_consumed"] = credits_consumed
    if call_count is not UNSET:
      field_dict["call_count"] = call_count
    if tools_called is not UNSET:
      field_dict["tools_called"] = tools_called
    if write_count is not UNSET:
      field_dict["write_count"] = write_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    operation_id = d.pop("operation_id")

    user_id = d.pop("user_id")

    operator_type = d.pop("operator_type")

    mode = d.pop("mode")

    status = OperatorRunSummaryStatus(d.pop("status"))

    question = d.pop("question")

    started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

    finished_at = datetime.datetime.fromisoformat(d.pop("finished_at"))

    duration_ms = d.pop("duration_ms")

    def _parse_thread_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

    def _parse_answer(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    answer = _parse_answer(d.pop("answer", UNSET))

    def _parse_error(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    error = _parse_error(d.pop("error", UNSET))

    credits_consumed = d.pop("credits_consumed", UNSET)

    call_count = d.pop("call_count", UNSET)

    tools_called = cast(list[str], d.pop("tools_called", UNSET))

    write_count = d.pop("write_count", UNSET)

    operator_run_summary = cls(
      operation_id=operation_id,
      user_id=user_id,
      operator_type=operator_type,
      mode=mode,
      status=status,
      question=question,
      started_at=started_at,
      finished_at=finished_at,
      duration_ms=duration_ms,
      thread_id=thread_id,
      answer=answer,
      error=error,
      credits_consumed=credits_consumed,
      call_count=call_count,
      tools_called=tools_called,
      write_count=write_count,
    )

    operator_run_summary.additional_properties = d
    return operator_run_summary

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
