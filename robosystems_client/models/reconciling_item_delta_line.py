from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcilingItemDeltaLine")


@_attrs_define
class ReconcilingItemDeltaLine:
  """One account's net change between the posted entries and the new payload.

  Amounts are signed minor units in debit-positive convention: a positive
  figure is a net debit, a negative one a net credit. ``delta`` is what a
  catch-up entry would post to bring the books level.

      Attributes:
          prior_net (int): Net of the posted entries, debit-positive
          accepted_net (int): Net of the new payload, debit-positive
          delta (int): accepted_net - prior_net
          element_id (None | str | Unset): CoA element id; null when the account is unmapped
          element_external_id (None | str | Unset): Source-system account id, when the line carried one
          element_code (None | str | Unset): Account code
          element_name (None | str | Unset): Account name
  """

  prior_net: int
  accepted_net: int
  delta: int
  element_id: None | str | Unset = UNSET
  element_external_id: None | str | Unset = UNSET
  element_code: None | str | Unset = UNSET
  element_name: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    prior_net = self.prior_net

    accepted_net = self.accepted_net

    delta = self.delta

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    element_external_id: None | str | Unset
    if isinstance(self.element_external_id, Unset):
      element_external_id = UNSET
    else:
      element_external_id = self.element_external_id

    element_code: None | str | Unset
    if isinstance(self.element_code, Unset):
      element_code = UNSET
    else:
      element_code = self.element_code

    element_name: None | str | Unset
    if isinstance(self.element_name, Unset):
      element_name = UNSET
    else:
      element_name = self.element_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "prior_net": prior_net,
        "accepted_net": accepted_net,
        "delta": delta,
      }
    )
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
    if element_external_id is not UNSET:
      field_dict["element_external_id"] = element_external_id
    if element_code is not UNSET:
      field_dict["element_code"] = element_code
    if element_name is not UNSET:
      field_dict["element_name"] = element_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    prior_net = d.pop("prior_net")

    accepted_net = d.pop("accepted_net")

    delta = d.pop("delta")

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    def _parse_element_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_external_id = _parse_element_external_id(
      d.pop("element_external_id", UNSET)
    )

    def _parse_element_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_code = _parse_element_code(d.pop("element_code", UNSET))

    def _parse_element_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_name = _parse_element_name(d.pop("element_name", UNSET))

    reconciling_item_delta_line = cls(
      prior_net=prior_net,
      accepted_net=accepted_net,
      delta=delta,
      element_id=element_id,
      element_external_id=element_external_id,
      element_code=element_code,
      element_name=element_name,
    )

    reconciling_item_delta_line.additional_properties = d
    return reconciling_item_delta_line

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
