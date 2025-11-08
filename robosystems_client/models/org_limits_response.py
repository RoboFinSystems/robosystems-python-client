from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.org_limits_response_current_usage import OrgLimitsResponseCurrentUsage


T = TypeVar("T", bound="OrgLimitsResponse")


@_attrs_define
class OrgLimitsResponse:
  """Organization limits response.

  Attributes:
      org_id (str):
      max_graphs (int):
      current_usage (OrgLimitsResponseCurrentUsage):
      warnings (list[str]):
      can_create_graph (bool):
  """

  org_id: str
  max_graphs: int
  current_usage: "OrgLimitsResponseCurrentUsage"
  warnings: list[str]
  can_create_graph: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    org_id = self.org_id

    max_graphs = self.max_graphs

    current_usage = self.current_usage.to_dict()

    warnings = self.warnings

    can_create_graph = self.can_create_graph

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "org_id": org_id,
        "max_graphs": max_graphs,
        "current_usage": current_usage,
        "warnings": warnings,
        "can_create_graph": can_create_graph,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.org_limits_response_current_usage import OrgLimitsResponseCurrentUsage

    d = dict(src_dict)
    org_id = d.pop("org_id")

    max_graphs = d.pop("max_graphs")

    current_usage = OrgLimitsResponseCurrentUsage.from_dict(d.pop("current_usage"))

    warnings = cast(list[str], d.pop("warnings"))

    can_create_graph = d.pop("can_create_graph")

    org_limits_response = cls(
      org_id=org_id,
      max_graphs=max_graphs,
      current_usage=current_usage,
      warnings=warnings,
      can_create_graph=can_create_graph,
    )

    org_limits_response.additional_properties = d
    return org_limits_response

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
