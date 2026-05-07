from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.event_block_envelope_metadata import EventBlockEnvelopeMetadata


T = TypeVar("T", bound="EventBlockEnvelope")


@_attrs_define
class EventBlockEnvelope:
  """Read projection for a single event block.

  Returned by `create-event-block`, `update-event-block`,
  `preview-event-block`, and the read-side `get-event-block`. Mirrors
  the request shape plus server-assigned fields (id, status, audit
  timestamps) and the four nullable correction/duality links.

      Attributes:
          id (str): Event ID (`evt_*` ULID).
          event_type (str): Open-vocabulary event type (e.g. `invoice_issued`, `bank_transaction`, `control_executed`).
          event_category (str): REA category — economic (`sales`, `purchase`, `financing`, `payroll`, `treasury`,
              `adjustment`, `recognition`, `other`) or support (`control`, `approval`, `reconciliation`, `inquiry`).
          status (str): Lifecycle state. One of: `captured` (raw, pre-classification), `classified` (handler ran, GL
              pending), `committed` (GL entries posted), `pending` (committed but awaiting fulfillment of an obligation),
              `fulfilled` (obligation discharged), `voided` (canceled — terminal), `superseded` (replaced by a corrected event
              — terminal). See `UpdateEventBlockRequest.transition_to` for the valid transition graph.
          occurred_at (datetime.datetime): When the event happened in the real world (UTC).
          source (str): Capture source (`quickbooks`, `xero`, `plaid`, `native`, `scheduled`, …). Used for adapter
              routing.
          currency (str): ISO 4217 currency code for `amount`.
          metadata (EventBlockEnvelopeMetadata): Free-form payload — handler-specific keys when the event ran through a
              handler, otherwise whatever the adapter captured.
          dimension_ids (list[str]): Dimension-member IDs tagging this event (department, fund, project). Propagate to GL
              entries produced by the handler.
          event_class (str): REA event class — `economic` (drives GL postings) or `support` (audit-trail / value-chain
              primitive, no GL impact).
          created_at (datetime.datetime): Row creation timestamp (UTC).
          created_by (str): ID of the user who captured the event. For adapter-sourced events, the system actor associated
              with the adapter.
          effective_at (datetime.datetime | None | Unset): Accounting recognition date, when different from `occurred_at`.
          external_id (None | str | Unset): Source-system dedup key. Unique with `source` when set, so adapter retries are
              idempotent.
          external_url (None | str | Unset): Deep link back to the source-system record.
          amount (int | None | Unset): Economic value in **cents** of `currency`, signed (inflows positive, outflows
              negative). `null` for non-economic events.
          description (None | str | Unset): Free-text human-readable summary.
          agent_id (None | str | Unset): Counterparty agent ID, when the event involves one.
          resource_type (None | str | Unset): REA resource kind being exchanged (`goods`, `services`, `money`, `right`,
              `obligation`, `information`, `labor`).
          resource_element_id (None | str | Unset): Specific element ID being exchanged, when known.
          replaced_by_event_id (None | str | Unset): ID of the event that replaces this one. Set when this event was
              superseded (`status='superseded'`); points forward in the correction chain.
          replaces_event_id (None | str | Unset): ID of the event this one replaces, when applicable. Points backward in
              the correction chain. Mirror of `replaced_by_event_id` on the predecessor.
          obligated_by_event_id (None | str | Unset): Forward-materialization link — the event that scheduled or obligated
              this one (e.g. depreciation entries point at the originating `asset_acquired` event).
          discharges_event_id (None | str | Unset): Settlement link — the obligation this event discharges (e.g.
              `cash_received` pointing at the originating `sale_invoiced`).
  """

  id: str
  event_type: str
  event_category: str
  status: str
  occurred_at: datetime.datetime
  source: str
  currency: str
  metadata: EventBlockEnvelopeMetadata
  dimension_ids: list[str]
  event_class: str
  created_at: datetime.datetime
  created_by: str
  effective_at: datetime.datetime | None | Unset = UNSET
  external_id: None | str | Unset = UNSET
  external_url: None | str | Unset = UNSET
  amount: int | None | Unset = UNSET
  description: None | str | Unset = UNSET
  agent_id: None | str | Unset = UNSET
  resource_type: None | str | Unset = UNSET
  resource_element_id: None | str | Unset = UNSET
  replaced_by_event_id: None | str | Unset = UNSET
  replaces_event_id: None | str | Unset = UNSET
  obligated_by_event_id: None | str | Unset = UNSET
  discharges_event_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    event_type = self.event_type

    event_category = self.event_category

    status = self.status

    occurred_at = self.occurred_at.isoformat()

    source = self.source

    currency = self.currency

    metadata = self.metadata.to_dict()

    dimension_ids = self.dimension_ids

    event_class = self.event_class

    created_at = self.created_at.isoformat()

    created_by = self.created_by

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

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    agent_id: None | str | Unset
    if isinstance(self.agent_id, Unset):
      agent_id = UNSET
    else:
      agent_id = self.agent_id

    resource_type: None | str | Unset
    if isinstance(self.resource_type, Unset):
      resource_type = UNSET
    else:
      resource_type = self.resource_type

    resource_element_id: None | str | Unset
    if isinstance(self.resource_element_id, Unset):
      resource_element_id = UNSET
    else:
      resource_element_id = self.resource_element_id

    replaced_by_event_id: None | str | Unset
    if isinstance(self.replaced_by_event_id, Unset):
      replaced_by_event_id = UNSET
    else:
      replaced_by_event_id = self.replaced_by_event_id

    replaces_event_id: None | str | Unset
    if isinstance(self.replaces_event_id, Unset):
      replaces_event_id = UNSET
    else:
      replaces_event_id = self.replaces_event_id

    obligated_by_event_id: None | str | Unset
    if isinstance(self.obligated_by_event_id, Unset):
      obligated_by_event_id = UNSET
    else:
      obligated_by_event_id = self.obligated_by_event_id

    discharges_event_id: None | str | Unset
    if isinstance(self.discharges_event_id, Unset):
      discharges_event_id = UNSET
    else:
      discharges_event_id = self.discharges_event_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "event_type": event_type,
        "event_category": event_category,
        "status": status,
        "occurred_at": occurred_at,
        "source": source,
        "currency": currency,
        "metadata": metadata,
        "dimension_ids": dimension_ids,
        "event_class": event_class,
        "created_at": created_at,
        "created_by": created_by,
      }
    )
    if effective_at is not UNSET:
      field_dict["effective_at"] = effective_at
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if external_url is not UNSET:
      field_dict["external_url"] = external_url
    if amount is not UNSET:
      field_dict["amount"] = amount
    if description is not UNSET:
      field_dict["description"] = description
    if agent_id is not UNSET:
      field_dict["agent_id"] = agent_id
    if resource_type is not UNSET:
      field_dict["resource_type"] = resource_type
    if resource_element_id is not UNSET:
      field_dict["resource_element_id"] = resource_element_id
    if replaced_by_event_id is not UNSET:
      field_dict["replaced_by_event_id"] = replaced_by_event_id
    if replaces_event_id is not UNSET:
      field_dict["replaces_event_id"] = replaces_event_id
    if obligated_by_event_id is not UNSET:
      field_dict["obligated_by_event_id"] = obligated_by_event_id
    if discharges_event_id is not UNSET:
      field_dict["discharges_event_id"] = discharges_event_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.event_block_envelope_metadata import EventBlockEnvelopeMetadata

    d = dict(src_dict)
    id = d.pop("id")

    event_type = d.pop("event_type")

    event_category = d.pop("event_category")

    status = d.pop("status")

    occurred_at = isoparse(d.pop("occurred_at"))

    source = d.pop("source")

    currency = d.pop("currency")

    metadata = EventBlockEnvelopeMetadata.from_dict(d.pop("metadata"))

    dimension_ids = cast(list[str], d.pop("dimension_ids"))

    event_class = d.pop("event_class")

    created_at = isoparse(d.pop("created_at"))

    created_by = d.pop("created_by")

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

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_agent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

    def _parse_resource_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

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

    def _parse_replaced_by_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    replaced_by_event_id = _parse_replaced_by_event_id(
      d.pop("replaced_by_event_id", UNSET)
    )

    def _parse_replaces_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    replaces_event_id = _parse_replaces_event_id(d.pop("replaces_event_id", UNSET))

    def _parse_obligated_by_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    obligated_by_event_id = _parse_obligated_by_event_id(
      d.pop("obligated_by_event_id", UNSET)
    )

    def _parse_discharges_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    discharges_event_id = _parse_discharges_event_id(
      d.pop("discharges_event_id", UNSET)
    )

    event_block_envelope = cls(
      id=id,
      event_type=event_type,
      event_category=event_category,
      status=status,
      occurred_at=occurred_at,
      source=source,
      currency=currency,
      metadata=metadata,
      dimension_ids=dimension_ids,
      event_class=event_class,
      created_at=created_at,
      created_by=created_by,
      effective_at=effective_at,
      external_id=external_id,
      external_url=external_url,
      amount=amount,
      description=description,
      agent_id=agent_id,
      resource_type=resource_type,
      resource_element_id=resource_element_id,
      replaced_by_event_id=replaced_by_event_id,
      replaces_event_id=replaces_event_id,
      obligated_by_event_id=obligated_by_event_id,
      discharges_event_id=discharges_event_id,
    )

    event_block_envelope.additional_properties = d
    return event_block_envelope

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
