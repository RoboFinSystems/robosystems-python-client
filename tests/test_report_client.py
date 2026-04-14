"""Unit tests for ReportClient.

Reports + publish lists + statements ride the same transport split as
LedgerClient: GraphQL for reads, operation envelopes for writes.
"""

from __future__ import annotations

from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from robosystems_client.extensions.report_client import ReportClient
from robosystems_client.models.operation_envelope import OperationEnvelope
from robosystems_client.models.operation_envelope_status import OperationEnvelopeStatus


def _envelope(
  operation: str,
  result: dict | list | None,
  status: OperationEnvelopeStatus = OperationEnvelopeStatus.COMPLETED,
) -> OperationEnvelope:
  return OperationEnvelope(
    operation=operation,
    operation_id=f"op_{operation.upper()}_01",
    status=status,
    result=result,
    at="2026-04-14T12:00:00Z",
  )


def _mock_response(
  envelope: OperationEnvelope, status_code: int = HTTPStatus.OK
) -> Mock:
  resp = Mock()
  resp.status_code = status_code
  resp.parsed = envelope
  resp.content = b""
  return resp


@pytest.mark.unit
class TestReportReads:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "reports": {
        "reports": [
          {
            "id": "rep_1",
            "name": "Q1 2026",
            "taxonomyId": "tax_usgaap",
            "generationStatus": "completed",
            "periodType": "quarterly",
            "periodStart": "2026-01-01",
            "periodEnd": "2026-03-31",
            "comparative": True,
            "mappingId": "map_1",
            "aiGenerated": False,
            "createdAt": "2026-04-01T00:00:00Z",
            "lastGenerated": "2026-04-01T00:00:00Z",
            "entityName": "ACME",
            "sourceGraphId": None,
            "sourceReportId": None,
            "sharedAt": None,
            "periods": [],
            "structures": [],
          }
        ]
      }
    }
    client = ReportClient(mock_config)
    reports = client.list(graph_id)
    assert len(reports) == 1
    assert reports[0]["id"] == "rep_1"
    assert reports[0]["generation_status"] == "completed"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_returns_none_when_missing(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {"report": None}
    client = ReportClient(mock_config)
    assert client.get(graph_id, "rep_x") is None

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_statement(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "statement": {
        "reportId": "rep_1",
        "structureId": "str_1",
        "structureName": "Income Statement",
        "structureType": "income_statement",
        "unmappedCount": 0,
        "periods": [{"start": "2026-01-01", "end": "2026-03-31", "label": "Q1"}],
        "rows": [
          {
            "elementId": "elem_rev",
            "elementQname": "us-gaap:Revenues",
            "elementName": "Revenues",
            "classification": "revenue",
            "values": [1000000],
            "isSubtotal": False,
            "depth": 0,
          }
        ],
        "validation": {
          "passed": True,
          "checks": [],
          "failures": [],
          "warnings": [],
        },
      }
    }
    client = ReportClient(mock_config)
    stmt = client.statement(graph_id, "rep_1", "income_statement")
    assert stmt is not None
    assert stmt["rows"][0]["values"][0] == 1000000
    assert stmt["validation"]["passed"] is True

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_publish_lists(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "publishLists": {
        "publishLists": [
          {
            "id": "pl_1",
            "name": "Investors",
            "description": None,
            "memberCount": 2,
            "createdBy": "user_1",
            "createdAt": "2026-01-01T00:00:00Z",
            "updatedAt": "2026-01-01T00:00:00Z",
          }
        ],
        "pagination": {"total": 1, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = ReportClient(mock_config)
    result = client.list_publish_lists(graph_id)
    assert result is not None
    assert len(result["publish_lists"]) == 1
    assert result["publish_lists"][0]["member_count"] == 2

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_publish_list_with_members(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "publishList": {
        "id": "pl_1",
        "name": "Investors",
        "description": "VC distribution list",
        "memberCount": 1,
        "createdBy": "user_1",
        "createdAt": "2026-01-01T00:00:00Z",
        "updatedAt": "2026-01-01T00:00:00Z",
        "members": [
          {
            "id": "mem_1",
            "targetGraphId": "graph_investor",
            "targetGraphName": "Acme Ventures",
            "targetOrgName": None,
            "addedBy": "user_1",
            "addedAt": "2026-01-01T00:00:00Z",
          }
        ],
      }
    }
    client = ReportClient(mock_config)
    detail = client.get_publish_list(graph_id, "pl_1")
    assert detail is not None
    assert len(detail["members"]) == 1
    assert detail["members"][0]["target_graph_id"] == "graph_investor"


@pytest.mark.unit
class TestReportWrites:
  @patch("robosystems_client.extensions.report_client.op_create_report")
  def test_create_returns_ack(self, mock_op, mock_config, graph_id):
    envelope = _envelope("create-report", None, status=OperationEnvelopeStatus.PENDING)
    mock_op.return_value = _mock_response(envelope, status_code=HTTPStatus.ACCEPTED)
    client = ReportClient(mock_config)
    ack = client.create(
      graph_id,
      name="Q2 2026",
      mapping_id="map_1",
      period_start="2026-04-01",
      period_end="2026-06-30",
    )
    assert ack["status"] == OperationEnvelopeStatus.PENDING
    assert ack["operation_id"].startswith("op_")

  @patch("robosystems_client.extensions.report_client.op_regenerate_report")
  def test_regenerate_returns_ack(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "regenerate-report", None, status=OperationEnvelopeStatus.PENDING
    )
    mock_op.return_value = _mock_response(envelope, status_code=HTTPStatus.ACCEPTED)
    client = ReportClient(mock_config)
    ack = client.regenerate(
      graph_id, "rep_1", period_start="2026-04-01", period_end="2026-06-30"
    )
    assert ack["status"] == OperationEnvelopeStatus.PENDING

  @patch("robosystems_client.extensions.report_client.op_delete_report")
  def test_delete(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-report", {"deleted": True})
    mock_op.return_value = _mock_response(envelope)
    client = ReportClient(mock_config)
    client.delete(graph_id, "rep_1")
    assert mock_op.called

  @patch("robosystems_client.extensions.report_client.op_share_report")
  def test_share_returns_ack(self, mock_op, mock_config, graph_id):
    envelope = _envelope("share-report", None, status=OperationEnvelopeStatus.PENDING)
    mock_op.return_value = _mock_response(envelope, status_code=HTTPStatus.ACCEPTED)
    client = ReportClient(mock_config)
    ack = client.share(graph_id, "rep_1", "pl_1")
    assert ack["operation_id"].startswith("op_")

  @patch("robosystems_client.extensions.report_client.op_create_publish_list")
  def test_create_publish_list(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-publish-list",
      {
        "id": "pl_new",
        "name": "New List",
        "description": None,
        "member_count": 0,
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = ReportClient(mock_config)
    result = client.create_publish_list(graph_id, "New List")
    assert result["id"] == "pl_new"

  @patch("robosystems_client.extensions.report_client.op_add_publish_list_members")
  def test_add_members(self, mock_op, mock_config, graph_id):
    envelope = _envelope("add-publish-list-members", {"added": 2})
    mock_op.return_value = _mock_response(envelope)
    client = ReportClient(mock_config)
    result = client.add_members(graph_id, "pl_1", ["graph_a", "graph_b"])
    assert result["added"] == 2
    body = mock_op.call_args.kwargs["body"]
    assert body.list_id == "pl_1"
    assert body.target_graph_ids == ["graph_a", "graph_b"]

  @patch("robosystems_client.extensions.report_client.op_remove_publish_list_member")
  def test_remove_member(self, mock_op, mock_config, graph_id):
    envelope = _envelope("remove-publish-list-member", {"deleted": True})
    mock_op.return_value = _mock_response(envelope)
    client = ReportClient(mock_config)
    result = client.remove_member(graph_id, "pl_1", "mem_1")
    assert result["deleted"] is True


@pytest.mark.unit
class TestReportHelpers:
  def test_is_shared_report_with_dict(self, mock_config):
    client = ReportClient(mock_config)
    assert client.is_shared_report({"source_graph_id": "graph_src"}) is True
    assert client.is_shared_report({"source_graph_id": None}) is False

  def test_is_shared_report_with_object(self, mock_config):
    client = ReportClient(mock_config)
    obj = Mock()
    obj.source_graph_id = "graph_src"
    assert client.is_shared_report(obj) is True
