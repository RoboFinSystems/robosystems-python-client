from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_agent_request_address_type_0 import (
    UpdateAgentRequestAddressType0,
  )
  from ..models.update_agent_request_metadata_patch import (
    UpdateAgentRequestMetadataPatch,
  )


T = TypeVar("T", bound="UpdateAgentRequest")


@_attrs_define
class UpdateAgentRequest:
  """
  Attributes:
      agent_id (str):
      name (None | str | Unset):
      legal_name (None | str | Unset):
      tax_id (None | str | Unset):
      registration_number (None | str | Unset):
      duns (None | str | Unset):
      lei (None | str | Unset):
      email (None | str | Unset):
      phone (None | str | Unset):
      address (None | Unset | UpdateAgentRequestAddressType0):
      is_active (bool | None | Unset):
      is_1099_recipient (bool | None | Unset):
      metadata_patch (UpdateAgentRequestMetadataPatch | Unset):
  """

  agent_id: str
  name: None | str | Unset = UNSET
  legal_name: None | str | Unset = UNSET
  tax_id: None | str | Unset = UNSET
  registration_number: None | str | Unset = UNSET
  duns: None | str | Unset = UNSET
  lei: None | str | Unset = UNSET
  email: None | str | Unset = UNSET
  phone: None | str | Unset = UNSET
  address: None | Unset | UpdateAgentRequestAddressType0 = UNSET
  is_active: bool | None | Unset = UNSET
  is_1099_recipient: bool | None | Unset = UNSET
  metadata_patch: UpdateAgentRequestMetadataPatch | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.update_agent_request_address_type_0 import (
      UpdateAgentRequestAddressType0,
    )

    agent_id = self.agent_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
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
    elif isinstance(self.address, UpdateAgentRequestAddressType0):
      address = self.address.to_dict()
    else:
      address = self.address

    is_active: bool | None | Unset
    if isinstance(self.is_active, Unset):
      is_active = UNSET
    else:
      is_active = self.is_active

    is_1099_recipient: bool | None | Unset
    if isinstance(self.is_1099_recipient, Unset):
      is_1099_recipient = UNSET
    else:
      is_1099_recipient = self.is_1099_recipient

    metadata_patch: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata_patch, Unset):
      metadata_patch = self.metadata_patch.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "agent_id": agent_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
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
    if is_active is not UNSET:
      field_dict["is_active"] = is_active
    if is_1099_recipient is not UNSET:
      field_dict["is_1099_recipient"] = is_1099_recipient
    if metadata_patch is not UNSET:
      field_dict["metadata_patch"] = metadata_patch

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.update_agent_request_address_type_0 import (
      UpdateAgentRequestAddressType0,
    )
    from ..models.update_agent_request_metadata_patch import (
      UpdateAgentRequestMetadataPatch,
    )

    d = dict(src_dict)
    agent_id = d.pop("agent_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

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

    def _parse_address(data: object) -> None | Unset | UpdateAgentRequestAddressType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        address_type_0 = UpdateAgentRequestAddressType0.from_dict(data)

        return address_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateAgentRequestAddressType0, data)

    address = _parse_address(d.pop("address", UNSET))

    def _parse_is_active(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    is_active = _parse_is_active(d.pop("is_active", UNSET))

    def _parse_is_1099_recipient(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    is_1099_recipient = _parse_is_1099_recipient(d.pop("is_1099_recipient", UNSET))

    _metadata_patch = d.pop("metadata_patch", UNSET)
    metadata_patch: UpdateAgentRequestMetadataPatch | Unset
    if isinstance(_metadata_patch, Unset):
      metadata_patch = UNSET
    else:
      metadata_patch = UpdateAgentRequestMetadataPatch.from_dict(_metadata_patch)

    update_agent_request = cls(
      agent_id=agent_id,
      name=name,
      legal_name=legal_name,
      tax_id=tax_id,
      registration_number=registration_number,
      duns=duns,
      lei=lei,
      email=email,
      phone=phone,
      address=address,
      is_active=is_active,
      is_1099_recipient=is_1099_recipient,
      metadata_patch=metadata_patch,
    )

    update_agent_request.additional_properties = d
    return update_agent_request

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
