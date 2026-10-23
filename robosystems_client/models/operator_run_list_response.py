from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operator_run_summary import OperatorRunSummary


T = TypeVar("T", bound="OperatorRunListResponse")


@_attrs_define
class OperatorRunListResponse:
  """A page of the graph's operator runs, newest first.

  Attributes:
      graph_id (str):
      runs (list[OperatorRunSummary]):
      next_cursor (None | str | Unset): Pass as `cursor` for the next, older page; null on the last page
  """

  graph_id: str
  runs: list[OperatorRunSummary]
  next_cursor: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    runs = []
    for runs_item_data in self.runs:
      runs_item = runs_item_data.to_dict()
      runs.append(runs_item)

    next_cursor: None | str | Unset
    if isinstance(self.next_cursor, Unset):
      next_cursor = UNSET
    else:
      next_cursor = self.next_cursor

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "runs": runs,
      }
    )
    if next_cursor is not UNSET:
      field_dict["next_cursor"] = next_cursor

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operator_run_summary import OperatorRunSummary

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    runs = []
    _runs = d.pop("runs")
    for runs_item_data in _runs:
      runs_item = OperatorRunSummary.from_dict(runs_item_data)

      runs.append(runs_item)

    def _parse_next_cursor(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

    operator_run_list_response = cls(
      graph_id=graph_id,
      runs=runs,
      next_cursor=next_cursor,
    )

    operator_run_list_response.additional_properties = d
    return operator_run_list_response

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
