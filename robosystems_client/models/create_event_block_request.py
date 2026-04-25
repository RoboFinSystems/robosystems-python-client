from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_event_block_request_event_category import (
  CreateEventBlockRequestEventCategory,
)
from ..models.create_event_block_request_resource_type_type_0 import (
  CreateEventBlockRequestResourceTypeType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_event_block_request_metadata import (
    CreateEventBlockRequestMetadata,
  )


T = TypeVar("T", bound="CreateEventBlockRequest")


@_attrs_define
class CreateEventBlockRequest:
  """Write surface for a single business event.

  Attributes:
      event_type (str): Open vocabulary: 'invoice_issued' | 'contract_signed' | 'bank_transaction' | ...
      event_category (CreateEventBlockRequestEventCategory): REA economic classification. One of: sales, purchase,
          financing, payroll, treasury, adjustment, recognition, other.
      occurred_at (datetime.datetime): When the event happened in the real world
      source (str): 'quickbooks' | 'xero' | 'plaid' | 'native' | 'scheduled' | ...
      agent_id (None | str | Unset): Counterparty agent id
      resource_type (CreateEventBlockRequestResourceTypeType0 | None | Unset): REA resource kind. One of: goods,
          services, money, right, obligation, information, labor.
      resource_element_id (None | str | Unset): Specific element being exchanged, if applicable
      effective_at (datetime.datetime | None | Unset): Accounting recognition date, if different from occurred_at
      external_id (None | str | Unset): Source-system dedup key. (source, external_id) is enforced unique when
          external_id is provided, so retries from external adapters are idempotent at the DB level.
      external_url (None | str | Unset): Deep link back to source-system record
      amount (int | None | Unset): Cents, signed
      currency (str | Unset): ISO 4217 currency code Default: 'USD'.
      description (None | str | Unset):
      metadata (CreateEventBlockRequestMetadata | Unset): Event-type-specific payload
      dimension_ids (list[str] | Unset):
      apply_handlers (bool | Unset): When True, resolves the event_type to a handler (Python registry first, then DSL)
          and fires it atomically with event creation. Default: False.
  """

  event_type: str
  event_category: CreateEventBlockRequestEventCategory
  occurred_at: datetime.datetime
  source: str
  agent_id: None | str | Unset = UNSET
  resource_type: CreateEventBlockRequestResourceTypeType0 | None | Unset = UNSET
  resource_element_id: None | str | Unset = UNSET
  effective_at: datetime.datetime | None | Unset = UNSET
  external_id: None | str | Unset = UNSET
  external_url: None | str | Unset = UNSET
  amount: int | None | Unset = UNSET
  currency: str | Unset = "USD"
  description: None | str | Unset = UNSET
  metadata: CreateEventBlockRequestMetadata | Unset = UNSET
  dimension_ids: list[str] | Unset = UNSET
  apply_handlers: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_type = self.event_type

    event_category = self.event_category.value

    occurred_at = self.occurred_at.isoformat()

    source = self.source

    agent_id: None | str | Unset
    if isinstance(self.agent_id, Unset):
      agent_id = UNSET
    else:
      agent_id = self.agent_id

    resource_type: None | str | Unset
    if isinstance(self.resource_type, Unset):
      resource_type = UNSET
    elif isinstance(self.resource_type, CreateEventBlockRequestResourceTypeType0):
      resource_type = self.resource_type.value
    else:
      resource_type = self.resource_type

    resource_element_id: None | str | Unset
    if isinstance(self.resource_element_id, Unset):
      resource_element_id = UNSET
    else:
      resource_element_id = self.resource_element_id

    effective_at: None | str | Unset
    if isinstance(self.effective_at, Unset):
      effective_at = UNSET
    elif isinstance(self.effective_at, datetime.datetime):
      effective_at = self.effective_at.isoformat()
    else:
      effective_at = self.effective_at

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    external_url: None | str | Unset
    if isinstance(self.external_url, Unset):
      external_url = UNSET
    else:
      external_url = self.external_url

    amount: int | None | Unset
    if isinstance(self.amount, Unset):
      amount = UNSET
    else:
      amount = self.amount

    currency = self.currency

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    dimension_ids: list[str] | Unset = UNSET
    if not isinstance(self.dimension_ids, Unset):
      dimension_ids = self.dimension_ids

    apply_handlers = self.apply_handlers

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_type": event_type,
        "event_category": event_category,
        "occurred_at": occurred_at,
        "source": source,
      }
    )
    if agent_id is not UNSET:
      field_dict["agent_id"] = agent_id
    if resource_type is not UNSET:
      field_dict["resource_type"] = resource_type
    if resource_element_id is not UNSET:
      field_dict["resource_element_id"] = resource_element_id
    if effective_at is not UNSET:
      field_dict["effective_at"] = effective_at
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if external_url is not UNSET:
      field_dict["external_url"] = external_url
    if amount is not UNSET:
      field_dict["amount"] = amount
    if currency is not UNSET:
      field_dict["currency"] = currency
    if description is not UNSET:
      field_dict["description"] = description
    if metadata is not UNSET:
      field_dict["metadata"] = metadata
    if dimension_ids is not UNSET:
      field_dict["dimension_ids"] = dimension_ids
    if apply_handlers is not UNSET:
      field_dict["apply_handlers"] = apply_handlers

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_event_block_request_metadata import (
      CreateEventBlockRequestMetadata,
    )

    d = dict(src_dict)
    event_type = d.pop("event_type")

    event_category = CreateEventBlockRequestEventCategory(d.pop("event_category"))

    occurred_at = isoparse(d.pop("occurred_at"))

    source = d.pop("source")

    def _parse_agent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

    def _parse_resource_type(
      data: object,
    ) -> CreateEventBlockRequestResourceTypeType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        resource_type_type_0 = CreateEventBlockRequestResourceTypeType0(data)

        return resource_type_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(CreateEventBlockRequestResourceTypeType0 | None | Unset, data)

    resource_type = _parse_resource_type(d.pop("resource_type", UNSET))

    def _parse_resource_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    resource_element_id = _parse_resource_element_id(
      d.pop("resource_element_id", UNSET)
    )

    def _parse_effective_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        effective_at_type_0 = isoparse(data)

        return effective_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    effective_at = _parse_effective_at(d.pop("effective_at", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    def _parse_external_url(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_url = _parse_external_url(d.pop("external_url", UNSET))

    def _parse_amount(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    amount = _parse_amount(d.pop("amount", UNSET))

    currency = d.pop("currency", UNSET)

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    _metadata = d.pop("metadata", UNSET)
    metadata: CreateEventBlockRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = CreateEventBlockRequestMetadata.from_dict(_metadata)

    dimension_ids = cast(list[str], d.pop("dimension_ids", UNSET))

    apply_handlers = d.pop("apply_handlers", UNSET)

    create_event_block_request = cls(
      event_type=event_type,
      event_category=event_category,
      occurred_at=occurred_at,
      source=source,
      agent_id=agent_id,
      resource_type=resource_type,
      resource_element_id=resource_element_id,
      effective_at=effective_at,
      external_id=external_id,
      external_url=external_url,
      amount=amount,
      currency=currency,
      description=description,
      metadata=metadata,
      dimension_ids=dimension_ids,
      apply_handlers=apply_handlers,
    )

    create_event_block_request.additional_properties = d
    return create_event_block_request

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
