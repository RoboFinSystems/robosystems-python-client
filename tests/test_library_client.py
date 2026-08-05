"""Unit tests for LibraryClient.

LibraryClient is read-only and speaks a single wire protocol: GraphQL at
POST /extensions/{graph_id}/graphql, where ``graph_id`` is either the
``"library"`` sentinel (canonical public-schema browse) or a tenant
graph id (tenant copy + extensions).

These tests mock at the transport boundary — ``GraphQLClient.execute``
is patched exactly like tests/test_ledger_client.py does for ledger
reads — and assert both the typed model validation of responses and the
variables forwarded on the wire.
"""

from __future__ import annotations

from unittest.mock import patch

import pytest

from robosystems_client.clients.library_client import (
  LIBRARY_GRAPH_ID,
  LibraryClient,
)


# ── Shared element payload helpers ─────────────────────────────────────


def _element(id: str = "el_1", qname: str = "rs-gaap:Cash") -> dict:
  """A full element payload matching the list/search/get selection set."""
  return {
    "id": id,
    "qname": qname,
    "namespace": "https://taxonomy.robosystems.ai/rs-gaap",
    "name": "Cash",
    "trait": "asset",
    "balanceType": "debit",
    "periodType": "instant",
    "isAbstract": False,
    "isMonetary": True,
    "elementType": "monetaryItemType",
    "source": "rs-gaap",
    "taxonomyId": "tax_rsgaap",
    "parentId": None,
    "labels": [{"role": "label", "language": "en", "text": "Cash"}],
    "references": [],
  }


def _taxonomy(id: str = "tax_rsgaap") -> dict:
  return {
    "id": id,
    "name": "RoboSystems GAAP",
    "description": None,
    "standard": "rs-gaap",
    "version": "2026",
    "namespaceUri": "https://taxonomy.robosystems.ai/rs-gaap",
    "taxonomyType": "reporting",
    "isShared": True,
    "isActive": True,
    "isLocked": True,
    "elementCount": 512,
  }


# ── Init ───────────────────────────────────────────────────────────────


@pytest.mark.unit
class TestLibraryClientInit:
  def test_client_initialization(self, mock_config):
    client = LibraryClient(mock_config)
    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.timeout == 60

  def test_get_graphql_client_no_token(self, mock_config):
    mock_config["token"] = None
    client = LibraryClient(mock_config)
    with pytest.raises(RuntimeError, match="No API key"):
      client._get_graphql_client()

  @patch("robosystems_client.clients.library_client.GraphQLClient")
  def test_token_provider_wins_over_static_token(self, mock_gql, mock_config):
    """A configured token_provider is consulted per request and takes
    precedence over the static token."""
    mock_config["token_provider"] = lambda: "rfs_rotated"
    client = LibraryClient(mock_config)
    mock_gql.return_value.execute.return_value = {"libraryTaxonomies": []}
    client.list_library_taxonomies()
    assert mock_gql.call_args.kwargs["token"] == "rfs_rotated"


# ── Taxonomies ─────────────────────────────────────────────────────────


@pytest.mark.unit
class TestLibraryTaxonomies:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_taxonomies(self, mock_execute, mock_config):
    mock_execute.return_value = {"libraryTaxonomies": [_taxonomy()]}
    client = LibraryClient(mock_config)
    taxonomies = client.list_library_taxonomies()
    assert len(taxonomies) == 1
    assert taxonomies[0].id == "tax_rsgaap"
    assert taxonomies[0].taxonomy_type == "reporting"
    assert taxonomies[0].element_count == 512
    # Defaults to the "library" sentinel graph
    assert mock_execute.call_args[0][0] == LIBRARY_GRAPH_ID

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_taxonomies_forwards_filters(self, mock_execute, mock_config):
    mock_execute.return_value = {"libraryTaxonomies": []}
    client = LibraryClient(mock_config)
    client.list_library_taxonomies(
      "kg1a2b3c", standard="rs-gaap", include_element_count=True
    )
    # Tenant graph_id passes through as the first positional arg
    assert mock_execute.call_args[0][0] == "kg1a2b3c"
    variables = mock_execute.call_args[0][2]
    assert variables["standard"] == "rs-gaap"
    assert variables["includeElementCount"] is True

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_taxonomy(self, mock_execute, mock_config):
    mock_execute.return_value = {"libraryTaxonomy": _taxonomy()}
    client = LibraryClient(mock_config)
    taxonomy = client.get_library_taxonomy(standard="rs-gaap", version="2026")
    assert taxonomy is not None
    assert taxonomy.standard == "rs-gaap"
    variables = mock_execute.call_args[0][2]
    assert variables["standard"] == "rs-gaap"
    assert variables["version"] == "2026"
    # None-valued variables are stripped before sending
    assert "id" not in variables

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_taxonomy_returns_none_when_missing(
    self, mock_execute, mock_config
  ):
    mock_execute.return_value = {"libraryTaxonomy": None}
    client = LibraryClient(mock_config)
    assert client.get_library_taxonomy(id="tax_nope") is None


