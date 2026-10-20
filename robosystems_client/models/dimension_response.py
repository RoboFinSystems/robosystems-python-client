from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DimensionResponse")


@_attrs_define
class DimensionResponse:
  """One member of a management dimension.

  Attributes:
      id (str): The member's id, as lines carry it.
      dimension_type (str): The axis: department, class, location, project, or another.
      name (str): The member's label.
      value (str): The member's stable key within its axis: the source's id for a synced member, a slug of the name
          for one created here.
      is_active (bool): False once retired: the member stays on the lines that carry it and can no longer be put on
          new ones.
      source (str | Unset): Where the member came from: `native` or `quickbooks`. Default: 'native'.
      line_count (int | Unset): How many ledger lines carry the member. Default: 0.
      created_at (datetime.datetime | None | Unset): When it was created.
  """

  id: str
  dimension_type: str
  name: str
  value: str
  is_active: bool
  source: str | Unset = "native"
  line_count: int | Unset = 0
  created_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    dimension_type = self.dimension_type

    name = self.name

    value = self.value

    is_active = self.is_active

    source = self.source

    line_count = self.line_count

    created_at: None | str | Unset
    if isinstance(self.created_at, Unset):
      created_at = UNSET
    elif isinstance(self.created_at, datetime.datetime):
      created_at = self.created_at.isoformat()
    else:
      created_at = self.created_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "dimension_type": dimension_type,
        "name": name,
        "value": value,
        "is_active": is_active,
      }
    )
    if source is not UNSET:
      field_dict["source"] = source
    if line_count is not UNSET:
      field_dict["line_count"] = line_count
    if created_at is not UNSET:
      field_dict["created_at"] = created_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    dimension_type = d.pop("dimension_type")

    name = d.pop("name")

    value = d.pop("value")

    is_active = d.pop("is_active")

    source = d.pop("source", UNSET)

    line_count = d.pop("line_count", UNSET)

    def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        created_at_type_0 = datetime.datetime.fromisoformat(data)

        return created_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    created_at = _parse_created_at(d.pop("created_at", UNSET))

    dimension_response = cls(
      id=id,
      dimension_type=dimension_type,
      name=name,
      value=value,
      is_active=is_active,
      source=source,
      line_count=line_count,
      created_at=created_at,
    )

    dimension_response.additional_properties = d
    return dimension_response

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
