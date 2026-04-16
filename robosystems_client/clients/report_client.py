"""Report Client for RoboSystems API.

High-level facade for the report + publish-list surface: create/list/
view/regenerate/share/delete reports, render financial statements, and
manage publish lists (distribution lists for shared reports).

**Transport split:**
- **Reads** (list, get, statement, list_publish_lists, get_publish_list)
  go through GraphQL at `/extensions/{graph_id}/graphql`.
- **Writes** (create, regenerate, delete, share, publish-list CRUD) go
  through named operations at
  `/extensions/roboledger/{graph_id}/operations/{operation_name}`.

Async dispatches (create, regenerate, share) return a small ack dict
`{operation_id, status}`; consumers can subscribe to progress via
`/v1/operations/{operation_id}/stream`.
"""

from __future__ import annotations

from http import HTTPStatus
from typing import Any

from ..api.extensions_robo_ledger.op_add_publish_list_members import (
  sync_detailed as op_add_publish_list_members,
)
from ..api.extensions_robo_ledger.op_create_publish_list import (
  sync_detailed as op_create_publish_list,
)
from ..api.extensions_robo_ledger.op_create_report import (
  sync_detailed as op_create_report,
)
from ..api.extensions_robo_ledger.op_delete_publish_list import (
  sync_detailed as op_delete_publish_list,
)
from ..api.extensions_robo_ledger.op_delete_report import (
  sync_detailed as op_delete_report,
)
from ..api.extensions_robo_ledger.op_regenerate_report import (
  sync_detailed as op_regenerate_report,
)
from ..api.extensions_robo_ledger.op_remove_publish_list_member import (
  sync_detailed as op_remove_publish_list_member,
)
from ..api.extensions_robo_ledger.op_share_report import (
  sync_detailed as op_share_report,
)
from ..api.extensions_robo_ledger.op_update_publish_list import (
  sync_detailed as op_update_publish_list,
)
from ..client import AuthenticatedClient
from ..graphql.client import GraphQLClient
from ..graphql.queries.ledger import (
  GET_PUBLISH_LIST_QUERY,
  GET_REPORT_QUERY,
  GET_STATEMENT_QUERY,
  LIST_PUBLISH_LISTS_QUERY,
  LIST_REPORTS_QUERY,
  parse_publish_list,
  parse_publish_lists,
  parse_report,
  parse_reports,
  parse_statement,
)
from ..models.add_publish_list_members_operation import AddPublishListMembersOperation
from ..models.create_publish_list_request import CreatePublishListRequest
from ..models.create_report_request import CreateReportRequest
from ..models.delete_publish_list_operation import DeletePublishListOperation
from ..models.delete_report_operation import DeleteReportOperation
from ..models.operation_envelope import OperationEnvelope
from ..models.regenerate_report_operation import RegenerateReportOperation
from ..models.remove_publish_list_member_operation import (
  RemovePublishListMemberOperation,
)
from ..models.share_report_operation import ShareReportOperation
from ..models.update_publish_list_operation import UpdatePublishListOperation
from ..types import UNSET


