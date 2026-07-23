from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.structure_update_patch_concept_arrangement_type_0 import (
  StructureUpdatePatchConceptArrangementType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.structure_update_patch_metadata_type_0 import (
    StructureUpdatePatchMetadataType0,
  )


T = TypeVar("T", bound="StructureUpdatePatch")


@_attrs_define
class StructureUpdatePatch:
  """Partial-update patch for a single structure, keyed by structure_id.

  ``concept_arrangement`` makes a mis-CAP'd structure repairable in
  place (e.g. promoting a ``set`` note to ``roll_up`` so it gains a
  footing rule); ``block_type`` stays immutable — it drives block-type
  routing, so changing it is a re-create, not an edit.

      Attributes:
          structure_id (str): Structure id to update.
          name (None | str | Unset):
          description (None | str | Unset):
          role_uri (None | str | Unset):
          concept_arrangement (None | StructureUpdatePatchConceptArrangementType0 | Unset):
          metadata (None | StructureUpdatePatchMetadataType0 | Unset):
  """

  structure_id: str
  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  role_uri: None | str | Unset = UNSET
  concept_arrangement: None | StructureUpdatePatchConceptArrangementType0 | Unset = (
    UNSET
  )
  metadata: None | StructureUpdatePatchMetadataType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.structure_update_patch_metadata_type_0 import (
      StructureUpdatePatchMetadataType0,
    )

    structure_id = self.structure_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    role_uri: None | str | Unset
    if isinstance(self.role_uri, Unset):
      role_uri = UNSET
    else:
      role_uri = self.role_uri

    concept_arrangement: None | str | Unset
    if isinstance(self.concept_arrangement, Unset):
      concept_arrangement = UNSET
    elif isinstance(
      self.concept_arrangement, StructureUpdatePatchConceptArrangementType0
    ):
      concept_arrangement = self.concept_arrangement.value
    else:
      concept_arrangement = self.concept_arrangement

    metadata: dict[str, Any] | None | Unset
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, StructureUpdatePatchMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if description is not UNSET:
      field_dict["description"] = description
    if role_uri is not UNSET:
      field_dict["role_uri"] = role_uri
    if concept_arrangement is not UNSET:
      field_dict["concept_arrangement"] = concept_arrangement
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.structure_update_patch_metadata_type_0 import (
      StructureUpdatePatchMetadataType0,
    )

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_role_uri(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    role_uri = _parse_role_uri(d.pop("role_uri", UNSET))

    def _parse_concept_arrangement(
      data: object,
    ) -> None | StructureUpdatePatchConceptArrangementType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        concept_arrangement_type_0 = StructureUpdatePatchConceptArrangementType0(data)

        return concept_arrangement_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | StructureUpdatePatchConceptArrangementType0 | Unset, data)

    concept_arrangement = _parse_concept_arrangement(
      d.pop("concept_arrangement", UNSET)
    )

    def _parse_metadata(
      data: object,
    ) -> None | StructureUpdatePatchMetadataType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = StructureUpdatePatchMetadataType0.from_dict(data)

        return metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | StructureUpdatePatchMetadataType0 | Unset, data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    structure_update_patch = cls(
      structure_id=structure_id,
      name=name,
      description=description,
      role_uri=role_uri,
      concept_arrangement=concept_arrangement,
      metadata=metadata,
    )

    structure_update_patch.additional_properties = d
    return structure_update_patch

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
