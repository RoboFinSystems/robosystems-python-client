from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taxonomy_block_rule_request_rule_category import (
  TaxonomyBlockRuleRequestRuleCategory,
)
from ..models.taxonomy_block_rule_request_rule_pattern import (
  TaxonomyBlockRuleRequestRulePattern,
)
from ..models.taxonomy_block_rule_request_severity import (
  TaxonomyBlockRuleRequestSeverity,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.taxonomy_block_rule_request_metadata import (
    TaxonomyBlockRuleRequestMetadata,
  )
  from ..models.taxonomy_block_rule_request_variables_item import (
    TaxonomyBlockRuleRequestVariablesItem,
  )


T = TypeVar("T", bound="TaxonomyBlockRuleRequest")


@_attrs_define
class TaxonomyBlockRuleRequest:
  """Rule definition inside a Taxonomy Block envelope.

  Exactly one of ``target_structure_ref``, ``target_element_qname``, or
  ``target_taxonomy_self`` must be set (or all null for a global rule).
  The ``model_validator`` enforces this contract at the Pydantic layer.

      Attributes:
          name (str): Rule identifier, unique within envelope.
          rule_category (TaxonomyBlockRuleRequestRuleCategory): One of 8 cm:VerificationRule subclasses.
          rule_pattern (TaxonomyBlockRuleRequestRulePattern): One of 11 cm:BusinessRulePattern mechanisms.
          expression (str): XPath-flavored predicate body (the rule expression).
          description (None | str | Unset):
          variables (list[TaxonomyBlockRuleRequestVariablesItem] | Unset): ``$Variable`` → qname bindings. Each entry is
              ``{'variable_name': str, 'variable_qname': str}``.
          severity (TaxonomyBlockRuleRequestSeverity | Unset):  Default: TaxonomyBlockRuleRequestSeverity.ERROR.
          target_structure_ref (None | str | Unset): Envelope-local structure name this rule targets (for structure-scoped
              rules). Mutually exclusive with the other target_* fields.
          target_element_qname (None | str | Unset): qname of the element this rule targets. Mutually exclusive with the
              other target_* fields.
          target_taxonomy_self (bool | Unset): True iff the rule targets the envelope's own taxonomy row
              (``target_kind='taxonomy'``). Mutually exclusive with the other target_* fields. Default: False.
          message (None | str | Unset):
          metadata (TaxonomyBlockRuleRequestMetadata | Unset):
  """

  name: str
  rule_category: TaxonomyBlockRuleRequestRuleCategory
  rule_pattern: TaxonomyBlockRuleRequestRulePattern
  expression: str
  description: None | str | Unset = UNSET
  variables: list[TaxonomyBlockRuleRequestVariablesItem] | Unset = UNSET
  severity: TaxonomyBlockRuleRequestSeverity | Unset = (
    TaxonomyBlockRuleRequestSeverity.ERROR
  )
  target_structure_ref: None | str | Unset = UNSET
  target_element_qname: None | str | Unset = UNSET
  target_taxonomy_self: bool | Unset = False
  message: None | str | Unset = UNSET
  metadata: TaxonomyBlockRuleRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    rule_category = self.rule_category.value

    rule_pattern = self.rule_pattern.value

    expression = self.expression

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    variables: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.variables, Unset):
      variables = []
      for variables_item_data in self.variables:
        variables_item = variables_item_data.to_dict()
        variables.append(variables_item)

    severity: str | Unset = UNSET
    if not isinstance(self.severity, Unset):
      severity = self.severity.value

    target_structure_ref: None | str | Unset
    if isinstance(self.target_structure_ref, Unset):
      target_structure_ref = UNSET
    else:
      target_structure_ref = self.target_structure_ref

    target_element_qname: None | str | Unset
    if isinstance(self.target_element_qname, Unset):
      target_element_qname = UNSET
    else:
      target_element_qname = self.target_element_qname

    target_taxonomy_self = self.target_taxonomy_self

    message: None | str | Unset
    if isinstance(self.message, Unset):
      message = UNSET
    else:
      message = self.message

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "rule_category": rule_category,
        "rule_pattern": rule_pattern,
        "expression": expression,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if variables is not UNSET:
      field_dict["variables"] = variables
    if severity is not UNSET:
      field_dict["severity"] = severity
    if target_structure_ref is not UNSET:
      field_dict["target_structure_ref"] = target_structure_ref
    if target_element_qname is not UNSET:
      field_dict["target_element_qname"] = target_element_qname
    if target_taxonomy_self is not UNSET:
      field_dict["target_taxonomy_self"] = target_taxonomy_self
    if message is not UNSET:
      field_dict["message"] = message
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.taxonomy_block_rule_request_metadata import (
      TaxonomyBlockRuleRequestMetadata,
    )
    from ..models.taxonomy_block_rule_request_variables_item import (
      TaxonomyBlockRuleRequestVariablesItem,
    )

    d = dict(src_dict)
    name = d.pop("name")

    rule_category = TaxonomyBlockRuleRequestRuleCategory(d.pop("rule_category"))

    rule_pattern = TaxonomyBlockRuleRequestRulePattern(d.pop("rule_pattern"))

    expression = d.pop("expression")

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    _variables = d.pop("variables", UNSET)
    variables: list[TaxonomyBlockRuleRequestVariablesItem] | Unset = UNSET
    if _variables is not UNSET:
      variables = []
      for variables_item_data in _variables:
        variables_item = TaxonomyBlockRuleRequestVariablesItem.from_dict(
          variables_item_data
        )

        variables.append(variables_item)

    _severity = d.pop("severity", UNSET)
    severity: TaxonomyBlockRuleRequestSeverity | Unset
    if isinstance(_severity, Unset):
      severity = UNSET
    else:
      severity = TaxonomyBlockRuleRequestSeverity(_severity)

    def _parse_target_structure_ref(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_structure_ref = _parse_target_structure_ref(
      d.pop("target_structure_ref", UNSET)
    )

    def _parse_target_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_element_qname = _parse_target_element_qname(
      d.pop("target_element_qname", UNSET)
    )

    target_taxonomy_self = d.pop("target_taxonomy_self", UNSET)

    def _parse_message(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    message = _parse_message(d.pop("message", UNSET))

    _metadata = d.pop("metadata", UNSET)
    metadata: TaxonomyBlockRuleRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = TaxonomyBlockRuleRequestMetadata.from_dict(_metadata)

    taxonomy_block_rule_request = cls(
      name=name,
      rule_category=rule_category,
      rule_pattern=rule_pattern,
      expression=expression,
      description=description,
      variables=variables,
      severity=severity,
      target_structure_ref=target_structure_ref,
      target_element_qname=target_element_qname,
      target_taxonomy_self=target_taxonomy_self,
      message=message,
      metadata=metadata,
    )

    taxonomy_block_rule_request.additional_properties = d
    return taxonomy_block_rule_request

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
