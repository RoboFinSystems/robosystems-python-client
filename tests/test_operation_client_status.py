"""Unit tests for OperationClient's status and cancel calls.

Both read the response body of a free-form operations endpoint. The
generator emits models whose only field is ``additional_properties``, so
attribute access on them raises whatever the payload held — and both
methods wrap the call in a broad ``except``, which turned that
AttributeError into a plausible-looking failure result for *every*
response, successful ones included.

``operator_client._poll_for_completion`` already read these through
``to_dict()``; these tests pin that the same accessor is used here.
"""

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from robosystems_client.clients.operation_client import (
  OperationClient,
  _parsed_dict,
)
from robosystems_client.models.cancel_operation_response_canceloperation import (
  CancelOperationResponseCanceloperation,
)
from robosystems_client.models.get_operation_status_response_getoperationstatus import (
  GetOperationStatusResponseGetoperationstatus,
)


@pytest.fixture
def client() -> OperationClient:
  return OperationClient(
    {"base_url": "http://localhost:8000", "token": "rfs_test", "headers": {}}
  )


def _status_response(body: dict[str, Any]) -> MagicMock:
  response = MagicMock()
  response.parsed = GetOperationStatusResponseGetoperationstatus.from_dict(body)
  return response


def _cancel_response(body: dict[str, Any]) -> MagicMock:
  response = MagicMock()
  response.parsed = CancelOperationResponseCanceloperation.from_dict(body)
  return response


@pytest.mark.unit
class TestParsedDict:
  def test_reads_an_additional_properties_model(self):
    parsed = GetOperationStatusResponseGetoperationstatus.from_dict(
      {"status": "completed"}
    )
    # The accessor that motivated this helper: attribute access does not
    # work on these models, whatever the payload contained.
    assert not hasattr(parsed, "status")
    assert _parsed_dict(parsed) == {"status": "completed"}

  def test_passes_a_plain_dict_through(self):
    assert _parsed_dict({"status": "queued"}) == {"status": "queued"}

  def test_none_when_there_is_no_body(self):
    assert _parsed_dict(None) is None


@pytest.mark.unit
class TestGetOperationStatus:
  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_returns_the_real_status(self, mock_get, client: OperationClient):
    mock_get.return_value = _status_response(
      {
        "operation_id": "op_1",
        "status": "completed",
        "progress": 100,
        "result": {"rows": 3},
      }
    )

    result = client.get_operation_status("op_1")

    # Previously this whole payload was discarded and the method returned
    # {"status": "error", "error": "...has no attribute 'status'"}.
    assert result["status"] == "completed"
    assert result["progress"] == 100
    assert result["result"] == {"rows": 3}
    assert result["error"] is None
    assert result["operation_id"] == "op_1"

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_surfaces_a_failed_operation(self, mock_get, client: OperationClient):
    mock_get.return_value = _status_response(
      {"status": "failed", "error": "materialization timed out"}
    )

    result = client.get_operation_status("op_1")

    assert result["status"] == "failed"
    assert result["error"] == "materialization timed out"

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_unknown_when_the_body_omits_status(self, mock_get, client: OperationClient):
    mock_get.return_value = _status_response({"operation_id": "op_1"})

    assert client.get_operation_status("op_1")["status"] == "unknown"

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_unknown_when_there_is_no_body(self, mock_get, client: OperationClient):
    response = MagicMock()
    response.parsed = None
    mock_get.return_value = response

    assert client.get_operation_status("op_1")["status"] == "unknown"

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_transport_failure_still_reports_an_error(
    self, mock_get, client: OperationClient
  ):
    mock_get.side_effect = RuntimeError("connection refused")

    result = client.get_operation_status("op_1")

    assert result["status"] == "error"
    assert "connection refused" in result["error"]


@pytest.mark.unit
class TestCancelOperation:
  @patch("robosystems_client.api.operations.cancel_operation.sync_detailed")
  def test_returns_true_when_the_cancel_lands(self, mock_cancel, client):
    mock_cancel.return_value = _cancel_response({"cancelled": True})

    assert client.cancel_operation("op_1") is True

  @patch("robosystems_client.api.operations.cancel_operation.sync_detailed")
  def test_returns_false_when_the_server_declines(self, mock_cancel, client):
    mock_cancel.return_value = _cancel_response({"cancelled": False})

    assert client.cancel_operation("op_1") is False

  @patch("robosystems_client.api.operations.cancel_operation.sync_detailed")
  def test_closes_the_stream_on_a_successful_cancel(self, mock_cancel, client):
    # The cleanup used to sit after an early `return` on the success path,
    # so the one case that needs it skipped it and leaked the stream.
    mock_cancel.return_value = _cancel_response({"cancelled": True})
    stream = MagicMock()
    client.active_operations["op_1"] = stream

    assert client.cancel_operation("op_1") is True
    stream.close.assert_called_once()
    assert "op_1" not in client.active_operations

  @patch("robosystems_client.api.operations.cancel_operation.sync_detailed")
  def test_transport_failure_returns_false(self, mock_cancel, client):
    mock_cancel.side_effect = RuntimeError("connection refused")

    assert client.cancel_operation("op_1") is False
