from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.transaction_template import TransactionTemplate
  from ..models.update_event_handler_request_match_metadata_expression_type_0 import (
    UpdateEventHandlerRequestMatchMetadataExpressionType0,
  )
  from ..models.update_event_handler_request_metadata_patch import (
    UpdateEventHandlerRequestMetadataPatch,
  )


T = TypeVar("T", bound="UpdateEventHandlerRequest")


@_attrs_define
class UpdateEventHandlerRequest:
  """Update an existing event handler. All fields except
  ``event_handler_id`` are optional — pass only what changes.

  ``transaction_template`` is **fully replaced** when supplied (no
  partial template patches). ``metadata_patch`` does deep-merge into
  the existing metadata. ``approve=true`` sets ``approved_by`` and
  ``approved_at``; ``approve=false`` clears them.

      Attributes:
          event_handler_id (str): The handler to update.
          name (None | str | Unset): New name. Omit to leave unchanged.
          description (None | str | Unset): New description.
          event_category (None | str | Unset):
          match_source (None | str | Unset):
          match_agent_type (None | str | Unset):
          match_resource_type (None | str | Unset):
          match_metadata_expression (None | Unset | UpdateEventHandlerRequestMatchMetadataExpressionType0):
          transaction_template (None | TransactionTemplate | Unset): Replacement template. Whole-template replace — no
              partial patch. Omit to leave unchanged.
          priority (int | None | Unset):
          is_active (bool | None | Unset): Toggle activation. False removes the handler from match-time consideration
              without deleting it.
          approve (bool | None | Unset): Approval shortcut: True stamps approved_by/approved_at to the current user; False
              clears both.
          metadata_patch (UpdateEventHandlerRequestMetadataPatch | Unset): Deep-merged into the existing handler.metadata.
              Pass `{}` to leave metadata unchanged.
  """

  event_handler_id: str
  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  event_category: None | str | Unset = UNSET
  match_source: None | str | Unset = UNSET
  match_agent_type: None | str | Unset = UNSET
  match_resource_type: None | str | Unset = UNSET
  match_metadata_expression: (
    None | Unset | UpdateEventHandlerRequestMatchMetadataExpressionType0
  ) = UNSET
  transaction_template: None | TransactionTemplate | Unset = UNSET
  priority: int | None | Unset = UNSET
  is_active: bool | None | Unset = UNSET
  approve: bool | None | Unset = UNSET
  metadata_patch: UpdateEventHandlerRequestMetadataPatch | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.transaction_template import TransactionTemplate
    from ..models.update_event_handler_request_match_metadata_expression_type_0 import (
      UpdateEventHandlerRequestMatchMetadataExpressionType0,
    )

    event_handler_id = self.event_handler_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    event_category: None | str | Unset
    if isinstance(self.event_category, Unset):
      event_category = UNSET
    else:
      event_category = self.event_category

    match_source: None | str | Unset
    if isinstance(self.match_source, Unset):
      match_source = UNSET
    else:
      match_source = self.match_source

    match_agent_type: None | str | Unset
    if isinstance(self.match_agent_type, Unset):
      match_agent_type = UNSET
    else:
      match_agent_type = self.match_agent_type

    match_resource_type: None | str | Unset
    if isinstance(self.match_resource_type, Unset):
      match_resource_type = UNSET
    else:
      match_resource_type = self.match_resource_type

    match_metadata_expression: dict[str, Any] | None | Unset
    if isinstance(self.match_metadata_expression, Unset):
      match_metadata_expression = UNSET
    elif isinstance(
      self.match_metadata_expression,
      UpdateEventHandlerRequestMatchMetadataExpressionType0,
    ):
      match_metadata_expression = self.match_metadata_expression.to_dict()
    else:
      match_metadata_expression = self.match_metadata_expression

    transaction_template: dict[str, Any] | None | Unset
    if isinstance(self.transaction_template, Unset):
      transaction_template = UNSET
    elif isinstance(self.transaction_template, TransactionTemplate):
      transaction_template = self.transaction_template.to_dict()
    else:
      transaction_template = self.transaction_template

    priority: int | None | Unset
    if isinstance(self.priority, Unset):
      priority = UNSET
    else:
      priority = self.priority

    is_active: bool | None | Unset
    if isinstance(self.is_active, Unset):
      is_active = UNSET
    else:
      is_active = self.is_active

    approve: bool | None | Unset
    if isinstance(self.approve, Unset):
      approve = UNSET
    else:
      approve = self.approve

    metadata_patch: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata_patch, Unset):
      metadata_patch = self.metadata_patch.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_handler_id": event_handler_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if description is not UNSET:
      field_dict["description"] = description
    if event_category is not UNSET:
      field_dict["event_category"] = event_category
    if match_source is not UNSET:
      field_dict["match_source"] = match_source
    if match_agent_type is not UNSET:
      field_dict["match_agent_type"] = match_agent_type
    if match_resource_type is not UNSET:
      field_dict["match_resource_type"] = match_resource_type
    if match_metadata_expression is not UNSET:
      field_dict["match_metadata_expression"] = match_metadata_expression
    if transaction_template is not UNSET:
      field_dict["transaction_template"] = transaction_template
    if priority is not UNSET:
      field_dict["priority"] = priority
    if is_active is not UNSET:
      field_dict["is_active"] = is_active
    if approve is not UNSET:
      field_dict["approve"] = approve
    if metadata_patch is not UNSET:
      field_dict["metadata_patch"] = metadata_patch

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.transaction_template import TransactionTemplate
    from ..models.update_event_handler_request_match_metadata_expression_type_0 import (
      UpdateEventHandlerRequestMatchMetadataExpressionType0,
    )
    from ..models.update_event_handler_request_metadata_patch import (
      UpdateEventHandlerRequestMetadataPatch,
    )

    d = dict(src_dict)
    event_handler_id = d.pop("event_handler_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_event_category(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    event_category = _parse_event_category(d.pop("event_category", UNSET))

    def _parse_match_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    match_source = _parse_match_source(d.pop("match_source", UNSET))

    def _parse_match_agent_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    match_agent_type = _parse_match_agent_type(d.pop("match_agent_type", UNSET))

    def _parse_match_resource_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    match_resource_type = _parse_match_resource_type(
      d.pop("match_resource_type", UNSET)
    )

    def _parse_match_metadata_expression(
      data: object,
    ) -> None | Unset | UpdateEventHandlerRequestMatchMetadataExpressionType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        match_metadata_expression_type_0 = (
          UpdateEventHandlerRequestMatchMetadataExpressionType0.from_dict(data)
        )

        return match_metadata_expression_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(
        None | Unset | UpdateEventHandlerRequestMatchMetadataExpressionType0, data
      )

    match_metadata_expression = _parse_match_metadata_expression(
      d.pop("match_metadata_expression", UNSET)
    )

    def _parse_transaction_template(data: object) -> None | TransactionTemplate | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        transaction_template_type_0 = TransactionTemplate.from_dict(data)

        return transaction_template_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | TransactionTemplate | Unset, data)

    transaction_template = _parse_transaction_template(
      d.pop("transaction_template", UNSET)
    )

    def _parse_priority(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    priority = _parse_priority(d.pop("priority", UNSET))

    def _parse_is_active(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    is_active = _parse_is_active(d.pop("is_active", UNSET))

    def _parse_approve(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    approve = _parse_approve(d.pop("approve", UNSET))

    _metadata_patch = d.pop("metadata_patch", UNSET)
    metadata_patch: UpdateEventHandlerRequestMetadataPatch | Unset
    if isinstance(_metadata_patch, Unset):
      metadata_patch = UNSET
    else:
      metadata_patch = UpdateEventHandlerRequestMetadataPatch.from_dict(_metadata_patch)

    update_event_handler_request = cls(
      event_handler_id=event_handler_id,
      name=name,
      description=description,
      event_category=event_category,
      match_source=match_source,
      match_agent_type=match_agent_type,
      match_resource_type=match_resource_type,
      match_metadata_expression=match_metadata_expression,
      transaction_template=transaction_template,
      priority=priority,
      is_active=is_active,
      approve=approve,
      metadata_patch=metadata_patch,
    )

    update_event_handler_request.additional_properties = d
    return update_event_handler_request

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
