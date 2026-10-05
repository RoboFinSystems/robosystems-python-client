from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.filing_links_exhibits_type_0 import FilingLinksExhibitsType0


T = TypeVar("T", bound="FilingLinks")


@_attrs_define
class FilingLinks:
  """Where a filing on a shared repository is served.

  Attributes:
      viewer (None | str | Unset): The xbrlkit viewer over the published holon — the link to show the filing
      holon (None | str | Unset):
      tavi (None | str | Unset):
      as_filed (None | str | Unset): The primary document as filed
      exhibits (FilingLinksExhibitsType0 | None | Unset): An 8-K's exhibits by exhibit number (EX-99.1)
      manifest (None | str | Unset): Every file in the filing's public folder, with its URL
      edgar (None | str | Unset): The filing's folder on EDGAR
  """

  viewer: None | str | Unset = UNSET
  holon: None | str | Unset = UNSET
  tavi: None | str | Unset = UNSET
  as_filed: None | str | Unset = UNSET
  exhibits: FilingLinksExhibitsType0 | None | Unset = UNSET
  manifest: None | str | Unset = UNSET
  edgar: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.filing_links_exhibits_type_0 import FilingLinksExhibitsType0

    viewer: None | str | Unset
    if isinstance(self.viewer, Unset):
      viewer = UNSET
    else:
      viewer = self.viewer

    holon: None | str | Unset
    if isinstance(self.holon, Unset):
      holon = UNSET
    else:
      holon = self.holon

    tavi: None | str | Unset
    if isinstance(self.tavi, Unset):
      tavi = UNSET
    else:
      tavi = self.tavi

    as_filed: None | str | Unset
    if isinstance(self.as_filed, Unset):
      as_filed = UNSET
    else:
      as_filed = self.as_filed

    exhibits: dict[str, Any] | None | Unset
    if isinstance(self.exhibits, Unset):
      exhibits = UNSET
    elif isinstance(self.exhibits, FilingLinksExhibitsType0):
      exhibits = self.exhibits.to_dict()
    else:
      exhibits = self.exhibits

    manifest: None | str | Unset
    if isinstance(self.manifest, Unset):
      manifest = UNSET
    else:
      manifest = self.manifest

    edgar: None | str | Unset
    if isinstance(self.edgar, Unset):
      edgar = UNSET
    else:
      edgar = self.edgar

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if viewer is not UNSET:
      field_dict["viewer"] = viewer
    if holon is not UNSET:
      field_dict["holon"] = holon
    if tavi is not UNSET:
      field_dict["tavi"] = tavi
    if as_filed is not UNSET:
      field_dict["as_filed"] = as_filed
    if exhibits is not UNSET:
      field_dict["exhibits"] = exhibits
    if manifest is not UNSET:
      field_dict["manifest"] = manifest
    if edgar is not UNSET:
      field_dict["edgar"] = edgar

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.filing_links_exhibits_type_0 import FilingLinksExhibitsType0

    d = dict(src_dict)

    def _parse_viewer(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    viewer = _parse_viewer(d.pop("viewer", UNSET))

    def _parse_holon(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    holon = _parse_holon(d.pop("holon", UNSET))

    def _parse_tavi(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    tavi = _parse_tavi(d.pop("tavi", UNSET))

    def _parse_as_filed(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    as_filed = _parse_as_filed(d.pop("as_filed", UNSET))

    def _parse_exhibits(data: object) -> FilingLinksExhibitsType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        exhibits_type_0 = FilingLinksExhibitsType0.from_dict(data)

        return exhibits_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(FilingLinksExhibitsType0 | None | Unset, data)

    exhibits = _parse_exhibits(d.pop("exhibits", UNSET))

    def _parse_manifest(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    manifest = _parse_manifest(d.pop("manifest", UNSET))

    def _parse_edgar(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    edgar = _parse_edgar(d.pop("edgar", UNSET))

    filing_links = cls(
      viewer=viewer,
      holon=holon,
      tavi=tavi,
      as_filed=as_filed,
      exhibits=exhibits,
      manifest=manifest,
      edgar=edgar,
    )

    filing_links.additional_properties = d
    return filing_links

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
