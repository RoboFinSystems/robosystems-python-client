"""Tests for DataFrame utilities"""

import pytest
from unittest.mock import Mock, patch
import tempfile
import os

# Make pandas optional for tests
try:
  import pandas as pd

  HAS_PANDAS = True
except ImportError:
  HAS_PANDAS = False
  pd = None

# Only run tests if pandas is available
pytestmark = pytest.mark.skipif(not HAS_PANDAS, reason="pandas not installed")

if HAS_PANDAS:
  from robosystems_client.extensions.dataframe_utils import (
    query_result_to_dataframe,
    parse_datetime_columns,
    stream_to_dataframe,
    dataframe_to_cypher_params,
    export_query_to_csv,
    compare_dataframes,
    DataFrameQueryClient,
  )


class TestQueryResultToDataFrame:
  """Test converting query results to DataFrames"""

  def test_query_result_to_dataframe_basic(self):
    """Test basic conversion from query result to DataFrame"""
    result = {
      "data": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
      ],
      "columns": ["name", "age"],
      "row_count": 3,
    }

    df = query_result_to_dataframe(result)

    assert len(df) == 3
    assert list(df.columns) == ["name", "age"]
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[1]["age"] == 25

  def test_query_result_to_dataframe_nested(self):
    """Test conversion with nested data"""
    result = {
      "data": [
        {"name": "Alice", "company": {"name": "TechCorp", "revenue": 1000000}},
        {"name": "Bob", "company": {"name": "StartupInc", "revenue": 500000}},
      ],
      "columns": ["name", "company"],
    }

    df = query_result_to_dataframe(result, normalize_nested=True)

    assert "name" in df.columns
    assert "company.name" in df.columns
    assert "company.revenue" in df.columns
    assert df.iloc[0]["company.name"] == "TechCorp"

  def test_query_result_to_dataframe_empty(self):
    """Test conversion of empty result"""
    result = {"data": [], "columns": ["name", "age"], "row_count": 0}

    df = query_result_to_dataframe(result)

    assert len(df) == 0
    assert list(df.columns) == ["name", "age"]

  def test_query_result_to_dataframe_with_dates(self):
    """Test conversion with date parsing"""
    result = {
      "data": [
        {"name": "Alice", "created_at": "2023-01-15T10:30:00"},
        {"name": "Bob", "created_at": "2023-02-20T14:45:00"},
      ],
      "columns": ["name", "created_at"],
    }

    df = query_result_to_dataframe(result, parse_dates=True)

    assert pd.api.types.is_datetime64_any_dtype(df["created_at"])
    assert df.iloc[0]["created_at"].year == 2023


class TestParseDateTimeColumns:
  """Test datetime parsing functionality"""

  def test_parse_datetime_columns_specific(self):
    """Test parsing specific datetime columns"""
    df = pd.DataFrame(
      {
        "name": ["Alice", "Bob"],
        "created_at": ["2023-01-15", "2023-02-20"],
        "updated_at": ["2023-01-16T10:30:00", "2023-02-21T14:45:00"],
        "count": [1, 2],
      }
    )

    df = parse_datetime_columns(df, date_columns=["created_at", "updated_at"])

    assert pd.api.types.is_datetime64_any_dtype(df["created_at"])
    assert pd.api.types.is_datetime64_any_dtype(df["updated_at"])
    assert not pd.api.types.is_datetime64_any_dtype(df["count"])

  def test_parse_datetime_columns_infer(self):
    """Test automatic datetime column inference"""
    df = pd.DataFrame(
      {
        "name": ["Alice", "Bob"],
        "timestamp": ["2023-01-15T10:30:00", "2023-02-20T14:45:00"],
        "not_a_date": ["abc", "def"],
      }
    )

    df = parse_datetime_columns(df, infer=True)

    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])
    assert df["not_a_date"].dtype == "object"


class TestStreamToDataFrame:
  """Test streaming results to DataFrame"""

  def test_stream_to_dataframe_basic(self):
    """Test converting stream to DataFrame"""

    def mock_stream():
      for i in range(10):
        yield {"id": i, "value": i * 2}

    df = stream_to_dataframe(mock_stream(), chunk_size=3)

    assert len(df) == 10
    assert df.iloc[5]["value"] == 10

  def test_stream_to_dataframe_with_callback(self):
    """Test stream with chunk callback"""
    chunk_counts = []

    def on_chunk(chunk_df, total):
      chunk_counts.append(len(chunk_df))

    def mock_stream():
      for i in range(10):
        yield {"id": i, "value": i * 2}

    df = stream_to_dataframe(mock_stream(), chunk_size=3, on_chunk=on_chunk)

    assert len(df) == 10
    assert chunk_counts == [3, 3, 3, 1]  # 3 chunks of 3, 1 chunk of 1


