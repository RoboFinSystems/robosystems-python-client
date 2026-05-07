from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.event_handler_response import EventHandlerResponse
  from ..models.preview_event_block_response_handler_metadata import (
    PreviewEventBlockResponseHandlerMetadata,
  )
  from ..models.transaction_preview import TransactionPreview


T = TypeVar("T", bound="PreviewEventBlockResponse")


@_attrs_define
class PreviewEventBlockResponse:
  """Dry-run result — what would happen if this event block were created.

  Attributes:
      would_succeed (bool):
      matched_handler (EventHandlerResponse | None | Unset):
      planned_transactions (list[TransactionPreview] | Unset):
      validation_errors (list[str] | Unset):
      handler_metadata (PreviewEventBlockResponseHandlerMetadata | Unset): Handler-specific compute output. For Python
          handlers like 'asset_disposed', includes NBV, gain/loss, accumulated depreciation. Empty for DSL-handler
          previews.
  """

  would_succeed: bool
  matched_handler: EventHandlerResponse | None | Unset = UNSET
  planned_transactions: list[TransactionPreview] | Unset = UNSET
  validation_errors: list[str] | Unset = UNSET
  handler_metadata: PreviewEventBlockResponseHandlerMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.event_handler_response import EventHandlerResponse

    would_succeed = self.would_succeed

    matched_handler: dict[str, Any] | None | Unset
    if isinstance(self.matched_handler, Unset):
      matched_handler = UNSET
    elif isinstance(self.matched_handler, EventHandlerResponse):
      matched_handler = self.matched_handler.to_dict()
    else:
      matched_handler = self.matched_handler

    planned_transactions: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.planned_transactions, Unset):
      planned_transactions = []
      for planned_transactions_item_data in self.planned_transactions:
        planned_transactions_item = planned_transactions_item_data.to_dict()
        planned_transactions.append(planned_transactions_item)

    validation_errors: list[str] | Unset = UNSET
    if not isinstance(self.validation_errors, Unset):
      validation_errors = self.validation_errors

    handler_metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.handler_metadata, Unset):
      handler_metadata = self.handler_metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "would_succeed": would_succeed,
      }
    )
    if matched_handler is not UNSET:
      field_dict["matched_handler"] = matched_handler
    if planned_transactions is not UNSET:
      field_dict["planned_transactions"] = planned_transactions
    if validation_errors is not UNSET:
      field_dict["validation_errors"] = validation_errors
    if handler_metadata is not UNSET:
      field_dict["handler_metadata"] = handler_metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.event_handler_response import EventHandlerResponse
    from ..models.preview_event_block_response_handler_metadata import (
      PreviewEventBlockResponseHandlerMetadata,
    )
    from ..models.transaction_preview import TransactionPreview

    d = dict(src_dict)
    would_succeed = d.pop("would_succeed")

    def _parse_matched_handler(data: object) -> EventHandlerResponse | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        matched_handler_type_0 = EventHandlerResponse.from_dict(data)

        return matched_handler_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EventHandlerResponse | None | Unset, data)

    matched_handler = _parse_matched_handler(d.pop("matched_handler", UNSET))

    _planned_transactions = d.pop("planned_transactions", UNSET)
    planned_transactions: list[TransactionPreview] | Unset = UNSET
    if _planned_transactions is not UNSET:
      planned_transactions = []
      for planned_transactions_item_data in _planned_transactions:
        planned_transactions_item = TransactionPreview.from_dict(
          planned_transactions_item_data
        )

        planned_transactions.append(planned_transactions_item)

    validation_errors = cast(list[str], d.pop("validation_errors", UNSET))

    _handler_metadata = d.pop("handler_metadata", UNSET)
    handler_metadata: PreviewEventBlockResponseHandlerMetadata | Unset
    if isinstance(_handler_metadata, Unset):
      handler_metadata = UNSET
    else:
      handler_metadata = PreviewEventBlockResponseHandlerMetadata.from_dict(
        _handler_metadata
      )

    preview_event_block_response = cls(
      would_succeed=would_succeed,
      matched_handler=matched_handler,
      planned_transactions=planned_transactions,
      validation_errors=validation_errors,
      handler_metadata=handler_metadata,
    )

    preview_event_block_response.additional_properties = d
    return preview_event_block_response

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
