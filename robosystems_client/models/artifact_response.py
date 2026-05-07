from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.artifact_response_template_type_0 import ArtifactResponseTemplateType0
  from ..models.metric_mechanics import MetricMechanics
  from ..models.schedule_mechanics import ScheduleMechanics
  from ..models.statement_mechanics import StatementMechanics


T = TypeVar("T", bound="ArtifactResponse")


@_attrs_define
class ArtifactResponse:
  """The block's producible-artifact envelope — topic, template, mechanics.

  Attributes:
      mechanics (MetricMechanics | ScheduleMechanics | StatementMechanics):
      topic (None | str | Unset): Structure.description — the block's human-readable topic.
      parenthetical_note (None | str | Unset): e.g. 'in thousands', 'except per share'.
      template (ArtifactResponseTemplateType0 | None | Unset): Reusable layout (ordering, subtotals, styling) when
          attached. First-class templates are not yet implemented; this field is always null on currently-shipped block
          types.
  """

  mechanics: MetricMechanics | ScheduleMechanics | StatementMechanics
  topic: None | str | Unset = UNSET
  parenthetical_note: None | str | Unset = UNSET
  template: ArtifactResponseTemplateType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.artifact_response_template_type_0 import ArtifactResponseTemplateType0
    from ..models.schedule_mechanics import ScheduleMechanics
    from ..models.statement_mechanics import StatementMechanics

    mechanics: dict[str, Any]
    if isinstance(self.mechanics, ScheduleMechanics):
      mechanics = self.mechanics.to_dict()
    elif isinstance(self.mechanics, StatementMechanics):
      mechanics = self.mechanics.to_dict()
    else:
      mechanics = self.mechanics.to_dict()

    topic: None | str | Unset
    if isinstance(self.topic, Unset):
      topic = UNSET
    else:
      topic = self.topic

    parenthetical_note: None | str | Unset
    if isinstance(self.parenthetical_note, Unset):
      parenthetical_note = UNSET
    else:
      parenthetical_note = self.parenthetical_note

    template: dict[str, Any] | None | Unset
    if isinstance(self.template, Unset):
      template = UNSET
    elif isinstance(self.template, ArtifactResponseTemplateType0):
      template = self.template.to_dict()
    else:
      template = self.template

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "mechanics": mechanics,
      }
    )
    if topic is not UNSET:
      field_dict["topic"] = topic
    if parenthetical_note is not UNSET:
      field_dict["parenthetical_note"] = parenthetical_note
    if template is not UNSET:
      field_dict["template"] = template

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.artifact_response_template_type_0 import ArtifactResponseTemplateType0
    from ..models.metric_mechanics import MetricMechanics
    from ..models.schedule_mechanics import ScheduleMechanics
    from ..models.statement_mechanics import StatementMechanics

    d = dict(src_dict)

    def _parse_mechanics(
      data: object,
    ) -> MetricMechanics | ScheduleMechanics | StatementMechanics:
      try:
        if not isinstance(data, dict):
          raise TypeError()
        mechanics_type_0 = ScheduleMechanics.from_dict(data)

        return mechanics_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      try:
        if not isinstance(data, dict):
          raise TypeError()
        mechanics_type_1 = StatementMechanics.from_dict(data)

        return mechanics_type_1
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      if not isinstance(data, dict):
        raise TypeError()
      mechanics_type_2 = MetricMechanics.from_dict(data)

      return mechanics_type_2

    mechanics = _parse_mechanics(d.pop("mechanics"))

    def _parse_topic(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    topic = _parse_topic(d.pop("topic", UNSET))

    def _parse_parenthetical_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parenthetical_note = _parse_parenthetical_note(d.pop("parenthetical_note", UNSET))

    def _parse_template(data: object) -> ArtifactResponseTemplateType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        template_type_0 = ArtifactResponseTemplateType0.from_dict(data)

        return template_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ArtifactResponseTemplateType0 | None | Unset, data)

    template = _parse_template(d.pop("template", UNSET))

    artifact_response = cls(
      mechanics=mechanics,
      topic=topic,
      parenthetical_note=parenthetical_note,
      template=template,
    )

    artifact_response.additional_properties = d
    return artifact_response

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
