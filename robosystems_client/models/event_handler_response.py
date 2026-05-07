from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.event_handler_response_match_metadata_expression_type_0 import (
    EventHandlerResponseMatchMetadataExpressionType0,
  )
  from ..models.event_handler_response_transaction_template import (
    EventHandlerResponseTransactionTemplate,
  )


T = TypeVar("T", bound="EventHandlerResponse")


@_attrs_define
class EventHandlerResponse:
  """
  Attributes:
      id (str):
      name (str):
      event_type (str):
      transaction_template (EventHandlerResponseTransactionTemplate):
      priority (int):
      is_active (bool):
      origin (str):
      description (None | str | Unset):
      event_category (None | str | Unset):
      match_source (None | str | Unset):
      match_agent_type (None | str | Unset):
      match_resource_type (None | str | Unset):
      match_metadata_expression (EventHandlerResponseMatchMetadataExpressionType0 | None | Unset):
      suggested_by (None | str | Unset):
      confidence (float | None | Unset):
      approved_by (None | str | Unset):
      approved_at (datetime.datetime | None | Unset):
      created_at (datetime.datetime | None | Unset):
      updated_at (datetime.datetime | None | Unset):
      created_by (None | str | Unset):
  """

  id: str
  name: str
  event_type: str
  transaction_template: EventHandlerResponseTransactionTemplate
  priority: int
  is_active: bool
  origin: str
  description: None | str | Unset = UNSET
  event_category: None | str | Unset = UNSET
  match_source: None | str | Unset = UNSET
  match_agent_type: None | str | Unset = UNSET
  match_resource_type: None | str | Unset = UNSET
  match_metadata_expression: (
    EventHandlerResponseMatchMetadataExpressionType0 | None | Unset
  ) = UNSET
  suggested_by: None | str | Unset = UNSET
  confidence: float | None | Unset = UNSET
  approved_by: None | str | Unset = UNSET
  approved_at: datetime.datetime | None | Unset = UNSET
  created_at: datetime.datetime | None | Unset = UNSET
  updated_at: datetime.datetime | None | Unset = UNSET
  created_by: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.event_handler_response_match_metadata_expression_type_0 import (
      EventHandlerResponseMatchMetadataExpressionType0,
    )

    id = self.id

    name = self.name

    event_type = self.event_type

    transaction_template = self.transaction_template.to_dict()

    priority = self.priority

    is_active = self.is_active

    origin = self.origin

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
      self.match_metadata_expression, EventHandlerResponseMatchMetadataExpressionType0
    ):
      match_metadata_expression = self.match_metadata_expression.to_dict()
    else:
      match_metadata_expression = self.match_metadata_expression

    suggested_by: None | str | Unset
    if isinstance(self.suggested_by, Unset):
      suggested_by = UNSET
    else:
      suggested_by = self.suggested_by

    confidence: float | None | Unset
    if isinstance(self.confidence, Unset):
      confidence = UNSET
    else:
      confidence = self.confidence

    approved_by: None | str | Unset
    if isinstance(self.approved_by, Unset):
      approved_by = UNSET
    else:
      approved_by = self.approved_by

    approved_at: None | str | Unset
    if isinstance(self.approved_at, Unset):
      approved_at = UNSET
    elif isinstance(self.approved_at, datetime.datetime):
      approved_at = self.approved_at.isoformat()
    else:
      approved_at = self.approved_at

    created_at: None | str | Unset
    if isinstance(self.created_at, Unset):
      created_at = UNSET
    elif isinstance(self.created_at, datetime.datetime):
      created_at = self.created_at.isoformat()
    else:
      created_at = self.created_at

    updated_at: None | str | Unset
    if isinstance(self.updated_at, Unset):
      updated_at = UNSET
    elif isinstance(self.updated_at, datetime.datetime):
      updated_at = self.updated_at.isoformat()
    else:
      updated_at = self.updated_at

    created_by: None | str | Unset
    if isinstance(self.created_by, Unset):
      created_by = UNSET
    else:
      created_by = self.created_by

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "event_type": event_type,
        "transaction_template": transaction_template,
        "priority": priority,
        "is_active": is_active,
        "origin": origin,
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
    if suggested_by is not UNSET:
      field_dict["suggested_by"] = suggested_by
    if confidence is not UNSET:
      field_dict["confidence"] = confidence
    if approved_by is not UNSET:
      field_dict["approved_by"] = approved_by
    if approved_at is not UNSET:
      field_dict["approved_at"] = approved_at
    if created_at is not UNSET:
      field_dict["created_at"] = created_at
    if updated_at is not UNSET:
      field_dict["updated_at"] = updated_at
    if created_by is not UNSET:
      field_dict["created_by"] = created_by

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.event_handler_response_match_metadata_expression_type_0 import (
      EventHandlerResponseMatchMetadataExpressionType0,
    )
    from ..models.event_handler_response_transaction_template import (
      EventHandlerResponseTransactionTemplate,
    )

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    event_type = d.pop("event_type")

    transaction_template = EventHandlerResponseTransactionTemplate.from_dict(
      d.pop("transaction_template")
    )

    priority = d.pop("priority")

    is_active = d.pop("is_active")

    origin = d.pop("origin")

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
    ) -> EventHandlerResponseMatchMetadataExpressionType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        match_metadata_expression_type_0 = (
          EventHandlerResponseMatchMetadataExpressionType0.from_dict(data)
        )

        return match_metadata_expression_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EventHandlerResponseMatchMetadataExpressionType0 | None | Unset, data)

    match_metadata_expression = _parse_match_metadata_expression(
      d.pop("match_metadata_expression", UNSET)
    )

    def _parse_suggested_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    suggested_by = _parse_suggested_by(d.pop("suggested_by", UNSET))

    def _parse_confidence(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    confidence = _parse_confidence(d.pop("confidence", UNSET))

    def _parse_approved_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

    def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        approved_at_type_0 = isoparse(data)

        return approved_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    approved_at = _parse_approved_at(d.pop("approved_at", UNSET))

    def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        created_at_type_0 = isoparse(data)

        return created_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    created_at = _parse_created_at(d.pop("created_at", UNSET))

    def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        updated_at_type_0 = isoparse(data)

        return updated_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

    def _parse_created_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    created_by = _parse_created_by(d.pop("created_by", UNSET))

    event_handler_response = cls(
      id=id,
      name=name,
      event_type=event_type,
      transaction_template=transaction_template,
      priority=priority,
      is_active=is_active,
      origin=origin,
      description=description,
      event_category=event_category,
      match_source=match_source,
      match_agent_type=match_agent_type,
      match_resource_type=match_resource_type,
      match_metadata_expression=match_metadata_expression,
      suggested_by=suggested_by,
      confidence=confidence,
      approved_by=approved_by,
      approved_at=approved_at,
      created_at=created_at,
      updated_at=updated_at,
      created_by=created_by,
    )

    event_handler_response.additional_properties = d
    return event_handler_response

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
