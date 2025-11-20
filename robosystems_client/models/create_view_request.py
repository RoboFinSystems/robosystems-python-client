from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.view_config import ViewConfig
  from ..models.view_source import ViewSource


T = TypeVar("T", bound="CreateViewRequest")


@_attrs_define
class CreateViewRequest:
  """
  Attributes:
      source (ViewSource):
      name (None | str | Unset): Optional name for the view
      view_config (ViewConfig | Unset):
      presentation_formats (list[str] | Unset): Presentation formats to generate
      mapping_structure_id (None | str | Unset): Optional mapping structure ID to aggregate Chart of Accounts elements
          into reporting taxonomy elements
  """

  source: ViewSource
  name: None | str | Unset = UNSET
  view_config: ViewConfig | Unset = UNSET
  presentation_formats: list[str] | Unset = UNSET
  mapping_structure_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    source = self.source.to_dict()

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    view_config: dict[str, Any] | Unset = UNSET
    if not isinstance(self.view_config, Unset):
      view_config = self.view_config.to_dict()

    presentation_formats: list[str] | Unset = UNSET
    if not isinstance(self.presentation_formats, Unset):
      presentation_formats = self.presentation_formats

    mapping_structure_id: None | str | Unset
    if isinstance(self.mapping_structure_id, Unset):
      mapping_structure_id = UNSET
    else:
      mapping_structure_id = self.mapping_structure_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "source": source,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if view_config is not UNSET:
      field_dict["view_config"] = view_config
    if presentation_formats is not UNSET:
      field_dict["presentation_formats"] = presentation_formats
    if mapping_structure_id is not UNSET:
      field_dict["mapping_structure_id"] = mapping_structure_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.view_config import ViewConfig
    from ..models.view_source import ViewSource

    d = dict(src_dict)
    source = ViewSource.from_dict(d.pop("source"))

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    _view_config = d.pop("view_config", UNSET)
    view_config: ViewConfig | Unset
    if isinstance(_view_config, Unset):
      view_config = UNSET
    else:
      view_config = ViewConfig.from_dict(_view_config)

    presentation_formats = cast(list[str], d.pop("presentation_formats", UNSET))

    def _parse_mapping_structure_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    mapping_structure_id = _parse_mapping_structure_id(
      d.pop("mapping_structure_id", UNSET)
    )

    create_view_request = cls(
      source=source,
      name=name,
      view_config=view_config,
      presentation_formats=presentation_formats,
      mapping_structure_id=mapping_structure_id,
    )

    create_view_request.additional_properties = d
    return create_view_request

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
