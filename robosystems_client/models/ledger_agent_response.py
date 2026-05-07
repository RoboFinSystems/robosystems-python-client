from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ledger_agent_response_address_type_0 import (
    LedgerAgentResponseAddressType0,
  )


T = TypeVar("T", bound="LedgerAgentResponse")


@_attrs_define
class LedgerAgentResponse:
  """
  Attributes:
      id (str):
      agent_type (str):
      name (str):
      source (str):
      is_active (bool):
      is_1099_recipient (bool):
      legal_name (None | str | Unset):
      tax_id (None | str | Unset):
      registration_number (None | str | Unset):
      duns (None | str | Unset):
      lei (None | str | Unset):
      email (None | str | Unset):
      phone (None | str | Unset):
      address (LedgerAgentResponseAddressType0 | None | Unset):
      external_id (None | str | Unset):
      created_at (datetime.datetime | None | Unset):
      updated_at (datetime.datetime | None | Unset):
      created_by (None | str | Unset):
  """

  id: str
  agent_type: str
  name: str
  source: str
  is_active: bool
  is_1099_recipient: bool
  legal_name: None | str | Unset = UNSET
  tax_id: None | str | Unset = UNSET
  registration_number: None | str | Unset = UNSET
  duns: None | str | Unset = UNSET
  lei: None | str | Unset = UNSET
  email: None | str | Unset = UNSET
  phone: None | str | Unset = UNSET
  address: LedgerAgentResponseAddressType0 | None | Unset = UNSET
  external_id: None | str | Unset = UNSET
  created_at: datetime.datetime | None | Unset = UNSET
  updated_at: datetime.datetime | None | Unset = UNSET
  created_by: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.ledger_agent_response_address_type_0 import (
      LedgerAgentResponseAddressType0,
    )

    id = self.id

    agent_type = self.agent_type

    name = self.name

    source = self.source

    is_active = self.is_active

    is_1099_recipient = self.is_1099_recipient

    legal_name: None | str | Unset
    if isinstance(self.legal_name, Unset):
      legal_name = UNSET
    else:
      legal_name = self.legal_name

    tax_id: None | str | Unset
    if isinstance(self.tax_id, Unset):
      tax_id = UNSET
    else:
      tax_id = self.tax_id

    registration_number: None | str | Unset
    if isinstance(self.registration_number, Unset):
      registration_number = UNSET
    else:
      registration_number = self.registration_number

    duns: None | str | Unset
    if isinstance(self.duns, Unset):
      duns = UNSET
    else:
      duns = self.duns

    lei: None | str | Unset
    if isinstance(self.lei, Unset):
      lei = UNSET
    else:
      lei = self.lei

    email: None | str | Unset
    if isinstance(self.email, Unset):
      email = UNSET
    else:
      email = self.email

    phone: None | str | Unset
    if isinstance(self.phone, Unset):
      phone = UNSET
    else:
      phone = self.phone

    address: dict[str, Any] | None | Unset
    if isinstance(self.address, Unset):
      address = UNSET
    elif isinstance(self.address, LedgerAgentResponseAddressType0):
      address = self.address.to_dict()
    else:
      address = self.address

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

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
        "agent_type": agent_type,
        "name": name,
        "source": source,
        "is_active": is_active,
        "is_1099_recipient": is_1099_recipient,
      }
    )
    if legal_name is not UNSET:
      field_dict["legal_name"] = legal_name
    if tax_id is not UNSET:
      field_dict["tax_id"] = tax_id
    if registration_number is not UNSET:
      field_dict["registration_number"] = registration_number
    if duns is not UNSET:
      field_dict["duns"] = duns
    if lei is not UNSET:
      field_dict["lei"] = lei
    if email is not UNSET:
      field_dict["email"] = email
    if phone is not UNSET:
      field_dict["phone"] = phone
    if address is not UNSET:
      field_dict["address"] = address
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if created_at is not UNSET:
      field_dict["created_at"] = created_at
    if updated_at is not UNSET:
      field_dict["updated_at"] = updated_at
    if created_by is not UNSET:
      field_dict["created_by"] = created_by

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.ledger_agent_response_address_type_0 import (
      LedgerAgentResponseAddressType0,
    )

    d = dict(src_dict)
    id = d.pop("id")

    agent_type = d.pop("agent_type")

    name = d.pop("name")

    source = d.pop("source")

    is_active = d.pop("is_active")

    is_1099_recipient = d.pop("is_1099_recipient")

    def _parse_legal_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

    def _parse_tax_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    tax_id = _parse_tax_id(d.pop("tax_id", UNSET))

    def _parse_registration_number(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    registration_number = _parse_registration_number(
      d.pop("registration_number", UNSET)
    )

    def _parse_duns(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    duns = _parse_duns(d.pop("duns", UNSET))

    def _parse_lei(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    lei = _parse_lei(d.pop("lei", UNSET))

    def _parse_email(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    email = _parse_email(d.pop("email", UNSET))

    def _parse_phone(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    phone = _parse_phone(d.pop("phone", UNSET))

    def _parse_address(data: object) -> LedgerAgentResponseAddressType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        address_type_0 = LedgerAgentResponseAddressType0.from_dict(data)

        return address_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(LedgerAgentResponseAddressType0 | None | Unset, data)

    address = _parse_address(d.pop("address", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

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

    ledger_agent_response = cls(
      id=id,
      agent_type=agent_type,
      name=name,
      source=source,
      is_active=is_active,
      is_1099_recipient=is_1099_recipient,
      legal_name=legal_name,
      tax_id=tax_id,
      registration_number=registration_number,
      duns=duns,
      lei=lei,
      email=email,
      phone=phone,
      address=address,
      external_id=external_id,
      created_at=created_at,
      updated_at=updated_at,
      created_by=created_by,
    )

    ledger_agent_response.additional_properties = d
    return ledger_agent_response

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