class TestDataFrameToCypherParams:
  """Test DataFrame to Cypher parameter conversion"""

  def test_dataframe_to_cypher_params(self):
    """Test converting DataFrame to Cypher parameters"""
    df = pd.DataFrame(
      {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [30, 25, 35],
        "active": [True, False, True],
      }
    )

    params = dataframe_to_cypher_params(df)

    assert "data" in params
    assert len(params["data"]) == 3
    assert params["data"][0]["name"] == "Alice"
    assert params["data"][1]["age"] == 25

  def test_dataframe_to_cypher_params_with_nan(self):
    """Test handling NaN values"""
    df = pd.DataFrame(
      {"name": ["Alice", "Bob"], "age": [30, pd.NA], "score": [95.5, None]}
    )

    params = dataframe_to_cypher_params(df, param_name="records")

    assert "records" in params
    assert params["records"][1]["age"] is None
    assert params["records"][1]["score"] is None


class TestExportQueryToCSV:
  """Test CSV export functionality"""

  @patch("robosystems_client.extensions.dataframe_utils.logger")
  def test_export_query_to_csv(self, mock_logger):
    """Test exporting query results to CSV"""
    mock_client = Mock()

    def mock_stream(*args, **kwargs):
      for i in range(5):
        yield {"id": i, "name": f"Item {i}"}

    mock_client.stream_query = Mock(side_effect=mock_stream)

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
      temp_file = f.name

    try:
      count = export_query_to_csv(
        mock_client, "graph_id", "MATCH (n) RETURN n", temp_file, chunk_size=2
      )

      assert count == 5
      mock_logger.info.assert_called()

      # Verify CSV content
      df = pd.read_csv(temp_file)
      assert len(df) == 5
      assert df.iloc[0]["name"] == "Item 0"

    finally:
      if os.path.exists(temp_file):
        os.unlink(temp_file)


class TestCompareDataFrames:
  """Test DataFrame comparison"""

  def test_compare_dataframes_with_keys(self):
    """Test comparing DataFrames with key columns"""
    df1 = pd.DataFrame(
      {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"], "age": [30, 25, 35]}
    )

    df2 = pd.DataFrame(
      {"id": [1, 2, 4], "name": ["Alice", "Robert", "David"], "age": [31, 25, 40]}
    )

    diff = compare_dataframes(df1, df2, key_columns=["id"])

    assert "_merge" in diff.columns
    assert "name_old" in diff.columns
    assert "name_new" in diff.columns

  def test_compare_dataframes_without_keys(self):
    """Test comparing DataFrames without keys"""
    df1 = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})

    df2 = pd.DataFrame({"name": ["Alice", "Charlie"], "age": [30, 35]})

    diff = compare_dataframes(df1, df2)

    assert len(diff) == 2  # Bob and Charlie rows


class TestDataFrameQueryClient:
  """Test DataFrameQueryClient class"""

  def test_query_df(self):
    """Test query_df method"""
    mock_client = Mock()
    mock_client.query.return_value = {
      "data": [{"name": "Alice"}, {"name": "Bob"}],
      "columns": ["name"],
      "row_count": 2,
    }

    df_client = DataFrameQueryClient(mock_client)
    df = df_client.query_df("graph_id", "MATCH (n) RETURN n")

    assert len(df) == 2
    assert df.iloc[0]["name"] == "Alice"
    mock_client.query.assert_called_once()

  def test_stream_df(self):
    """Test stream_df method"""
    mock_client = Mock()

    def mock_stream(*args, **kwargs):
      for i in range(3):
        yield {"id": i, "value": i * 10}

    mock_client.stream_query.return_value = mock_stream()

    df_client = DataFrameQueryClient(mock_client)
    df = df_client.stream_df("graph_id", "MATCH (n) RETURN n")

    assert len(df) == 3
    assert df.iloc[1]["value"] == 10

  def test_query_batch_df(self):
    """Test query_batch_df method"""
    mock_client = Mock()
    mock_client.query_batch.return_value = [
      {"data": [{"count": 10}], "columns": ["count"]},
      {"data": [{"count": 20}], "columns": ["count"]},
      {"error": "Query failed", "query": "INVALID"},
    ]

    df_client = DataFrameQueryClient(mock_client)
    dfs = df_client.query_batch_df(
      "graph_id",
      [
        "MATCH (p:Person) RETURN count(p)",
        "MATCH (c:Company) RETURN count(c)",
        "INVALID",
      ],
    )

    assert len(dfs) == 3
    assert dfs[0].iloc[0]["count"] == 10
    assert dfs[1].iloc[0]["count"] == 20
    assert "error" in dfs[2].columns

  def test_export_to_csv(self):
    """Test export_to_csv method"""
    mock_client = Mock()

    with patch(
      "robosystems_client.extensions.dataframe_utils.export_query_to_csv"
    ) as mock_export:
      mock_export.return_value = 100

      df_client = DataFrameQueryClient(mock_client)
      count = df_client.export_to_csv("graph_id", "MATCH (n) RETURN n", "output.csv")

      assert count == 100
      mock_export.assert_called_once()
