"""Element Mapping Client Extension

Client-side extension for managing element mappings in subgraph workspaces.
Constructs Cypher queries for execution via the public /query endpoint.

This replaces server-side mapping endpoints with client-side logic,
following the architecture where mappings are written to subgraphs
and later published to the main graph via parquet export/ingest.
"""

import uuid
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum
import pandas as pd


class AggregationMethod(Enum):
  """Aggregation methods for element mapping"""

  SUM = "sum"
  AVERAGE = "average"
  WEIGHTED_AVERAGE = "weighted_average"
  FIRST = "first"
  LAST = "last"
  CALCULATED = "calculated"


@dataclass
class MappingStructure:
  """Element mapping structure"""

  identifier: str
  name: str
  description: Optional[str] = None
  taxonomy_uri: Optional[str] = None
  target_taxonomy_uri: Optional[str] = None
  associations: Optional[List["ElementAssociation"]] = None

  def __post_init__(self):
    if self.associations is None:
      self.associations = []


@dataclass
class ElementAssociation:
  """Association between source and target elements"""

  identifier: str
  source_element: str
  target_element: str
  aggregation_method: AggregationMethod = AggregationMethod.SUM
  weight: float = 1.0
  formula: Optional[str] = None
  order_value: float = 1.0


class ElementMappingClient:
  """
  Client for managing element mappings in subgraph workspaces.

  All operations construct Cypher queries that are executed via the
  public /query endpoint against a subgraph workspace.
  """

  def __init__(self, query_client):
    """
    Initialize with a query client for executing Cypher.

    Args:
        query_client: RoboSystemsExtensions query client
    """
    self.query = query_client

  def _generate_uuid(self, seed: str = None) -> str:
    """Generate a deterministic or random UUID"""
    if seed:
      # For deterministic UUID based on seed
      import hashlib

      hash_obj = hashlib.sha256(seed.encode())
      hash_hex = hash_obj.hexdigest()
      return f"{hash_hex[:8]}-{hash_hex[8:12]}-7{hash_hex[13:16]}-{hash_hex[16:20]}-{hash_hex[20:32]}"
    else:
      return str(uuid.uuid4())

  async def create_mapping_structure(
    self,
    graph_id: str,
    name: str,
    description: str = None,
    taxonomy_uri: str = None,
    target_taxonomy_uri: str = None,
  ) -> MappingStructure:
    """
    Create a new element mapping structure in the subgraph.

    Args:
        graph_id: Subgraph workspace ID (e.g., kg123_workspace)
        name: Name of the mapping structure
        description: Optional description
        taxonomy_uri: Source taxonomy URI (e.g., "qb:chart-of-accounts")
        target_taxonomy_uri: Target taxonomy URI (e.g., "us-gaap:2024")

    Returns:
        Created MappingStructure
    """
    structure_id = self._generate_uuid(f"mapping_structure_{name}_{graph_id}")

    cypher = """
        CREATE (s:Structure {
            identifier: $identifier,
            type: 'ElementMapping',
            name: $name,
            definition: $description,
            uri: $uri,
            network_uri: $network_uri
        })
        RETURN s
        """

    params = {
      "identifier": structure_id,
      "name": name,
      "description": description or "",
      "uri": taxonomy_uri or "",
      "network_uri": target_taxonomy_uri or "",
    }

    self.query.query(graph_id, cypher, params)

    return MappingStructure(
      identifier=structure_id,
      name=name,
      description=description,
      taxonomy_uri=taxonomy_uri,
      target_taxonomy_uri=target_taxonomy_uri,
      associations=[],
    )

  async def get_mapping_structure(
    self, graph_id: str, structure_id: str
  ) -> Optional[MappingStructure]:
    """
    Get a mapping structure with all its associations.

    Args:
        graph_id: Subgraph workspace ID
        structure_id: Structure identifier

    Returns:
        MappingStructure with associations, or None if not found
    """
    cypher = """
        MATCH (s:Structure)
        WHERE s.identifier = $structure_id AND s.type = 'ElementMapping'
        OPTIONAL MATCH (s)-[:STRUCTURE_HAS_ASSOCIATION]->(a:Association)
        OPTIONAL MATCH (a)-[:ASSOCIATION_HAS_FROM_ELEMENT]->(from_el:Element)
        OPTIONAL MATCH (a)-[:ASSOCIATION_HAS_TO_ELEMENT]->(to_el:Element)
        RETURN s,
               collect({
                 identifier: a.identifier,
                 source_element: from_el.uri,
                 target_element: to_el.uri,
                 aggregation_method: a.preferred_label,
                 weight: a.weight,
                 order_value: a.order_value
               }) as associations
        """

    result = self.query.query(graph_id, cypher, {"structure_id": structure_id})

    if not result or not result.data:
      return None

    row = result.data[0]
    structure_data = row["s"]

    associations = []
    for assoc in row["associations"]:
      if assoc["identifier"]:
        associations.append(
          ElementAssociation(
            identifier=assoc["identifier"],
            source_element=assoc["source_element"] or "",
            target_element=assoc["target_element"] or "",
            aggregation_method=AggregationMethod(assoc["aggregation_method"] or "sum"),
            weight=assoc["weight"] or 1.0,
            order_value=assoc["order_value"] or 1.0,
          )
        )

    return MappingStructure(
      identifier=structure_data["identifier"],
      name=structure_data["name"],
      description=structure_data.get("definition"),
      taxonomy_uri=structure_data.get("uri"),
      target_taxonomy_uri=structure_data.get("network_uri"),
      associations=associations,
    )

  async def list_mapping_structures(self, graph_id: str) -> List[MappingStructure]:
    """
    List all mapping structures in the subgraph.

    Args:
        graph_id: Subgraph workspace ID

    Returns:
        List of MappingStructure objects
    """
    cypher = """
        MATCH (s:Structure)
        WHERE s.type = 'ElementMapping'
        OPTIONAL MATCH (s)-[:STRUCTURE_HAS_ASSOCIATION]->(a:Association)
        RETURN s,
               count(a) as association_count
        ORDER BY s.name
        """

    result = self.query.query(graph_id, cypher, {})

    structures = []
    if result and result.data:
      for row in result.data:
        structure_data = row["s"]
        structures.append(
          MappingStructure(
            identifier=structure_data["identifier"],
            name=structure_data["name"],
            description=structure_data.get("definition"),
            taxonomy_uri=structure_data.get("uri"),
            target_taxonomy_uri=structure_data.get("network_uri"),
            associations=[],  # Not loading associations in list view
          )
        )

    return structures

  async def create_association(
    self,
    graph_id: str,
    structure_id: str,
    source_element: str,
    target_element: str,
    aggregation_method: AggregationMethod = AggregationMethod.SUM,
    weight: float = 1.0,
    order_value: float = 1.0,
  ) -> ElementAssociation:
    """
    Add an association to a mapping structure.

    Creates an Association node linking source element to target element.
    If the target element doesn't exist, it will be created.

    Args:
        graph_id: Subgraph workspace ID
        structure_id: Structure identifier
        source_element: Source element URI (e.g., "qb:BankAccount1")
        target_element: Target element URI (e.g., "us-gaap:Cash")
        aggregation_method: How to aggregate values
        weight: Weight for weighted aggregation
        order_value: Display order

    Returns:
        Created ElementAssociation
    """
    association_id = self._generate_uuid(
      f"association_{structure_id}_{source_element}_{target_element}"
    )

    # Generate identifier for target element
    target_element_id = self._generate_uuid(f"element_{target_element}")
    target_element_name = (
      target_element.split(":")[-1] if ":" in target_element else target_element
    )

    cypher = """
        MATCH (s:Structure)
        WHERE s.identifier = $structure_id AND s.type = 'ElementMapping'
        MATCH (from_el:Element {uri: $source_element})
        MERGE (to_el:Element {identifier: $target_element_identifier})
        ON CREATE SET to_el.uri = $target_element, to_el.name = $target_element_name
        CREATE (a:Association {
            identifier: $identifier,
            association_type: 'ElementMapping',
            arcrole: 'aggregation',
            preferred_label: $preferred_label,
            weight: $weight,
            order_value: $order_value
        })
        CREATE (s)-[:STRUCTURE_HAS_ASSOCIATION]->(a)
        CREATE (a)-[:ASSOCIATION_HAS_FROM_ELEMENT]->(from_el)
        CREATE (a)-[:ASSOCIATION_HAS_TO_ELEMENT]->(to_el)
        RETURN a
        """

    params = {
      "structure_id": structure_id,
      "identifier": association_id,
      "preferred_label": aggregation_method.value,
      "weight": weight,
      "order_value": order_value,
      "source_element": source_element,
      "target_element": target_element,
      "target_element_identifier": target_element_id,
      "target_element_name": target_element_name,
    }

    self.query.query(graph_id, cypher, params)

    return ElementAssociation(
      identifier=association_id,
      source_element=source_element,
      target_element=target_element,
      aggregation_method=aggregation_method,
      weight=weight,
      order_value=order_value,
    )

  async def update_association(
    self,
    graph_id: str,
    structure_id: str,
    association_id: str,
    aggregation_method: AggregationMethod = None,
    weight: float = None,
    order_value: float = None,
  ) -> Optional[ElementAssociation]:
    """
    Update an existing association.

    Args:
        graph_id: Subgraph workspace ID
        structure_id: Structure identifier
        association_id: Association identifier
        aggregation_method: New aggregation method
        weight: New weight
        order_value: New order value

    Returns:
        Updated ElementAssociation, or None if not found
    """
    set_clauses = []
    params = {"structure_id": structure_id, "association_id": association_id}

    if aggregation_method is not None:
      set_clauses.append("a.preferred_label = $aggregation_method")
      params["aggregation_method"] = aggregation_method.value

    if weight is not None:
      set_clauses.append("a.weight = $weight")
      params["weight"] = weight

    if order_value is not None:
      set_clauses.append("a.order_value = $order_value")
      params["order_value"] = order_value

    if not set_clauses:
      return None

    update_cypher = f"""
        MATCH (s:Structure)-[:STRUCTURE_HAS_ASSOCIATION]->(a:Association)
        WHERE s.identifier = $structure_id AND a.identifier = $association_id
        SET {", ".join(set_clauses)}
        RETURN a
        """

    self.query.query(graph_id, update_cypher, params)

    # Get updated association
    get_cypher = """
        MATCH (s:Structure)-[:STRUCTURE_HAS_ASSOCIATION]->(a:Association)
        WHERE s.identifier = $structure_id AND a.identifier = $association_id
        MATCH (a)-[:ASSOCIATION_HAS_FROM_ELEMENT]->(from_el:Element)
        MATCH (a)-[:ASSOCIATION_HAS_TO_ELEMENT]->(to_el:Element)
        RETURN a, from_el.uri as source_element, to_el.uri as target_element
        """

    result = self.query.query(graph_id, get_cypher, params)

    if not result or not result.data:
      return None

    row = result.data[0]
    assoc_data = row["a"]

    return ElementAssociation(
      identifier=assoc_data["identifier"],
      source_element=row["source_element"],
      target_element=row["target_element"],
      aggregation_method=AggregationMethod(assoc_data["preferred_label"]),
      weight=assoc_data["weight"],
      order_value=assoc_data["order_value"],
    )

  async def delete_association(
    self, graph_id: str, structure_id: str, association_id: str
  ) -> bool:
    """
    Delete an association from a mapping structure.

    Args:
        graph_id: Subgraph workspace ID
        structure_id: Structure identifier
        association_id: Association identifier

    Returns:
        True if deleted
    """
    cypher = """
        MATCH (s:Structure)-[:STRUCTURE_HAS_ASSOCIATION]->(a:Association)
        WHERE s.identifier = $structure_id AND a.identifier = $association_id
        DETACH DELETE a
        """

    self.query.query(
      graph_id, cypher, {"structure_id": structure_id, "association_id": association_id}
    )

    return True

  async def delete_mapping_structure(self, graph_id: str, structure_id: str) -> bool:
    """
    Delete a mapping structure and all its associations.

    Args:
        graph_id: Subgraph workspace ID
        structure_id: Structure identifier

    Returns:
        True if deleted
    """
    cypher = """
        MATCH (s:Structure)
        WHERE s.identifier = $structure_id AND s.type = 'ElementMapping'
        OPTIONAL MATCH (s)-[:STRUCTURE_HAS_ASSOCIATION]->(a:Association)
        DETACH DELETE s, a
        """

    self.query.query(graph_id, cypher, {"structure_id": structure_id})

    return True

  @staticmethod
  def apply_element_mapping(
    fact_data: pd.DataFrame, mapping_structure: MappingStructure
  ) -> pd.DataFrame:
    """
    Apply element mapping to aggregate source elements into target elements.

    This is a client-side pandas operation that doesn't require graph access.

    Args:
        fact_data: DataFrame with columns including element_id, numeric_value, etc.
        mapping_structure: MappingStructure with associations defining aggregation

    Returns:
        DataFrame with aggregated facts mapped to target elements
    """
    if fact_data.empty or not mapping_structure.associations:
      return fact_data

    df = fact_data.copy()
    aggregated_rows = []

    # Handle both numeric_value (from facts) and net_balance (from trial balance)
    value_col = "numeric_value" if "numeric_value" in df.columns else "net_balance"

    # Group associations by target element
    target_groups = {}
    for assoc in mapping_structure.associations:
      if assoc.target_element not in target_groups:
        target_groups[assoc.target_element] = []
      target_groups[assoc.target_element].append(assoc)

    # Build URI to ID mapping if both columns exist
    uri_to_id_map = {}
    if "element_uri" in df.columns and "element_id" in df.columns:
      for _, row in df[["element_uri", "element_id"]].drop_duplicates().iterrows():
        uri_to_id_map[row["element_uri"]] = row["element_id"]

    # Determine groupby columns
    groupby_columns = []
    if "period_end" in df.columns:
      groupby_columns.append("period_end")
    if "period_start" in df.columns:
      groupby_columns.append("period_start")
    if "entity_id" in df.columns:
      groupby_columns.append("entity_id")
    if "dimension_axis" in df.columns:
      groupby_columns.append("dimension_axis")
    if "dimension_member" in df.columns:
      groupby_columns.append("dimension_member")

    # Aggregate for each target element
    for target_element, associations in target_groups.items():
      # Map source URIs to IDs
      source_element_uris = [assoc.source_element for assoc in associations]
      source_element_ids = [uri_to_id_map.get(uri, uri) for uri in source_element_uris]

      # Filter source facts
      source_facts = df[df["element_id"].isin(source_element_ids)].copy()

      if source_facts.empty:
        continue

      aggregation_method = associations[0].aggregation_method

      if groupby_columns:
        # Group and aggregate
        for group_keys, group_df in source_facts.groupby(groupby_columns):
          aggregated_value = ElementMappingClient._aggregate_values(
            group_df, associations, aggregation_method, value_col
          )

          # Create aggregated row
          aggregated_row = group_df.iloc[0].copy()
          aggregated_row["element_id"] = target_element
          aggregated_row["element_name"] = target_element.split(":")[-1]
          aggregated_row[value_col] = aggregated_value

          if "element_label" in aggregated_row:
            aggregated_row["element_label"] = target_element.split(":")[-1]

          aggregated_rows.append(aggregated_row)
      else:
        # No grouping, aggregate all
        aggregated_value = ElementMappingClient._aggregate_values(
          source_facts, associations, aggregation_method, value_col
        )

        aggregated_row = source_facts.iloc[0].copy()
        aggregated_row["element_id"] = target_element
        aggregated_row["element_name"] = target_element.split(":")[-1]
        aggregated_row[value_col] = aggregated_value

        if "element_label" in aggregated_row:
          aggregated_row["element_label"] = target_element.split(":")[-1]

        aggregated_rows.append(aggregated_row)

    if not aggregated_rows:
      return df

    return pd.DataFrame(aggregated_rows)

  @staticmethod
  def _aggregate_values(
    facts: pd.DataFrame,
    associations: List[ElementAssociation],
    method: AggregationMethod,
    value_col: str,
  ) -> float:
    """Helper function to aggregate values based on method."""
    if method == AggregationMethod.SUM:
      return facts[value_col].sum()

    elif method == AggregationMethod.AVERAGE:
      return facts[value_col].mean()

    elif method == AggregationMethod.WEIGHTED_AVERAGE:
      weights_map = {assoc.source_element: assoc.weight for assoc in associations}
      facts_with_weights = facts.copy()
      facts_with_weights["weight"] = facts_with_weights["element_id"].map(weights_map)
      facts_with_weights["weighted_value"] = (
        facts_with_weights[value_col] * facts_with_weights["weight"]
      )
      total_weight = facts_with_weights["weight"].sum()
      if total_weight == 0:
        return 0.0
      return facts_with_weights["weighted_value"].sum() / total_weight

    elif method == AggregationMethod.FIRST:
      return facts[value_col].iloc[0]

    elif method == AggregationMethod.LAST:
      return facts[value_col].iloc[-1]

    elif method == AggregationMethod.CALCULATED:
      # For calculated, use sum as default (could be customized)
      return facts[value_col].sum()

    # Default to sum
    return facts[value_col].sum()
