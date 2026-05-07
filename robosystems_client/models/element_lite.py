from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementLite")


@_attrs_define
class ElementLite:
  """Element projection for bundling inside an Information Block envelope.

  Narrower than :class:`LibraryElementResponse` — excludes the heavy fields
  (labels, references, classifications) that library browsing needs but
  block consumers don't. Agents + frontends ask for those on demand via
  the full library GraphQL fields when they need them.

      Attributes:
          id (str):
          name (str):
          element_type (str): concept | abstract | axis | member | hypercube
          qname (None | str | Unset):
          code (None | str | Unset):
          is_abstract (bool | Unset):  Default: False.
          is_monetary (bool | Unset):  Default: True.
          balance_type (None | str | Unset):
          period_type (None | str | Unset):
  """

  id: str
  name: str
  element_type: str
  qname: None | str | Unset = UNSET
  code: None | str | Unset = UNSET
  is_abstract: bool | Unset = False
  is_monetary: bool | Unset = True
  balance_type: None | str | Unset = UNSET
  period_type: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    element_type = self.element_type

    qname: None | str | Unset
    if isinstance(self.qname, Unset):
      qname = UNSET
    else:
      qname = self.qname

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    is_abstract = self.is_abstract

    is_monetary = self.is_monetary

    balance_type: None | str | Unset
    if isinstance(self.balance_type, Unset):
      balance_type = UNSET
    else:
      balance_type = self.balance_type

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "element_type": element_type,
      }
    )
    if qname is not UNSET:
      field_dict["qname"] = qname
    if code is not UNSET:
      field_dict["code"] = code
    if is_abstract is not UNSET:
      field_dict["is_abstract"] = is_abstract
    if is_monetary is not UNSET:
      field_dict["is_monetary"] = is_monetary
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if period_type is not UNSET:
      field_dict["period_type"] = period_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    element_type = d.pop("element_type")

    def _parse_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    qname = _parse_qname(d.pop("qname", UNSET))

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    is_abstract = d.pop("is_abstract", UNSET)

    is_monetary = d.pop("is_monetary", UNSET)

    def _parse_balance_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    balance_type = _parse_balance_type(d.pop("balance_type", UNSET))

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    element_lite = cls(
      id=id,
      name=name,
      element_type=element_type,
      qname=qname,
      code=code,
      is_abstract=is_abstract,
      is_monetary=is_monetary,
      balance_type=balance_type,
      period_type=period_type,
    )

    element_lite.additional_properties = d
    return element_lite

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
