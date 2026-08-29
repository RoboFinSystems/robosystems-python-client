"""Unit tests for per-call credential resolution shared by the SSE-backed clients.

The stream endpoint authenticates whatever credential the request carries and
the backend revokes the previous JWT on every session refresh, so headers
captured at facade construction go dead the moment the session rotates.
`resolve_auth_headers` is what every stream connect and REST call now builds
its headers from.
"""

from unittest.mock import MagicMock, patch

import pytest

from robosystems_client.clients.auth_integration import _apply_auth_header
from robosystems_client.clients.operation_client import OperationClient
from robosystems_client.clients.sse_client import SSEClient, event_error_message
from robosystems_client.clients.token_utils import (
  apply_auth_header,
  resolve_auth_headers,
)


@pytest.mark.unit
class TestResolveAuthHeaders:
  def test_static_headers_untouched_without_provider(self):
    config = {
      "headers": {"X-API-Key": "legacy-key", "X-Trace": "1"},
      "token": "legacy-key",
    }

    assert resolve_auth_headers(config) == {"X-API-Key": "legacy-key", "X-Trace": "1"}

  def test_static_token_routed_when_headers_carry_no_credential(self):
    assert resolve_auth_headers({"headers": {}, "token": "rfs_key"}) == {
      "X-API-Key": "rfs_key"
    }
    assert resolve_auth_headers({"token": "eyJ.jwt"}) == {
      "Authorization": "Bearer eyJ.jwt"
    }

  def test_no_credential_at_all(self):
    assert resolve_auth_headers({"headers": {"X-Trace": "1"}}) == {"X-Trace": "1"}

  def test_provider_replaces_stale_static_credential(self):
    config = {
      "headers": {"Authorization": "Bearer stale", "X-Trace": "1"},
      "token": "stale",
      "token_provider": lambda: "fresh",
    }

    assert resolve_auth_headers(config) == {
      "Authorization": "Bearer fresh",
      "X-Trace": "1",
    }

  def test_provider_consulted_on_every_call(self):
    tokens = iter(["jwt-1", "jwt-2"])
    config = {"token_provider": lambda: next(tokens)}

    assert resolve_auth_headers(config)["Authorization"] == "Bearer jwt-1"
    assert resolve_auth_headers(config)["Authorization"] == "Bearer jwt-2"

  def test_provider_api_key_routes_to_x_api_key(self):
    config = {
      "headers": {"Authorization": "Bearer old"},
      "token_provider": lambda: "rfs_new",
    }

    assert resolve_auth_headers(config) == {"X-API-Key": "rfs_new"}

  def test_provider_returning_none_sends_no_credential(self):
    config = {"headers": {"X-API-Key": "stale"}, "token_provider": lambda: None}

    assert resolve_auth_headers(config) == {}

  def test_does_not_mutate_configured_headers(self):
    static = {"Authorization": "Bearer stale"}
    resolve_auth_headers({"headers": static, "token_provider": lambda: "fresh"})

    assert static == {"Authorization": "Bearer stale"}


@pytest.mark.unit
class TestApplyAuthHeader:
  def test_routes_by_credential_shape(self):
    headers = {}
    apply_auth_header(headers, "rfs_key")
    assert headers == {"X-API-Key": "rfs_key"}

    headers = {}
    apply_auth_header(headers, "eyJ.jwt")
    assert headers == {"Authorization": "Bearer eyJ.jwt"}

  def test_auth_integration_alias_shares_the_rule(self):
    headers = {}
    _apply_auth_header(headers, "rfs_key")
    assert headers == {"X-API-Key": "rfs_key"}


@pytest.mark.unit
class TestEventErrorMessage:
  def test_dict_payloads(self):
    assert event_error_message({"message": "boom"}) == "boom"
    assert event_error_message({"error": "bad"}) == "bad"
    assert event_error_message({}) == "Unknown error"

  def test_exception_payloads(self):
    assert event_error_message(RuntimeError("HTTP 401")) == "HTTP 401"


@pytest.mark.unit
class TestOperationClientHeaders:
  @patch("time.sleep")
  @patch("robosystems_client.clients.operation_client.SSEClient")
  def test_stream_headers_resolved_from_provider_at_connect(
    self, MockSSE, mock_sleep, mock_config
  ):
    current = {"jwt": "jwt-old"}
    config = {
      **mock_config,
      "headers": {"Authorization": "Bearer jwt-old"},
      "token": "jwt-old",
      "token_provider": lambda: current["jwt"],
    }
    client = OperationClient(config)
    current["jwt"] = "jwt-rotated"

    fake = MagicMock(spec=SSEClient)
    listeners = {}
    fake.on.side_effect = lambda event, handler: listeners.__setitem__(event, handler)
    fake.connect.side_effect = lambda op_id: listeners["operation_completed"](
      {"result": {"ok": True}}
    )
    MockSSE.return_value = fake

    client.monitor_operation("op-1")

    assert MockSSE.call_args[0][0].headers == {"Authorization": "Bearer jwt-rotated"}

  # `Client` is imported inside the method, so patch it at its source module.
  @patch("robosystems_client.client.Client")
  def test_status_call_uses_provider_credential(self, MockClient, mock_config):
    config = {**mock_config, "token_provider": lambda: "rfs_fresh"}
    with patch(
      "robosystems_client.api.operations.get_operation_status.sync_detailed"
    ) as mock_get:
      mock_get.return_value.parsed = None
      OperationClient(config).get_operation_status("op-1")

    assert MockClient.call_args.kwargs["headers"] == {"X-API-Key": "rfs_fresh"}
