from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePositionRequest")


@_attrs_define
class UpdatePositionRequest:
  """
  Attributes:
      quantity (float | None | Unset):
      quantity_type (None | str | Unset):
      cost_basis (int | None | Unset):
      current_value (int | None | Unset):
      valuation_date (datetime.date | None | Unset):
      valuation_source (None | str | Unset):
      acquisition_date (datetime.date | None | Unset):
      disposition_date (datetime.date | None | Unset):
      status (None | str | Unset):
      notes (None | str | Unset):
  """

  quantity: float | None | Unset = UNSET
  quantity_type: None | str | Unset = UNSET
  cost_basis: int | None | Unset = UNSET
  current_value: int | None | Unset = UNSET
  valuation_date: datetime.date | None | Unset = UNSET
  valuation_source: None | str | Unset = UNSET
  acquisition_date: datetime.date | None | Unset = UNSET
  disposition_date: datetime.date | None | Unset = UNSET
  status: None | str | Unset = UNSET
  notes: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    quantity: float | None | Unset
    if isinstance(self.quantity, Unset):
      quantity = UNSET
    else:
      quantity = self.quantity

    quantity_type: None | str | Unset
    if isinstance(self.quantity_type, Unset):
      quantity_type = UNSET
    else:
      quantity_type = self.quantity_type

    cost_basis: int | None | Unset
    if isinstance(self.cost_basis, Unset):
      cost_basis = UNSET
    else:
      cost_basis = self.cost_basis

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

    disposition_date: None | str | Unset
    if isinstance(self.disposition_date, Unset):
      disposition_date = UNSET
    elif isinstance(self.disposition_date, datetime.date):
      disposition_date = self.disposition_date.isoformat()
    else:
      disposition_date = self.disposition_date

    status: None | str | Unset
    if isinstance(self.status, Unset):
      status = UNSET
    else:
      status = self.status

    notes: None | str | Unset
    if isinstance(self.notes, Unset):
      notes = UNSET
    else:
      notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if quantity is not UNSET:
      field_dict["quantity"] = quantity
    if quantity_type is not UNSET:
      field_dict["quantity_type"] = quantity_type
    if cost_basis is not UNSET:
      field_dict["cost_basis"] = cost_basis
    if current_value is not UNSET:
      field_dict["current_value"] = current_value
    if valuation_date is not UNSET:
      field_dict["valuation_date"] = valuation_date
    if valuation_source is not UNSET:
      field_dict["valuation_source"] = valuation_source
    if acquisition_date is not UNSET:
      field_dict["acquisition_date"] = acquisition_date
    if disposition_date is not UNSET:
      field_dict["disposition_date"] = disposition_date
    if status is not UNSET:
      field_dict["status"] = status
    if notes is not UNSET:
      field_dict["notes"] = notes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_quantity(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    quantity = _parse_quantity(d.pop("quantity", UNSET))

    def _parse_quantity_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    quantity_type = _parse_quantity_type(d.pop("quantity_type", UNSET))

    def _parse_cost_basis(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    cost_basis = _parse_cost_basis(d.pop("cost_basis", UNSET))

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

    def _parse_status(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    status = _parse_status(d.pop("status", UNSET))

    def _parse_notes(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    notes = _parse_notes(d.pop("notes", UNSET))

    update_position_request = cls(
      quantity=quantity,
      quantity_type=quantity_type,
      cost_basis=cost_basis,
      current_value=current_value,
      valuation_date=valuation_date,
      valuation_source=valuation_source,
      acquisition_date=acquisition_date,
      disposition_date=disposition_date,
      status=status,
      notes=notes,
    )

    update_position_request.additional_properties = d
    return update_position_request

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