# ── Elements ───────────────────────────────────────────────────────────


@pytest.mark.unit
class TestLibraryElements:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_elements(self, mock_execute, mock_config):
    payload = _element()
    # The list read omits labels/references unless requested
    del payload["labels"], payload["references"]
    mock_execute.return_value = {"libraryElements": [payload]}
    client = LibraryClient(mock_config)
    elements = client.list_library_elements(
      classification="asset", activity_type="operatingActivity", limit=10
    )
    assert len(elements) == 1
    assert elements[0].qname == "rs-gaap:Cash"
    assert elements[0].balance_type == "debit"
    variables = mock_execute.call_args[0][2]
    assert variables["classification"] == "asset"
    assert variables["activityType"] == "operatingActivity"
    assert variables["limit"] == 10
    assert variables["includeLabels"] is False

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_search_library_elements(self, mock_execute, mock_config):
    mock_execute.return_value = {"searchLibraryElements": [_element()]}
    client = LibraryClient(mock_config)
    results = client.search_library_elements("cash", source="rs-gaap", limit=5)
    assert len(results) == 1
    assert results[0].labels[0].text == "Cash"
    variables = mock_execute.call_args[0][2]
    assert variables["query"] == "cash"
    assert variables["source"] == "rs-gaap"
    assert variables["limit"] == 5

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_element_by_qname(self, mock_execute, mock_config):
    mock_execute.return_value = {"libraryElement": _element()}
    client = LibraryClient(mock_config)
    element = client.get_library_element(qname="rs-gaap:Cash")
    assert element is not None
    assert element.is_monetary is True
    variables = mock_execute.call_args[0][2]
    assert variables["qname"] == "rs-gaap:Cash"
    assert "id" not in variables

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_element_returns_none_when_missing(
    self, mock_execute, mock_config
  ):
    mock_execute.return_value = {"libraryElement": None}
    client = LibraryClient(mock_config)
    assert client.get_library_element(id="el_nope") is None


# ── Arcs ───────────────────────────────────────────────────────────────


@pytest.mark.unit
class TestLibraryArcs:
  _ARC = {
    "id": "arc_1",
    "structureId": "struct_1",
    "structureName": "BS-classified",
    "fromElementId": "el_1",
    "fromElementQname": "sfac6:Assets",
    "fromElementName": "Assets",
    "fromElementTrait": "asset",
    "fromElementIsAbstract": True,
    "toElementId": "el_2",
    "toElementQname": "rs-gaap:Cash",
    "toElementName": "Cash",
    "toElementTrait": "asset",
    "toElementIsAbstract": False,
    "associationType": "presentation",
    "arcrole": None,
    "orderValue": 1.0,
    "weight": None,
  }

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_taxonomy_arcs(self, mock_execute, mock_config):
    mock_execute.return_value = {
      "libraryTaxonomyArcCount": 42,
      "libraryTaxonomyArcs": [self._ARC],
    }
    client = LibraryClient(mock_config)
    result = client.list_library_taxonomy_arcs("tax_rsgaap")
    # Typed response carries both root fields
    assert result.library_taxonomy_arc_count == 42
    assert len(result.library_taxonomy_arcs) == 1
    arc = result.library_taxonomy_arcs[0]
    assert arc.from_element_trait == "asset"
    assert arc.to_element_is_abstract is False
    variables = mock_execute.call_args[0][2]
    assert variables["taxonomyId"] == "tax_rsgaap"
    # Optional filters stripped when not provided
    assert "structureId" not in variables
    assert "associationType" not in variables

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_taxonomy_arcs_structure_id_filter(
    self, mock_execute, mock_config
  ):
    mock_execute.return_value = {
      "libraryTaxonomyArcCount": 1,
      "libraryTaxonomyArcs": [self._ARC],
    }
    client = LibraryClient(mock_config)
    result = client.list_library_taxonomy_arcs(
      "tax_rsgaap",
      association_type="presentation",
      structure_id="struct_1",
      limit=50,
      offset=10,
    )
    assert result.library_taxonomy_arc_count == 1
    variables = mock_execute.call_args[0][2]
    assert variables["structureId"] == "struct_1"
    assert variables["associationType"] == "presentation"
    assert variables["limit"] == 50
    assert variables["offset"] == 10

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_element_arcs(self, mock_execute, mock_config):
    mock_execute.return_value = {
      "libraryElementArcs": [
        {
          "id": "arc_1",
          "direction": "outgoing",
          "associationType": "general-special",
          "arcrole": None,
          "taxonomyId": "tax_map",
          "taxonomyStandard": "fac-to-rs-gaap",
          "taxonomyName": "FAC to RS-GAAP",
          "structureId": "struct_1",
          "structureName": None,
          "peer": {
            "id": "el_2",
            "qname": "rs-gaap:Cash",
            "name": "Cash",
            "trait": "asset",
            "source": "rs-gaap",
          },
        }
      ]
    }
    client = LibraryClient(mock_config)
    arcs = client.get_library_element_arcs("el_1")
    assert len(arcs) == 1
    assert arcs[0].direction == "outgoing"
    assert arcs[0].peer.qname == "rs-gaap:Cash"
    variables = mock_execute.call_args[0][2]
    assert variables["id"] == "el_1"


