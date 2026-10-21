from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.live_statement_fact_row import LiveStatementFactRow
  from ..models.period_spec import PeriodSpec
  from ..models.statement_dimension_response import StatementDimensionResponse
  from ..models.validation_check_response import ValidationCheckResponse


T = TypeVar("T", bound="LiveFinancialStatementResponse")


@_attrs_define
class LiveFinancialStatementResponse:
  """Rendered OLTP-backed ad-hoc statement.

  Attributes:
      graph_id (str):
      statement_type (str):
      periods (list[PeriodSpec]): Rendered columns, aligned with each row's `values`. Current and prior for
          income_statement and balance_sheet; current only for cash_flow_statement — the prior period is pivoted as the
          indirect-method delta basis and not rendered.
      facts (list[LiveStatementFactRow]):
      fact_count (int):
      entity_id (None | str | Unset): The entity whose books were rendered.
      scope (str | Unset): What was rendered: `entity`, `combined` (the members summed, nothing eliminated) or
          `consolidated` (the members plus the consolidation entity's adjustments). Default: 'entity'.
      consolidated (bool | Unset): Whether the group's entities were summed into this — true for the `combined` and
          `consolidated` scopes. Default: False.
      combined_entity_ids (list[str] | Unset): The entities summed, parent first; on `consolidated` the consolidation
          entity comes last.
      presentation (str | Unset): Always 'live': the books as they stand, through the current mapping. A closed
          month's figures as its close stamped them (`as_closed` on build-fact-grid and on statement columns) can differ
          once a mapping was reclassified after the close. Default: 'live'.
      omitted_periods (list[PeriodSpec] | Unset): Columns left out because they reach back before the books begin: on
          books that start from an opening balance, a flow statement column that starts before the first day it covers, or
          a balance sheet dated before it. They would show a partial figure, not the months before the books. On a group
          read, also a cash flow or equity statement column a member joined or left the group within.
      validation (None | Unset | ValidationCheckResponse): Guard-rail outcome for the rendered columns — accounting
          equation, net-income equation, totals footing, operating-plug size. Null only when no structure rendered.
      unmapped_count (int | Unset):  Default: 0.
      truncated (bool | Unset):  Default: False.
      dimension (None | StatementDimensionResponse | Unset): How the statement was sliced by a management dimension,
          when it was: the axis, the one member read, or the columns and whether they tie out to the Total.
  """

  graph_id: str
  statement_type: str
  periods: list[PeriodSpec]
  facts: list[LiveStatementFactRow]
  fact_count: int
  entity_id: None | str | Unset = UNSET
  scope: str | Unset = "entity"
  consolidated: bool | Unset = False
  combined_entity_ids: list[str] | Unset = UNSET
  presentation: str | Unset = "live"
  omitted_periods: list[PeriodSpec] | Unset = UNSET
  validation: None | Unset | ValidationCheckResponse = UNSET
  unmapped_count: int | Unset = 0
  truncated: bool | Unset = False
  dimension: None | StatementDimensionResponse | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.statement_dimension_response import StatementDimensionResponse
    from ..models.validation_check_response import ValidationCheckResponse

    graph_id = self.graph_id

    statement_type = self.statement_type

    periods = []
    for periods_item_data in self.periods:
      periods_item = periods_item_data.to_dict()
      periods.append(periods_item)

    facts = []
    for facts_item_data in self.facts:
      facts_item = facts_item_data.to_dict()
      facts.append(facts_item)

    fact_count = self.fact_count

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    scope = self.scope

    consolidated = self.consolidated

    combined_entity_ids: list[str] | Unset = UNSET
    if not isinstance(self.combined_entity_ids, Unset):
      combined_entity_ids = self.combined_entity_ids

    presentation = self.presentation

    omitted_periods: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.omitted_periods, Unset):
      omitted_periods = []
      for omitted_periods_item_data in self.omitted_periods:
        omitted_periods_item = omitted_periods_item_data.to_dict()
        omitted_periods.append(omitted_periods_item)

    validation: dict[str, Any] | None | Unset
    if isinstance(self.validation, Unset):
      validation = UNSET
    elif isinstance(self.validation, ValidationCheckResponse):
      validation = self.validation.to_dict()
    else:
      validation = self.validation

    unmapped_count = self.unmapped_count

    truncated = self.truncated

    dimension: dict[str, Any] | None | Unset
    if isinstance(self.dimension, Unset):
      dimension = UNSET
    elif isinstance(self.dimension, StatementDimensionResponse):
      dimension = self.dimension.to_dict()
    else:
      dimension = self.dimension

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "statement_type": statement_type,
        "periods": periods,
        "facts": facts,
        "fact_count": fact_count,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if scope is not UNSET:
      field_dict["scope"] = scope
    if consolidated is not UNSET:
      field_dict["consolidated"] = consolidated
    if combined_entity_ids is not UNSET:
      field_dict["combined_entity_ids"] = combined_entity_ids
    if presentation is not UNSET:
      field_dict["presentation"] = presentation
    if omitted_periods is not UNSET:
      field_dict["omitted_periods"] = omitted_periods
    if validation is not UNSET:
      field_dict["validation"] = validation
    if unmapped_count is not UNSET:
      field_dict["unmapped_count"] = unmapped_count
    if truncated is not UNSET:
      field_dict["truncated"] = truncated
    if dimension is not UNSET:
      field_dict["dimension"] = dimension

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.live_statement_fact_row import LiveStatementFactRow
    from ..models.period_spec import PeriodSpec
    from ..models.statement_dimension_response import StatementDimensionResponse
    from ..models.validation_check_response import ValidationCheckResponse

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    statement_type = d.pop("statement_type")

    periods = []
    _periods = d.pop("periods")
    for periods_item_data in _periods:
      periods_item = PeriodSpec.from_dict(periods_item_data)

      periods.append(periods_item)

    facts = []
    _facts = d.pop("facts")
    for facts_item_data in _facts:
      facts_item = LiveStatementFactRow.from_dict(facts_item_data)

      facts.append(facts_item)

    fact_count = d.pop("fact_count")

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    scope = d.pop("scope", UNSET)

    consolidated = d.pop("consolidated", UNSET)

    combined_entity_ids = cast(list[str], d.pop("combined_entity_ids", UNSET))

    presentation = d.pop("presentation", UNSET)

    _omitted_periods = d.pop("omitted_periods", UNSET)
    omitted_periods: list[PeriodSpec] | Unset = UNSET
    if _omitted_periods is not UNSET:
      omitted_periods = []
      for omitted_periods_item_data in _omitted_periods:
        omitted_periods_item = PeriodSpec.from_dict(omitted_periods_item_data)

        omitted_periods.append(omitted_periods_item)

    def _parse_validation(data: object) -> None | Unset | ValidationCheckResponse:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        validation_type_0 = ValidationCheckResponse.from_dict(data)

        return validation_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | ValidationCheckResponse, data)

    validation = _parse_validation(d.pop("validation", UNSET))

    unmapped_count = d.pop("unmapped_count", UNSET)

    truncated = d.pop("truncated", UNSET)

    def _parse_dimension(data: object) -> None | StatementDimensionResponse | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        dimension_type_0 = StatementDimensionResponse.from_dict(data)

        return dimension_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | StatementDimensionResponse | Unset, data)

    dimension = _parse_dimension(d.pop("dimension", UNSET))

    live_financial_statement_response = cls(
      graph_id=graph_id,
      statement_type=statement_type,
      periods=periods,
      facts=facts,
      fact_count=fact_count,
      entity_id=entity_id,
      scope=scope,
      consolidated=consolidated,
      combined_entity_ids=combined_entity_ids,
      presentation=presentation,
      omitted_periods=omitted_periods,
      validation=validation,
      unmapped_count=unmapped_count,
      truncated=truncated,
      dimension=dimension,
    )

    live_financial_statement_response.additional_properties = d
    return live_financial_statement_response

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