class ReportClient:
  """High-level facade for reports + publish lists + statements."""

  def __init__(self, config: dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.timeout = config.get("timeout", 60)

  def _get_client(self) -> AuthenticatedClient:
    if not self.token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

  def _get_graphql_client(self) -> GraphQLClient:
    if not self.token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return GraphQLClient(
      base_url=self.base_url,
      token=self.token,
      headers=self.headers,
      timeout=self.timeout,
    )

  def _query(
    self,
    graph_id: str,
    query: str,
    variables: dict[str, Any] | None = None,
  ) -> dict[str, Any]:
    return self._get_graphql_client().execute(graph_id, query, variables)

  def _call_op(self, label: str, response: Any) -> OperationEnvelope:
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.ACCEPTED):
      raise RuntimeError(
        f"{label} failed: {response.status_code}: {response.content!r}"
      )
    envelope = response.parsed
    if not isinstance(envelope, OperationEnvelope):
      raise RuntimeError(f"{label} failed: unexpected response shape: {envelope!r}")
    return envelope

  # ── Reports ─────────────────────────────────────────────────────────

  def create(
    self,
    graph_id: str,
    name: str,
    mapping_id: str,
    period_start: str,
    period_end: str,
    taxonomy_id: str = "tax_usgaap_reporting",
    period_type: str = "quarterly",
    comparative: bool = True,
  ) -> dict[str, Any]:
    """Kick off report creation (async). Returns an operation ack."""
    body = CreateReportRequest(
      name=name,
      mapping_id=mapping_id,
      period_start=period_start,
      period_end=period_end,
      taxonomy_id=taxonomy_id,
      period_type=period_type,
      comparative=comparative,
    )
    response = op_create_report(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Create report", response)
    return {"operation_id": envelope.operation_id, "status": envelope.status}

  def list(self, graph_id: str) -> list[dict[str, Any]]:
    """List all reports for a graph (includes received shared reports)."""
    data = self._query(graph_id, LIST_REPORTS_QUERY)
    return parse_reports(data)

  def get(self, graph_id: str, report_id: str) -> dict[str, Any] | None:
    """Get a single report with its period list + available structures."""
    data = self._query(graph_id, GET_REPORT_QUERY, {"reportId": report_id})
    return parse_report(data)

  def statement(
    self, graph_id: str, report_id: str, structure_type: str
  ) -> dict[str, Any] | None:
    """Render a financial statement — facts viewed through a structure.

    `structure_type`: income_statement, balance_sheet, cash_flow_statement, …
    """
    data = self._query(
      graph_id,
      GET_STATEMENT_QUERY,
      {"reportId": report_id, "structureType": structure_type},
    )
    return parse_statement(data)

  def regenerate(
    self,
    graph_id: str,
    report_id: str,
    period_start: str | None = None,
    period_end: str | None = None,
  ) -> dict[str, Any]:
    """Regenerate an existing report (async). Returns an operation ack."""
    body = RegenerateReportOperation(
      report_id=report_id,
      period_start=period_start if period_start is not None else UNSET,
      period_end=period_end if period_end is not None else UNSET,
    )
    response = op_regenerate_report(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Regenerate report", response)
    return {"operation_id": envelope.operation_id, "status": envelope.status}

  def delete(self, graph_id: str, report_id: str) -> None:
    """Delete a report and its generated facts."""
    body = DeleteReportOperation(report_id=report_id)
    response = op_delete_report(graph_id=graph_id, body=body, client=self._get_client())
    self._call_op("Delete report", response)

  def share(
    self, graph_id: str, report_id: str, publish_list_id: str
  ) -> dict[str, Any]:
    """Share a published report to every member of a publish list (async)."""
    body = ShareReportOperation(report_id=report_id, publish_list_id=publish_list_id)
    response = op_share_report(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Share report", response)
    return {"operation_id": envelope.operation_id, "status": envelope.status}

  def is_shared_report(self, report: dict[str, Any] | Any) -> bool:
    """Check if a report was received via sharing (vs locally created)."""
    if isinstance(report, dict):
      return report.get("source_graph_id") is not None
    return getattr(report, "source_graph_id", None) is not None

  # ── Publish Lists ────────────────────────────────────────────────────

  def list_publish_lists(
    self, graph_id: str, limit: int = 100, offset: int = 0
  ) -> dict[str, Any] | None:
    """List publish lists with pagination."""
    data = self._query(
      graph_id, LIST_PUBLISH_LISTS_QUERY, {"limit": limit, "offset": offset}
    )
    return parse_publish_lists(data)

  def get_publish_list(self, graph_id: str, list_id: str) -> dict[str, Any] | None:
    """Get a single publish list with its full member list."""
    data = self._query(graph_id, GET_PUBLISH_LIST_QUERY, {"listId": list_id})
    return parse_publish_list(data)

  def create_publish_list(
    self, graph_id: str, name: str, description: str | None = None
  ) -> dict[str, Any]:
    """Create a new publish list."""
    body = CreatePublishListRequest(
      name=name,
      description=description if description is not None else UNSET,
    )
    response = op_create_publish_list(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create publish list", response)
    return envelope.result or {}

  def update_publish_list(
    self,
    graph_id: str,
    list_id: str,
    name: str | None = None,
    description: str | None = None,
  ) -> dict[str, Any]:
    """Update a publish list's name or description."""
    body = UpdatePublishListOperation(
      list_id=list_id,
      name=name if name is not None else UNSET,
      description=description if description is not None else UNSET,
    )
    response = op_update_publish_list(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update publish list", response)
    return envelope.result or {}

  def delete_publish_list(self, graph_id: str, list_id: str) -> None:
    """Delete a publish list."""
    body = DeletePublishListOperation(list_id=list_id)
    response = op_delete_publish_list(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    self._call_op("Delete publish list", response)

  def add_members(
    self, graph_id: str, list_id: str, target_graph_ids: list[str]
  ) -> dict[str, Any]:
    """Add target graphs as members of a publish list."""
    body = AddPublishListMembersOperation(
      list_id=list_id, target_graph_ids=target_graph_ids
    )
    response = op_add_publish_list_members(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Add publish list members", response)
    return envelope.result or {}

  def remove_member(
    self, graph_id: str, list_id: str, member_id: str
  ) -> dict[str, Any]:
    """Remove a single member from a publish list."""
    body = RemovePublishListMemberOperation(list_id=list_id, member_id=member_id)
    response = op_remove_publish_list_member(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Remove publish list member", response)
    return envelope.result if envelope.result is not None else {"deleted": True}
