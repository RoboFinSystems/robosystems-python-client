from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.live_statement_fact_row import LiveStatementFactRow
  from ..models.period_spec import PeriodSpec
  from ..models.validation_check_response import ValidationCheckResponse


T = TypeVar("T", bound="LiveFinancialStatementResponse")


@_attrs_define
class LiveFinancialStatementResponse:
  """Rendered OLTP-backed ad-hoc statement.

  Attributes:
      graph_id (str):
      statement_type (str):
      periods (list[PeriodSpec]): Rendered columns, aligned with each row's ``values``. Current and prior for
          income_statement and balance_sheet; current only for cash_flow_statement — the prior period is pivoted as the
          indirect-method delta basis and not rendered.
      facts (list[LiveStatementFactRow]):
      fact_count (int):
      validation (None | Unset | ValidationCheckResponse): Guard-rail outcome for the rendered columns — accounting
          equation, net-income equation, totals footing, operating-plug size. Null only when no structure rendered.
      unmapped_count (int | Unset):  Default: 0.
      truncated (bool | Unset):  Default: False.
  """

  graph_id: str
  statement_type: str
  periods: list[PeriodSpec]
  facts: list[LiveStatementFactRow]
  fact_count: int
  validation: None | Unset | ValidationCheckResponse = UNSET
  unmapped_count: int | Unset = 0
  truncated: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
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

    validation: dict[str, Any] | None | Unset
    if isinstance(self.validation, Unset):
      validation = UNSET
    elif isinstance(self.validation, ValidationCheckResponse):
      validation = self.validation.to_dict()
    else:
      validation = self.validation

    unmapped_count = self.unmapped_count

    truncated = self.truncated

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
    if validation is not UNSET:
      field_dict["validation"] = validation
    if unmapped_count is not UNSET:
      field_dict["unmapped_count"] = unmapped_count
    if truncated is not UNSET:
      field_dict["truncated"] = truncated

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.live_statement_fact_row import LiveStatementFactRow
    from ..models.period_spec import PeriodSpec
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

    live_financial_statement_response = cls(
      graph_id=graph_id,
      statement_type=statement_type,
      periods=periods,
      facts=facts,
      fact_count=fact_count,
      validation=validation,
      unmapped_count=unmapped_count,
      truncated=truncated,
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
