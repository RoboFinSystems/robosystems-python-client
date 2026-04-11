"""Unit tests for LedgerClient."""

import pytest
from http import HTTPStatus
from unittest.mock import Mock, patch
from robosystems_client.extensions.ledger_client import LedgerClient


@pytest.mark.unit
class TestLedgerClientInit:
  """Test suite for LedgerClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = LedgerClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.timeout == 60

  def test_get_client_no_token(self, mock_config):
    """Test _get_client raises without token."""
    mock_config["token"] = None
    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="No API key"):
      client._get_client()


@pytest.mark.unit
class TestLedgerEntity:
  """Test suite for entity operations."""

  @patch("robosystems_client.extensions.ledger_client.get_ledger_entity")
  def test_get_entity(self, mock_get, mock_config, graph_id):
    """Test getting entity for a graph."""
    mock_parsed = Mock()
    mock_parsed.entity_name = "ACME Corp"
    mock_parsed.cik = "0001234567"

    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = mock_parsed
    mock_get.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_entity(graph_id)

    assert result.entity_name == "ACME Corp"

  @patch("robosystems_client.extensions.ledger_client.get_ledger_entity")
  def test_get_entity_not_found(self, mock_get, mock_config, graph_id):
    """Test getting entity that doesn't exist."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_get.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_entity(graph_id)

    assert result is None

  @patch("robosystems_client.extensions.ledger_client.get_ledger_entity")
  def test_get_entity_error(self, mock_get, mock_config, graph_id):
    """Test get entity raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_get.return_value = mock_resp

    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="Get entity failed"):
      client.get_entity(graph_id)


@pytest.mark.unit
class TestLedgerAccounts:
  """Test suite for account operations."""

  @patch("robosystems_client.extensions.ledger_client.list_ledger_accounts")
  def test_list_accounts(self, mock_list, mock_config, graph_id):
    """Test listing accounts."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(accounts=[Mock(), Mock()])
    mock_list.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.list_accounts(graph_id)

    assert len(result.accounts) == 2

  @patch("robosystems_client.extensions.ledger_client.list_ledger_accounts")
  def test_list_accounts_error(self, mock_list, mock_config, graph_id):
    """Test list accounts raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_list.return_value = mock_resp

    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="List accounts failed"):
      client.list_accounts(graph_id)

  @patch("robosystems_client.extensions.ledger_client.get_ledger_account_tree")
  def test_get_account_tree(self, mock_tree, mock_config, graph_id):
    """Test getting account tree."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(root=Mock(children=[Mock(), Mock()]))
    mock_tree.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_account_tree(graph_id)

    assert len(result.root.children) == 2


@pytest.mark.unit
class TestLedgerTransactions:
  """Test suite for transaction operations."""

  @patch("robosystems_client.extensions.ledger_client.list_ledger_transactions")
  def test_list_transactions(self, mock_list, mock_config, graph_id):
    """Test listing transactions."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(transactions=[Mock()])
    mock_list.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.list_transactions(graph_id)

    assert len(result.transactions) == 1

  @patch("robosystems_client.extensions.ledger_client.list_ledger_transactions")
  def test_list_transactions_with_filters(self, mock_list, mock_config, graph_id):
    """Test listing transactions with date filters."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(transactions=[])
    mock_list.return_value = mock_resp

    client = LedgerClient(mock_config)
    client.list_transactions(
      graph_id,
      start_date="2025-01-01",
      end_date="2025-03-31",
      limit=50,
      offset=0,
    )

    mock_list.assert_called_once()
    call_kwargs = mock_list.call_args[1]
    assert call_kwargs["start_date"] == "2025-01-01"
    assert call_kwargs["end_date"] == "2025-03-31"
    assert call_kwargs["limit"] == 50

  @patch("robosystems_client.extensions.ledger_client.get_ledger_transaction")
  def test_get_transaction(self, mock_get, mock_config, graph_id):
    """Test getting a specific transaction."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(transaction_id="txn-123", entries=[Mock()])
    mock_get.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_transaction(graph_id, "txn-123")

    assert result.transaction_id == "txn-123"

  @patch("robosystems_client.extensions.ledger_client.get_ledger_transaction")
  def test_get_transaction_error(self, mock_get, mock_config, graph_id):
    """Test get transaction raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_get.return_value = mock_resp

    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="Get transaction failed"):
      client.get_transaction(graph_id, "nonexistent")


