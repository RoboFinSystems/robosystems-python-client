from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_event_handler_request_origin import CreateEventHandlerRequestOrigin
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_event_handler_request_match_metadata_expression_type_0 import (
    CreateEventHandlerRequestMatchMetadataExpressionType0,
  )
  from ..models.create_event_handler_request_metadata import (
    CreateEventHandlerRequestMetadata,
  )
  from ..models.transaction_template import TransactionTemplate


T = TypeVar("T", bound="CreateEventHandlerRequest")


@_attrs_define
class CreateEventHandlerRequest:
  """
  Attributes:
      name (str):
      event_type (str):
      transaction_template (TransactionTemplate): The handler's output spec — one or more balanced entries to post.

          Wire shape::

              {
                "transactions": [{
                  "entry_template": {
                    "debit": {"element_id": "elem_...", "amount": "{{ event.amount }}"},
                    "credit": {"element_id": "elem_...", "amount": "{{ event.amount }}"}
                  }
                }]
              }
      description (None | str | Unset):
      event_category (None | str | Unset):
      match_source (None | str | Unset):
      match_agent_type (None | str | Unset):
      match_resource_type (None | str | Unset):
      match_metadata_expression (CreateEventHandlerRequestMatchMetadataExpressionType0 | None | Unset): JSONPath-style
          equality map, e.g. {"metadata.category": "payroll"}
      priority (int | Unset):  Default: 0.
      is_active (bool | Unset):  Default: True.
      origin (CreateEventHandlerRequestOrigin | Unset):  Default: CreateEventHandlerRequestOrigin.TENANT.
      metadata (CreateEventHandlerRequestMetadata | Unset):
  """

  name: str
  event_type: str
  transaction_template: TransactionTemplate
  description: None | str | Unset = UNSET
  event_category: None | str | Unset = UNSET
  match_source: None | str | Unset = UNSET
  match_agent_type: None | str | Unset = UNSET
  match_resource_type: None | str | Unset = UNSET
  match_metadata_expression: (
    CreateEventHandlerRequestMatchMetadataExpressionType0 | None | Unset
  ) = UNSET
  priority: int | Unset = 0
  is_active: bool | Unset = True
  origin: CreateEventHandlerRequestOrigin | Unset = (
    CreateEventHandlerRequestOrigin.TENANT
  )
  metadata: CreateEventHandlerRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.create_event_handler_request_match_metadata_expression_type_0 import (
      CreateEventHandlerRequestMatchMetadataExpressionType0,
    )

    name = self.name

    event_type = self.event_type

    transaction_template = self.transaction_template.to_dict()

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
      CreateEventHandlerRequestMatchMetadataExpressionType0,
    ):
      match_metadata_expression = self.match_metadata_expression.to_dict()
    else:
      match_metadata_expression = self.match_metadata_expression

    priority = self.priority

    is_active = self.is_active

    origin: str | Unset = UNSET
    if not isinstance(self.origin, Unset):
      origin = self.origin.value

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "event_type": event_type,
        "transaction_template": transaction_template,
      }
    )
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
    if priority is not UNSET:
      field_dict["priority"] = priority
    if is_active is not UNSET:
      field_dict["is_active"] = is_active
    if origin is not UNSET:
      field_dict["origin"] = origin
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_event_handler_request_match_metadata_expression_type_0 import (
      CreateEventHandlerRequestMatchMetadataExpressionType0,
    )
    from ..models.create_event_handler_request_metadata import (
      CreateEventHandlerRequestMetadata,
    )
    from ..models.transaction_template import TransactionTemplate

    d = dict(src_dict)
    name = d.pop("name")

    event_type = d.pop("event_type")

    transaction_template = TransactionTemplate.from_dict(d.pop("transaction_template"))

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
    ) -> CreateEventHandlerRequestMatchMetadataExpressionType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        match_metadata_expression_type_0 = (
          CreateEventHandlerRequestMatchMetadataExpressionType0.from_dict(data)
        )

        return match_metadata_expression_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(
        CreateEventHandlerRequestMatchMetadataExpressionType0 | None | Unset, data
      )

    match_metadata_expression = _parse_match_metadata_expression(
      d.pop("match_metadata_expression", UNSET)
    )

    priority = d.pop("priority", UNSET)

    is_active = d.pop("is_active", UNSET)

    _origin = d.pop("origin", UNSET)
    origin: CreateEventHandlerRequestOrigin | Unset
    if isinstance(_origin, Unset):
      origin = UNSET
    else:
      origin = CreateEventHandlerRequestOrigin(_origin)

    _metadata = d.pop("metadata", UNSET)
    metadata: CreateEventHandlerRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = CreateEventHandlerRequestMetadata.from_dict(_metadata)

    create_event_handler_request = cls(
      name=name,
      event_type=event_type,
      transaction_template=transaction_template,
      description=description,
      event_category=event_category,
      match_source=match_source,
      match_agent_type=match_agent_type,
      match_resource_type=match_resource_type,
      match_metadata_expression=match_metadata_expression,
      priority=priority,
      is_active=is_active,
      origin=origin,
      metadata=metadata,
    )

    create_event_handler_request.additional_properties = d
    return create_event_handler_request

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
