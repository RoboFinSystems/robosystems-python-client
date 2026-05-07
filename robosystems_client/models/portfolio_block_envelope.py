from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entity_lite import EntityLite
  from ..models.position_block import PositionBlock


T = TypeVar("T", bound="PortfolioBlockEnvelope")


@_attrs_define
class PortfolioBlockEnvelope:
  """Molecular response shape for portfolio-block operations.

  Bundles the portfolio core, its embedded positions, and pre-computed
  totals into a single payload — the contract for `create-portfolio-block`,
  `update-portfolio-block`, and the read-side `get-portfolio-block`.
  Cents-precision values aren't surfaced here; use `PositionResponse`
  / `PortfolioResponse` for those.

      Attributes:
          id (str): Portfolio ID (`port_*` ULID).
          name (str): Display name.
          base_currency (str): ISO 4217 currency code for portfolio aggregates.
          positions (list[PositionBlock]): All positions in this portfolio, including disposed ones (filter by `status`
              for active-only display).
          total_cost_basis_dollars (float): Sum of `cost_basis_dollars` across every position.
          active_position_count (int): Count of positions with `status='active'`.
          created_at (datetime.datetime): Row creation timestamp (UTC).
          updated_at (datetime.datetime): Last-modified timestamp (UTC).
          description (None | str | Unset): Free-text description.
          strategy (None | str | Unset): Free-text strategy classification.
          inception_date (datetime.date | None | Unset): Date the portfolio was established.
          owner (EntityLite | None | Unset): Embedded owning entity, when set. `null` for unattributed portfolios.
          total_current_value_dollars (float | None | Unset): Sum of `current_value_dollars` across every position. `null`
              when any active position lacks a mark.
  """

  id: str
  name: str
  base_currency: str
  positions: list[PositionBlock]
  total_cost_basis_dollars: float
  active_position_count: int
  created_at: datetime.datetime
  updated_at: datetime.datetime
  description: None | str | Unset = UNSET
  strategy: None | str | Unset = UNSET
  inception_date: datetime.date | None | Unset = UNSET
  owner: EntityLite | None | Unset = UNSET
  total_current_value_dollars: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.entity_lite import EntityLite

    id = self.id

    name = self.name

    base_currency = self.base_currency

    positions = []
    for positions_item_data in self.positions:
      positions_item = positions_item_data.to_dict()
      positions.append(positions_item)

    total_cost_basis_dollars = self.total_cost_basis_dollars

    active_position_count = self.active_position_count

    created_at = self.created_at.isoformat()

    updated_at = self.updated_at.isoformat()

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    strategy: None | str | Unset
    if isinstance(self.strategy, Unset):
      strategy = UNSET
    else:
      strategy = self.strategy

    inception_date: None | str | Unset
    if isinstance(self.inception_date, Unset):
      inception_date = UNSET
    elif isinstance(self.inception_date, datetime.date):
      inception_date = self.inception_date.isoformat()
    else:
      inception_date = self.inception_date

    owner: dict[str, Any] | None | Unset
    if isinstance(self.owner, Unset):
      owner = UNSET
    elif isinstance(self.owner, EntityLite):
      owner = self.owner.to_dict()
    else:
      owner = self.owner

    total_current_value_dollars: float | None | Unset
    if isinstance(self.total_current_value_dollars, Unset):
      total_current_value_dollars = UNSET
    else:
      total_current_value_dollars = self.total_current_value_dollars

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "base_currency": base_currency,
        "positions": positions,
        "total_cost_basis_dollars": total_cost_basis_dollars,
        "active_position_count": active_position_count,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if strategy is not UNSET:
      field_dict["strategy"] = strategy
    if inception_date is not UNSET:
      field_dict["inception_date"] = inception_date
    if owner is not UNSET:
      field_dict["owner"] = owner
    if total_current_value_dollars is not UNSET:
      field_dict["total_current_value_dollars"] = total_current_value_dollars

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entity_lite import EntityLite
    from ..models.position_block import PositionBlock

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    base_currency = d.pop("base_currency")

    positions = []
    _positions = d.pop("positions")
    for positions_item_data in _positions:
      positions_item = PositionBlock.from_dict(positions_item_data)

      positions.append(positions_item)

    total_cost_basis_dollars = d.pop("total_cost_basis_dollars")

    active_position_count = d.pop("active_position_count")

    created_at = isoparse(d.pop("created_at"))

    updated_at = isoparse(d.pop("updated_at"))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_strategy(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    strategy = _parse_strategy(d.pop("strategy", UNSET))

    def _parse_inception_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        inception_date_type_0 = isoparse(data).date()

        return inception_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    inception_date = _parse_inception_date(d.pop("inception_date", UNSET))

    def _parse_owner(data: object) -> EntityLite | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        owner_type_0 = EntityLite.from_dict(data)

        return owner_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EntityLite | None | Unset, data)

    owner = _parse_owner(d.pop("owner", UNSET))

    def _parse_total_current_value_dollars(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    total_current_value_dollars = _parse_total_current_value_dollars(
      d.pop("total_current_value_dollars", UNSET)
    )

    portfolio_block_envelope = cls(
      id=id,
      name=name,
      base_currency=base_currency,
      positions=positions,
      total_cost_basis_dollars=total_cost_basis_dollars,
      active_position_count=active_position_count,
      created_at=created_at,
      updated_at=updated_at,
      description=description,
      strategy=strategy,
      inception_date=inception_date,
      owner=owner,
      total_current_value_dollars=total_current_value_dollars,
    )

    portfolio_block_envelope.additional_properties = d
    return portfolio_block_envelope

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
