from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_agent_request_address_type_0 import (
    CreateAgentRequestAddressType0,
  )
  from ..models.create_agent_request_metadata import CreateAgentRequestMetadata


T = TypeVar("T", bound="CreateAgentRequest")


@_attrs_define
class CreateAgentRequest:
  """
  Attributes:
      agent_type (str): 'customer' | 'vendor' | 'employee' | 'owner' | 'supplier' | 'government' | 'lender' | 'self' |
          'other'
      name (str):
      legal_name (None | str | Unset):
      tax_id (None | str | Unset):
      registration_number (None | str | Unset):
      duns (None | str | Unset):
      lei (None | str | Unset):
      email (None | str | Unset):
      phone (None | str | Unset):
      address (CreateAgentRequestAddressType0 | None | Unset):
      source (str | Unset): 'quickbooks' | 'xero' | 'plaid' | 'native' Default: 'native'.
      external_id (None | str | Unset):
      is_active (bool | Unset):  Default: True.
      is_1099_recipient (bool | Unset):  Default: False.
      metadata (CreateAgentRequestMetadata | Unset):
  """

  agent_type: str
  name: str
  legal_name: None | str | Unset = UNSET
  tax_id: None | str | Unset = UNSET
  registration_number: None | str | Unset = UNSET
  duns: None | str | Unset = UNSET
  lei: None | str | Unset = UNSET
  email: None | str | Unset = UNSET
  phone: None | str | Unset = UNSET
  address: CreateAgentRequestAddressType0 | None | Unset = UNSET
  source: str | Unset = "native"
  external_id: None | str | Unset = UNSET
  is_active: bool | Unset = True
  is_1099_recipient: bool | Unset = False
  metadata: CreateAgentRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.create_agent_request_address_type_0 import (
      CreateAgentRequestAddressType0,
    )

    agent_type = self.agent_type

    name = self.name

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
    elif isinstance(self.address, CreateAgentRequestAddressType0):
      address = self.address.to_dict()
    else:
      address = self.address

    source = self.source

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    is_active = self.is_active

    is_1099_recipient = self.is_1099_recipient

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "agent_type": agent_type,
        "name": name,
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
    if source is not UNSET:
      field_dict["source"] = source
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if is_active is not UNSET:
      field_dict["is_active"] = is_active
    if is_1099_recipient is not UNSET:
      field_dict["is_1099_recipient"] = is_1099_recipient
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_agent_request_address_type_0 import (
      CreateAgentRequestAddressType0,
    )
    from ..models.create_agent_request_metadata import CreateAgentRequestMetadata

    d = dict(src_dict)
    agent_type = d.pop("agent_type")

    name = d.pop("name")

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

    def _parse_address(data: object) -> CreateAgentRequestAddressType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        address_type_0 = CreateAgentRequestAddressType0.from_dict(data)

        return address_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(CreateAgentRequestAddressType0 | None | Unset, data)

    address = _parse_address(d.pop("address", UNSET))

    source = d.pop("source", UNSET)

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    is_active = d.pop("is_active", UNSET)

    is_1099_recipient = d.pop("is_1099_recipient", UNSET)

    _metadata = d.pop("metadata", UNSET)
    metadata: CreateAgentRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = CreateAgentRequestMetadata.from_dict(_metadata)

    create_agent_request = cls(
      agent_type=agent_type,
      name=name,
      legal_name=legal_name,
      tax_id=tax_id,
      registration_number=registration_number,
      duns=duns,
      lei=lei,
      email=email,
      phone=phone,
      address=address,
      source=source,
      external_id=external_id,
      is_active=is_active,
      is_1099_recipient=is_1099_recipient,
      metadata=metadata,
    )

    create_agent_request.additional_properties = d
    return create_agent_request

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
