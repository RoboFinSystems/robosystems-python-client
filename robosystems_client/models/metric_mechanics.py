from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricMechanics")


@_attrs_define
class MetricMechanics:
  """Derivative mechanics for ``block_type='metric'``.

  A metric block composes its facts from one or more source blocks at
  read time — covenant tests, ratios, KPI trend computations. The typed
  arm ships today so the discriminated union covers all three
  construction modes (declarative / compositional / derivative); the
  derivation evaluator that actually computes facts from source-block
  FactSets is not yet implemented.

  ``source_block_ids`` is the ordered list of Structure ids this metric
  derives from; ``derivation_type`` names the kind of computation
  (``ratio``, ``trailing_twelve_month``, ``covenant_test``, …), and
  ``expression`` carries the agent-authored derivation string that the
  evaluator will consume at envelope build time.

      Attributes:
          kind (Literal['metric'] | Unset):  Default: 'metric'.
          source_block_ids (list[str] | Unset): Ordered list of Structure ids this metric sources from. Must be non-empty
              at evaluation time; empty lists are accepted so library scaffolding can register metric templates before source
              linkage is wired.
          derivation_type (None | str | Unset): Free-form label for the derivation kind — 'ratio',
              'trailing_twelve_month', 'covenant_test', etc. The evaluator dispatches on this tag; the set may be locked with
              a CHECK constraint once the derivation catalog stabilizes.
          expression (None | str | Unset): Derivation expression in the metric DSL — evaluated at envelope read time to
              produce the derivative fact value. Opaque string today; the metric-side parser / evaluator is not yet
              implemented.
          unit (str | Unset): Output unit of the derived value — 'ratio', 'percent', 'USD', 'count', etc. Used by the
              renderer to format the metric badge. Default: 'ratio'.
  """

  kind: Literal["metric"] | Unset = "metric"
  source_block_ids: list[str] | Unset = UNSET
  derivation_type: None | str | Unset = UNSET
  expression: None | str | Unset = UNSET
  unit: str | Unset = "ratio"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    kind = self.kind

    source_block_ids: list[str] | Unset = UNSET
    if not isinstance(self.source_block_ids, Unset):
      source_block_ids = self.source_block_ids

    derivation_type: None | str | Unset
    if isinstance(self.derivation_type, Unset):
      derivation_type = UNSET
    else:
      derivation_type = self.derivation_type

    expression: None | str | Unset
    if isinstance(self.expression, Unset):
      expression = UNSET
    else:
      expression = self.expression

    unit = self.unit

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if kind is not UNSET:
      field_dict["kind"] = kind
    if source_block_ids is not UNSET:
      field_dict["source_block_ids"] = source_block_ids
    if derivation_type is not UNSET:
      field_dict["derivation_type"] = derivation_type
    if expression is not UNSET:
      field_dict["expression"] = expression
    if unit is not UNSET:
      field_dict["unit"] = unit

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    kind = cast(Literal["metric"] | Unset, d.pop("kind", UNSET))
    if kind != "metric" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'metric', got '{kind}'")

    source_block_ids = cast(list[str], d.pop("source_block_ids", UNSET))

    def _parse_derivation_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    derivation_type = _parse_derivation_type(d.pop("derivation_type", UNSET))

    def _parse_expression(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    expression = _parse_expression(d.pop("expression", UNSET))

    unit = d.pop("unit", UNSET)

    metric_mechanics = cls(
      kind=kind,
      source_block_ids=source_block_ids,
      derivation_type=derivation_type,
      expression=expression,
      unit=unit,
    )

    metric_mechanics.additional_properties = d
    return metric_mechanics

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
