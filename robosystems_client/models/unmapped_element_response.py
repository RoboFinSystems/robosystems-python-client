from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.suggested_target import SuggestedTarget


T = TypeVar("T", bound="UnmappedElementResponse")


@_attrs_define
class UnmappedElementResponse:
  """An element not yet mapped to the reporting taxonomy.

  Attributes:
      id (str):
      name (str):
      classification (str):
      balance_type (str):
      code (None | str | Unset):
      external_source (None | str | Unset):
      suggested_targets (list[SuggestedTarget] | Unset):
  """

  id: str
  name: str
  classification: str
  balance_type: str
  code: None | str | Unset = UNSET
  external_source: None | str | Unset = UNSET
  suggested_targets: list[SuggestedTarget] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    classification = self.classification

    balance_type = self.balance_type

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    external_source: None | str | Unset
    if isinstance(self.external_source, Unset):
      external_source = UNSET
    else:
      external_source = self.external_source

    suggested_targets: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.suggested_targets, Unset):
      suggested_targets = []
      for suggested_targets_item_data in self.suggested_targets:
        suggested_targets_item = suggested_targets_item_data.to_dict()
        suggested_targets.append(suggested_targets_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "classification": classification,
        "balance_type": balance_type,
      }
    )
    if code is not UNSET:
      field_dict["code"] = code
    if external_source is not UNSET:
      field_dict["external_source"] = external_source
    if suggested_targets is not UNSET:
      field_dict["suggested_targets"] = suggested_targets

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.suggested_target import SuggestedTarget

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    classification = d.pop("classification")

    balance_type = d.pop("balance_type")

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    def _parse_external_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_source = _parse_external_source(d.pop("external_source", UNSET))

    _suggested_targets = d.pop("suggested_targets", UNSET)
    suggested_targets: list[SuggestedTarget] | Unset = UNSET
    if _suggested_targets is not UNSET:
      suggested_targets = []
      for suggested_targets_item_data in _suggested_targets:
        suggested_targets_item = SuggestedTarget.from_dict(suggested_targets_item_data)

        suggested_targets.append(suggested_targets_item)

    unmapped_element_response = cls(
      id=id,
      name=name,
      classification=classification,
      balance_type=balance_type,
      code=code,
      external_source=external_source,
      suggested_targets=suggested_targets,
    )

    unmapped_element_response.additional_properties = d
    return unmapped_element_response

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
