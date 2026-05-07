from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.security_lite import SecurityLite


T = TypeVar("T", bound="PositionBlock")


@_attrs_define
class PositionBlock:
  """Position projection embedded inside a `PortfolioBlockEnvelope`.

  Pre-converts cents fields to dollars (`cost_basis_dollars`,
  `current_value_dollars`) for display; the cents-precision fields
  live on the standalone `PositionResponse`. Embeds a `SecurityLite`
  so callers can render the security name without a follow-up fetch.

      Attributes:
          id (str): Position ID (`pos_*` ULID).
          quantity (float): Quantity held in `quantity_type` units.
          quantity_type (str): Unit basis (`shares`, `units`, `principal`).
          cost_basis_dollars (float): Cost basis in dollars (pre-converted from cents).
          status (str): Lifecycle state (`active`, `disposed`, `archived`). See `PositionResponse.status` for the full
              vocabulary.
          security (SecurityLite): Lightweight security projection for embedding in position
              envelopes. Skips `terms`, `outstanding_shares`, etc. — fetch the
              full `SecurityResponse` when those are needed.
          current_value_dollars (float | None | Unset): Latest mark-to-market value in dollars. `null` when the position
              has not been marked.
          valuation_date (datetime.date | None | Unset): Date the current value was sourced.
          valuation_source (None | str | Unset): Free-text source attribution for the valuation.
          acquisition_date (datetime.date | None | Unset): Date the position was acquired.
          notes (None | str | Unset): Free-text notes attached to the position.
  """

  id: str
  quantity: float
  quantity_type: str
  cost_basis_dollars: float
  status: str
  security: SecurityLite
  current_value_dollars: float | None | Unset = UNSET
  valuation_date: datetime.date | None | Unset = UNSET
  valuation_source: None | str | Unset = UNSET
  acquisition_date: datetime.date | None | Unset = UNSET
  notes: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    quantity = self.quantity

    quantity_type = self.quantity_type

    cost_basis_dollars = self.cost_basis_dollars

    status = self.status

    security = self.security.to_dict()

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
        "quantity": quantity,
        "quantity_type": quantity_type,
        "cost_basis_dollars": cost_basis_dollars,
        "status": status,
        "security": security,
      }
    )
    if current_value_dollars is not UNSET:
      field_dict["current_value_dollars"] = current_value_dollars
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
    from ..models.security_lite import SecurityLite

    d = dict(src_dict)
    id = d.pop("id")

    quantity = d.pop("quantity")

    quantity_type = d.pop("quantity_type")

    cost_basis_dollars = d.pop("cost_basis_dollars")

    status = d.pop("status")

    security = SecurityLite.from_dict(d.pop("security"))

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

    def _parse_notes(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    notes = _parse_notes(d.pop("notes", UNSET))

    position_block = cls(
      id=id,
      quantity=quantity,
      quantity_type=quantity_type,
      cost_basis_dollars=cost_basis_dollars,
      status=status,
      security=security,
      current_value_dollars=current_value_dollars,
      valuation_date=valuation_date,
      valuation_source=valuation_source,
      acquisition_date=acquisition_date,
      notes=notes,
    )

    position_block.additional_properties = d
    return position_block

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
