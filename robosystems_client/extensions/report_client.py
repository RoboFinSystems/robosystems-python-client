"""Report Client for RoboSystems API

High-level client for report lifecycle: create, list, view statements,
regenerate, share, and delete.
"""

from __future__ import annotations

from http import HTTPStatus
from typing import Any

from ..api.ledger.create_report import sync_detailed as create_report
from ..api.ledger.delete_report import sync_detailed as delete_report
from ..api.ledger.get_report import sync_detailed as get_report
from ..api.ledger.get_statement import sync_detailed as get_statement
from ..api.ledger.list_reports import sync_detailed as list_reports
from ..api.ledger.regenerate_report import sync_detailed as regenerate_report
from ..api.ledger.share_report import sync_detailed as share_report
from ..client import AuthenticatedClient


class ReportClient:
  """Client for report lifecycle: create, list, view, share, delete."""

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
  ) -> Any:
    """Create a report — generates facts for all structures in the taxonomy."""
    from ..models.create_report_request import CreateReportRequest

    body = CreateReportRequest(
      name=name,
      mapping_id=mapping_id,
      period_start=period_start,
      period_end=period_end,
      taxonomy_id=taxonomy_id,
      period_type=period_type,
      comparative=comparative,
    )
    response = create_report(graph_id=graph_id, body=body, client=self._get_client())
    if response.status_code != HTTPStatus.CREATED:
      raise RuntimeError(f"Create report failed: {response.status_code}")
    return response.parsed

  def list(self, graph_id: str) -> Any:
    """List all reports for a graph (includes received shared reports)."""
    response = list_reports(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List reports failed: {response.status_code}")
    return response.parsed

  def get(self, graph_id: str, report_id: str) -> Any:
    """Get a report with its available structures."""
    response = get_report(
      graph_id=graph_id, report_id=report_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get report failed: {response.status_code}")
    return response.parsed

  def statement(self, graph_id: str, report_id: str, structure_type: str) -> Any:
    """Render a financial statement — facts viewed through a structure."""
    response = get_statement(
      graph_id=graph_id,
      report_id=report_id,
      structure_type=structure_type,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get statement failed: {response.status_code}")
    return response.parsed

  def regenerate(
    self, graph_id: str, report_id: str, period_start: str, period_end: str
  ) -> Any:
    """Regenerate a report with new period dates."""
    from ..models.regenerate_report_request import RegenerateReportRequest

    body = RegenerateReportRequest(period_start=period_start, period_end=period_end)
    response = regenerate_report(
      graph_id=graph_id, report_id=report_id, body=body, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Regenerate report failed: {response.status_code}")
    return response.parsed

  def delete(self, graph_id: str, report_id: str) -> None:
    """Delete a report and its generated facts."""
    response = delete_report(
      graph_id=graph_id, report_id=report_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.NO_CONTENT:
      raise RuntimeError(f"Delete report failed: {response.status_code}")

  def share(self, graph_id: str, report_id: str, target_graph_ids: list[str]) -> Any:
    """Share a published report to other graphs (snapshot copy)."""
    from ..models.share_report_request import ShareReportRequest

    body = ShareReportRequest(target_graph_ids=target_graph_ids)
    response = share_report(
      graph_id=graph_id, report_id=report_id, body=body, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Share report failed: {response.status_code}")
    return response.parsed

  def is_shared_report(self, report: Any) -> bool:
    """Check if a report was received via sharing."""
    return getattr(report, "source_graph_id", None) is not None
