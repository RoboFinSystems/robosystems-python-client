from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.journal_entry_line_item_input_metadata_type_0 import (
    JournalEntryLineItemInputMetadataType0,
  )


T = TypeVar("T", bound="JournalEntryLineItemInput")


@_attrs_define
class JournalEntryLineItemInput:
  """One debit/credit line in a journal entry create/update payload.

  Exactly one of `debit_amount` / `credit_amount` must be non-zero; the
  other must be zero. Amounts are in minor currency units (cents).

      Attributes:
          element_id (str): Element ULID identifying the account to post to.
          debit_amount (int | Unset): Debit amount in cents. Must be 0 if `credit_amount` > 0. Default: 0.
          credit_amount (int | Unset): Credit amount in cents. Must be 0 if `debit_amount` > 0. Default: 0.
          description (None | str | Unset): Per-line memo (overrides the entry-level memo on this line).
          metadata (JournalEntryLineItemInputMetadataType0 | None | Unset): Optional per-line metadata stamped on
              ``LineItem.metadata_``. Used to carry source-system fields the standard columns don't cover — e.g. an external
              flow-tag code that drives rollforward attribution (``transaction_description_code``), an external memo, or a
              cost-center hint. Pass-through is non-validating; the renderer / filter engine reads keys it knows about and
              ignores the rest. ``None`` is normalized to ``{}`` at persist time.
  """

  element_id: str
  debit_amount: int | Unset = 0
  credit_amount: int | Unset = 0
  description: None | str | Unset = UNSET
  metadata: JournalEntryLineItemInputMetadataType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.journal_entry_line_item_input_metadata_type_0 import (
      JournalEntryLineItemInputMetadataType0,
    )

    element_id = self.element_id

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    metadata: dict[str, Any] | None | Unset
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, JournalEntryLineItemInputMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
      }
    )
    if debit_amount is not UNSET:
      field_dict["debit_amount"] = debit_amount
    if credit_amount is not UNSET:
      field_dict["credit_amount"] = credit_amount
    if description is not UNSET:
      field_dict["description"] = description
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.journal_entry_line_item_input_metadata_type_0 import (
      JournalEntryLineItemInputMetadataType0,
    )

    d = dict(src_dict)
    element_id = d.pop("element_id")

    debit_amount = d.pop("debit_amount", UNSET)

    credit_amount = d.pop("credit_amount", UNSET)

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_metadata(
      data: object,
    ) -> JournalEntryLineItemInputMetadataType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = JournalEntryLineItemInputMetadataType0.from_dict(data)

        return metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(JournalEntryLineItemInputMetadataType0 | None | Unset, data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    journal_entry_line_item_input = cls(
      element_id=element_id,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      description=description,
      metadata=metadata,
    )

    journal_entry_line_item_input.additional_properties = d
    return journal_entry_line_item_input

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
