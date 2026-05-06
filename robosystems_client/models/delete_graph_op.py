from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteGraphOp")


@_attrs_define
class DeleteGraphOp:
  """Body for the delete-graph operation.

  Permanently destroys the graph: cancels its subscription immediately, then
  triggers fast-path deprovisioning (LadybugDB database removed, DynamoDB slot
  freed, PG records cleaned). Requires `confirm` to equal the URL `graph_id`
  as a guard against accidental destructive calls.

      Attributes:
          confirm (str): Must equal the graph_id in the URL — confirms the caller intends to destroy this specific graph.
  """

  confirm: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    confirm = self.confirm

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "confirm": confirm,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    confirm = d.pop("confirm")

    delete_graph_op = cls(
      confirm=confirm,
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
