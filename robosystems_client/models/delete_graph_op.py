from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteGraphOp")


@_attrs_define
class DeleteGraphOp:
  """Body for the delete-graph operation.

  Permanently destroys the graph and cancels its subscription. Two modes:

  - **Immediate** (default): subscription canceled now (`ends_at = now`) and
    fast-path deprovisioning fires within ~10 minutes. Use when you want
    the data gone and the slot freed right away.
  - **At period end** (`at_period_end=true`): subscription canceled but
    `ends_at = current_period_end` so the graph stays usable through the
    paid period. The existing suspend → deprovision sensor pipeline tears
    it down after the retention window once the period closes.

  Requires `confirm` to equal the URL `graph_id` as a guard against
  accidental destructive calls.

      Attributes:
          confirm (str): Must equal the graph_id in the URL — confirms the caller intends to destroy this specific graph.
          at_period_end (bool | Unset): If true, defer cancellation and teardown to the end of the current billing period
              (graph stays usable until then). If false (default), cancel and tear down immediately. Default: False.
  """

  confirm: str
  at_period_end: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    confirm = self.confirm

    at_period_end = self.at_period_end

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "confirm": confirm,
      }
    )
    if at_period_end is not UNSET:
      field_dict["at_period_end"] = at_period_end

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    confirm = d.pop("confirm")

    at_period_end = d.pop("at_period_end", UNSET)

    delete_graph_op = cls(
      confirm=confirm,
      at_period_end=at_period_end,
    )

    delete_graph_op.additional_properties = d
    return delete_graph_op

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
