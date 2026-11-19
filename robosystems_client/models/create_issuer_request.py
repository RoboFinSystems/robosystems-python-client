from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateIssuerRequest")


@_attrs_define
class CreateIssuerRequest:
  """CQRS body for `POST /operations/create-issuer`.

  An issuer is a company the fund holds or follows that does not keep its
  books on this platform: an entity in the fund's graph that securities and
  received reports attach to. A company that shares a report in from its own
  graph gets its entity from the share instead.

      Attributes:
          name (str): The company's name.
          legal_name (None | str | Unset): Its legal name, when different.
          lei (None | str | Unset): Legal Entity Identifier, if it has one.
          cik (None | str | Unset): SEC Central Index Key, if it has one.
          tax_id (None | str | Unset): Tax identifier (an EIN in the United States).
          entity_type (None | str | Unset): Legal form, e.g. `corporation`, `llc`, `partnership`.
          industry (None | str | Unset): Industry, as free text.
          website (None | str | Unset): The company's website.
  """

  name: str
  legal_name: None | str | Unset = UNSET
  lei: None | str | Unset = UNSET
  cik: None | str | Unset = UNSET
  tax_id: None | str | Unset = UNSET
  entity_type: None | str | Unset = UNSET
  industry: None | str | Unset = UNSET
  website: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    legal_name: None | str | Unset
    if isinstance(self.legal_name, Unset):
      legal_name = UNSET
    else:
      legal_name = self.legal_name

    lei: None | str | Unset
    if isinstance(self.lei, Unset):
      lei = UNSET
    else:
      lei = self.lei

    cik: None | str | Unset
    if isinstance(self.cik, Unset):
      cik = UNSET
    else:
      cik = self.cik

    tax_id: None | str | Unset
    if isinstance(self.tax_id, Unset):
      tax_id = UNSET
    else:
      tax_id = self.tax_id

    entity_type: None | str | Unset
    if isinstance(self.entity_type, Unset):
      entity_type = UNSET
    else:
      entity_type = self.entity_type

    industry: None | str | Unset
    if isinstance(self.industry, Unset):
      industry = UNSET
    else:
      industry = self.industry

    website: None | str | Unset
    if isinstance(self.website, Unset):
      website = UNSET
    else:
      website = self.website

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if legal_name is not UNSET:
      field_dict["legal_name"] = legal_name
    if lei is not UNSET:
      field_dict["lei"] = lei
    if cik is not UNSET:
      field_dict["cik"] = cik
    if tax_id is not UNSET:
      field_dict["tax_id"] = tax_id
    if entity_type is not UNSET:
      field_dict["entity_type"] = entity_type
    if industry is not UNSET:
      field_dict["industry"] = industry
    if website is not UNSET:
      field_dict["website"] = website

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    def _parse_legal_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

    def _parse_lei(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    lei = _parse_lei(d.pop("lei", UNSET))

    def _parse_cik(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    cik = _parse_cik(d.pop("cik", UNSET))

    def _parse_tax_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    tax_id = _parse_tax_id(d.pop("tax_id", UNSET))

    def _parse_entity_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

    def _parse_industry(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    industry = _parse_industry(d.pop("industry", UNSET))

    def _parse_website(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    website = _parse_website(d.pop("website", UNSET))

    create_issuer_request = cls(
      name=name,
      legal_name=legal_name,
      lei=lei,
      cik=cik,
      tax_id=tax_id,
      entity_type=entity_type,
      industry=industry,
      website=website,
    )

    create_issuer_request.additional_properties = d
    return create_issuer_request

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
