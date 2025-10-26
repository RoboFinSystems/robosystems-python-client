"""Shared test fixtures for RoboSystems extension tests."""

import pytest
from io import BytesIO
from typing import Dict, Any


@pytest.fixture
def mock_config() -> Dict[str, Any]:
  """Mock configuration for extension clients."""
  return {
    "base_url": "http://localhost:8000",
    "token": "test-api-key",
    "headers": {"X-API-Key": "test-api-key"},
  }


@pytest.fixture
def graph_id() -> str:
  """Test graph ID."""
  return "test-graph-123"


@pytest.fixture
def table_name() -> str:
  """Test table name."""
  return "Entity"


@pytest.fixture
def operation_id() -> str:
  """Test operation ID."""
  return "op-123-456"


@pytest.fixture
def sample_parquet_buffer() -> BytesIO:
  """Create a sample Parquet file in memory."""
  try:
    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq

    # Create sample DataFrame
    df = pd.DataFrame(
      {
        "identifier": ["entity_001", "entity_002", "entity_003"],
        "name": ["Company A", "Company B", "Company C"],
        "ticker": ["CMPA", "CMPB", "CMPC"],
      }
    )

    # Convert to Parquet in memory
    buffer = BytesIO()
    table = pa.Table.from_pandas(df)
    pq.write_table(table, buffer)
    buffer.seek(0)
    return buffer
  except ImportError:
    # If pandas/pyarrow not available, create a minimal buffer
    buffer = BytesIO(b"fake parquet data")
    buffer.seek(0)
    return buffer


@pytest.fixture
def mock_upload_response() -> Dict[str, Any]:
  """Mock response from upload URL endpoint."""
  return {
    "upload_url": "http://localhost:4566/test-bucket/file-123.parquet?signature=xyz",
    "file_id": "file-123",
  }


@pytest.fixture
def mock_table_list_response() -> Dict[str, Any]:
  """Mock response from list tables endpoint."""
  return {
    "tables": [
      {
        "table_name": "Entity",
        "row_count": 100,
        "file_count": 2,
        "total_size_bytes": 50000,
      },
      {
        "table_name": "Transaction",
        "row_count": 500,
        "file_count": 1,
        "total_size_bytes": 120000,
      },
    ]
  }


@pytest.fixture
def mock_ingest_response() -> Dict[str, Any]:
  """Mock response from ingest endpoint."""
  return {
    "operation_id": "op-ingest-123",
    "message": "Ingestion started",
    "status": "accepted",
  }


@pytest.fixture
def mock_query_response() -> Dict[str, Any]:
  """Mock response from query endpoint."""
  return {
    "data": [
      {"n.name": "Entity 1", "n.ticker": "ENT1"},
      {"n.name": "Entity 2", "n.ticker": "ENT2"},
    ],
    "row_count": 2,
    "execution_time_ms": 45,
  }


@pytest.fixture
def mock_operation_status_response() -> Dict[str, Any]:
  """Mock response from operation status endpoint."""
  return {
    "operation_id": "op-123-456",
    "status": "completed",
    "progress": 100,
    "message": "Operation completed successfully",
    "result": {"rows_processed": 1000},
  }