@pytest.mark.unit
class TestLedgerTrialBalance:
  """Test suite for trial balance operations."""

  @patch("robosystems_client.extensions.ledger_client.get_ledger_trial_balance")
  def test_get_trial_balance(self, mock_tb, mock_config, graph_id):
    """Test getting trial balance."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(
      total_debits=100000, total_credits=100000, accounts=[Mock()]
    )
    mock_tb.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_trial_balance(graph_id)

    assert result.total_debits == 100000
    assert result.total_credits == 100000

  @patch("robosystems_client.extensions.ledger_client.get_ledger_trial_balance")
  def test_get_trial_balance_with_dates(self, mock_tb, mock_config, graph_id):
    """Test getting trial balance with date range."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock()
    mock_tb.return_value = mock_resp

    client = LedgerClient(mock_config)
    client.get_trial_balance(graph_id, start_date="2025-01-01", end_date="2025-03-31")

    call_kwargs = mock_tb.call_args[1]
    assert call_kwargs["start_date"] == "2025-01-01"
    assert call_kwargs["end_date"] == "2025-03-31"

  @patch("robosystems_client.extensions.ledger_client.get_mapped_trial_balance")
  def test_get_mapped_trial_balance(self, mock_mtb, mock_config, graph_id):
    """Test getting mapped trial balance."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(elements=[Mock()])
    mock_mtb.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_mapped_trial_balance(graph_id, mapping_id="map-1")

    assert len(result.elements) == 1


@pytest.mark.unit
class TestLedgerSummary:
  """Test suite for summary operations."""

  @patch("robosystems_client.extensions.ledger_client.get_ledger_summary")
  def test_get_summary(self, mock_summary, mock_config, graph_id):
    """Test getting ledger summary."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(
      account_count=50, transaction_count=200, entity_name="ACME Corp"
    )
    mock_summary.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_summary(graph_id)

    assert result.account_count == 50
    assert result.transaction_count == 200


@pytest.mark.unit
class TestLedgerTaxonomy:
  """Test suite for taxonomy operations."""

  @patch("robosystems_client.extensions.ledger_client.get_reporting_taxonomy")
  def test_get_reporting_taxonomy(self, mock_tax, mock_config, graph_id):
    """Test getting reporting taxonomy."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(taxonomy_id="tax_usgaap_reporting")
    mock_tax.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_reporting_taxonomy(graph_id)

    assert result.taxonomy_id == "tax_usgaap_reporting"

  @patch("robosystems_client.extensions.ledger_client.list_structures")
  def test_list_structures(self, mock_structs, mock_config, graph_id):
    """Test listing reporting structures."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(structures=[Mock(), Mock(), Mock()])
    mock_structs.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.list_structures(graph_id)

    assert len(result.structures) == 3

  @patch("robosystems_client.extensions.ledger_client.list_elements")
  def test_list_elements(self, mock_elems, mock_config, graph_id):
    """Test listing elements."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(elements=[Mock()])
    mock_elems.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.list_elements(graph_id, source="coa", limit=10)

    assert len(result.elements) == 1
    call_kwargs = mock_elems.call_args[1]
    assert call_kwargs["source"] == "coa"
    assert call_kwargs["limit"] == 10


@pytest.mark.unit
class TestLedgerMappings:
  """Test suite for mapping operations."""

  @patch("robosystems_client.extensions.ledger_client.list_mappings")
  def test_list_mappings(self, mock_list, mock_config, graph_id):
    """Test listing mappings."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(mappings=[Mock()])
    mock_list.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.list_mappings(graph_id)

    assert len(result.mappings) == 1

  @patch("robosystems_client.extensions.ledger_client.get_mapping_detail")
  def test_get_mapping_detail(self, mock_detail, mock_config, graph_id):
    """Test getting mapping detail."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(mapping_id="map-1", associations=[Mock(), Mock()])
    mock_detail.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_mapping_detail(graph_id, "map-1")

    assert len(result.associations) == 2

  @patch("robosystems_client.extensions.ledger_client.get_mapping_coverage")
  def test_get_mapping_coverage(self, mock_cov, mock_config, graph_id):
    """Test getting mapping coverage."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(total_elements=50, mapped_elements=45, coverage=0.9)
    mock_cov.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_mapping_coverage(graph_id, "map-1")

    assert result.coverage == 0.9

  @patch("robosystems_client.extensions.ledger_client.create_mapping_association")
  def test_create_mapping(self, mock_create, mock_config, graph_id):
    """Test creating a mapping association."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.CREATED
    mock_create.return_value = mock_resp

    client = LedgerClient(mock_config)
    client.create_mapping(
      graph_id, "map-1", from_element_id="elem-a", to_element_id="elem-b"
    )

    mock_create.assert_called_once()

  @patch("robosystems_client.extensions.ledger_client.create_mapping_association")
  def test_create_mapping_error(self, mock_create, mock_config, graph_id):
    """Test create mapping raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.BAD_REQUEST
    mock_create.return_value = mock_resp

    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="Create mapping failed"):
      client.create_mapping(graph_id, "map-1", "elem-a", "elem-b")

  @patch("robosystems_client.extensions.ledger_client.delete_mapping_association")
  def test_delete_mapping(self, mock_delete, mock_config, graph_id):
    """Test deleting a mapping association."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NO_CONTENT
    mock_delete.return_value = mock_resp

    client = LedgerClient(mock_config)
    client.delete_mapping(graph_id, "map-1", "assoc-1")

    mock_delete.assert_called_once()

  @patch("robosystems_client.extensions.ledger_client.auto_map_elements")
  def test_auto_map(self, mock_auto, mock_config, graph_id):
    """Test triggering auto-mapping."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.ACCEPTED
    mock_resp.parsed = {"operation_id": "op-auto-1"}
    mock_auto.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.auto_map(graph_id, "map-1")

    assert result["operation_id"] == "op-auto-1"

  @patch("robosystems_client.extensions.ledger_client.auto_map_elements")
  def test_auto_map_error(self, mock_auto, mock_config, graph_id):
    """Test auto-map raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_auto.return_value = mock_resp

    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="Auto-map failed"):
      client.auto_map(graph_id, "map-1")

  @patch("robosystems_client.extensions.ledger_client.create_structure")
  def test_create_mapping_structure(self, mock_create_struct, mock_config, graph_id):
    """Test creating a mapping structure."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.CREATED
    mock_resp.parsed = Mock(structure_id="struct-new")
    mock_create_struct.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.create_mapping_structure(graph_id, name="Custom Mapping")

    assert result.structure_id == "struct-new"


