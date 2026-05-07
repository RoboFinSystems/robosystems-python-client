from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RuleVariableLite")


@_attrs_define
class RuleVariableLite:
  """`$Variable` → concept qname binding for a rule expression.

  Attributes:
      variable_name (str): Local name in the rule expression, e.g. 'Assets'.
      variable_qname (str): Concept qname the variable resolves to, e.g. 'fac:Assets'.
  """

  variable_name: str
  variable_qname: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    variable_name = self.variable_name

    variable_qname = self.variable_qname

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "variable_name": variable_name,
        "variable_qname": variable_qname,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    variable_name = d.pop("variable_name")

    variable_qname = d.pop("variable_qname")

    rule_variable_lite = cls(
      variable_name=variable_name,
      variable_qname=variable_qname,
    )

    rule_variable_lite.additional_properties = d
    return rule_variable_lite

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
