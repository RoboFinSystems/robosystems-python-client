"""Unit tests for ReportClient."""

import pytest
from http import HTTPStatus
from unittest.mock import Mock, patch
from robosystems_client.extensions.report_client import ReportClient


@pytest.mark.unit
class TestReportClientInit:
  """Test suite for ReportClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = ReportClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.timeout == 60

  def test_get_client_no_token(self, mock_config):
    """Test _get_client raises without token."""
    mock_config["token"] = None
    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="No API key"):
      client._get_client()


@pytest.mark.unit
class TestReportCreate:
  """Test suite for ReportClient.create method."""

  @patch("robosystems_client.extensions.report_client.create_report")
  def test_create_report(self, mock_create, mock_config, graph_id):
    """Test creating a report."""
    mock_parsed = Mock()
    mock_parsed.report_id = "rpt-123"
    mock_parsed.report_name = "Q1 Report"

    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.CREATED
    mock_resp.parsed = mock_parsed
    mock_create.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.create(
      graph_id=graph_id,
      name="Q1 Report",
      mapping_id="map-1",
      period_start="2025-01-01",
      period_end="2025-03-31",
    )

    assert result.report_id == "rpt-123"
    assert result.report_name == "Q1 Report"

  @patch("robosystems_client.extensions.report_client.create_report")
  def test_create_report_with_options(self, mock_create, mock_config, graph_id):
    """Test creating a report with all options."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.CREATED
    mock_resp.parsed = Mock(report_id="rpt-full")
    mock_create.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.create(
      graph_id=graph_id,
      name="Annual Report",
      mapping_id="map-2",
      period_start="2024-01-01",
      period_end="2024-12-31",
      taxonomy_id="tax_usgaap_reporting",
      period_type="annual",
      comparative=False,
    )

    assert result.report_id == "rpt-full"
    mock_create.assert_called_once()

  @patch("robosystems_client.extensions.report_client.create_report")
  def test_create_report_error(self, mock_create, mock_config, graph_id):
    """Test create report raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.BAD_REQUEST
    mock_create.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="Create report failed"):
      client.create(
        graph_id=graph_id,
        name="Bad",
        mapping_id="map-x",
        period_start="bad",
        period_end="bad",
      )


@pytest.mark.unit
class TestReportList:
  """Test suite for ReportClient.list method."""

  @patch("robosystems_client.extensions.report_client.list_reports")
  def test_list_reports(self, mock_list, mock_config, graph_id):
    """Test listing reports."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(reports=[Mock(), Mock()])
    mock_list.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.list(graph_id)

    assert len(result.reports) == 2

  @patch("robosystems_client.extensions.report_client.list_reports")
  def test_list_reports_error(self, mock_list, mock_config, graph_id):
    """Test list reports raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_list.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="List reports failed"):
      client.list(graph_id)


@pytest.mark.unit
class TestReportGet:
  """Test suite for ReportClient.get method."""

  @patch("robosystems_client.extensions.report_client.get_report")
  def test_get_report(self, mock_get, mock_config, graph_id):
    """Test getting a report."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(report_id="rpt-456", name="Q2 Report", structures=[Mock()])
    mock_get.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.get(graph_id, "rpt-456")

    assert result.report_id == "rpt-456"
    assert len(result.structures) == 1

  @patch("robosystems_client.extensions.report_client.get_report")
  def test_get_report_error(self, mock_get, mock_config, graph_id):
    """Test get report raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_get.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="Get report failed"):
      client.get(graph_id, "nonexistent")


@pytest.mark.unit
class TestReportStatement:
  """Test suite for ReportClient.statement method."""

  @patch("robosystems_client.extensions.report_client.get_statement")
  def test_get_statement(self, mock_stmt, mock_config, graph_id):
    """Test getting a financial statement."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(
      structure_type="income_statement", line_items=[Mock(), Mock()]
    )
    mock_stmt.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.statement(graph_id, "rpt-123", "income_statement")

    assert result.structure_type == "income_statement"
    assert len(result.line_items) == 2

  @patch("robosystems_client.extensions.report_client.get_statement")
  def test_get_statement_error(self, mock_stmt, mock_config, graph_id):
    """Test statement raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_stmt.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="Get statement failed"):
      client.statement(graph_id, "rpt-bad", "income_statement")


@pytest.mark.unit
class TestReportRegenerate:
  """Test suite for ReportClient.regenerate method."""

  @patch("robosystems_client.extensions.report_client.regenerate_report")
  def test_regenerate_report(self, mock_regen, mock_config, graph_id):
    """Test regenerating a report."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(report_id="rpt-regen")
    mock_regen.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.regenerate(
      graph_id, "rpt-regen", period_start="2025-04-01", period_end="2025-06-30"
    )

    assert result.report_id == "rpt-regen"

  @patch("robosystems_client.extensions.report_client.regenerate_report")
  def test_regenerate_report_error(self, mock_regen, mock_config, graph_id):
    """Test regenerate raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.BAD_REQUEST
    mock_regen.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="Regenerate report failed"):
      client.regenerate(graph_id, "rpt-bad", "bad", "bad")


@pytest.mark.unit
class TestReportDelete:
  """Test suite for ReportClient.delete method."""

  @patch("robosystems_client.extensions.report_client.delete_report")
  def test_delete_report(self, mock_delete, mock_config, graph_id):
    """Test deleting a report."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NO_CONTENT
    mock_delete.return_value = mock_resp

    client = ReportClient(mock_config)
    client.delete(graph_id, "rpt-del")  # Should not raise

    mock_delete.assert_called_once()

  @patch("robosystems_client.extensions.report_client.delete_report")
  def test_delete_report_error(self, mock_delete, mock_config, graph_id):
    """Test delete raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_delete.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="Delete report failed"):
      client.delete(graph_id, "rpt-err")


@pytest.mark.unit
class TestReportShare:
  """Test suite for ReportClient.share method."""

  @patch("robosystems_client.extensions.report_client.share_report")
  def test_share_report(self, mock_share, mock_config, graph_id):
    """Test sharing a report."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(shared_count=3)
    mock_share.return_value = mock_resp

    client = ReportClient(mock_config)
    result = client.share(graph_id, "rpt-share", "pub-list-1")

    assert result.shared_count == 3

  @patch("robosystems_client.extensions.report_client.share_report")
  def test_share_report_error(self, mock_share, mock_config, graph_id):
    """Test share raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_share.return_value = mock_resp

    client = ReportClient(mock_config)

    with pytest.raises(RuntimeError, match="Share report failed"):
      client.share(graph_id, "rpt-bad", "pub-bad")


@pytest.mark.unit
class TestReportIsShared:
  """Test suite for ReportClient.is_shared_report method."""

  def test_is_shared_report_true(self, mock_config):
    """Test detecting a shared report."""
    client = ReportClient(mock_config)
    report = Mock(source_graph_id="other-graph-123")

    assert client.is_shared_report(report) is True

  def test_is_shared_report_false(self, mock_config):
    """Test detecting a non-shared report."""
    client = ReportClient(mock_config)
    report = Mock(spec=[])  # No source_graph_id attribute

    assert client.is_shared_report(report) is False
