"""Pandas DataFrame integration utilities for RoboSystems SDK

Provides seamless integration between query results and Pandas DataFrames.
"""

from typing import Dict, Any, Optional, List, Union, TYPE_CHECKING
import logging

if TYPE_CHECKING:
  from .query_client import QueryResult

# Make pandas optional to avoid forcing dependency
try:
  import pandas as pd

  HAS_PANDAS = True
except ImportError:
  HAS_PANDAS = False
  pd = None

logger = logging.getLogger(__name__)


def require_pandas():
  """Check if pandas is available, raise helpful error if not"""
  if not HAS_PANDAS:
    raise ImportError(
      "Pandas is required for DataFrame features. Install it with: pip install pandas"
    )


def query_result_to_dataframe(
  result: Union[Dict[str, Any], "QueryResult"],
  normalize_nested: bool = True,
  parse_dates: bool = True,
) -> "pd.DataFrame":
  """Convert query result to Pandas DataFrame

  Args:
      result: Query result dict or QueryResult object
      normalize_nested: Flatten nested dictionaries in results
      parse_dates: Automatically parse date/datetime strings

  Returns:
      Pandas DataFrame with query results

  Example:
      >>> result = query_client.query(graph_id, "MATCH (c:Company) RETURN c")
      >>> df = query_result_to_dataframe(result)
      >>> print(df.head())
  """
  require_pandas()

  # Handle QueryResult object
  if hasattr(result, "data") and hasattr(result, "columns"):
    data = result.data
    columns = result.columns
  # Handle dict result
  elif isinstance(result, dict):
    data = result.get("data", [])
    columns = result.get("columns", [])
  else:
    raise ValueError("Invalid result format")

  # Create DataFrame
  if not data:
    # Empty DataFrame with columns
    df = pd.DataFrame(columns=columns if columns else [])
  elif normalize_nested and data and isinstance(data[0], dict):
    # Use json_normalize for nested data
    df = pd.json_normalize(data)
  else:
    df = pd.DataFrame(data, columns=columns if columns else None)

  # Parse dates if requested
  if parse_dates and not df.empty:
    df = parse_datetime_columns(df)

  return df


def parse_datetime_columns(
  df: "pd.DataFrame", date_columns: Optional[List[str]] = None, infer: bool = True
) -> "pd.DataFrame":
  """Parse datetime columns in DataFrame

  Args:
      df: Input DataFrame
      date_columns: Specific columns to parse as dates
      infer: Automatically infer date columns

  Returns:
      DataFrame with parsed datetime columns

  Example:
      >>> df = parse_datetime_columns(df, date_columns=['created_at', 'updated_at'])
  """
  require_pandas()

  if date_columns:
    for col in date_columns:
      if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

  elif infer:
    # Infer datetime columns
    for col in df.columns:
      if df[col].dtype == "object":
        # Check if column contains date-like strings
        sample = df[col].dropna().head(10)
        if len(sample) > 0:
          try:
            # Try to parse sample
            pd.to_datetime(sample, errors="raise")
            # If successful, parse entire column
            df[col] = pd.to_datetime(df[col], errors="coerce")
          except (ValueError, TypeError):
            # Not a date column
            pass

  return df


def stream_to_dataframe(
  stream_iterator,
  chunk_size: int = 10000,
  columns: Optional[List[str]] = None,
  on_chunk: Optional[callable] = None,
) -> "pd.DataFrame":
  """Convert streaming query results to DataFrame

  Args:
      stream_iterator: Iterator from stream_query
      chunk_size: Process records in chunks
      columns: Column names (will be inferred if not provided)
      on_chunk: Callback for each chunk processed

  Returns:
      Complete DataFrame from streamed results

  Example:
      >>> stream = query_client.stream_query(graph_id, "MATCH (n) RETURN n")
      >>> df = stream_to_dataframe(stream, chunk_size=5000)
  """
  require_pandas()

  chunks = []
  current_chunk = []

  for i, record in enumerate(stream_iterator):
    current_chunk.append(record)

    if len(current_chunk) >= chunk_size:
      # Process chunk
      chunk_df = pd.DataFrame(current_chunk, columns=columns)
      chunks.append(chunk_df)

      if on_chunk:
        on_chunk(chunk_df, i + 1)

      current_chunk = []

  # Process remaining records
  if current_chunk:
    chunk_df = pd.DataFrame(current_chunk, columns=columns)
    chunks.append(chunk_df)

    if on_chunk:
      on_chunk(chunk_df, len(current_chunk))

  # Combine all chunks
  if chunks:
    return pd.concat(chunks, ignore_index=True)
  else:
    return pd.DataFrame(columns=columns if columns else [])


