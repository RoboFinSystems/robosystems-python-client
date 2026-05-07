from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.artifact_response import ArtifactResponse
  from ..models.connection_lite import ConnectionLite
  from ..models.element_lite import ElementLite
  from ..models.fact_lite import FactLite
  from ..models.fact_set_lite import FactSetLite
  from ..models.information_block_envelope_dimensions_item import (
    InformationBlockEnvelopeDimensionsItem,
  )
  from ..models.information_model_response import InformationModelResponse
  from ..models.rule_lite import RuleLite
  from ..models.verification_result_lite import VerificationResultLite
  from ..models.view_projections import ViewProjections


T = TypeVar("T", bound="InformationBlockEnvelope")


@_attrs_define
class InformationBlockEnvelope:
  """The Information Block exchange format.

  One envelope per block instance. Carries the block's identity + type,
  Information-Model attributes, the Artifact branch (mechanics +
  topic/template), and bundled atoms (elements, connections, facts).
  Rules / dimensions / FactSet / verification_results are present-but-
  empty for blocks where the upstream content (rule engine, FactSet
  expand, dimension catalog) has not yet been implemented.

      Attributes:
          id (str):
          block_type (str): Discriminator — 'schedule', …
          name (str):
          display_name (str): Registry-sourced display label (e.g., 'Schedule').
          category (str): Registry-sourced sidebar grouping ('Close', 'Reporting', …).
          information_model (InformationModelResponse): The block's intrinsic shape — concept + member arrangement
              patterns.
          artifact (ArtifactResponse): The block's producible-artifact envelope — topic, template, mechanics.
          taxonomy_id (None | str | Unset): Source taxonomy the Structure was seeded from. Always present for currently-
              registered block types (the Structure → Taxonomy FK is non-null); declared optional to keep the shape forward-
              compatible with future synthetic blocks that don't originate from a taxonomy.
          taxonomy_name (None | str | Unset): Display name of the source taxonomy.
          elements (list[ElementLite] | Unset):
          connections (list[ConnectionLite] | Unset):
          facts (list[FactLite] | Unset):
          rules (list[RuleLite] | Unset):
          dimensions (list[InformationBlockEnvelopeDimensionsItem] | Unset):
          fact_set (FactSetLite | None | Unset): The period-specific FactSet this envelope instantiates. Null when the
              underlying block has no FactSet row yet — typically library-seeded statement Structures with no tenant-generated
              facts, or Schedule rows written before the create-side FactSet stamping was added.
          verification_results (list[VerificationResultLite] | Unset):
          view (ViewProjections | Unset): Charlie's six ``type-of View`` arms, surfaced at the envelope boundary.

              Each projection is computed server-side at envelope-build time when
              its source data is available. The frontend's ``BlockView`` dispatcher
              routes to the projection component matching the user's selected view
              mode; missing projections (those still in backlog) render as empty
              states without breaking the dispatcher.

              Today: ``rendering`` is computed for the statement family.
              Other arms (``fact_table``, ``model_structure``, ``verification_results``,
              ``report_elements``, ``business_rules``) come online as their backend
              support lands; ``fact_table`` is trivially derivable from
              ``InformationBlockEnvelope.facts`` and may stay as a frontend-only
              projection.
  """

  id: str
  block_type: str
  name: str
  display_name: str
  category: str
  information_model: InformationModelResponse
  artifact: ArtifactResponse
  taxonomy_id: None | str | Unset = UNSET
  taxonomy_name: None | str | Unset = UNSET
  elements: list[ElementLite] | Unset = UNSET
  connections: list[ConnectionLite] | Unset = UNSET
  facts: list[FactLite] | Unset = UNSET
  rules: list[RuleLite] | Unset = UNSET
  dimensions: list[InformationBlockEnvelopeDimensionsItem] | Unset = UNSET
  fact_set: FactSetLite | None | Unset = UNSET
  verification_results: list[VerificationResultLite] | Unset = UNSET
  view: ViewProjections | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.fact_set_lite import FactSetLite

    id = self.id

    block_type = self.block_type

    name = self.name

    display_name = self.display_name

    category = self.category

    information_model = self.information_model.to_dict()

    artifact = self.artifact.to_dict()

    taxonomy_id: None | str | Unset
    if isinstance(self.taxonomy_id, Unset):
      taxonomy_id = UNSET
    else:
      taxonomy_id = self.taxonomy_id

    taxonomy_name: None | str | Unset
    if isinstance(self.taxonomy_name, Unset):
      taxonomy_name = UNSET
    else:
      taxonomy_name = self.taxonomy_name

    elements: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.elements, Unset):
      elements = []
      for elements_item_data in self.elements:
        elements_item = elements_item_data.to_dict()
        elements.append(elements_item)

    connections: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.connections, Unset):
      connections = []
      for connections_item_data in self.connections:
        connections_item = connections_item_data.to_dict()
        connections.append(connections_item)

    facts: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.facts, Unset):
      facts = []
      for facts_item_data in self.facts:
        facts_item = facts_item_data.to_dict()
        facts.append(facts_item)

    rules: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rules, Unset):
      rules = []
      for rules_item_data in self.rules:
        rules_item = rules_item_data.to_dict()
        rules.append(rules_item)

    dimensions: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.dimensions, Unset):
      dimensions = []
      for dimensions_item_data in self.dimensions:
        dimensions_item = dimensions_item_data.to_dict()
        dimensions.append(dimensions_item)

    fact_set: dict[str, Any] | None | Unset
    if isinstance(self.fact_set, Unset):
      fact_set = UNSET
    elif isinstance(self.fact_set, FactSetLite):
      fact_set = self.fact_set.to_dict()
    else:
      fact_set = self.fact_set

    verification_results: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.verification_results, Unset):
      verification_results = []
      for verification_results_item_data in self.verification_results:
        verification_results_item = verification_results_item_data.to_dict()
        verification_results.append(verification_results_item)

    view: dict[str, Any] | Unset = UNSET
    if not isinstance(self.view, Unset):
      view = self.view.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "block_type": block_type,
        "name": name,
        "display_name": display_name,
        "category": category,
        "information_model": information_model,
        "artifact": artifact,
      }
    )
    if taxonomy_id is not UNSET:
      field_dict["taxonomy_id"] = taxonomy_id
    if taxonomy_name is not UNSET:
      field_dict["taxonomy_name"] = taxonomy_name
    if elements is not UNSET:
      field_dict["elements"] = elements
    if connections is not UNSET:
      field_dict["connections"] = connections
    if facts is not UNSET:
      field_dict["facts"] = facts
    if rules is not UNSET:
      field_dict["rules"] = rules
    if dimensions is not UNSET:
      field_dict["dimensions"] = dimensions
    if fact_set is not UNSET:
      field_dict["fact_set"] = fact_set
    if verification_results is not UNSET:
      field_dict["verification_results"] = verification_results
    if view is not UNSET:
      field_dict["view"] = view

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.artifact_response import ArtifactResponse
    from ..models.connection_lite import ConnectionLite
    from ..models.element_lite import ElementLite
    from ..models.fact_lite import FactLite
    from ..models.fact_set_lite import FactSetLite
    from ..models.information_block_envelope_dimensions_item import (
      InformationBlockEnvelopeDimensionsItem,
    )
    from ..models.information_model_response import InformationModelResponse
    from ..models.rule_lite import RuleLite
    from ..models.verification_result_lite import VerificationResultLite
    from ..models.view_projections import ViewProjections

    d = dict(src_dict)
    id = d.pop("id")

    block_type = d.pop("block_type")

    name = d.pop("name")

    display_name = d.pop("display_name")

    category = d.pop("category")

    information_model = InformationModelResponse.from_dict(d.pop("information_model"))

    artifact = ArtifactResponse.from_dict(d.pop("artifact"))

    def _parse_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    taxonomy_id = _parse_taxonomy_id(d.pop("taxonomy_id", UNSET))

    def _parse_taxonomy_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    taxonomy_name = _parse_taxonomy_name(d.pop("taxonomy_name", UNSET))

    _elements = d.pop("elements", UNSET)
    elements: list[ElementLite] | Unset = UNSET
    if _elements is not UNSET:
      elements = []
      for elements_item_data in _elements:
        elements_item = ElementLite.from_dict(elements_item_data)

        elements.append(elements_item)

    _connections = d.pop("connections", UNSET)
    connections: list[ConnectionLite] | Unset = UNSET
    if _connections is not UNSET:
      connections = []
      for connections_item_data in _connections:
        connections_item = ConnectionLite.from_dict(connections_item_data)

        connections.append(connections_item)

    _facts = d.pop("facts", UNSET)
    facts: list[FactLite] | Unset = UNSET
    if _facts is not UNSET:
      facts = []
      for facts_item_data in _facts:
        facts_item = FactLite.from_dict(facts_item_data)

        facts.append(facts_item)

    _rules = d.pop("rules", UNSET)
    rules: list[RuleLite] | Unset = UNSET
    if _rules is not UNSET:
      rules = []
      for rules_item_data in _rules:
        rules_item = RuleLite.from_dict(rules_item_data)

        rules.append(rules_item)

    _dimensions = d.pop("dimensions", UNSET)
    dimensions: list[InformationBlockEnvelopeDimensionsItem] | Unset = UNSET
    if _dimensions is not UNSET:
      dimensions = []
      for dimensions_item_data in _dimensions:
        dimensions_item = InformationBlockEnvelopeDimensionsItem.from_dict(
          dimensions_item_data
        )

        dimensions.append(dimensions_item)

    def _parse_fact_set(data: object) -> FactSetLite | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        fact_set_type_0 = FactSetLite.from_dict(data)

        return fact_set_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(FactSetLite | None | Unset, data)

    fact_set = _parse_fact_set(d.pop("fact_set", UNSET))

    _verification_results = d.pop("verification_results", UNSET)
    verification_results: list[VerificationResultLite] | Unset = UNSET
    if _verification_results is not UNSET:
      verification_results = []
      for verification_results_item_data in _verification_results:
        verification_results_item = VerificationResultLite.from_dict(
          verification_results_item_data
        )

        verification_results.append(verification_results_item)

    _view = d.pop("view", UNSET)
    view: ViewProjections | Unset
    if isinstance(_view, Unset):
      view = UNSET
    else:
      view = ViewProjections.from_dict(_view)

    information_block_envelope = cls(
      id=id,
      block_type=block_type,
      name=name,
      display_name=display_name,
      category=category,
      information_model=information_model,
      artifact=artifact,
      taxonomy_id=taxonomy_id,
      taxonomy_name=taxonomy_name,
      elements=elements,
      connections=connections,
      facts=facts,
      rules=rules,
      dimensions=dimensions,
      fact_set=fact_set,
      verification_results=verification_results,
      view=view,
    )

    information_block_envelope.additional_properties = d
    return information_block_envelope

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
