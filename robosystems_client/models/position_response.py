from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionResponse")


@_attrs_define
class PositionResponse:
  """
  Attributes:
      id (str):
      portfolio_id (str):
      security_id (str):
      quantity (float):
      quantity_type (str):
      cost_basis (int):
      cost_basis_dollars (float):
      currency (str):
      status (str):
      created_at (datetime.datetime):
      updated_at (datetime.datetime):
      security_name (None | str | Unset):
      entity_name (None | str | Unset):
      current_value (int | None | Unset):
      current_value_dollars (float | None | Unset):
      valuation_date (datetime.date | None | Unset):
      valuation_source (None | str | Unset):
      acquisition_date (datetime.date | None | Unset):
      disposition_date (datetime.date | None | Unset):
      notes (None | str | Unset):
  """

  id: str
  portfolio_id: str
  security_id: str
  quantity: float
  quantity_type: str
  cost_basis: int
  cost_basis_dollars: float
  currency: str
  status: str
  created_at: datetime.datetime
  updated_at: datetime.datetime
  security_name: None | str | Unset = UNSET
  entity_name: None | str | Unset = UNSET
  current_value: int | None | Unset = UNSET
  current_value_dollars: float | None | Unset = UNSET
  valuation_date: datetime.date | None | Unset = UNSET
  valuation_source: None | str | Unset = UNSET
  acquisition_date: datetime.date | None | Unset = UNSET
  disposition_date: datetime.date | None | Unset = UNSET
  notes: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    portfolio_id = self.portfolio_id

    security_id = self.security_id

    quantity = self.quantity

    quantity_type = self.quantity_type

    cost_basis = self.cost_basis

    cost_basis_dollars = self.cost_basis_dollars

    currency = self.currency

    status = self.status

    created_at = self.created_at.isoformat()

    updated_at = self.updated_at.isoformat()

    security_name: None | str | Unset
    if isinstance(self.security_name, Unset):
      security_name = UNSET
    else:
      security_name = self.security_name

    entity_name: None | str | Unset
    if isinstance(self.entity_name, Unset):
      entity_name = UNSET
    else:
      entity_name = self.entity_name

    current_value: int | None | Unset
    if isinstance(self.current_value, Unset):
      current_value = UNSET
    else:
      current_value = self.current_value

    current_value_dollars: float | None | Unset
    if isinstance(self.current_value_dollars, Unset):
      current_value_dollars = UNSET
    else:
      current_value_dollars = self.current_value_dollars

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

    disposition_date: None | str | Unset
    if isinstance(self.disposition_date, Unset):
      disposition_date = UNSET
    elif isinstance(self.disposition_date, datetime.date):
      disposition_date = self.disposition_date.isoformat()
    else:
      disposition_date = self.disposition_date

    notes: None | str | Unset
    if isinstance(self.notes, Unset):
      notes = UNSET
    else:
      notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "portfolio_id": portfolio_id,
        "security_id": security_id,
        "quantity": quantity,
        "quantity_type": quantity_type,
        "cost_basis": cost_basis,
        "cost_basis_dollars": cost_basis_dollars,
        "currency": currency,
        "status": status,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if security_name is not UNSET:
      field_dict["security_name"] = security_name
    if entity_name is not UNSET:
      field_dict["entity_name"] = entity_name
    if current_value is not UNSET:
      field_dict["current_value"] = current_value
    if current_value_dollars is not UNSET:
      field_dict["current_value_dollars"] = current_value_dollars
    if valuation_date is not UNSET:
      field_dict["valuation_date"] = valuation_date
    if valuation_source is not UNSET:
      field_dict["valuation_source"] = valuation_source
    if acquisition_date is not UNSET:
      field_dict["acquisition_date"] = acquisition_date
    if disposition_date is not UNSET:
      field_dict["disposition_date"] = disposition_date
    if notes is not UNSET:
      field_dict["notes"] = notes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    portfolio_id = d.pop("portfolio_id")

    security_id = d.pop("security_id")

    quantity = d.pop("quantity")

    quantity_type = d.pop("quantity_type")

    cost_basis = d.pop("cost_basis")

    cost_basis_dollars = d.pop("cost_basis_dollars")

    currency = d.pop("currency")

    status = d.pop("status")

    created_at = isoparse(d.pop("created_at"))

    updated_at = isoparse(d.pop("updated_at"))

    def _parse_security_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    security_name = _parse_security_name(d.pop("security_name", UNSET))

    def _parse_entity_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_name = _parse_entity_name(d.pop("entity_name", UNSET))

    def _parse_current_value(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    current_value = _parse_current_value(d.pop("current_value", UNSET))

    def _parse_current_value_dollars(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    current_value_dollars = _parse_current_value_dollars(
      d.pop("current_value_dollars", UNSET)
    )

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

    def _parse_disposition_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        disposition_date_type_0 = isoparse(data).date()

        return disposition_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    disposition_date = _parse_disposition_date(d.pop("disposition_date", UNSET))

    def _parse_notes(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    notes = _parse_notes(d.pop("notes", UNSET))

    position_response = cls(
      id=id,
      portfolio_id=portfolio_id,
      security_id=security_id,
      quantity=quantity,
      quantity_type=quantity_type,
      cost_basis=cost_basis,
      cost_basis_dollars=cost_basis_dollars,
      currency=currency,
      status=status,
      created_at=created_at,
      updated_at=updated_at,
      security_name=security_name,
      entity_name=entity_name,
      current_value=current_value,
      current_value_dollars=current_value_dollars,
      valuation_date=valuation_date,
      valuation_source=valuation_source,
      acquisition_date=acquisition_date,
      disposition_date=disposition_date,
      notes=notes,
    )

    position_response.additional_properties = d
    return position_response

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
