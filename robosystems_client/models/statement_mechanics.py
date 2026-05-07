from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatementMechanics")


@_attrs_define
class StatementMechanics:
  """Renderer mechanics for the statement family of block types.

  Covers ``balance_sheet``, ``income_statement``, ``cash_flow_statement``,
  and ``equity_statement``. All fields are optional so library-seeded
  rows that haven't been enriched yet still validate against an empty
  tagged body. The existing ``statement(...)`` GraphQL field continues
  to serve rendered output; this mechanics model is the source of truth
  for future renderer configuration.

      Attributes:
          kind (Literal['statement_renderer'] | Unset):  Default: 'statement_renderer'.
          template_id (None | str | Unset): Pinned template id — when set, the renderer uses that template's layout
              instead of the block's default. The templates table is not yet implemented; the column is reserved so tenant
              writes can stamp it without another migration round-trip when it lands.
          rollup_root_element_ids (list[str] | Unset): Element ids that anchor the statement's roll-up roots (e.g. the
              Assets and LiabilitiesAndEquity totals on a Balance Sheet). Empty on library-seeded rows until tenant adoption.
          period_comparisons (int | Unset): Number of period columns to render in comparative mode: 1 = single-period, 2 =
              prior-period comparison, 3-4 = multi-year trailing view. Defaults to single-period; overridden by the template
              when one is attached. Default: 1.
  """

  kind: Literal["statement_renderer"] | Unset = "statement_renderer"
  template_id: None | str | Unset = UNSET
  rollup_root_element_ids: list[str] | Unset = UNSET
  period_comparisons: int | Unset = 1
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    kind = self.kind

    template_id: None | str | Unset
    if isinstance(self.template_id, Unset):
      template_id = UNSET
    else:
      template_id = self.template_id

    rollup_root_element_ids: list[str] | Unset = UNSET
    if not isinstance(self.rollup_root_element_ids, Unset):
      rollup_root_element_ids = self.rollup_root_element_ids

    period_comparisons = self.period_comparisons

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if kind is not UNSET:
      field_dict["kind"] = kind
    if template_id is not UNSET:
      field_dict["template_id"] = template_id
    if rollup_root_element_ids is not UNSET:
      field_dict["rollup_root_element_ids"] = rollup_root_element_ids
    if period_comparisons is not UNSET:
      field_dict["period_comparisons"] = period_comparisons

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    kind = cast(Literal["statement_renderer"] | Unset, d.pop("kind", UNSET))
    if kind != "statement_renderer" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'statement_renderer', got '{kind}'")

    def _parse_template_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    template_id = _parse_template_id(d.pop("template_id", UNSET))

    rollup_root_element_ids = cast(list[str], d.pop("rollup_root_element_ids", UNSET))

    period_comparisons = d.pop("period_comparisons", UNSET)

    statement_mechanics = cls(
      kind=kind,
      template_id=template_id,
      rollup_root_element_ids=rollup_root_element_ids,
      period_comparisons=period_comparisons,
    )

    statement_mechanics.additional_properties = d
    return statement_mechanics

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
