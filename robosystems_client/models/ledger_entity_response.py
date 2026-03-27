from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerEntityResponse")


@_attrs_define
class LedgerEntityResponse:
  """Entity details from the extensions OLTP database.

  Attributes:
      id (str):
      name (str):
      legal_name (None | str | Unset):
      uri (None | str | Unset):
      cik (None | str | Unset):
      ticker (None | str | Unset):
      exchange (None | str | Unset):
      sic (None | str | Unset):
      sic_description (None | str | Unset):
      category (None | str | Unset):
      state_of_incorporation (None | str | Unset):
      fiscal_year_end (None | str | Unset):
      tax_id (None | str | Unset):
      lei (None | str | Unset):
      industry (None | str | Unset):
      entity_type (None | str | Unset):
      phone (None | str | Unset):
      website (None | str | Unset):
      status (str | Unset):  Default: 'active'.
      is_parent (bool | Unset):  Default: True.
      parent_entity_id (None | str | Unset):
      source (str | Unset):  Default: 'native'.
      source_id (None | str | Unset):
      connection_id (None | str | Unset):
      address_line1 (None | str | Unset):
      address_city (None | str | Unset):
      address_state (None | str | Unset):
      address_postal_code (None | str | Unset):
      address_country (None | str | Unset):
      created_at (None | str | Unset):
      updated_at (None | str | Unset):
  """

  id: str
  name: str
  legal_name: None | str | Unset = UNSET
  uri: None | str | Unset = UNSET
  cik: None | str | Unset = UNSET
  ticker: None | str | Unset = UNSET
  exchange: None | str | Unset = UNSET
  sic: None | str | Unset = UNSET
  sic_description: None | str | Unset = UNSET
  category: None | str | Unset = UNSET
  state_of_incorporation: None | str | Unset = UNSET
  fiscal_year_end: None | str | Unset = UNSET
  tax_id: None | str | Unset = UNSET
  lei: None | str | Unset = UNSET
  industry: None | str | Unset = UNSET
  entity_type: None | str | Unset = UNSET
  phone: None | str | Unset = UNSET
  website: None | str | Unset = UNSET
  status: str | Unset = "active"
  is_parent: bool | Unset = True
  parent_entity_id: None | str | Unset = UNSET
  source: str | Unset = "native"
  source_id: None | str | Unset = UNSET
  connection_id: None | str | Unset = UNSET
  address_line1: None | str | Unset = UNSET
  address_city: None | str | Unset = UNSET
  address_state: None | str | Unset = UNSET
  address_postal_code: None | str | Unset = UNSET
  address_country: None | str | Unset = UNSET
  created_at: None | str | Unset = UNSET
  updated_at: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    legal_name: None | str | Unset
    if isinstance(self.legal_name, Unset):
      legal_name = UNSET
    else:
      legal_name = self.legal_name

    uri: None | str | Unset
    if isinstance(self.uri, Unset):
      uri = UNSET
    else:
      uri = self.uri

    cik: None | str | Unset
    if isinstance(self.cik, Unset):
      cik = UNSET
    else:
      cik = self.cik

    ticker: None | str | Unset
    if isinstance(self.ticker, Unset):
      ticker = UNSET
    else:
      ticker = self.ticker

    exchange: None | str | Unset
    if isinstance(self.exchange, Unset):
      exchange = UNSET
    else:
      exchange = self.exchange

    sic: None | str | Unset
    if isinstance(self.sic, Unset):
      sic = UNSET
    else:
      sic = self.sic

    sic_description: None | str | Unset
    if isinstance(self.sic_description, Unset):
      sic_description = UNSET
    else:
      sic_description = self.sic_description

    category: None | str | Unset
    if isinstance(self.category, Unset):
      category = UNSET
    else:
      category = self.category

    state_of_incorporation: None | str | Unset
    if isinstance(self.state_of_incorporation, Unset):
      state_of_incorporation = UNSET
    else:
      state_of_incorporation = self.state_of_incorporation

    fiscal_year_end: None | str | Unset
    if isinstance(self.fiscal_year_end, Unset):
      fiscal_year_end = UNSET
    else:
      fiscal_year_end = self.fiscal_year_end

    tax_id: None | str | Unset
    if isinstance(self.tax_id, Unset):
      tax_id = UNSET
    else:
      tax_id = self.tax_id

    lei: None | str | Unset
    if isinstance(self.lei, Unset):
      lei = UNSET
    else:
      lei = self.lei

    industry: None | str | Unset
    if isinstance(self.industry, Unset):
      industry = UNSET
    else:
      industry = self.industry

    entity_type: None | str | Unset
    if isinstance(self.entity_type, Unset):
      entity_type = UNSET
    else:
      entity_type = self.entity_type

    phone: None | str | Unset
    if isinstance(self.phone, Unset):
      phone = UNSET
    else:
      phone = self.phone

    website: None | str | Unset
    if isinstance(self.website, Unset):
      website = UNSET
    else:
      website = self.website

    status = self.status

    is_parent = self.is_parent

    parent_entity_id: None | str | Unset
    if isinstance(self.parent_entity_id, Unset):
      parent_entity_id = UNSET
    else:
      parent_entity_id = self.parent_entity_id

    source = self.source

    source_id: None | str | Unset
    if isinstance(self.source_id, Unset):
      source_id = UNSET
    else:
      source_id = self.source_id

    connection_id: None | str | Unset
    if isinstance(self.connection_id, Unset):
      connection_id = UNSET
    else:
      connection_id = self.connection_id

    address_line1: None | str | Unset
    if isinstance(self.address_line1, Unset):
      address_line1 = UNSET
    else:
      address_line1 = self.address_line1

    address_city: None | str | Unset
    if isinstance(self.address_city, Unset):
      address_city = UNSET
    else:
      address_city = self.address_city

    address_state: None | str | Unset
    if isinstance(self.address_state, Unset):
      address_state = UNSET
    else:
      address_state = self.address_state

    address_postal_code: None | str | Unset
    if isinstance(self.address_postal_code, Unset):
      address_postal_code = UNSET
    else:
      address_postal_code = self.address_postal_code

    address_country: None | str | Unset
    if isinstance(self.address_country, Unset):
      address_country = UNSET
    else:
      address_country = self.address_country

    created_at: None | str | Unset
    if isinstance(self.created_at, Unset):
      created_at = UNSET
    else:
      created_at = self.created_at

    updated_at: None | str | Unset
    if isinstance(self.updated_at, Unset):
      updated_at = UNSET
    else:
      updated_at = self.updated_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
      }
    )
    if legal_name is not UNSET:
      field_dict["legal_name"] = legal_name
    if uri is not UNSET:
      field_dict["uri"] = uri
    if cik is not UNSET:
      field_dict["cik"] = cik
    if ticker is not UNSET:
      field_dict["ticker"] = ticker
    if exchange is not UNSET:
      field_dict["exchange"] = exchange
    if sic is not UNSET:
      field_dict["sic"] = sic
    if sic_description is not UNSET:
      field_dict["sic_description"] = sic_description
    if category is not UNSET:
      field_dict["category"] = category
    if state_of_incorporation is not UNSET:
      field_dict["state_of_incorporation"] = state_of_incorporation
    if fiscal_year_end is not UNSET:
      field_dict["fiscal_year_end"] = fiscal_year_end
    if tax_id is not UNSET:
      field_dict["tax_id"] = tax_id
    if lei is not UNSET:
      field_dict["lei"] = lei
    if industry is not UNSET:
      field_dict["industry"] = industry
    if entity_type is not UNSET:
      field_dict["entity_type"] = entity_type
    if phone is not UNSET:
      field_dict["phone"] = phone
    if website is not UNSET:
      field_dict["website"] = website
    if status is not UNSET:
      field_dict["status"] = status
    if is_parent is not UNSET:
      field_dict["is_parent"] = is_parent
    if parent_entity_id is not UNSET:
      field_dict["parent_entity_id"] = parent_entity_id
    if source is not UNSET:
      field_dict["source"] = source
    if source_id is not UNSET:
      field_dict["source_id"] = source_id
    if connection_id is not UNSET:
      field_dict["connection_id"] = connection_id
    if address_line1 is not UNSET:
      field_dict["address_line1"] = address_line1
    if address_city is not UNSET:
      field_dict["address_city"] = address_city
    if address_state is not UNSET:
      field_dict["address_state"] = address_state
    if address_postal_code is not UNSET:
      field_dict["address_postal_code"] = address_postal_code
    if address_country is not UNSET:
      field_dict["address_country"] = address_country
    if created_at is not UNSET:
      field_dict["created_at"] = created_at
    if updated_at is not UNSET:
      field_dict["updated_at"] = updated_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    def _parse_legal_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

    def _parse_uri(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    uri = _parse_uri(d.pop("uri", UNSET))

    def _parse_cik(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    cik = _parse_cik(d.pop("cik", UNSET))

    def _parse_ticker(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    ticker = _parse_ticker(d.pop("ticker", UNSET))

    def _parse_exchange(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    exchange = _parse_exchange(d.pop("exchange", UNSET))

    def _parse_sic(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sic = _parse_sic(d.pop("sic", UNSET))

    def _parse_sic_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sic_description = _parse_sic_description(d.pop("sic_description", UNSET))

    def _parse_category(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    category = _parse_category(d.pop("category", UNSET))

    def _parse_state_of_incorporation(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    state_of_incorporation = _parse_state_of_incorporation(
      d.pop("state_of_incorporation", UNSET)
    )

    def _parse_fiscal_year_end(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fiscal_year_end = _parse_fiscal_year_end(d.pop("fiscal_year_end", UNSET))

    def _parse_tax_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    tax_id = _parse_tax_id(d.pop("tax_id", UNSET))

    def _parse_lei(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    lei = _parse_lei(d.pop("lei", UNSET))

    def _parse_industry(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    industry = _parse_industry(d.pop("industry", UNSET))

    def _parse_entity_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

    def _parse_phone(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    phone = _parse_phone(d.pop("phone", UNSET))

    def _parse_website(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    website = _parse_website(d.pop("website", UNSET))

    status = d.pop("status", UNSET)

    is_parent = d.pop("is_parent", UNSET)

    def _parse_parent_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_entity_id = _parse_parent_entity_id(d.pop("parent_entity_id", UNSET))

    source = d.pop("source", UNSET)

    def _parse_source_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_id = _parse_source_id(d.pop("source_id", UNSET))

    def _parse_connection_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    connection_id = _parse_connection_id(d.pop("connection_id", UNSET))

    def _parse_address_line1(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    address_line1 = _parse_address_line1(d.pop("address_line1", UNSET))

    def _parse_address_city(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    address_city = _parse_address_city(d.pop("address_city", UNSET))

    def _parse_address_state(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    address_state = _parse_address_state(d.pop("address_state", UNSET))

    def _parse_address_postal_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    address_postal_code = _parse_address_postal_code(
      d.pop("address_postal_code", UNSET)
    )

    def _parse_address_country(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    address_country = _parse_address_country(d.pop("address_country", UNSET))

    def _parse_created_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    created_at = _parse_created_at(d.pop("created_at", UNSET))

    def _parse_updated_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

    ledger_entity_response = cls(
      id=id,
      name=name,
      legal_name=legal_name,
      uri=uri,
      cik=cik,
      ticker=ticker,
      exchange=exchange,
      sic=sic,
      sic_description=sic_description,
      category=category,
      state_of_incorporation=state_of_incorporation,
      fiscal_year_end=fiscal_year_end,
      tax_id=tax_id,
      lei=lei,
      industry=industry,
      entity_type=entity_type,
      phone=phone,
      website=website,
      status=status,
      is_parent=is_parent,
      parent_entity_id=parent_entity_id,
      source=source,
      source_id=source_id,
      connection_id=connection_id,
      address_line1=address_line1,
      address_city=address_city,
      address_state=address_state,
      address_postal_code=address_postal_code,
      address_country=address_country,
      created_at=created_at,
      updated_at=updated_at,
    )

    ledger_entity_response.additional_properties = d
    return ledger_entity_response

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
