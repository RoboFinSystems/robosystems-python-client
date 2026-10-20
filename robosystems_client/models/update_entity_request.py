from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_entity_request_consolidation_method_type_0 import (
  UpdateEntityRequestConsolidationMethodType0,
)
from ..models.update_entity_request_entity_role_type_0 import (
  UpdateEntityRequestEntityRoleType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEntityRequest")


@_attrs_define
class UpdateEntityRequest:
  """Update an entity of the graph's reporting group. All fields are
  optional — pass only what changes. Identifiers (CIK, LEI, tax_id) are
  typically set once at onboarding; address fields are flattened to make
  them easy to project into reporting forms (1099, state filings).

  Omit `entity_id` to target the group parent.

      Attributes:
          entity_id (None | str | Unset): The entity to update. Omit to target the group parent — the single-entity
              default.
          name (None | str | Unset):
          legal_name (None | str | Unset):
          uri (None | str | Unset):
          cik (None | str | Unset):
          ticker (None | str | Unset):
          exchange (None | str | Unset):
          sic (None | str | Unset):
          sic_description (None | str | Unset):
          category (None | str | Unset):
          state_of_incorporation (None | str | Unset):
          fiscal_year_end (None | str | Unset): Fiscal year-end as MM-DD (e.g. '12-31', '06-30').
          tax_id (None | str | Unset):
          lei (None | str | Unset):
          industry (None | str | Unset):
          entity_type (None | str | Unset):
          phone (None | str | Unset):
          website (None | str | Unset):
          address_line1 (None | str | Unset):
          address_city (None | str | Unset):
          address_state (None | str | Unset):
          address_postal_code (None | str | Unset):
          address_country (None | str | Unset):
          ownership_pct (float | None | Unset): The parent's share of this entity, as a percent. Refused on the group
              parent, which has no owner in the graph. A new share re-derives `consolidation_method` unless that is given too.
          consolidation_method (None | Unset | UpdateEntityRequestConsolidationMethodType0): How the group's consolidated
              statements treat this entity: `full` (its books are summed and an outside owner's share is carried as
              noncontrolling interest), `equity` (one investment line and one income line), `cost` (an investment at cost) or
              `none` (the group parent, the consolidation entity, a linked counterparty). Derived from `ownership_pct` when
              not given — 50 and above `full`, 20 to 50 `equity`, below 20 `cost`, unrecorded `full` — and set by a person
              where control is not the percentage: a managing member with a minority stake consolidates in full, a majority
              without control takes the equity method. On the group parent and the consolidation entity only `none` holds.
          entity_role (None | Unset | UpdateEntityRequestEntityRoleType0): `operating` keeps a company's books.
              `consolidation` is the group's one entity for the consolidating entries — eliminations, noncontrolling interest,
              the equity-method pick-up — the adjustments column of a consolidation worksheet, which only the consolidated
              statements read and no operating company's statements ever include. Its method is `none`. Refused on the group
              parent. Marking an entity `consolidation` sets its method to `none`.
          joined_on (datetime.date | None | Unset): The month this entity became a member of the group, as any date in it;
              null is a member since the beginning. The consolidated statements include it from that month. Membership is by
              month: a period column wider than a month that overlaps the interval is summed whole, so a member's books in
              this graph should hold only the months it belonged. Pass null to clear it. Refused on the consolidation entity.
          left_on (datetime.date | None | Unset): The month this entity left the group, as any date in it; null is a
              member still. The consolidated statements include it through that month and leave it out after. Membership is by
              month: a period column wider than a month that overlaps the interval is summed whole, so a member's books in
              this graph should hold only the months it belonged. Must not precede `joined_on`. Set it when a subsidiary is
              sold, dissolved or deconsolidated; its closed months and stamped statements stay readable under the group. Pass
              null to reopen membership. Refused on the consolidation entity.
  """

  entity_id: None | str | Unset = UNSET
  name: None | str | Unset = UNSET
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
  address_line1: None | str | Unset = UNSET
  address_city: None | str | Unset = UNSET
  address_state: None | str | Unset = UNSET
  address_postal_code: None | str | Unset = UNSET
  address_country: None | str | Unset = UNSET
  ownership_pct: float | None | Unset = UNSET
  consolidation_method: None | Unset | UpdateEntityRequestConsolidationMethodType0 = (
    UNSET
  )
  entity_role: None | Unset | UpdateEntityRequestEntityRoleType0 = UNSET
  joined_on: datetime.date | None | Unset = UNSET
  left_on: datetime.date | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
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

    ownership_pct: float | None | Unset
    if isinstance(self.ownership_pct, Unset):
      ownership_pct = UNSET
    else:
      ownership_pct = self.ownership_pct

    consolidation_method: None | str | Unset
    if isinstance(self.consolidation_method, Unset):
      consolidation_method = UNSET
    elif isinstance(
      self.consolidation_method, UpdateEntityRequestConsolidationMethodType0
    ):
      consolidation_method = self.consolidation_method.value
    else:
      consolidation_method = self.consolidation_method

    entity_role: None | str | Unset
    if isinstance(self.entity_role, Unset):
      entity_role = UNSET
    elif isinstance(self.entity_role, UpdateEntityRequestEntityRoleType0):
      entity_role = self.entity_role.value
    else:
      entity_role = self.entity_role

    joined_on: None | str | Unset
    if isinstance(self.joined_on, Unset):
      joined_on = UNSET
    elif isinstance(self.joined_on, datetime.date):
      joined_on = self.joined_on.isoformat()
    else:
      joined_on = self.joined_on

    left_on: None | str | Unset
    if isinstance(self.left_on, Unset):
      left_on = UNSET
    elif isinstance(self.left_on, datetime.date):
      left_on = self.left_on.isoformat()
    else:
      left_on = self.left_on

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if name is not UNSET:
      field_dict["name"] = name
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
    if ownership_pct is not UNSET:
      field_dict["ownership_pct"] = ownership_pct
    if consolidation_method is not UNSET:
      field_dict["consolidation_method"] = consolidation_method
    if entity_role is not UNSET:
      field_dict["entity_role"] = entity_role
    if joined_on is not UNSET:
      field_dict["joined_on"] = joined_on
    if left_on is not UNSET:
      field_dict["left_on"] = left_on

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

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

    def _parse_ownership_pct(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    ownership_pct = _parse_ownership_pct(d.pop("ownership_pct", UNSET))

    def _parse_consolidation_method(
      data: object,
    ) -> None | Unset | UpdateEntityRequestConsolidationMethodType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        consolidation_method_type_0 = UpdateEntityRequestConsolidationMethodType0(data)

        return consolidation_method_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateEntityRequestConsolidationMethodType0, data)

    consolidation_method = _parse_consolidation_method(
      d.pop("consolidation_method", UNSET)
    )

    def _parse_entity_role(
      data: object,
    ) -> None | Unset | UpdateEntityRequestEntityRoleType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        entity_role_type_0 = UpdateEntityRequestEntityRoleType0(data)

        return entity_role_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateEntityRequestEntityRoleType0, data)

    entity_role = _parse_entity_role(d.pop("entity_role", UNSET))

    def _parse_joined_on(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        joined_on_type_0 = datetime.date.fromisoformat(data)

        return joined_on_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    joined_on = _parse_joined_on(d.pop("joined_on", UNSET))

    def _parse_left_on(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        left_on_type_0 = datetime.date.fromisoformat(data)

        return left_on_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    left_on = _parse_left_on(d.pop("left_on", UNSET))

    update_entity_request = cls(
      entity_id=entity_id,
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
      address_line1=address_line1,
      address_city=address_city,
      address_state=address_state,
      address_postal_code=address_postal_code,
      address_country=address_country,
      ownership_pct=ownership_pct,
      consolidation_method=consolidation_method,
      entity_role=entity_role,
      joined_on=joined_on,
      left_on=left_on,
    )

    update_entity_request.additional_properties = d
    return update_entity_request

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
