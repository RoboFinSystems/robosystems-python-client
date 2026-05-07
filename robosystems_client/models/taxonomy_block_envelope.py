from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.taxonomy_block_association import TaxonomyBlockAssociation
  from ..models.taxonomy_block_element import TaxonomyBlockElement
  from ..models.taxonomy_block_envelope_verification_results_item import (
    TaxonomyBlockEnvelopeVerificationResultsItem,
  )
  from ..models.taxonomy_block_rule import TaxonomyBlockRule
  from ..models.taxonomy_block_structure import TaxonomyBlockStructure


T = TypeVar("T", bound="TaxonomyBlockEnvelope")


@_attrs_define
class TaxonomyBlockEnvelope:
  """The Taxonomy Block exchange format.

  One envelope per taxonomy instance. Carries identity + type,
  registry-sourced display metadata, the parent taxonomy pointer (for
  ``reporting_extension`` blocks), and bundled atoms (elements,
  structures, associations, rules, verification results).

      Attributes:
          id (str): Taxonomy row id.
          name (str):
          taxonomy_type (str): Block-type discriminator — 'reporting_standard' | 'reporting_extension' |
              'chart_of_accounts' | 'custom_ontology'.
          display_name (str): Registry-sourced display label.
          category (str): Registry-sourced sidebar grouping.
          parent_taxonomy_id (None | str | Unset):
          parent_taxonomy_name (None | str | Unset):
          version (None | str | Unset):
          standard (None | str | Unset):
          namespace_uri (None | str | Unset):
          is_locked (bool | Unset):  Default: False.
          elements (list[TaxonomyBlockElement] | Unset):
          structures (list[TaxonomyBlockStructure] | Unset):
          associations (list[TaxonomyBlockAssociation] | Unset):
          rules (list[TaxonomyBlockRule] | Unset):
          verification_results (list[TaxonomyBlockEnvelopeVerificationResultsItem] | Unset):
          element_count (int | Unset):  Default: 0.
          structure_count (int | Unset):  Default: 0.
          association_count (int | Unset):  Default: 0.
  """

  id: str
  name: str
  taxonomy_type: str
  display_name: str
  category: str
  parent_taxonomy_id: None | str | Unset = UNSET
  parent_taxonomy_name: None | str | Unset = UNSET
  version: None | str | Unset = UNSET
  standard: None | str | Unset = UNSET
  namespace_uri: None | str | Unset = UNSET
  is_locked: bool | Unset = False
  elements: list[TaxonomyBlockElement] | Unset = UNSET
  structures: list[TaxonomyBlockStructure] | Unset = UNSET
  associations: list[TaxonomyBlockAssociation] | Unset = UNSET
  rules: list[TaxonomyBlockRule] | Unset = UNSET
  verification_results: list[TaxonomyBlockEnvelopeVerificationResultsItem] | Unset = (
    UNSET
  )
  element_count: int | Unset = 0
  structure_count: int | Unset = 0
  association_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    taxonomy_type = self.taxonomy_type

    display_name = self.display_name

    category = self.category

    parent_taxonomy_id: None | str | Unset
    if isinstance(self.parent_taxonomy_id, Unset):
      parent_taxonomy_id = UNSET
    else:
      parent_taxonomy_id = self.parent_taxonomy_id

    parent_taxonomy_name: None | str | Unset
    if isinstance(self.parent_taxonomy_name, Unset):
      parent_taxonomy_name = UNSET
    else:
      parent_taxonomy_name = self.parent_taxonomy_name

    version: None | str | Unset
    if isinstance(self.version, Unset):
      version = UNSET
    else:
      version = self.version

    standard: None | str | Unset
    if isinstance(self.standard, Unset):
      standard = UNSET
    else:
      standard = self.standard

    namespace_uri: None | str | Unset
    if isinstance(self.namespace_uri, Unset):
      namespace_uri = UNSET
    else:
      namespace_uri = self.namespace_uri

    is_locked = self.is_locked

    elements: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.elements, Unset):
      elements = []
      for elements_item_data in self.elements:
        elements_item = elements_item_data.to_dict()
        elements.append(elements_item)

    structures: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.structures, Unset):
      structures = []
      for structures_item_data in self.structures:
        structures_item = structures_item_data.to_dict()
        structures.append(structures_item)

    associations: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.associations, Unset):
      associations = []
      for associations_item_data in self.associations:
        associations_item = associations_item_data.to_dict()
        associations.append(associations_item)

    rules: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rules, Unset):
      rules = []
      for rules_item_data in self.rules:
        rules_item = rules_item_data.to_dict()
        rules.append(rules_item)

    verification_results: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.verification_results, Unset):
      verification_results = []
      for verification_results_item_data in self.verification_results:
        verification_results_item = verification_results_item_data.to_dict()
        verification_results.append(verification_results_item)

    element_count = self.element_count

    structure_count = self.structure_count

    association_count = self.association_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "taxonomy_type": taxonomy_type,
        "display_name": display_name,
        "category": category,
      }
    )
    if parent_taxonomy_id is not UNSET:
      field_dict["parent_taxonomy_id"] = parent_taxonomy_id
    if parent_taxonomy_name is not UNSET:
      field_dict["parent_taxonomy_name"] = parent_taxonomy_name
    if version is not UNSET:
      field_dict["version"] = version
    if standard is not UNSET:
      field_dict["standard"] = standard
    if namespace_uri is not UNSET:
      field_dict["namespace_uri"] = namespace_uri
    if is_locked is not UNSET:
      field_dict["is_locked"] = is_locked
    if elements is not UNSET:
      field_dict["elements"] = elements
    if structures is not UNSET:
      field_dict["structures"] = structures
    if associations is not UNSET:
      field_dict["associations"] = associations
    if rules is not UNSET:
      field_dict["rules"] = rules
    if verification_results is not UNSET:
      field_dict["verification_results"] = verification_results
    if element_count is not UNSET:
      field_dict["element_count"] = element_count
    if structure_count is not UNSET:
      field_dict["structure_count"] = structure_count
    if association_count is not UNSET:
      field_dict["association_count"] = association_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.taxonomy_block_association import TaxonomyBlockAssociation
    from ..models.taxonomy_block_element import TaxonomyBlockElement
    from ..models.taxonomy_block_envelope_verification_results_item import (
      TaxonomyBlockEnvelopeVerificationResultsItem,
    )
    from ..models.taxonomy_block_rule import TaxonomyBlockRule
    from ..models.taxonomy_block_structure import TaxonomyBlockStructure

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    taxonomy_type = d.pop("taxonomy_type")

    display_name = d.pop("display_name")

    category = d.pop("category")

    def _parse_parent_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_taxonomy_id = _parse_parent_taxonomy_id(d.pop("parent_taxonomy_id", UNSET))

    def _parse_parent_taxonomy_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_taxonomy_name = _parse_parent_taxonomy_name(
      d.pop("parent_taxonomy_name", UNSET)
    )

    def _parse_version(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    version = _parse_version(d.pop("version", UNSET))

    def _parse_standard(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    standard = _parse_standard(d.pop("standard", UNSET))

    def _parse_namespace_uri(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    namespace_uri = _parse_namespace_uri(d.pop("namespace_uri", UNSET))

    is_locked = d.pop("is_locked", UNSET)

    _elements = d.pop("elements", UNSET)
    elements: list[TaxonomyBlockElement] | Unset = UNSET
    if _elements is not UNSET:
      elements = []
      for elements_item_data in _elements:
        elements_item = TaxonomyBlockElement.from_dict(elements_item_data)

        elements.append(elements_item)

    _structures = d.pop("structures", UNSET)
    structures: list[TaxonomyBlockStructure] | Unset = UNSET
    if _structures is not UNSET:
      structures = []
      for structures_item_data in _structures:
        structures_item = TaxonomyBlockStructure.from_dict(structures_item_data)

        structures.append(structures_item)

    _associations = d.pop("associations", UNSET)
    associations: list[TaxonomyBlockAssociation] | Unset = UNSET
    if _associations is not UNSET:
      associations = []
      for associations_item_data in _associations:
        associations_item = TaxonomyBlockAssociation.from_dict(associations_item_data)

        associations.append(associations_item)

    _rules = d.pop("rules", UNSET)
    rules: list[TaxonomyBlockRule] | Unset = UNSET
    if _rules is not UNSET:
      rules = []
      for rules_item_data in _rules:
        rules_item = TaxonomyBlockRule.from_dict(rules_item_data)

        rules.append(rules_item)

    _verification_results = d.pop("verification_results", UNSET)
    verification_results: list[TaxonomyBlockEnvelopeVerificationResultsItem] | Unset = (
      UNSET
    )
    if _verification_results is not UNSET:
      verification_results = []
      for verification_results_item_data in _verification_results:
        verification_results_item = (
          TaxonomyBlockEnvelopeVerificationResultsItem.from_dict(
            verification_results_item_data
          )
        )

        verification_results.append(verification_results_item)

    element_count = d.pop("element_count", UNSET)

    structure_count = d.pop("structure_count", UNSET)

    association_count = d.pop("association_count", UNSET)

    taxonomy_block_envelope = cls(
      id=id,
      name=name,
      taxonomy_type=taxonomy_type,
      display_name=display_name,
      category=category,
      parent_taxonomy_id=parent_taxonomy_id,
      parent_taxonomy_name=parent_taxonomy_name,
      version=version,
      standard=standard,
      namespace_uri=namespace_uri,
      is_locked=is_locked,
      elements=elements,
      structures=structures,
      associations=associations,
      rules=rules,
      verification_results=verification_results,
      element_count=element_count,
      structure_count=structure_count,
      association_count=association_count,
    )

    taxonomy_block_envelope.additional_properties = d
    return taxonomy_block_envelope

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
