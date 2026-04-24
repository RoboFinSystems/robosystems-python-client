from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.element_update_patch import ElementUpdatePatch
  from ..models.structure_update_patch import StructureUpdatePatch
  from ..models.taxonomy_block_association_request import (
    TaxonomyBlockAssociationRequest,
  )
  from ..models.taxonomy_block_element_request import TaxonomyBlockElementRequest
  from ..models.taxonomy_block_rule_request import TaxonomyBlockRuleRequest
  from ..models.taxonomy_block_structure_request import TaxonomyBlockStructureRequest


T = TypeVar("T", bound="UpdateTaxonomyBlockRequest")


@_attrs_define
class UpdateTaxonomyBlockRequest:
  """Request body for the ``update-taxonomy-block`` operation.

  Top-level fields (name / description / version) apply to the taxonomy
  row itself. The delta lists mutate atoms incrementally — the validator
  (Phase 2.3) re-runs the seven-phase check across the projected post-
  update state before anything commits.

      Attributes:
          taxonomy_id (str):
          name (None | str | Unset):
          description (None | str | Unset):
          version (None | str | Unset):
          elements_to_add (list[TaxonomyBlockElementRequest] | Unset):
          elements_to_update (list[ElementUpdatePatch] | Unset):
          elements_to_remove (list[str] | Unset): qnames of elements to remove.
          structures_to_add (list[TaxonomyBlockStructureRequest] | Unset):
          structures_to_update (list[StructureUpdatePatch] | Unset):
          structures_to_remove (list[str] | Unset): Structure ids to remove.
          associations_to_add (list[TaxonomyBlockAssociationRequest] | Unset):
          associations_to_remove (list[str] | Unset): Association ids to remove.
          rules_to_add (list[TaxonomyBlockRuleRequest] | Unset):
          rules_to_remove (list[str] | Unset): Rule ids to remove.
  """

  taxonomy_id: str
  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  version: None | str | Unset = UNSET
  elements_to_add: list[TaxonomyBlockElementRequest] | Unset = UNSET
  elements_to_update: list[ElementUpdatePatch] | Unset = UNSET
  elements_to_remove: list[str] | Unset = UNSET
  structures_to_add: list[TaxonomyBlockStructureRequest] | Unset = UNSET
  structures_to_update: list[StructureUpdatePatch] | Unset = UNSET
  structures_to_remove: list[str] | Unset = UNSET
  associations_to_add: list[TaxonomyBlockAssociationRequest] | Unset = UNSET
  associations_to_remove: list[str] | Unset = UNSET
  rules_to_add: list[TaxonomyBlockRuleRequest] | Unset = UNSET
  rules_to_remove: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

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

    version: None | str | Unset
    if isinstance(self.version, Unset):
      version = UNSET
    else:
      version = self.version

    elements_to_add: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.elements_to_add, Unset):
      elements_to_add = []
      for elements_to_add_item_data in self.elements_to_add:
        elements_to_add_item = elements_to_add_item_data.to_dict()
        elements_to_add.append(elements_to_add_item)

    elements_to_update: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.elements_to_update, Unset):
      elements_to_update = []
      for elements_to_update_item_data in self.elements_to_update:
        elements_to_update_item = elements_to_update_item_data.to_dict()
        elements_to_update.append(elements_to_update_item)

    elements_to_remove: list[str] | Unset = UNSET
    if not isinstance(self.elements_to_remove, Unset):
      elements_to_remove = self.elements_to_remove

    structures_to_add: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.structures_to_add, Unset):
      structures_to_add = []
      for structures_to_add_item_data in self.structures_to_add:
        structures_to_add_item = structures_to_add_item_data.to_dict()
        structures_to_add.append(structures_to_add_item)

    structures_to_update: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.structures_to_update, Unset):
      structures_to_update = []
      for structures_to_update_item_data in self.structures_to_update:
        structures_to_update_item = structures_to_update_item_data.to_dict()
        structures_to_update.append(structures_to_update_item)

    structures_to_remove: list[str] | Unset = UNSET
    if not isinstance(self.structures_to_remove, Unset):
      structures_to_remove = self.structures_to_remove

    associations_to_add: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.associations_to_add, Unset):
      associations_to_add = []
      for associations_to_add_item_data in self.associations_to_add:
        associations_to_add_item = associations_to_add_item_data.to_dict()
        associations_to_add.append(associations_to_add_item)

    associations_to_remove: list[str] | Unset = UNSET
    if not isinstance(self.associations_to_remove, Unset):
      associations_to_remove = self.associations_to_remove

    rules_to_add: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rules_to_add, Unset):
      rules_to_add = []
      for rules_to_add_item_data in self.rules_to_add:
        rules_to_add_item = rules_to_add_item_data.to_dict()
        rules_to_add.append(rules_to_add_item)

    rules_to_remove: list[str] | Unset = UNSET
    if not isinstance(self.rules_to_remove, Unset):
      rules_to_remove = self.rules_to_remove

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "taxonomy_id": taxonomy_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if description is not UNSET:
      field_dict["description"] = description
    if version is not UNSET:
      field_dict["version"] = version
    if elements_to_add is not UNSET:
      field_dict["elements_to_add"] = elements_to_add
    if elements_to_update is not UNSET:
      field_dict["elements_to_update"] = elements_to_update
    if elements_to_remove is not UNSET:
      field_dict["elements_to_remove"] = elements_to_remove
    if structures_to_add is not UNSET:
      field_dict["structures_to_add"] = structures_to_add
    if structures_to_update is not UNSET:
      field_dict["structures_to_update"] = structures_to_update
    if structures_to_remove is not UNSET:
      field_dict["structures_to_remove"] = structures_to_remove
    if associations_to_add is not UNSET:
      field_dict["associations_to_add"] = associations_to_add
    if associations_to_remove is not UNSET:
      field_dict["associations_to_remove"] = associations_to_remove
    if rules_to_add is not UNSET:
      field_dict["rules_to_add"] = rules_to_add
    if rules_to_remove is not UNSET:
      field_dict["rules_to_remove"] = rules_to_remove

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.element_update_patch import ElementUpdatePatch
    from ..models.structure_update_patch import StructureUpdatePatch
    from ..models.taxonomy_block_association_request import (
      TaxonomyBlockAssociationRequest,
    )
    from ..models.taxonomy_block_element_request import TaxonomyBlockElementRequest
    from ..models.taxonomy_block_rule_request import TaxonomyBlockRuleRequest
    from ..models.taxonomy_block_structure_request import TaxonomyBlockStructureRequest

    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

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

    def _parse_version(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    version = _parse_version(d.pop("version", UNSET))

    _elements_to_add = d.pop("elements_to_add", UNSET)
    elements_to_add: list[TaxonomyBlockElementRequest] | Unset = UNSET
    if _elements_to_add is not UNSET:
      elements_to_add = []
      for elements_to_add_item_data in _elements_to_add:
        elements_to_add_item = TaxonomyBlockElementRequest.from_dict(
          elements_to_add_item_data
        )

        elements_to_add.append(elements_to_add_item)

    _elements_to_update = d.pop("elements_to_update", UNSET)
    elements_to_update: list[ElementUpdatePatch] | Unset = UNSET
    if _elements_to_update is not UNSET:
      elements_to_update = []
      for elements_to_update_item_data in _elements_to_update:
        elements_to_update_item = ElementUpdatePatch.from_dict(
          elements_to_update_item_data
        )

        elements_to_update.append(elements_to_update_item)

    elements_to_remove = cast(list[str], d.pop("elements_to_remove", UNSET))

    _structures_to_add = d.pop("structures_to_add", UNSET)
    structures_to_add: list[TaxonomyBlockStructureRequest] | Unset = UNSET
    if _structures_to_add is not UNSET:
      structures_to_add = []
      for structures_to_add_item_data in _structures_to_add:
        structures_to_add_item = TaxonomyBlockStructureRequest.from_dict(
          structures_to_add_item_data
        )

        structures_to_add.append(structures_to_add_item)

    _structures_to_update = d.pop("structures_to_update", UNSET)
    structures_to_update: list[StructureUpdatePatch] | Unset = UNSET
    if _structures_to_update is not UNSET:
      structures_to_update = []
      for structures_to_update_item_data in _structures_to_update:
        structures_to_update_item = StructureUpdatePatch.from_dict(
          structures_to_update_item_data
        )

        structures_to_update.append(structures_to_update_item)

    structures_to_remove = cast(list[str], d.pop("structures_to_remove", UNSET))

    _associations_to_add = d.pop("associations_to_add", UNSET)
    associations_to_add: list[TaxonomyBlockAssociationRequest] | Unset = UNSET
    if _associations_to_add is not UNSET:
      associations_to_add = []
      for associations_to_add_item_data in _associations_to_add:
        associations_to_add_item = TaxonomyBlockAssociationRequest.from_dict(
          associations_to_add_item_data
        )

        associations_to_add.append(associations_to_add_item)

    associations_to_remove = cast(list[str], d.pop("associations_to_remove", UNSET))

    _rules_to_add = d.pop("rules_to_add", UNSET)
    rules_to_add: list[TaxonomyBlockRuleRequest] | Unset = UNSET
    if _rules_to_add is not UNSET:
      rules_to_add = []
      for rules_to_add_item_data in _rules_to_add:
        rules_to_add_item = TaxonomyBlockRuleRequest.from_dict(rules_to_add_item_data)

        rules_to_add.append(rules_to_add_item)

    rules_to_remove = cast(list[str], d.pop("rules_to_remove", UNSET))

    update_taxonomy_block_request = cls(
      taxonomy_id=taxonomy_id,
      name=name,
      description=description,
      version=version,
      elements_to_add=elements_to_add,
      elements_to_update=elements_to_update,
      elements_to_remove=elements_to_remove,
      structures_to_add=structures_to_add,
      structures_to_update=structures_to_update,
      structures_to_remove=structures_to_remove,
      associations_to_add=associations_to_add,
      associations_to_remove=associations_to_remove,
      rules_to_add=rules_to_add,
      rules_to_remove=rules_to_remove,
    )

    update_taxonomy_block_request.additional_properties = d
    return update_taxonomy_block_request

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
