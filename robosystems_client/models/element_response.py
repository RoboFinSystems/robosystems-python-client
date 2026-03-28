from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementResponse")


@_attrs_define
class ElementResponse:
  """Element with taxonomy context — extends AccountResponse.

  Attributes:
      id (str):
      name (str):
      classification (str):
      balance_type (str):
      period_type (str):
      is_abstract (bool):
      element_type (str):
      source (str):
      depth (int):
      is_active (bool):
      code (None | str | Unset):
      description (None | str | Unset):
      qname (None | str | Unset):
      namespace (None | str | Unset):
      sub_classification (None | str | Unset):
      taxonomy_id (None | str | Unset):
      parent_id (None | str | Unset):
      external_id (None | str | Unset):
      external_source (None | str | Unset):
  """

  id: str
  name: str
  classification: str
  balance_type: str
  period_type: str
  is_abstract: bool
  element_type: str
  source: str
  depth: int
  is_active: bool
  code: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  qname: None | str | Unset = UNSET
  namespace: None | str | Unset = UNSET
  sub_classification: None | str | Unset = UNSET
  taxonomy_id: None | str | Unset = UNSET
  parent_id: None | str | Unset = UNSET
  external_id: None | str | Unset = UNSET
  external_source: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    classification = self.classification

    balance_type = self.balance_type

    period_type = self.period_type

    is_abstract = self.is_abstract

    element_type = self.element_type

    source = self.source

    depth = self.depth

    is_active = self.is_active

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    qname: None | str | Unset
    if isinstance(self.qname, Unset):
      qname = UNSET
    else:
      qname = self.qname

    namespace: None | str | Unset
    if isinstance(self.namespace, Unset):
      namespace = UNSET
    else:
      namespace = self.namespace

    sub_classification: None | str | Unset
    if isinstance(self.sub_classification, Unset):
      sub_classification = UNSET
    else:
      sub_classification = self.sub_classification

    taxonomy_id: None | str | Unset
    if isinstance(self.taxonomy_id, Unset):
      taxonomy_id = UNSET
    else:
      taxonomy_id = self.taxonomy_id

    parent_id: None | str | Unset
    if isinstance(self.parent_id, Unset):
      parent_id = UNSET
    else:
      parent_id = self.parent_id

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    external_source: None | str | Unset
    if isinstance(self.external_source, Unset):
      external_source = UNSET
    else:
      external_source = self.external_source

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "classification": classification,
        "balance_type": balance_type,
        "period_type": period_type,
        "is_abstract": is_abstract,
        "element_type": element_type,
        "source": source,
        "depth": depth,
        "is_active": is_active,
      }
    )
    if code is not UNSET:
      field_dict["code"] = code
    if description is not UNSET:
      field_dict["description"] = description
    if qname is not UNSET:
      field_dict["qname"] = qname
    if namespace is not UNSET:
      field_dict["namespace"] = namespace
    if sub_classification is not UNSET:
      field_dict["sub_classification"] = sub_classification
    if taxonomy_id is not UNSET:
      field_dict["taxonomy_id"] = taxonomy_id
    if parent_id is not UNSET:
      field_dict["parent_id"] = parent_id
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if external_source is not UNSET:
      field_dict["external_source"] = external_source

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    classification = d.pop("classification")

    balance_type = d.pop("balance_type")

    period_type = d.pop("period_type")

    is_abstract = d.pop("is_abstract")

    element_type = d.pop("element_type")

    source = d.pop("source")

    depth = d.pop("depth")

    is_active = d.pop("is_active")

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    qname = _parse_qname(d.pop("qname", UNSET))

    def _parse_namespace(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    namespace = _parse_namespace(d.pop("namespace", UNSET))

    def _parse_sub_classification(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sub_classification = _parse_sub_classification(d.pop("sub_classification", UNSET))

    def _parse_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    taxonomy_id = _parse_taxonomy_id(d.pop("taxonomy_id", UNSET))

    def _parse_parent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    def _parse_external_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_source = _parse_external_source(d.pop("external_source", UNSET))

    element_response = cls(
      id=id,
      name=name,
      classification=classification,
      balance_type=balance_type,
      period_type=period_type,
      is_abstract=is_abstract,
      element_type=element_type,
      source=source,
      depth=depth,
      is_active=is_active,
      code=code,
      description=description,
      qname=qname,
      namespace=namespace,
      sub_classification=sub_classification,
      taxonomy_id=taxonomy_id,
      parent_id=parent_id,
      external_id=external_id,
      external_source=external_source,
    )

    element_response.additional_properties = d
    return element_response

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
