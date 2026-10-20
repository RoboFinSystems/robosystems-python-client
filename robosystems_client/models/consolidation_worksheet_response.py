from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.period_spec import PeriodSpec
  from ..models.validation_check_response import ValidationCheckResponse
  from ..models.worksheet_column import WorksheetColumn
  from ..models.worksheet_row import WorksheetRow


T = TypeVar("T", bound="ConsolidationWorksheetResponse")


@_attrs_define
class ConsolidationWorksheetResponse:
  """The group's statement with the entity as the column.

  Attributes:
      graph_id (str): The graph read.
      entity_id (str): The group parent.
      statement_type (str): The statement rendered.
      period (PeriodSpec): A single reporting period column.

          Reports render facts in N period columns side-by-side. Each
          `PeriodSpec` is one column — its `start`/`end` define the
          window the report's facts roll up into; `label` is what the renderer
          prints in the column header. For year-over-year statements, supply two
          PeriodSpecs (current + comparative); for YTD by quarter, supply four.
      columns (list[WorksheetColumn]): The parent, each member consolidated in full, `combined`, the consolidation
          entity's adjustments (when the group has one), `consolidated`, then the equity-method and cost members outside
          the sum. A member outside its membership interval for the period has no column.
      rows (list[WorksheetRow]): The union of every column's lines in the parent's Style order; a line zero in every
          column is left out.
      omitted_periods (list[PeriodSpec] | Unset): Windows the worksheet does not total, as live-financial-statement
          leaves them out: before a summed entity's books begin, or, on a cash flow or equity statement, one a member
          joined or left the group within. When it names `period`, `rows` is empty.
      validation (None | Unset | ValidationCheckResponse): The guard-rail outcome for the consolidated column, the
          same checks live-financial-statement runs.
      unmapped_entity_ids (list[str] | Unset): Entities with no CoA mapping yet, so with no column.
      unmapped_count (int | Unset): Unmapped accounts across the summed columns. Default: 0.
      truncated (bool | Unset): Whether `limit` cut rows. Default: False.
  """

  graph_id: str
  entity_id: str
  statement_type: str
  period: PeriodSpec
  columns: list[WorksheetColumn]
  rows: list[WorksheetRow]
  omitted_periods: list[PeriodSpec] | Unset = UNSET
  validation: None | Unset | ValidationCheckResponse = UNSET
  unmapped_entity_ids: list[str] | Unset = UNSET
  unmapped_count: int | Unset = 0
  truncated: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.validation_check_response import ValidationCheckResponse

    graph_id = self.graph_id

    entity_id = self.entity_id

    statement_type = self.statement_type

    period = self.period.to_dict()

    columns = []
    for columns_item_data in self.columns:
      columns_item = columns_item_data.to_dict()
      columns.append(columns_item)

    rows = []
    for rows_item_data in self.rows:
      rows_item = rows_item_data.to_dict()
      rows.append(rows_item)

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

    unmapped_entity_ids: list[str] | Unset = UNSET
    if not isinstance(self.unmapped_entity_ids, Unset):
      unmapped_entity_ids = self.unmapped_entity_ids

    unmapped_count = self.unmapped_count

    truncated = self.truncated

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "entity_id": entity_id,
        "statement_type": statement_type,
        "period": period,
        "columns": columns,
        "rows": rows,
      }
    )
    if omitted_periods is not UNSET:
      field_dict["omitted_periods"] = omitted_periods
    if validation is not UNSET:
      field_dict["validation"] = validation
    if unmapped_entity_ids is not UNSET:
      field_dict["unmapped_entity_ids"] = unmapped_entity_ids
    if unmapped_count is not UNSET:
      field_dict["unmapped_count"] = unmapped_count
    if truncated is not UNSET:
      field_dict["truncated"] = truncated

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.period_spec import PeriodSpec
    from ..models.validation_check_response import ValidationCheckResponse
    from ..models.worksheet_column import WorksheetColumn
    from ..models.worksheet_row import WorksheetRow

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    entity_id = d.pop("entity_id")

    statement_type = d.pop("statement_type")

    period = PeriodSpec.from_dict(d.pop("period"))

    columns = []
    _columns = d.pop("columns")
    for columns_item_data in _columns:
      columns_item = WorksheetColumn.from_dict(columns_item_data)

      columns.append(columns_item)

    rows = []
    _rows = d.pop("rows")
    for rows_item_data in _rows:
      rows_item = WorksheetRow.from_dict(rows_item_data)

      rows.append(rows_item)

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

    unmapped_entity_ids = cast(list[str], d.pop("unmapped_entity_ids", UNSET))

    unmapped_count = d.pop("unmapped_count", UNSET)

    truncated = d.pop("truncated", UNSET)

    consolidation_worksheet_response = cls(
      graph_id=graph_id,
      entity_id=entity_id,
      statement_type=statement_type,
      period=period,
      columns=columns,
      rows=rows,
      omitted_periods=omitted_periods,
      validation=validation,
      unmapped_entity_ids=unmapped_entity_ids,
      unmapped_count=unmapped_count,
      truncated=truncated,
    )

    consolidation_worksheet_response.additional_properties = d
    return consolidation_worksheet_response

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
