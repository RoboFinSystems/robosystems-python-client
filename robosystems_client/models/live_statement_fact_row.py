from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_statement_fact_row_origin_type_0 import (
  LiveStatementFactRowOriginType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.statement_row_source import StatementRowSource


T = TypeVar("T", bound="LiveStatementFactRow")


@_attrs_define
class LiveStatementFactRow:
  """A single row of an OLTP-backed ad-hoc statement.

  Attributes:
      qname (str):
      name (str):
      values (list[float | None]):
      trait (None | str | Unset):
      depth (int | Unset):  Default: 0.
      is_subtotal (bool | Unset):  Default: False.
      period_role (None | str | Unset): On the equity roll-forward, `start` for the beginning-balance row and `end`
          for the ending-balance row. Null elsewhere.
      origin (LiveStatementFactRowOriginType0 | None | Unset): With `include_sources`, how the figure was made:
          `accounts` (summed from accounts in at least one column; read each column's `sources`, which may be empty where
          they do not add up), `subtotal` (the rows beneath it), or `computed` (derived from other figures, or a flow,
          with no accounts of its own). Null without `include_sources`.
      sources (list[list[StatementRowSource]] | None | Unset): With `include_sources`, per column (aligned with
          `values`), the accounts the figure was summed from, largest first; their values add up to the figure. Empty for
          a column with nothing to show, and for a subtotal or computed row.
  """

  qname: str
  name: str
  values: list[float | None]
  trait: None | str | Unset = UNSET
  depth: int | Unset = 0
  is_subtotal: bool | Unset = False
  period_role: None | str | Unset = UNSET
  origin: LiveStatementFactRowOriginType0 | None | Unset = UNSET
  sources: list[list[StatementRowSource]] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    name = self.name

    values = []
    for values_item_data in self.values:
      values_item: float | None
      values_item = values_item_data
      values.append(values_item)

    trait: None | str | Unset
    if isinstance(self.trait, Unset):
      trait = UNSET
    else:
      trait = self.trait

    depth = self.depth

    is_subtotal = self.is_subtotal

    period_role: None | str | Unset
    if isinstance(self.period_role, Unset):
      period_role = UNSET
    else:
      period_role = self.period_role

    origin: None | str | Unset
    if isinstance(self.origin, Unset):
      origin = UNSET
    elif isinstance(self.origin, LiveStatementFactRowOriginType0):
      origin = self.origin.value
    else:
      origin = self.origin

    sources: list[list[dict[str, Any]]] | None | Unset
    if isinstance(self.sources, Unset):
      sources = UNSET
    elif isinstance(self.sources, list):
      sources = []
      for sources_type_0_item_data in self.sources:
        sources_type_0_item = []
        for sources_type_0_item_item_data in sources_type_0_item_data:
          sources_type_0_item_item = sources_type_0_item_item_data.to_dict()
          sources_type_0_item.append(sources_type_0_item_item)

        sources.append(sources_type_0_item)

    else:
      sources = self.sources

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
        "name": name,
        "values": values,
      }
    )
    if trait is not UNSET:
      field_dict["trait"] = trait
    if depth is not UNSET:
      field_dict["depth"] = depth
    if is_subtotal is not UNSET:
      field_dict["is_subtotal"] = is_subtotal
    if period_role is not UNSET:
      field_dict["period_role"] = period_role
    if origin is not UNSET:
      field_dict["origin"] = origin
    if sources is not UNSET:
      field_dict["sources"] = sources

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.statement_row_source import StatementRowSource

    d = dict(src_dict)
    qname = d.pop("qname")

    name = d.pop("name")

    values = []
    _values = d.pop("values")
    for values_item_data in _values:

      def _parse_values_item(data: object) -> float | None:
        if data is None:
          return data
        return cast(float | None, data)

      values_item = _parse_values_item(values_item_data)

      values.append(values_item)

    def _parse_trait(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    trait = _parse_trait(d.pop("trait", UNSET))

    depth = d.pop("depth", UNSET)

    is_subtotal = d.pop("is_subtotal", UNSET)

    def _parse_period_role(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_role = _parse_period_role(d.pop("period_role", UNSET))

    def _parse_origin(data: object) -> LiveStatementFactRowOriginType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        origin_type_0 = LiveStatementFactRowOriginType0(data)

        return origin_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(LiveStatementFactRowOriginType0 | None | Unset, data)

    origin = _parse_origin(d.pop("origin", UNSET))

    def _parse_sources(data: object) -> list[list[StatementRowSource]] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        sources_type_0 = []
        _sources_type_0 = data
        for sources_type_0_item_data in _sources_type_0:
          sources_type_0_item = []
          _sources_type_0_item = sources_type_0_item_data
          for sources_type_0_item_item_data in _sources_type_0_item:
            sources_type_0_item_item = StatementRowSource.from_dict(
              sources_type_0_item_item_data
            )

            sources_type_0_item.append(sources_type_0_item_item)

          sources_type_0.append(sources_type_0_item)

        return sources_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[list[StatementRowSource]] | None | Unset, data)

    sources = _parse_sources(d.pop("sources", UNSET))

    live_statement_fact_row = cls(
      qname=qname,
      name=name,
      values=values,
      trait=trait,
      depth=depth,
      is_subtotal=is_subtotal,
      period_role=period_role,
      origin=origin,
      sources=sources,
    )

    live_statement_fact_row.additional_properties = d
    return live_statement_fact_row

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
