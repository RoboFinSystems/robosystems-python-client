"""View Builder Client Extension

Client for building financial views and reports following the Financial Report Creator architecture.
Queries data from main graph, applies mappings, and generates views.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
import pandas as pd
from datetime import datetime


class ViewSourceType(Enum):
  """Source type for view generation"""

  TRANSACTIONS = "transactions"  # Generate from transaction aggregation
  FACT_SET = "fact_set"  # Pivot existing facts


@dataclass
class ViewSource:
  """Source configuration for view generation"""

  type: ViewSourceType
  period_start: Optional[str] = None
  period_end: Optional[str] = None
  entity_id: Optional[str] = None
  fact_set_id: Optional[str] = None


@dataclass
class ViewAxis:
  """Axis configuration for pivot table"""

  type: str  # "element", "period", "dimension"
  dimension_axis: Optional[str] = None
  hierarchy_root: Optional[str] = None
  include_subtotals: bool = False


@dataclass
class ViewConfig:
  """Configuration for view presentation"""

  rows: List[ViewAxis]
  columns: List[ViewAxis]
  measures: Optional[List[str]] = None  # Fact value columns to include


@dataclass
class ViewResponse:
  """Response from view generation"""

  facts: pd.DataFrame
  metadata: Dict[str, Any]
  execution_time_ms: int


class ViewBuilderClient:
  """
  Client for building financial views and reports.

  Provides functionality to:
  - Query trial balance from transactions
  - Query existing facts with aspects
  - Apply element mappings for aggregation
  - Generate pivot table presentations
  - Write views to subgraph workspaces
  """

  def __init__(self, query_client, element_mapping_client=None):
    """
    Initialize with query client and optional element mapping client.

    Args:
        query_client: RoboSystems query client
        element_mapping_client: Optional ElementMappingClient for applying mappings
    """
    self.query = query_client
    self.element_mapping = element_mapping_client

  async def aggregate_trial_balance(
    self,
    graph_id: str,
    period_start: str,
    period_end: str,
    entity_id: Optional[str] = None,
    requested_dimensions: Optional[List[str]] = None,
  ) -> pd.DataFrame:
    """
    Aggregate transactions to trial balance (Mode 1: Transaction Aggregation).

    This queries transaction data from the main graph and aggregates it
    to create a trial balance with debit/credit totals and net balances.

    Args:
        graph_id: Graph ID to query (main graph)
        period_start: Start date (YYYY-MM-DD)
        period_end: End date (YYYY-MM-DD)
        entity_id: Optional entity filter
        requested_dimensions: Optional dimension axes

    Returns:
        DataFrame with trial balance data
    """
    # Build WHERE clause
    conditions = ["t.date >= $period_start", "t.date <= $period_end"]
    params = {"period_start": period_start, "period_end": period_end}

    if entity_id:
      conditions.append("e.identifier = $entity_id")
      params["entity_id"] = entity_id

    where_clause = " AND ".join(conditions)

    # Query transaction data with aggregation
    cypher = f"""
        MATCH (e:Entity)-[:ENTITY_HAS_TRANSACTION]->(t:Transaction)
              -[:TRANSACTION_HAS_LINE_ITEM]->(li:LineItem)
              -[:LINE_ITEM_RELATES_TO_ELEMENT]->(elem:Element)
        WHERE {where_clause}

        WITH elem,
             sum(li.debit_amount) AS total_debits,
             sum(li.credit_amount) AS total_credits

        RETURN elem.identifier AS element_id,
               elem.uri AS element_uri,
               elem.name AS element_name,
               elem.classification AS element_classification,
               elem.balance AS element_balance,
               elem.period_type AS element_period_type,
               total_debits,
               total_credits,
               total_debits - total_credits AS net_balance
        ORDER BY elem.name
        """

    result = await self.query.query(graph_id, cypher, params)

    if not result or not result.data:
      # Return empty DataFrame with expected columns
      return pd.DataFrame(
        columns=[
          "element_id",
          "element_uri",
          "element_name",
          "element_classification",
          "element_balance",
          "element_period_type",
          "total_debits",
          "total_credits",
          "net_balance",
        ]
      )

    return pd.DataFrame(result.data)

  async def query_facts_with_aspects(
    self,
    graph_id: str,
    fact_set_id: Optional[str] = None,
    period_start: Optional[str] = None,
    period_end: Optional[str] = None,
    entity_id: Optional[str] = None,
    requested_dimensions: Optional[List[str]] = None,
  ) -> pd.DataFrame:
    """
    Query existing facts with all aspects (Mode 2: Existing Facts).

    This queries pre-computed facts from the main graph with their
    elements, periods, units, and dimensions.

    Args:
        graph_id: Graph ID to query (main graph)
        fact_set_id: Optional fact set filter
        period_start: Optional start date filter
        period_end: Optional end date filter
        entity_id: Optional entity filter
        requested_dimensions: Optional dimension axes to include

    Returns:
        DataFrame with fact data and aspects
    """
    # Build WHERE clause
    conditions = []
    params = {}

    if fact_set_id:
      conditions.append("fs.identifier = $fact_set_id")
      params["fact_set_id"] = fact_set_id

    if period_start and period_end:
      conditions.append("p.end_date >= $period_start")
      conditions.append("p.end_date <= $period_end")
      params["period_start"] = period_start
      params["period_end"] = period_end

    if entity_id:
      conditions.append("e.identifier = $entity_id")
      params["entity_id"] = entity_id

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

    # Query facts with all relationships
    cypher = f"""
        MATCH (fs:FactSet)-[:FACT_SET_CONTAINS_FACT]->(f:Fact)
        MATCH (f)-[:FACT_HAS_ELEMENT]->(elem:Element)
        MATCH (f)-[:FACT_HAS_PERIOD]->(p:Period)
        OPTIONAL MATCH (f)-[:FACT_HAS_ENTITY]->(e:Entity)
        OPTIONAL MATCH (f)-[:FACT_HAS_UNIT]->(u:Unit)
        OPTIONAL MATCH (f)-[:FACT_HAS_DIMENSION]->(d:FactDimension)
        {where_clause}
        RETURN f.identifier AS fact_id,
               f.numeric_value AS numeric_value,
               f.value AS text_value,
               elem.identifier AS element_id,
               elem.uri AS element_uri,
               elem.name AS element_name,
               p.identifier AS period_id,
               p.start_date AS period_start,
               p.end_date AS period_end,
               p.period_type AS period_type,
               e.identifier AS entity_id,
               e.name AS entity_name,
               u.identifier AS unit_id,
               u.name AS unit_name,
               collect(DISTINCT {
      "axis": d.axis_uri,
                   "member": d.member_uri
               }) AS dimensions
        """

    result = await self.query.query(graph_id, cypher, params)

    if not result or not result.data:
      return pd.DataFrame()

    # Convert to DataFrame and expand dimensions if needed
    df = pd.DataFrame(result.data)

    # If requested_dimensions specified, filter/expand dimension columns
    if requested_dimensions and not df.empty:
      # This would expand dimension data into separate columns
      # For now, keeping as nested structure
      pass

    return df

  async def create_view(
    self,
    graph_id: str,
    source: ViewSource,
    view_config: Optional[ViewConfig] = None,
    mapping_structure_id: Optional[str] = None,
    workspace_id: Optional[str] = None,
  ) -> ViewResponse:
    """
    Create a financial view from source data.

    This is the main entry point for view generation. It:
    1. Queries source data (transactions or facts)
    2. Applies element mappings if specified
    3. Generates pivot table presentation if configured
    4. Optionally writes to subgraph workspace

    Args:
        graph_id: Main graph ID to query data from
        source: Source configuration (transactions or fact set)
        view_config: Optional pivot table configuration
        mapping_structure_id: Optional mapping to apply for aggregation
        workspace_id: Optional subgraph to write results to

    Returns:
        ViewResponse with generated view data
    """
    start_time = datetime.now()

    # Step 1: Get source data
    if source.type == ViewSourceType.TRANSACTIONS:
      fact_data = await self.aggregate_trial_balance(
        graph_id=graph_id,
        period_start=source.period_start,
        period_end=source.period_end,
        entity_id=source.entity_id,
      )
      source_type = "trial_balance_aggregation"

    elif source.type == ViewSourceType.FACT_SET:
      fact_data = await self.query_facts_with_aspects(
        graph_id=graph_id,
        fact_set_id=source.fact_set_id,
        period_start=source.period_start,
        period_end=source.period_end,
        entity_id=source.entity_id,
      )
      source_type = "fact_set_query"

    else:
      raise ValueError(f"Unsupported source type: {source.type}")

    # Step 2: Apply element mapping if specified
    if mapping_structure_id and self.element_mapping:
      # Get mapping structure from subgraph
      mapping = await self.element_mapping.get_mapping_structure(
        workspace_id or graph_id, mapping_structure_id
      )
      if mapping:
        fact_data = self.element_mapping.apply_element_mapping(fact_data, mapping)

    # Step 3: Generate pivot table if configured
    if view_config:
      fact_data = self._generate_pivot_table(fact_data, view_config)

    # Step 4: Write to workspace if specified
    if workspace_id:
      await self._write_to_workspace(workspace_id, fact_data, source_type)

    execution_time = int((datetime.now() - start_time).total_seconds() * 1000)

    return ViewResponse(
      facts=fact_data,
      metadata={
        "source": source_type,
        "fact_count": len(fact_data),
        "period_start": source.period_start,
        "period_end": source.period_end,
        "has_mapping": mapping_structure_id is not None,
        "has_pivot": view_config is not None,
      },
      execution_time_ms=execution_time,
    )

  def _generate_pivot_table(
    self, fact_data: pd.DataFrame, view_config: ViewConfig
  ) -> pd.DataFrame:
    """
    Generate pivot table from fact data.

    Args:
        fact_data: Source fact DataFrame
        view_config: Pivot configuration

    Returns:
        Pivoted DataFrame
    """
    if fact_data.empty:
      return fact_data

    # Determine value column
    value_col = (
      "numeric_value" if "numeric_value" in fact_data.columns else "net_balance"
    )

    # Build index (rows) and columns lists
    index_cols = []
    for axis in view_config.rows:
      if axis.type == "element":
        index_cols.append("element_name")
      elif axis.type == "period":
        index_cols.append("period_end")
      elif axis.type == "dimension" and axis.dimension_axis:
        # This would map dimension to column name
        index_cols.append(f"dim_{axis.dimension_axis}")

    column_cols = []
    for axis in view_config.columns:
      if axis.type == "element":
        column_cols.append("element_name")
      elif axis.type == "period":
        column_cols.append("period_end")
      elif axis.type == "dimension" and axis.dimension_axis:
        column_cols.append(f"dim_{axis.dimension_axis}")

    # Apply pivot_table
    if index_cols and column_cols:
      pivoted = pd.pivot_table(
        fact_data,
        values=value_col,
        index=index_cols,
        columns=column_cols,
        aggfunc="sum",
        fill_value=0,
      )
      # Flatten multi-index if needed
      if isinstance(pivoted.columns, pd.MultiIndex):
        pivoted.columns = ["_".join(map(str, col)) for col in pivoted.columns]
      pivoted = pivoted.reset_index()

    elif index_cols:
      # Group by index only
      pivoted = fact_data.groupby(index_cols)[value_col].sum().reset_index()

    else:
      pivoted = fact_data

    # Add subtotals if requested
    for axis in view_config.rows:
      if axis.include_subtotals and axis.type == "element":
        pivoted = self._add_subtotals(pivoted, axis.hierarchy_root)

    return pivoted

  def _add_subtotals(
    self, df: pd.DataFrame, hierarchy_root: str = None
  ) -> pd.DataFrame:
    """
    Add subtotal rows to DataFrame.

    This would implement hierarchical subtotal logic.
    Simplified for illustration.
    """
    # This would:
    # 1. Query hierarchy from graph
    # 2. Group elements by parent
    # 3. Calculate subtotals
    # 4. Insert subtotal rows
    return df

  async def _write_to_workspace(
    self, workspace_id: str, fact_data: pd.DataFrame, source_type: str
  ):
    """
    Write view data to subgraph workspace.

    Args:
        workspace_id: Subgraph workspace ID
        fact_data: Fact DataFrame to write
        source_type: Source type for metadata
    """
    if fact_data.empty:
      return

    # Create View node in workspace
    import uuid

    view_id = str(uuid.uuid4())

    cypher = f"""
        CREATE (v:View {{
            identifier: '{view_id}',
            source_type: '{source_type}',
            created_at: datetime(),
            fact_count: {len(fact_data)}
        }})
        RETURN v.identifier as view_id
        """

    await self.query.query(workspace_id, cypher)

    # Write facts in batches
    for batch_start in range(0, len(fact_data), 100):
      batch_end = min(batch_start + 100, len(fact_data))
      batch = fact_data.iloc[batch_start:batch_end]

      # Build CREATE statements for batch
      creates = []
      for _, row in batch.iterrows():
        fact_props = {
          "identifier": str(uuid.uuid4()),
          "element_id": row.get("element_id", ""),
          "value": float(row.get("net_balance", 0)),
          "period_end": row.get("period_end", ""),
        }

        # Convert to Cypher properties string
        props_str = ", ".join(
          [
            f"{k}: '{v}'" if isinstance(v, str) else f"{k}: {v}"
            for k, v in fact_props.items()
          ]
        )

        creates.append(f"CREATE (f:ViewFact {{{props_str}}})")

      batch_cypher = "\n".join(creates)
      await self.query.query(workspace_id, batch_cypher)

  async def build_fact_grid(
    self,
    graph_id: str,
    view_source: ViewSource,
    view_config: ViewConfig,
    workspace_id: Optional[str] = None,
  ) -> Dict[str, Any]:
    """
    Build a Fact Grid data structure for flexible presentation.

    This follows the hypercube model from the architecture document,
    creating a multidimensional structure that can generate multiple
    presentation formats.

    Args:
        graph_id: Main graph to query data from
        view_source: Source configuration
        view_config: View configuration
        workspace_id: Optional workspace to write to

    Returns:
        Fact Grid structure with dimensions, measures, and hierarchies
    """
    # Get base fact data
    view_response = await self.create_view(
      graph_id=graph_id,
      source=view_source,
      view_config=view_config,
      workspace_id=workspace_id,
    )

    fact_data = view_response.facts

    # Build Fact Grid structure
    fact_grid = {
      "dimensions": self._extract_dimensions(fact_data),
      "measures": self._extract_measures(fact_data),
      "hierarchies": await self._build_hierarchies(graph_id, fact_data),
      "facts": fact_data.to_dict("records"),
      "metadata": {
        "fact_count": len(fact_data),
        "source": view_source.type.value,
        "created_at": datetime.now().isoformat(),
        **view_response.metadata,
      },
    }

    return fact_grid

  def _extract_dimensions(self, fact_data: pd.DataFrame) -> List[Dict[str, Any]]:
    """Extract dimensions from fact data"""
    dimensions = []

    # Time dimension
    if "period_end" in fact_data.columns:
      dimensions.append(
        {
          "name": "Time",
          "type": "temporal",
          "values": fact_data["period_end"].unique().tolist(),
        }
      )

    # Element dimension
    if "element_name" in fact_data.columns:
      dimensions.append(
        {
          "name": "Element",
          "type": "hierarchical",
          "values": fact_data["element_name"].unique().tolist(),
        }
      )

    # Entity dimension
    if "entity_name" in fact_data.columns:
      dimensions.append(
        {
          "name": "Entity",
          "type": "categorical",
          "values": fact_data["entity_name"].unique().tolist(),
        }
      )

    return dimensions

  def _extract_measures(self, fact_data: pd.DataFrame) -> List[Dict[str, Any]]:
    """Extract measures from fact data"""
    measures = []

    # Numeric measures
    for col in ["net_balance", "numeric_value", "total_debits", "total_credits"]:
      if col in fact_data.columns:
        measures.append(
          {"name": col, "type": "numeric", "aggregation": "sum", "format": "currency"}
        )

    return measures

  async def _build_hierarchies(
    self, graph_id: str, fact_data: pd.DataFrame
  ) -> Dict[str, Any]:
    """Build element hierarchies from graph"""
    if "element_id" not in fact_data.columns:
      return {}

    element_ids = fact_data["element_id"].unique().tolist()

    # Query element hierarchy from graph
    cypher = """
        MATCH (e:Element)
        WHERE e.identifier IN $element_ids
        OPTIONAL MATCH (e)-[:ELEMENT_HAS_PARENT]->(parent:Element)
        RETURN e.identifier as element_id,
               e.name as element_name,
               parent.identifier as parent_id,
               parent.name as parent_name
        """

    result = await self.query.query(graph_id, cypher, {"element_ids": element_ids})

    if not result or not result.data:
      return {}

    # Build hierarchy tree
    hierarchy = {}
    for row in result.data:
      element_id = row["element_id"]
      parent_id = row.get("parent_id")

      if parent_id:
        if parent_id not in hierarchy:
          hierarchy[parent_id] = {"name": row["parent_name"], "children": []}
        hierarchy[parent_id]["children"].append(element_id)

      if element_id not in hierarchy:
        hierarchy[element_id] = {"name": row["element_name"], "children": []}

    return hierarchy
