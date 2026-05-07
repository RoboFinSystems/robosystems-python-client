from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taxonomy_block_element_origin import TaxonomyBlockElementOrigin
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyBlockElement")


@_attrs_define
class TaxonomyBlockElement:
  """Element projection for the Taxonomy Block envelope.

  Attributes:
      id (str):
      name (str):
      origin (TaxonomyBlockElementOrigin): Provenance — 'library' if the element's taxonomy is locked
          (``is_locked=true``), else 'tenant'.
      qname (None | str | Unset):
      trait (None | str | Unset):
      balance_type (None | str | Unset):
      period_type (None | str | Unset):
      element_type (str | Unset):  Default: 'concept'.
      is_monetary (bool | Unset):  Default: True.
      parent_qname (None | str | Unset):
      depth (int | None | Unset):
  """

  id: str
  name: str
  origin: TaxonomyBlockElementOrigin
  qname: None | str | Unset = UNSET
  trait: None | str | Unset = UNSET
  balance_type: None | str | Unset = UNSET
  period_type: None | str | Unset = UNSET
  element_type: str | Unset = "concept"
  is_monetary: bool | Unset = True
  parent_qname: None | str | Unset = UNSET
  depth: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    origin = self.origin.value

    qname: None | str | Unset
    if isinstance(self.qname, Unset):
      qname = UNSET
    else:
      qname = self.qname

    trait: None | str | Unset
    if isinstance(self.trait, Unset):
      trait = UNSET
    else:
      trait = self.trait

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

    element_type = self.element_type

    is_monetary = self.is_monetary

    parent_qname: None | str | Unset
    if isinstance(self.parent_qname, Unset):
      parent_qname = UNSET
    else:
      parent_qname = self.parent_qname

    depth: int | None | Unset
    if isinstance(self.depth, Unset):
      depth = UNSET
    else:
      depth = self.depth

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "origin": origin,
      }
    )
    if qname is not UNSET:
      field_dict["qname"] = qname
    if trait is not UNSET:
      field_dict["trait"] = trait
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if element_type is not UNSET:
      field_dict["element_type"] = element_type
    if is_monetary is not UNSET:
      field_dict["is_monetary"] = is_monetary
    if parent_qname is not UNSET:
      field_dict["parent_qname"] = parent_qname
    if depth is not UNSET:
      field_dict["depth"] = depth

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    origin = TaxonomyBlockElementOrigin(d.pop("origin"))

    def _parse_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    qname = _parse_qname(d.pop("qname", UNSET))

    def _parse_trait(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    trait = _parse_trait(d.pop("trait", UNSET))

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

    element_type = d.pop("element_type", UNSET)

    is_monetary = d.pop("is_monetary", UNSET)

    def _parse_parent_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_qname = _parse_parent_qname(d.pop("parent_qname", UNSET))

    def _parse_depth(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    depth = _parse_depth(d.pop("depth", UNSET))

    taxonomy_block_element = cls(
      id=id,
      name=name,
      origin=origin,
      qname=qname,
      trait=trait,
      balance_type=balance_type,
      period_type=period_type,
      element_type=element_type,
      is_monetary=is_monetary,
      parent_qname=parent_qname,
      depth=depth,
    )

    taxonomy_block_element.additional_properties = d
    return taxonomy_block_element

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
