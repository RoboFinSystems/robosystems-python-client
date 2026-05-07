from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioBlockPositionAdd")


@_attrs_define
class PortfolioBlockPositionAdd:
  """A single new position to mint inside a portfolio-block create/update.

  References an existing security; this surface never creates securities
  (Master Data CRUD owns that lifecycle).

      Attributes:
          security_id (str): ID of the existing security this position holds. Securities are minted via `create-security`;
              the operation returns 404 if the ID is unknown.
          quantity (float): Quantity held, in units defined by `quantity_type` (e.g. share count for `shares`, face value
              for `principal`).
          quantity_type (str | Unset): Unit basis for `quantity`. Common values: `shares` (equity units), `units`
              (generic), `principal` (debt face value). Default: 'shares'.
          cost_basis (int | Unset): Total cost basis for this lot, in **cents** of `currency`. Stored as integer cents to
              avoid float precision drift; $1,250.00 USD is `125000`. Default: 0.
          currency (str | Unset): ISO 4217 currency code for `cost_basis` and `current_value`. Default: 'USD'.
          current_value (int | None | Unset): Latest mark-to-market value in **cents** of `currency`, or `null` if
              unmarked. Pair with `valuation_date` and `valuation_source` when set.
          valuation_date (datetime.date | None | Unset): Date `current_value` was sourced (YYYY-MM-DD).
          valuation_source (None | str | Unset): Free-text source attribution for `current_value` (e.g. `manual`,
              `broker_statement`, vendor name).
          acquisition_date (datetime.date | None | Unset): Date the position was originally acquired (YYYY-MM-DD).
          notes (None | str | Unset): Free-text notes attached to the position.
  """

  security_id: str
  quantity: float
  quantity_type: str | Unset = "shares"
  cost_basis: int | Unset = 0
  currency: str | Unset = "USD"
  current_value: int | None | Unset = UNSET
  valuation_date: datetime.date | None | Unset = UNSET
  valuation_source: None | str | Unset = UNSET
  acquisition_date: datetime.date | None | Unset = UNSET
  notes: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    security_id = self.security_id

    quantity = self.quantity

    quantity_type = self.quantity_type

    cost_basis = self.cost_basis

    currency = self.currency

    current_value: int | None | Unset
    if isinstance(self.current_value, Unset):
      current_value = UNSET
    else:
      current_value = self.current_value

    valuation_date: None | str | Unset
    if isinstance(self.valuation_date, Unset):
      valuation_date = UNSET
    elif isinstance(self.valuation_date, datetime.date):
      valuation_date = self.valuation_date.isoformat()
    else:
      valuation_date = self.valuation_date

    valuation_source: None | str | Unset
    if isinstance(self.valuation_source, Unset):
      valuation_source = UNSET
    else:
      valuation_source = self.valuation_source

    acquisition_date: None | str | Unset
    if isinstance(self.acquisition_date, Unset):
      acquisition_date = UNSET
    elif isinstance(self.acquisition_date, datetime.date):
      acquisition_date = self.acquisition_date.isoformat()
    else:
      acquisition_date = self.acquisition_date

    notes: None | str | Unset
    if isinstance(self.notes, Unset):
      notes = UNSET
    else:
      notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "security_id": security_id,
        "quantity": quantity,
      }
    )
    if quantity_type is not UNSET:
      field_dict["quantity_type"] = quantity_type
    if cost_basis is not UNSET:
      field_dict["cost_basis"] = cost_basis
    if currency is not UNSET:
      field_dict["currency"] = currency
    if current_value is not UNSET:
      field_dict["current_value"] = current_value
    if valuation_date is not UNSET:
      field_dict["valuation_date"] = valuation_date
    if valuation_source is not UNSET:
      field_dict["valuation_source"] = valuation_source
    if acquisition_date is not UNSET:
      field_dict["acquisition_date"] = acquisition_date
    if notes is not UNSET:
      field_dict["notes"] = notes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    security_id = d.pop("security_id")

    quantity = d.pop("quantity")

    quantity_type = d.pop("quantity_type", UNSET)

    cost_basis = d.pop("cost_basis", UNSET)

    currency = d.pop("currency", UNSET)

    def _parse_current_value(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    current_value = _parse_current_value(d.pop("current_value", UNSET))

    def _parse_valuation_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        valuation_date_type_0 = isoparse(data).date()

        return valuation_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    valuation_date = _parse_valuation_date(d.pop("valuation_date", UNSET))

    def _parse_valuation_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    valuation_source = _parse_valuation_source(d.pop("valuation_source", UNSET))

    def _parse_acquisition_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        acquisition_date_type_0 = isoparse(data).date()

        return acquisition_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    acquisition_date = _parse_acquisition_date(d.pop("acquisition_date", UNSET))

    def _parse_notes(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    notes = _parse_notes(d.pop("notes", UNSET))

    portfolio_block_position_add = cls(
      security_id=security_id,
      quantity=quantity,
      quantity_type=quantity_type,
      cost_basis=cost_basis,
      currency=currency,
      current_value=current_value,
      valuation_date=valuation_date,
      valuation_source=valuation_source,
      acquisition_date=acquisition_date,
      notes=notes,
    )

    portfolio_block_position_add.additional_properties = d
    return portfolio_block_position_add

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
