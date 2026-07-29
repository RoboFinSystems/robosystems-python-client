from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.view_metadata import ViewMetadata
  from ..models.view_response_presentations import ViewResponsePresentations


T = TypeVar("T", bound="ViewResponse")


@_attrs_define
class ViewResponse:
  """
  Attributes:
      metadata (ViewMetadata):
      presentations (ViewResponsePresentations): Presentation formats (pivot_table, narrative, etc.)
  """

  metadata: ViewMetadata
  presentations: ViewResponsePresentations
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    metadata = self.metadata.to_dict()

    presentations = self.presentations.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "metadata": metadata,
        "presentations": presentations,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.view_metadata import ViewMetadata
    from ..models.view_response_presentations import ViewResponsePresentations

    d = dict(src_dict)
    metadata = ViewMetadata.from_dict(d.pop("metadata"))

    presentations = ViewResponsePresentations.from_dict(d.pop("presentations"))

    view_response = cls(
      metadata=metadata,
      presentations=presentations,
    )

    view_response.additional_properties = d
    return view_response

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