def dataframe_to_cypher_params(
  df: "pd.DataFrame", param_name: str = "data"
) -> Dict[str, List[Dict[str, Any]]]:
  """Convert DataFrame to Cypher query parameters

  Args:
      df: DataFrame to convert
      param_name: Parameter name for query

  Returns:
      Dict with parameter suitable for Cypher queries

  Example:
      >>> df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})
      >>> params = dataframe_to_cypher_params(df)
      >>> query = "UNWIND $data AS row CREATE (p:Person {name: row.name, age: row.age})"
      >>> result = query_client.query(graph_id, query, params)
  """
  require_pandas()
  import numpy as np

  # Convert DataFrame to list of dicts
  # First convert to dict format
  records = df.to_dict("records")

  # Then clean up NaN/NA values in each record
  for record in records:
    for key, value in record.items():
      # Check for any form of missing value (NaN, NA, NaT)
      if pd.isna(value):
        record[key] = None
      # Also handle numpy nan explicitly
      elif isinstance(value, float) and np.isnan(value):
        record[key] = None

  return {param_name: records}


def export_query_to_csv(
  query_client,
  graph_id: str,
  query: str,
  output_file: str,
  parameters: Optional[Dict[str, Any]] = None,
  chunk_size: int = 5000,
  **csv_kwargs,
) -> int:
  """Export query results directly to CSV file

  Args:
      query_client: QueryClient instance
      graph_id: Graph ID to query
      query: Cypher query
      output_file: Output CSV file path
      parameters: Query parameters
      chunk_size: Records per chunk for streaming
      **csv_kwargs: Additional arguments for to_csv

  Returns:
      Number of records exported

  Example:
      >>> count = export_query_to_csv(
      ...     query_client, 'graph_id',
      ...     "MATCH (c:Company) RETURN c.name, c.revenue",
      ...     "companies.csv"
      ... )
      >>> print(f"Exported {count} records")
  """
  require_pandas()

  # Stream query results
  stream = query_client.stream_query(graph_id, query, parameters, chunk_size)

  # Process in chunks for memory efficiency
  total_count = 0
  first_chunk = True

  chunks = []
  for record in stream:
    chunks.append(record)

    if len(chunks) >= chunk_size:
      # Convert chunk to DataFrame
      df_chunk = pd.DataFrame(chunks)

      # Write to CSV
      if first_chunk:
        df_chunk.to_csv(output_file, index=False, **csv_kwargs)
        first_chunk = False
      else:
        df_chunk.to_csv(output_file, mode="a", index=False, header=False, **csv_kwargs)

      total_count += len(chunks)
      chunks = []

  # Write remaining records
  if chunks:
    df_chunk = pd.DataFrame(chunks)
    if first_chunk:
      df_chunk.to_csv(output_file, index=False, **csv_kwargs)
    else:
      df_chunk.to_csv(output_file, mode="a", index=False, header=False, **csv_kwargs)
    total_count += len(chunks)

  logger.info(f"Exported {total_count} records to {output_file}")
  return total_count


