from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_taxonomy_block_request_taxonomy_type import (
  CreateTaxonomyBlockRequestTaxonomyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_taxonomy_block_request_metadata import (
    CreateTaxonomyBlockRequestMetadata,
  )
  from ..models.taxonomy_block_association_request import (
    TaxonomyBlockAssociationRequest,
  )
  from ..models.taxonomy_block_element_request import TaxonomyBlockElementRequest
  from ..models.taxonomy_block_rule_request import TaxonomyBlockRuleRequest
  from ..models.taxonomy_block_structure_request import TaxonomyBlockStructureRequest


T = TypeVar("T", bound="CreateTaxonomyBlockRequest")


@_attrs_define
class CreateTaxonomyBlockRequest:
  """Request body for the ``create-taxonomy-block`` operation.

  One envelope per taxonomy instance. ``taxonomy_type`` discriminates
  which block-type handler the command dispatcher routes to.
  ``parent_taxonomy_id`` is required for ``reporting_extension`` (which
  extends a library taxonomy) and ignored otherwise.

  The library path (seeding ``reporting_standard`` rows) does NOT flow
  through this envelope — it uses a dedicated library writer that bypasses
  these caps and tenant scoping.

      Attributes:
          name (str): Taxonomy display name.
          taxonomy_type (CreateTaxonomyBlockRequestTaxonomyType): Block-type discriminator. ``chart_of_accounts`` and
              ``custom_ontology`` construct from scratch; ``reporting_extension`` extends an existing library
              ``reporting_standard``.
          parent_taxonomy_id (None | str | Unset): Required when ``taxonomy_type == 'reporting_extension'`` — the id of
              the library ``reporting_standard`` being extended.
          version (None | str | Unset):
          description (None | str | Unset):
          standard (None | str | Unset):
          namespace_uri (None | str | Unset):
          elements (list[TaxonomyBlockElementRequest] | Unset):
          structures (list[TaxonomyBlockStructureRequest] | Unset):
          associations (list[TaxonomyBlockAssociationRequest] | Unset):
          rules (list[TaxonomyBlockRuleRequest] | Unset):
          metadata (CreateTaxonomyBlockRequestMetadata | Unset):
  """

  name: str
  taxonomy_type: CreateTaxonomyBlockRequestTaxonomyType
  parent_taxonomy_id: None | str | Unset = UNSET
  version: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  standard: None | str | Unset = UNSET
  namespace_uri: None | str | Unset = UNSET
  elements: list[TaxonomyBlockElementRequest] | Unset = UNSET
  structures: list[TaxonomyBlockStructureRequest] | Unset = UNSET
  associations: list[TaxonomyBlockAssociationRequest] | Unset = UNSET
  rules: list[TaxonomyBlockRuleRequest] | Unset = UNSET
  metadata: CreateTaxonomyBlockRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    taxonomy_type = self.taxonomy_type.value

    parent_taxonomy_id: None | str | Unset
    if isinstance(self.parent_taxonomy_id, Unset):
      parent_taxonomy_id = UNSET
    else:
      parent_taxonomy_id = self.parent_taxonomy_id

    version: None | str | Unset
    if isinstance(self.version, Unset):
      version = UNSET
    else:
      version = self.version

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

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

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "taxonomy_type": taxonomy_type,
      }
    )
    if parent_taxonomy_id is not UNSET:
      field_dict["parent_taxonomy_id"] = parent_taxonomy_id
    if version is not UNSET:
      field_dict["version"] = version
    if description is not UNSET:
      field_dict["description"] = description
    if standard is not UNSET:
      field_dict["standard"] = standard
    if namespace_uri is not UNSET:
      field_dict["namespace_uri"] = namespace_uri
    if elements is not UNSET:
      field_dict["elements"] = elements
    if structures is not UNSET:
      field_dict["structures"] = structures
    if associations is not UNSET:
      field_dict["associations"] = associations
    if rules is not UNSET:
      field_dict["rules"] = rules
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_taxonomy_block_request_metadata import (
      CreateTaxonomyBlockRequestMetadata,
    )
    from ..models.taxonomy_block_association_request import (
      TaxonomyBlockAssociationRequest,
    )
    from ..models.taxonomy_block_element_request import TaxonomyBlockElementRequest
    from ..models.taxonomy_block_rule_request import TaxonomyBlockRuleRequest
    from ..models.taxonomy_block_structure_request import TaxonomyBlockStructureRequest

    d = dict(src_dict)
    name = d.pop("name")

    taxonomy_type = CreateTaxonomyBlockRequestTaxonomyType(d.pop("taxonomy_type"))

    def _parse_parent_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_taxonomy_id = _parse_parent_taxonomy_id(d.pop("parent_taxonomy_id", UNSET))

    def _parse_version(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    version = _parse_version(d.pop("version", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

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

    _elements = d.pop("elements", UNSET)
    elements: list[TaxonomyBlockElementRequest] | Unset = UNSET
    if _elements is not UNSET:
      elements = []
      for elements_item_data in _elements:
        elements_item = TaxonomyBlockElementRequest.from_dict(elements_item_data)

        elements.append(elements_item)

    _structures = d.pop("structures", UNSET)
    structures: list[TaxonomyBlockStructureRequest] | Unset = UNSET
    if _structures is not UNSET:
      structures = []
      for structures_item_data in _structures:
        structures_item = TaxonomyBlockStructureRequest.from_dict(structures_item_data)

        structures.append(structures_item)

    _associations = d.pop("associations", UNSET)
    associations: list[TaxonomyBlockAssociationRequest] | Unset = UNSET
    if _associations is not UNSET:
      associations = []
      for associations_item_data in _associations:
        associations_item = TaxonomyBlockAssociationRequest.from_dict(
          associations_item_data
        )

        associations.append(associations_item)

    _rules = d.pop("rules", UNSET)
    rules: list[TaxonomyBlockRuleRequest] | Unset = UNSET
    if _rules is not UNSET:
      rules = []
      for rules_item_data in _rules:
        rules_item = TaxonomyBlockRuleRequest.from_dict(rules_item_data)

        rules.append(rules_item)

    _metadata = d.pop("metadata", UNSET)
    metadata: CreateTaxonomyBlockRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = CreateTaxonomyBlockRequestMetadata.from_dict(_metadata)

    create_taxonomy_block_request = cls(
      name=name,
      taxonomy_type=taxonomy_type,
      parent_taxonomy_id=parent_taxonomy_id,
      version=version,
      description=description,
      standard=standard,
      namespace_uri=namespace_uri,
      elements=elements,
      structures=structures,
      associations=associations,
      rules=rules,
      metadata=metadata,
    )

    create_taxonomy_block_request.additional_properties = d
    return create_taxonomy_block_request

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
