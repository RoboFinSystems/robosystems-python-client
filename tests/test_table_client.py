"""Unit tests for TableClient."""

import pytest
from unittest.mock import Mock, patch
from robosystems_client.extensions.table_client import (
  TableClient,
  TableInfo,
  QueryResult,
)


@pytest.mark.unit
class TestTableDataclasses:
  """Test suite for table-related dataclasses."""

  def test_table_info(self):
    """Test TableInfo dataclass."""
    info = TableInfo(
      table_name="Entity",
      table_type="parquet",
      row_count=100,
      file_count=3,
      total_size_bytes=50000,
    )

    assert info.table_name == "Entity"
    assert info.table_type == "parquet"
    assert info.row_count == 100
    assert info.file_count == 3
    assert info.total_size_bytes == 50000

  def test_query_result(self):
    """Test QueryResult dataclass."""
    result = QueryResult(
      columns=["name", "revenue"],
      rows=[["ACME", 1000000], ["Beta Corp", 2000000]],
      row_count=2,
      execution_time_ms=45.0,
    )

    assert result.columns == ["name", "revenue"]
    assert len(result.rows) == 2
    assert result.row_count == 2
    assert result.execution_time_ms == 45.0
    assert result.success is True
    assert result.error is None

  def test_query_result_with_error(self):
    """Test QueryResult with error."""
    result = QueryResult(
      columns=[],
      rows=[],
      row_count=0,
      execution_time_ms=0,
      success=False,
      error="SQL syntax error",
    )

    assert result.success is False
    assert result.error == "SQL syntax error"


@pytest.mark.unit
class TestTableClientInit:
  """Test suite for TableClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = TableClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}


@pytest.mark.unit
class TestTableList:
  """Test suite for TableClient.list method."""

  @patch("robosystems_client.extensions.table_client.list_tables")
  def test_list_tables(self, mock_list, mock_config, graph_id):
    """Test listing tables."""
    mock_table_1 = Mock()
    mock_table_1.table_name = "Entity"
    mock_table_1.table_type = "parquet"
    mock_table_1.row_count = 100
    mock_table_1.file_count = 2
    mock_table_1.total_size_bytes = 50000

    mock_table_2 = Mock()
    mock_table_2.table_name = "Transaction"
    mock_table_2.table_type = "parquet"
    mock_table_2.row_count = 500
    mock_table_2.file_count = 1
    mock_table_2.total_size_bytes = 120000

    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock()
    mock_resp.parsed.tables = [mock_table_1, mock_table_2]
    mock_list.return_value = mock_resp

    client = TableClient(mock_config)
    tables = client.list(graph_id)

    assert len(tables) == 2
    assert tables[0].table_name == "Entity"
    assert tables[0].row_count == 100
    assert tables[1].table_name == "Transaction"
    assert tables[1].row_count == 500

  @patch("robosystems_client.extensions.table_client.list_tables")
  def test_list_tables_failure(self, mock_list, mock_config, graph_id):
    """Test list tables returns empty list on failure."""
    mock_resp = Mock()
    mock_resp.status_code = 500
    mock_resp.parsed = None
    mock_list.return_value = mock_resp

    client = TableClient(mock_config)
    tables = client.list(graph_id)

    assert tables == []

  def test_list_tables_no_token(self, mock_config, graph_id):
    """Test list tables returns empty list without token."""
    mock_config["token"] = None
    client = TableClient(mock_config)
    tables = client.list(graph_id)

    assert tables == []

  @patch("robosystems_client.extensions.table_client.list_tables")
  def test_list_tables_empty(self, mock_list, mock_config, graph_id):
    """Test listing when no tables exist."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock()
    mock_resp.parsed.tables = []
    mock_list.return_value = mock_resp

    client = TableClient(mock_config)
    tables = client.list(graph_id)

    assert tables == []


@pytest.mark.unit
class TestTableQuery:
  """Test suite for TableClient.query method."""

  @patch("robosystems_client.extensions.table_client.query_tables")
  def test_query_success(self, mock_query, mock_config, graph_id):
    """Test successful SQL query."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock()
    mock_resp.parsed.columns = ["name", "ticker"]
    mock_resp.parsed.rows = [["ACME Corp", "ACM"], ["Beta Inc", "BET"]]
    mock_resp.parsed.execution_time_ms = 30.0
    mock_query.return_value = mock_resp

    client = TableClient(mock_config)
    result = client.query(graph_id, "SELECT name, ticker FROM Entity")

    assert result.success is True
    assert result.columns == ["name", "ticker"]
    assert len(result.rows) == 2
    assert result.row_count == 2
    assert result.execution_time_ms == 30.0

  @patch("robosystems_client.extensions.table_client.query_tables")
  def test_query_with_limit(self, mock_query, mock_config, graph_id):
    """Test query with limit appended."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock()
    mock_resp.parsed.columns = ["name"]
    mock_resp.parsed.rows = [["ACME"]]
    mock_resp.parsed.execution_time_ms = 10.0
    mock_query.return_value = mock_resp

    client = TableClient(mock_config)
    client.query(graph_id, "SELECT name FROM Entity", limit=5)

    call_kwargs = mock_query.call_args[1]
    assert "LIMIT 5" in call_kwargs["body"].sql

  @patch("robosystems_client.extensions.table_client.query_tables")
  def test_query_strips_trailing_semicolon(self, mock_query, mock_config, graph_id):
    """Test query strips trailing semicolon before adding LIMIT."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock()
    mock_resp.parsed.columns = ["name"]
    mock_resp.parsed.rows = []
    mock_resp.parsed.execution_time_ms = 5.0
    mock_query.return_value = mock_resp

    client = TableClient(mock_config)
    client.query(graph_id, "SELECT name FROM Entity;", limit=10)

    call_kwargs = mock_query.call_args[1]
    sql = call_kwargs["body"].sql
    assert not sql.endswith("; LIMIT 10")
    assert sql.endswith("LIMIT 10")

  @patch("robosystems_client.extensions.table_client.query_tables")
  def test_query_failure(self, mock_query, mock_config, graph_id):
    """Test query failure."""
    mock_resp = Mock()
    mock_resp.status_code = 400
    mock_resp.parsed = None
    mock_query.return_value = mock_resp

    client = TableClient(mock_config)
    result = client.query(graph_id, "INVALID SQL")

    assert result.success is False
    assert "Query failed" in result.error

  def test_query_no_token(self, mock_config, graph_id):
    """Test query fails without token."""
    mock_config["token"] = None
    client = TableClient(mock_config)
    result = client.query(graph_id, "SELECT 1")

    assert result.success is False
    assert "No API key" in result.error

  @patch("robosystems_client.extensions.table_client.query_tables")
  def test_query_exception_handling(self, mock_query, mock_config, graph_id):
    """Test query handles unexpected exceptions."""
    mock_query.side_effect = Exception("Network error")

    client = TableClient(mock_config)
    result = client.query(graph_id, "SELECT 1")

    assert result.success is False
    assert "Network error" in result.error
