from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_security_request_terms import CreateSecurityRequestTerms


T = TypeVar("T", bound="CreateSecurityRequest")


@_attrs_define
class CreateSecurityRequest:
  """
  Attributes:
      name (str):
      security_type (str):
      entity_id (None | str | Unset):
      source_graph_id (None | str | Unset):
      security_subtype (None | str | Unset):
      terms (CreateSecurityRequestTerms | Unset):
      authorized_shares (int | None | Unset):
      outstanding_shares (int | None | Unset):
  """

  name: str
  security_type: str
  entity_id: None | str | Unset = UNSET
  source_graph_id: None | str | Unset = UNSET
  security_subtype: None | str | Unset = UNSET
  terms: CreateSecurityRequestTerms | Unset = UNSET
  authorized_shares: int | None | Unset = UNSET
  outstanding_shares: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    security_type = self.security_type

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    source_graph_id: None | str | Unset
    if isinstance(self.source_graph_id, Unset):
      source_graph_id = UNSET
    else:
      source_graph_id = self.source_graph_id

    security_subtype: None | str | Unset
    if isinstance(self.security_subtype, Unset):
      security_subtype = UNSET
    else:
      security_subtype = self.security_subtype

    terms: dict[str, Any] | Unset = UNSET
    if not isinstance(self.terms, Unset):
      terms = self.terms.to_dict()

    authorized_shares: int | None | Unset
    if isinstance(self.authorized_shares, Unset):
      authorized_shares = UNSET
    else:
      authorized_shares = self.authorized_shares

    outstanding_shares: int | None | Unset
    if isinstance(self.outstanding_shares, Unset):
      outstanding_shares = UNSET
    else:
      outstanding_shares = self.outstanding_shares

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "security_type": security_type,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if source_graph_id is not UNSET:
      field_dict["source_graph_id"] = source_graph_id
    if security_subtype is not UNSET:
      field_dict["security_subtype"] = security_subtype
    if terms is not UNSET:
      field_dict["terms"] = terms
    if authorized_shares is not UNSET:
      field_dict["authorized_shares"] = authorized_shares
    if outstanding_shares is not UNSET:
      field_dict["outstanding_shares"] = outstanding_shares

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_security_request_terms import CreateSecurityRequestTerms

    d = dict(src_dict)
    name = d.pop("name")

    security_type = d.pop("security_type")

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_source_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_id = _parse_source_graph_id(d.pop("source_graph_id", UNSET))

    def _parse_security_subtype(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    security_subtype = _parse_security_subtype(d.pop("security_subtype", UNSET))

    _terms = d.pop("terms", UNSET)
    terms: CreateSecurityRequestTerms | Unset
    if isinstance(_terms, Unset):
      terms = UNSET
    else:
      terms = CreateSecurityRequestTerms.from_dict(_terms)

    def _parse_authorized_shares(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    authorized_shares = _parse_authorized_shares(d.pop("authorized_shares", UNSET))

    def _parse_outstanding_shares(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    outstanding_shares = _parse_outstanding_shares(d.pop("outstanding_shares", UNSET))

    create_security_request = cls(
      name=name,
      security_type=security_type,
      entity_id=entity_id,
      source_graph_id=source_graph_id,
      security_subtype=security_subtype,
      terms=terms,
      authorized_shares=authorized_shares,
      outstanding_shares=outstanding_shares,
    )

    create_security_request.additional_properties = d
    return create_security_request

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
