from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleVariableLite")


@_attrs_define
class RuleVariableLite:
  """`$Variable` → concept qname binding for a rule expression.

  Attributes:
      variable_name (str): Local name in the rule expression, e.g. 'Assets'.
      variable_qname (None | str | Unset): Concept qname the variable resolves to, e.g. 'fac:Assets'. Null for tenant
          CoA elements (which key on `code`/`element_id`, not qname) — in that case the binding is carried by
          `variable_element_id`.
      variable_element_id (None | str | Unset): Element id the variable binds to directly. Set for schedule SumEquals
          rules over CoA-debit elements that have no qname; null otherwise.
  """

  variable_name: str
  variable_qname: None | str | Unset = UNSET
  variable_element_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    variable_name = self.variable_name

    variable_qname: None | str | Unset
    if isinstance(self.variable_qname, Unset):
      variable_qname = UNSET
    else:
      variable_qname = self.variable_qname

    variable_element_id: None | str | Unset
    if isinstance(self.variable_element_id, Unset):
      variable_element_id = UNSET
    else:
      variable_element_id = self.variable_element_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "variable_name": variable_name,
      }
    )
    if variable_qname is not UNSET:
      field_dict["variable_qname"] = variable_qname
    if variable_element_id is not UNSET:
      field_dict["variable_element_id"] = variable_element_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    variable_name = d.pop("variable_name")

    def _parse_variable_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    variable_qname = _parse_variable_qname(d.pop("variable_qname", UNSET))

    def _parse_variable_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    variable_element_id = _parse_variable_element_id(
      d.pop("variable_element_id", UNSET)
    )

    rule_variable_lite = cls(
      variable_name=variable_name,
      variable_qname=variable_qname,
      variable_element_id=variable_element_id,
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
