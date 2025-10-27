"""Unit tests for GraphClient."""

import pytest
from robosystems_client.extensions.graph_client import (
  GraphClient,
  GraphMetadata,
  InitialEntityData,
  GraphInfo,
)


@pytest.mark.unit
class TestGraphClient:
  """Test suite for GraphClient."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = GraphClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}

  def test_graph_metadata_dataclass(self):
    """Test GraphMetadata dataclass."""
    metadata = GraphMetadata(
      graph_name="Test Graph",
      description="A test graph",
      schema_extensions=["custom_prop"],
      tags=["test", "demo"],
    )

    assert metadata.graph_name == "Test Graph"
    assert metadata.description == "A test graph"
    assert metadata.schema_extensions == ["custom_prop"]
    assert metadata.tags == ["test", "demo"]

  def test_graph_metadata_defaults(self):
    """Test GraphMetadata default values."""
    metadata = GraphMetadata(graph_name="Simple Graph")

    assert metadata.graph_name == "Simple Graph"
    assert metadata.description is None
    assert metadata.schema_extensions is None
    assert metadata.tags is None

  def test_initial_entity_data_dataclass(self):
    """Test InitialEntityData dataclass."""
    entity = InitialEntityData(
      name="ACME Corp",
      uri="https://example.com/acme",
      category="Technology",
      sic="7372",
      sic_description="Prepackaged Software",
    )

    assert entity.name == "ACME Corp"
    assert entity.uri == "https://example.com/acme"
    assert entity.category == "Technology"
    assert entity.sic == "7372"
    assert entity.sic_description == "Prepackaged Software"

  def test_initial_entity_data_defaults(self):
    """Test InitialEntityData default values."""
    entity = InitialEntityData(name="Basic Entity", uri="https://example.com")

    assert entity.name == "Basic Entity"
    assert entity.uri == "https://example.com"
    assert entity.category is None
    assert entity.sic is None
    assert entity.sic_description is None

  def test_graph_info_dataclass(self):
    """Test GraphInfo dataclass."""
    info = GraphInfo(
      graph_id="graph-123",
      graph_name="Production Graph",
      description="Production knowledge graph",
      schema_extensions=["prop1", "prop2"],
      tags=["prod"],
      created_at="2024-01-15T10:30:00Z",
      status="active",
    )

    assert info.graph_id == "graph-123"
    assert info.graph_name == "Production Graph"
    assert info.description == "Production knowledge graph"
    assert info.schema_extensions == ["prop1", "prop2"]
    assert info.tags == ["prod"]
    assert info.created_at == "2024-01-15T10:30:00Z"
    assert info.status == "active"

  def test_graph_info_minimal(self):
    """Test GraphInfo with minimal data."""
    info = GraphInfo(graph_id="graph-456", graph_name="Minimal Graph")

    assert info.graph_id == "graph-456"
    assert info.graph_name == "Minimal Graph"
    assert info.description is None
    assert info.schema_extensions is None
    assert info.tags is None
    assert info.created_at is None
    assert info.status is None

  def test_close_method(self, mock_config):
    """Test that close method exists and can be called."""
    client = GraphClient(mock_config)

    # Should not raise any exceptions
    client.close()
