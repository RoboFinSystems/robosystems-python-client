from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.holding_security_summary import HoldingSecuritySummary


T = TypeVar("T", bound="HoldingResponse")


@_attrs_define
class HoldingResponse:
  """
  Attributes:
      entity_id (str):
      entity_name (str):
      securities (list[HoldingSecuritySummary]):
      total_cost_basis_dollars (float):
      position_count (int):
      source_graph_id (None | str | Unset):
      total_current_value_dollars (float | None | Unset):
  """

  entity_id: str
  entity_name: str
  securities: list[HoldingSecuritySummary]
  total_cost_basis_dollars: float
  position_count: int
  source_graph_id: None | str | Unset = UNSET
  total_current_value_dollars: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    entity_name = self.entity_name

    securities = []
    for securities_item_data in self.securities:
      securities_item = securities_item_data.to_dict()
      securities.append(securities_item)

    total_cost_basis_dollars = self.total_cost_basis_dollars

    position_count = self.position_count

    source_graph_id: None | str | Unset
    if isinstance(self.source_graph_id, Unset):
      source_graph_id = UNSET
    else:
      source_graph_id = self.source_graph_id

    total_current_value_dollars: float | None | Unset
    if isinstance(self.total_current_value_dollars, Unset):
      total_current_value_dollars = UNSET
    else:
      total_current_value_dollars = self.total_current_value_dollars

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "entity_name": entity_name,
        "securities": securities,
        "total_cost_basis_dollars": total_cost_basis_dollars,
        "position_count": position_count,
      }
    )
    if source_graph_id is not UNSET:
      field_dict["source_graph_id"] = source_graph_id
    if total_current_value_dollars is not UNSET:
      field_dict["total_current_value_dollars"] = total_current_value_dollars

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.holding_security_summary import HoldingSecuritySummary

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    entity_name = d.pop("entity_name")

    securities = []
    _securities = d.pop("securities")
    for securities_item_data in _securities:
      securities_item = HoldingSecuritySummary.from_dict(securities_item_data)

      securities.append(securities_item)

    total_cost_basis_dollars = d.pop("total_cost_basis_dollars")

    position_count = d.pop("position_count")

    def _parse_source_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_id = _parse_source_graph_id(d.pop("source_graph_id", UNSET))

    def _parse_total_current_value_dollars(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    total_current_value_dollars = _parse_total_current_value_dollars(
      d.pop("total_current_value_dollars", UNSET)
    )

    holding_response = cls(
      entity_id=entity_id,
      entity_name=entity_name,
      securities=securities,
      total_cost_basis_dollars=total_cost_basis_dollars,
      position_count=position_count,
      source_graph_id=source_graph_id,
      total_current_value_dollars=total_current_value_dollars,
    )

    holding_response.additional_properties = d
    return holding_response

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