# ── Structures ─────────────────────────────────────────────────────────


@pytest.mark.unit
class TestLibraryStructures:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_structures(self, mock_execute, mock_config):
    mock_execute.return_value = {
      "libraryStructures": [
        {
          "id": "struct_1",
          "name": "BS-classified",
          "blockType": "balance_sheet",
          "taxonomyId": "tax_rsgaap",
          "roleUri": "https://taxonomy.robosystems.ai/roles/bs",
          "isActive": True,
        }
      ]
    }
    client = LibraryClient(mock_config)
    structures = client.list_library_structures()
    assert len(structures) == 1
    assert structures[0].block_type == "balance_sheet"
    assert structures[0].is_active is True
    assert mock_execute.call_args[0][0] == LIBRARY_GRAPH_ID

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_library_structures_forwards_filters(self, mock_execute, mock_config):
    mock_execute.return_value = {"libraryStructures": []}
    client = LibraryClient(mock_config)
    client.list_library_structures(
      "kg1a2b3c", taxonomy_id="tax_rsgaap", block_type="income_statement"
    )
    assert mock_execute.call_args[0][0] == "kg1a2b3c"
    variables = mock_execute.call_args[0][2]
    assert variables["taxonomyId"] == "tax_rsgaap"
    assert variables["blockType"] == "income_statement"


# ── Classifications / Equivalence ──────────────────────────────────────


@pytest.mark.unit
class TestLibraryElementClassifications:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_element_classifications(self, mock_execute, mock_config):
    mock_execute.return_value = {
      "libraryElementClassifications": [
        {
          "category": "elementsOfFinancialStatements",
          "identifier": "asset",
          "name": "Asset",
          "isPrimary": True,
        },
        {
          "category": "activity",
          "identifier": "operatingActivity",
          "name": None,
          "isPrimary": False,
        },
      ]
    }
    client = LibraryClient(mock_config)
    classifications = client.get_library_element_classifications("el_1")
    assert len(classifications) == 2
    assert classifications[0].category == "elementsOfFinancialStatements"
    assert classifications[0].is_primary is True
    assert classifications[1].name is None
    variables = mock_execute.call_args[0][2]
    assert variables["id"] == "el_1"


@pytest.mark.unit
class TestLibraryElementEquivalents:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_element_equivalents(self, mock_execute, mock_config):
    peer = {
      "id": "el_2",
      "qname": "us-gaap:Cash",
      "name": "Cash",
      "trait": "asset",
      "source": "us-gaap",
    }
    mock_execute.return_value = {
      "libraryElementEquivalents": {
        "element": {
          "id": "el_1",
          "qname": "fac:Cash",
          "name": "Cash",
          "trait": "asset",
          "source": "fac",
        },
        "equivalents": [peer],
      }
    }
    client = LibraryClient(mock_config)
    equivalence = client.get_library_element_equivalents("el_1")
    assert equivalence is not None
    assert equivalence.element.qname == "fac:Cash"
    assert len(equivalence.equivalents) == 1
    assert equivalence.equivalents[0].source == "us-gaap"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_library_element_equivalents_returns_none_when_missing(
    self, mock_execute, mock_config
  ):
    mock_execute.return_value = {"libraryElementEquivalents": None}
    client = LibraryClient(mock_config)
    assert client.get_library_element_equivalents("el_nope") is None