@pytest.mark.unit
class TestLedgerSchedules:
  """Test suite for schedule operations."""

  @patch("robosystems_client.extensions.ledger_client.list_schedules")
  def test_list_schedules(self, mock_list, mock_config, graph_id):
    """Test listing schedules."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(schedules=[Mock()])
    mock_list.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.list_schedules(graph_id)

    assert len(result.schedules) == 1

  @patch("robosystems_client.extensions.ledger_client.get_schedule_facts")
  def test_get_schedule_facts(self, mock_facts, mock_config, graph_id):
    """Test getting schedule facts."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(facts=[Mock(), Mock()])
    mock_facts.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_schedule_facts(graph_id, "struct-1")

    assert len(result.facts) == 2

  @patch("robosystems_client.extensions.ledger_client.get_period_close_status")
  def test_get_period_close_status(self, mock_status, mock_config, graph_id):
    """Test getting period close status."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(status="open", schedules=[Mock()])
    mock_status.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_period_close_status(
      graph_id, period_start="2025-01-01", period_end="2025-03-31"
    )

    assert result.status == "open"

  @patch("robosystems_client.extensions.ledger_client.create_closing_entry")
  def test_create_closing_entry(self, mock_close, mock_config, graph_id):
    """Test creating a closing entry."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.CREATED
    mock_resp.parsed = Mock(transaction_id="txn-close-1")
    mock_close.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.create_closing_entry(
      graph_id,
      structure_id="struct-1",
      posting_date="2025-03-31",
      period_start="2025-01-01",
      period_end="2025-03-31",
      memo="Q1 close",
    )

    assert result.transaction_id == "txn-close-1"

  @patch("robosystems_client.extensions.ledger_client.create_closing_entry")
  def test_create_closing_entry_error(self, mock_close, mock_config, graph_id):
    """Test create closing entry raises on error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.BAD_REQUEST
    mock_close.return_value = mock_resp

    client = LedgerClient(mock_config)

    with pytest.raises(RuntimeError, match="Create closing entry failed"):
      client.create_closing_entry(
        graph_id, "struct-1", "2025-03-31", "2025-01-01", "2025-03-31"
      )


@pytest.mark.unit
class TestLedgerClosingBook:
  """Test suite for closing book operations."""

  @patch("robosystems_client.extensions.ledger_client.get_closing_book_structures")
  def test_get_closing_book_structures(self, mock_cb, mock_config, graph_id):
    """Test getting closing book structures."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(categories=[Mock(), Mock()])
    mock_cb.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_closing_book_structures(graph_id)

    assert len(result.categories) == 2

  @patch("robosystems_client.extensions.ledger_client.get_account_rollups")
  def test_get_account_rollups(self, mock_rollups, mock_config, graph_id):
    """Test getting account rollups."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(rollups=[Mock()])
    mock_rollups.return_value = mock_resp

    client = LedgerClient(mock_config)
    result = client.get_account_rollups(
      graph_id, mapping_id="map-1", start_date="2025-01-01"
    )

    assert len(result.rollups) == 1
