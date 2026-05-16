from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.rule_target_lite import RuleTargetLite
  from ..models.rule_variable_lite import RuleVariableLite


T = TypeVar("T", bound="RuleLite")


@_attrs_define
class RuleLite:
  """Rule projection for the Information Block envelope.

  One row per ``public.rules`` entry scoped to this block. The rule
  engine consumes ``rule_expression`` + ``rule_variables`` to evaluate
  against the in-scope fact set; the envelope surfaces the rules so
  the UI can render them as a checklist alongside any persisted
  verification results.

      Attributes:
          id (str):
          rule_category (str): One of 8 cm:VerificationRule subclasses — AutomatedAccountingAndReportingChecks,
              FundamentalAccountingConceptRelation, PeerConsistencyRule, PriorPeriodConsistencyRule,
              ReportLevelModelStructureRule, ReportingSystemSpecificRule, ToDoManualTask, XBRLTechnicalSyntaxRule.
          rule_expression (str):
          rule_pattern (None | str | Unset): Arithmetic / logical pattern evaluated over fact values. One of 11
              cm:BusinessRulePattern mechanisms — Adjustment, CoExists, EqualTo, Exists, GreaterThan,
              GreaterThanOrEqualToZero, LessThan, RollForward, RollUp, SumEquals, Variance. Null when the rule is a structural
              check (see rule_check_kind).
          rule_check_kind (None | str | Unset): Model-structure check kind evaluated over the association graph. One of 6
              kinds — LeafHasClassification, LibraryOriginImmutability, NoCycles, NoOrphanArcs, ParentBeforeChild,
              UniqueQNameInTaxonomy. Null when the rule is an arithmetic pattern (see rule_pattern). Exactly one of
              rule_pattern / rule_check_kind is non-null per rule.
          rule_target (None | RuleTargetLite | Unset):
          rule_variables (list[RuleVariableLite] | Unset):
          rule_message (None | str | Unset):
          rule_severity (str | Unset): Failure severity — 'info' | 'warning' | 'error'. Enum closure enforced by the
              ``public.rules`` CHECK constraint. Default: 'error'.
          rule_origin (str | Unset): Provenance — 'forked' (from an upstream artifact, e.g. Seattle Method) or 'native'
              (authored in this seed or by a tenant). Enum closure enforced by the ``public.rules`` CHECK constraint. Default:
              'native'.
  """

  id: str
  rule_category: str
  rule_expression: str
  rule_pattern: None | str | Unset = UNSET
  rule_check_kind: None | str | Unset = UNSET
  rule_target: None | RuleTargetLite | Unset = UNSET
  rule_variables: list[RuleVariableLite] | Unset = UNSET
  rule_message: None | str | Unset = UNSET
  rule_severity: str | Unset = "error"
  rule_origin: str | Unset = "native"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.rule_target_lite import RuleTargetLite

    id = self.id

    rule_category = self.rule_category

    rule_expression = self.rule_expression

    rule_pattern: None | str | Unset
    if isinstance(self.rule_pattern, Unset):
      rule_pattern = UNSET
    else:
      rule_pattern = self.rule_pattern

    rule_check_kind: None | str | Unset
    if isinstance(self.rule_check_kind, Unset):
      rule_check_kind = UNSET
    else:
      rule_check_kind = self.rule_check_kind

    rule_target: dict[str, Any] | None | Unset
    if isinstance(self.rule_target, Unset):
      rule_target = UNSET
    elif isinstance(self.rule_target, RuleTargetLite):
      rule_target = self.rule_target.to_dict()
    else:
      rule_target = self.rule_target

    rule_variables: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rule_variables, Unset):
      rule_variables = []
      for rule_variables_item_data in self.rule_variables:
        rule_variables_item = rule_variables_item_data.to_dict()
        rule_variables.append(rule_variables_item)

    rule_message: None | str | Unset
    if isinstance(self.rule_message, Unset):
      rule_message = UNSET
    else:
      rule_message = self.rule_message

    rule_severity = self.rule_severity

    rule_origin = self.rule_origin

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "rule_category": rule_category,
        "rule_expression": rule_expression,
      }
    )
    if rule_pattern is not UNSET:
      field_dict["rule_pattern"] = rule_pattern
    if rule_check_kind is not UNSET:
      field_dict["rule_check_kind"] = rule_check_kind
    if rule_target is not UNSET:
      field_dict["rule_target"] = rule_target
    if rule_variables is not UNSET:
      field_dict["rule_variables"] = rule_variables
    if rule_message is not UNSET:
      field_dict["rule_message"] = rule_message
    if rule_severity is not UNSET:
      field_dict["rule_severity"] = rule_severity
    if rule_origin is not UNSET:
      field_dict["rule_origin"] = rule_origin

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.rule_target_lite import RuleTargetLite
    from ..models.rule_variable_lite import RuleVariableLite

    d = dict(src_dict)
    id = d.pop("id")

    rule_category = d.pop("rule_category")

    rule_expression = d.pop("rule_expression")

    def _parse_rule_pattern(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    rule_pattern = _parse_rule_pattern(d.pop("rule_pattern", UNSET))

    def _parse_rule_check_kind(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    rule_check_kind = _parse_rule_check_kind(d.pop("rule_check_kind", UNSET))

    def _parse_rule_target(data: object) -> None | RuleTargetLite | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rule_target_type_0 = RuleTargetLite.from_dict(data)

        return rule_target_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | RuleTargetLite | Unset, data)

    rule_target = _parse_rule_target(d.pop("rule_target", UNSET))

    _rule_variables = d.pop("rule_variables", UNSET)
    rule_variables: list[RuleVariableLite] | Unset = UNSET
    if _rule_variables is not UNSET:
      rule_variables = []
      for rule_variables_item_data in _rule_variables:
        rule_variables_item = RuleVariableLite.from_dict(rule_variables_item_data)

        rule_variables.append(rule_variables_item)

    def _parse_rule_message(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    rule_message = _parse_rule_message(d.pop("rule_message", UNSET))

    rule_severity = d.pop("rule_severity", UNSET)

    rule_origin = d.pop("rule_origin", UNSET)

    rule_lite = cls(
      id=id,
      rule_category=rule_category,
      rule_expression=rule_expression,
      rule_pattern=rule_pattern,
      rule_check_kind=rule_check_kind,
      rule_target=rule_target,
      rule_variables=rule_variables,
      rule_message=rule_message,
      rule_severity=rule_severity,
      rule_origin=rule_origin,
    )

    rule_lite.additional_properties = d
    return rule_lite

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
