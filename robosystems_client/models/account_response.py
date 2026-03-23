from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountResponse")


@_attrs_define
class AccountResponse:
  """
  Attributes:
      id (str):
      code (str):
      name (str):
      classification (str):
      balance_type (str):
      depth (int):
      currency (str):
      is_active (bool):
      is_placeholder (bool):
      description (None | str | Unset):
      sub_classification (None | str | Unset):
      parent_id (None | str | Unset):
      account_type (None | str | Unset):
      external_id (None | str | Unset):
      external_source (None | str | Unset):
  """

  id: str
  code: str
  name: str
  classification: str
  balance_type: str
  depth: int
  currency: str
  is_active: bool
  is_placeholder: bool
  description: None | str | Unset = UNSET
  sub_classification: None | str | Unset = UNSET
  parent_id: None | str | Unset = UNSET
  account_type: None | str | Unset = UNSET
  external_id: None | str | Unset = UNSET
  external_source: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    code = self.code

    name = self.name

    classification = self.classification

    balance_type = self.balance_type

    depth = self.depth

    currency = self.currency

    is_active = self.is_active

    is_placeholder = self.is_placeholder

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    sub_classification: None | str | Unset
    if isinstance(self.sub_classification, Unset):
      sub_classification = UNSET
    else:
      sub_classification = self.sub_classification

    parent_id: None | str | Unset
    if isinstance(self.parent_id, Unset):
      parent_id = UNSET
    else:
      parent_id = self.parent_id

    account_type: None | str | Unset
    if isinstance(self.account_type, Unset):
      account_type = UNSET
    else:
      account_type = self.account_type

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
        "code": code,
        "name": name,
        "classification": classification,
        "balance_type": balance_type,
        "depth": depth,
        "currency": currency,
        "is_active": is_active,
        "is_placeholder": is_placeholder,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if sub_classification is not UNSET:
      field_dict["sub_classification"] = sub_classification
    if parent_id is not UNSET:
      field_dict["parent_id"] = parent_id
    if account_type is not UNSET:
      field_dict["account_type"] = account_type
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if external_source is not UNSET:
      field_dict["external_source"] = external_source

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    code = d.pop("code")

    name = d.pop("name")

    classification = d.pop("classification")

    balance_type = d.pop("balance_type")

    depth = d.pop("depth")

    currency = d.pop("currency")

    is_active = d.pop("is_active")

    is_placeholder = d.pop("is_placeholder")

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_sub_classification(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sub_classification = _parse_sub_classification(d.pop("sub_classification", UNSET))

    def _parse_parent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

    def _parse_account_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_type = _parse_account_type(d.pop("account_type", UNSET))

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

    account_response = cls(
      id=id,
      code=code,
      name=name,
      classification=classification,
      balance_type=balance_type,
      depth=depth,
      currency=currency,
      is_active=is_active,
      is_placeholder=is_placeholder,
      description=description,
      sub_classification=sub_classification,
      parent_id=parent_id,
      account_type=account_type,
      external_id=external_id,
      external_source=external_source,
    )

    account_response.additional_properties = d
    return account_response

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