def compare_dataframes(
  df1: "pd.DataFrame",
  df2: "pd.DataFrame",
  key_columns: Optional[List[str]] = None,
  compare_columns: Optional[List[str]] = None,
) -> "pd.DataFrame":
  """Compare two DataFrames and return differences

  Args:
      df1: First DataFrame
      df2: Second DataFrame
      key_columns: Columns to use as keys for comparison
      compare_columns: Specific columns to compare

  Returns:
      DataFrame with differences

  Example:
      >>> old_data = query_to_dataframe(old_result)
      >>> new_data = query_to_dataframe(new_result)
      >>> diff = compare_dataframes(old_data, new_data, key_columns=['id'])
  """
  require_pandas()

  if key_columns:
    # Merge on key columns
    merged = pd.merge(
      df1, df2, on=key_columns, how="outer", suffixes=("_old", "_new"), indicator=True
    )

    # Find differences
    if compare_columns:
      for col in compare_columns:
        col_old = f"{col}_old"
        col_new = f"{col}_new"
        if col_old in merged.columns and col_new in merged.columns:
          merged[f"{col}_changed"] = merged[col_old] != merged[col_new]

    return merged
  else:
    # Compare entire DataFrames
    return pd.concat([df1, df2]).drop_duplicates(keep=False)


class DataFrameQueryClient:
  """Query client with built-in DataFrame support"""

  def __init__(self, query_client):
    """Initialize with a QueryClient instance

    Args:
        query_client: Existing QueryClient instance
    """
    require_pandas()
    self.query_client = query_client

  def query_df(
    self,
    graph_id: str,
    query: str,
    parameters: Optional[Dict[str, Any]] = None,
    normalize_nested: bool = True,
    parse_dates: bool = True,
  ) -> "pd.DataFrame":
    """Execute query and return results as DataFrame

    Args:
        graph_id: Graph ID to query
        query: Cypher query
        parameters: Query parameters
        normalize_nested: Flatten nested dictionaries
        parse_dates: Parse datetime columns

    Returns:
        Query results as pandas DataFrame

    Example:
        >>> df_client = DataFrameQueryClient(query_client)
        >>> df = df_client.query_df('graph_id', "MATCH (c:Company) RETURN c")
        >>> print(df.describe())
    """
    result = self.query_client.query(graph_id, query, parameters)
    return query_result_to_dataframe(result, normalize_nested, parse_dates)

  def stream_df(
    self,
    graph_id: str,
    query: str,
    parameters: Optional[Dict[str, Any]] = None,
    chunk_size: int = 10000,
  ) -> "pd.DataFrame":
    """Stream query results and return as DataFrame

    Args:
        graph_id: Graph ID to query
        query: Cypher query
        parameters: Query parameters
        chunk_size: Records per chunk

    Returns:
        Complete DataFrame from streamed results

    Example:
        >>> df = df_client.stream_df(
        ...     'graph_id',
        ...     "MATCH (n) RETURN n",
        ...     chunk_size=5000
        ... )
    """
    stream = self.query_client.stream_query(graph_id, query, parameters, chunk_size)
    return stream_to_dataframe(stream, chunk_size)

  def query_batch_df(
    self,
    graph_id: str,
    queries: List[str],
    parameters_list: Optional[List[Dict[str, Any]]] = None,
  ) -> List["pd.DataFrame"]:
    """Execute multiple queries and return as DataFrames

    Args:
        graph_id: Graph ID to query
        queries: List of Cypher queries
        parameters_list: List of parameter dicts

    Returns:
        List of DataFrames, one per query

    Example:
        >>> dfs = df_client.query_batch_df('graph_id', [
        ...     "MATCH (p:Person) RETURN p",
        ...     "MATCH (c:Company) RETURN c"
        ... ])
    """
    results = self.query_client.query_batch(graph_id, queries, parameters_list)
    dfs = []

    for result in results:
      if isinstance(result, dict) and "error" in result:
        # Create error DataFrame
        dfs.append(pd.DataFrame([result]))
      else:
        dfs.append(query_result_to_dataframe(result))

    return dfs

  def export_to_csv(
    self,
    graph_id: str,
    query: str,
    output_file: str,
    parameters: Optional[Dict[str, Any]] = None,
    **csv_kwargs,
  ) -> int:
    """Export query results to CSV

    Args:
        graph_id: Graph ID to query
        query: Cypher query
        output_file: Output CSV file path
        parameters: Query parameters
        **csv_kwargs: Additional arguments for to_csv

    Returns:
        Number of records exported
    """
    return export_query_to_csv(
      self.query_client, graph_id, query, output_file, parameters, **csv_kwargs
    )
