from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.view_config import ViewConfig


T = TypeVar("T", bound="CreateViewRequest")


@_attrs_define
class CreateViewRequest:
  """
  Attributes:
      elements (list[str] | Unset): Element qnames (e.g., 'us-gaap:Assets'). Can combine with canonical_concepts.
      canonical_concepts (list[str] | Unset): Canonical concept names (e.g., 'revenue', 'net_income'). Matches all
          mapped qnames.
      periods (list[str] | Unset): Period end dates (YYYY-MM-DD format)
      entity (None | str | Unset): Filter by entity ticker, CIK, or name
      entities (list[str] | Unset): Filter by multiple entity tickers (e.g., ['NVDA', 'AAPL'])
      form (None | str | Unset): Filter by SEC filing form type (e.g., '10-K', '10-Q')
      fiscal_year (int | None | Unset): Filter by fiscal year (e.g., 2024)
      fiscal_period (None | str | Unset): Filter by fiscal period (e.g., 'FY', 'Q1', 'Q2', 'Q3')
      period_type (None | str | Unset): Filter by period type: 'annual', 'quarterly', or 'instant'
      include_summary (bool | Unset): Include summary statistics per element Default: False.
      view_config (ViewConfig | Unset):
  """

  elements: list[str] | Unset = UNSET
  canonical_concepts: list[str] | Unset = UNSET
  periods: list[str] | Unset = UNSET
  entity: None | str | Unset = UNSET
  entities: list[str] | Unset = UNSET
  form: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  fiscal_period: None | str | Unset = UNSET
  period_type: None | str | Unset = UNSET
  include_summary: bool | Unset = False
  view_config: ViewConfig | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    elements: list[str] | Unset = UNSET
    if not isinstance(self.elements, Unset):
      elements = self.elements

    canonical_concepts: list[str] | Unset = UNSET
    if not isinstance(self.canonical_concepts, Unset):
      canonical_concepts = self.canonical_concepts

    periods: list[str] | Unset = UNSET
    if not isinstance(self.periods, Unset):
      periods = self.periods

    entity: None | str | Unset
    if isinstance(self.entity, Unset):
      entity = UNSET
    else:
      entity = self.entity

    entities: list[str] | Unset = UNSET
    if not isinstance(self.entities, Unset):
      entities = self.entities

    form: None | str | Unset
    if isinstance(self.form, Unset):
      form = UNSET
    else:
      form = self.form

    fiscal_year: int | None | Unset
    if isinstance(self.fiscal_year, Unset):
      fiscal_year = UNSET
    else:
      fiscal_year = self.fiscal_year

    fiscal_period: None | str | Unset
    if isinstance(self.fiscal_period, Unset):
      fiscal_period = UNSET
    else:
      fiscal_period = self.fiscal_period

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    include_summary = self.include_summary

    view_config: dict[str, Any] | Unset = UNSET
    if not isinstance(self.view_config, Unset):
      view_config = self.view_config.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if elements is not UNSET:
      field_dict["elements"] = elements
    if canonical_concepts is not UNSET:
      field_dict["canonical_concepts"] = canonical_concepts
    if periods is not UNSET:
      field_dict["periods"] = periods
    if entity is not UNSET:
      field_dict["entity"] = entity
    if entities is not UNSET:
      field_dict["entities"] = entities
    if form is not UNSET:
      field_dict["form"] = form
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if fiscal_period is not UNSET:
      field_dict["fiscal_period"] = fiscal_period
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if include_summary is not UNSET:
      field_dict["include_summary"] = include_summary
    if view_config is not UNSET:
      field_dict["view_config"] = view_config

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.view_config import ViewConfig

    d = dict(src_dict)
    elements = cast(list[str], d.pop("elements", UNSET))

    canonical_concepts = cast(list[str], d.pop("canonical_concepts", UNSET))

    periods = cast(list[str], d.pop("periods", UNSET))

    def _parse_entity(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity = _parse_entity(d.pop("entity", UNSET))

    entities = cast(list[str], d.pop("entities", UNSET))

    def _parse_form(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    form = _parse_form(d.pop("form", UNSET))

    def _parse_fiscal_year(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

    def _parse_fiscal_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fiscal_period = _parse_fiscal_period(d.pop("fiscal_period", UNSET))

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    include_summary = d.pop("include_summary", UNSET)

    _view_config = d.pop("view_config", UNSET)
    view_config: ViewConfig | Unset
    if isinstance(_view_config, Unset):
      view_config = UNSET
    else:
      view_config = ViewConfig.from_dict(_view_config)

    create_view_request = cls(
      elements=elements,
      canonical_concepts=canonical_concepts,
      periods=periods,
      entity=entity,
      entities=entities,
      form=form,
      fiscal_year=fiscal_year,
      fiscal_period=fiscal_period,
      period_type=period_type,
      include_summary=include_summary,
      view_config=view_config,
    )

    create_view_request.additional_properties = d
    return create_view_request

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
