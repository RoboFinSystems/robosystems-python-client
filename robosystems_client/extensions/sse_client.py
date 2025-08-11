"""Core SSE (Server-Sent Events) client for RoboSystems API

Provides automatic reconnection, event replay, and type-safe event handling.
"""

import json
import time
import asyncio
from datetime import datetime
from enum import Enum
from typing import Dict, Any, Optional, Callable, Set, TYPE_CHECKING
from dataclasses import dataclass
from urllib.parse import urljoin

try:
  import sseclient
except ImportError:
  sseclient = None

try:
  import httpx
except ImportError:
  httpx = None

if TYPE_CHECKING:
  if httpx:
    from httpx import Client, AsyncClient
  else:
    Client = Any
    AsyncClient = Any
else:
  Client = Any
  AsyncClient = Any


@dataclass
class SSEConfig:
  """Configuration for SSE client"""

  base_url: str
  headers: Optional[Dict[str, str]] = None
  max_retries: int = 5
  retry_delay: int = 1000  # milliseconds
  heartbeat_interval: int = 30000  # milliseconds
  timeout: int = 30  # seconds


@dataclass
class SSEEvent:
  """Represents an SSE event"""

  event: str
  data: Any
  id: Optional[str] = None
  retry: Optional[int] = None
  timestamp: datetime = None

  def __post_init__(self) -> None:
    if self.timestamp is None:
      self.timestamp = datetime.now()


class EventType(Enum):
  """Standard event types from RoboSystems API"""

  OPERATION_STARTED = "operation_started"
  OPERATION_PROGRESS = "operation_progress"
  OPERATION_COMPLETED = "operation_completed"
  OPERATION_ERROR = "operation_error"
  OPERATION_CANCELLED = "operation_cancelled"
  DATA_CHUNK = "data_chunk"
  METADATA = "metadata"
  HEARTBEAT = "heartbeat"
  QUEUE_UPDATE = "queue_update"


class SSEClient:
  """SSE client for RoboSystems API with automatic reconnection"""

  def __init__(self, config: SSEConfig) -> None:
    if not httpx:
      raise ImportError(
        "httpx is required for SSE client. Install with: pip install httpx"
      )

    self.config = config
    self.client: Optional[Client] = None
    self.reconnect_attempts = 0
    self.last_event_id: Optional[str] = None
    self.closed = False
    self.listeners: Dict[str, Set[Callable]] = {}
    self._response = None

  def connect(self, operation_id: str, from_sequence: int = 0) -> None:
    """Connect to SSE stream for the given operation"""
    url = urljoin(self.config.base_url, f"/v1/operations/{operation_id}/stream")
    params = {"from_sequence": from_sequence}

    headers = {
      "Accept": "text/event-stream",
      "Cache-Control": "no-cache",
      **(self.config.headers or {}),
    }

    try:
      self.client = httpx.Client(timeout=self.config.timeout)
      self._response = self.client.stream("GET", url, params=params, headers=headers)
      self._response.__enter__()

      self.reconnect_attempts = 0
      self.emit("connected", None)

      # Start processing events
      self._process_events()

    except Exception as error:
      if not self.closed:
        self._handle_error(error, operation_id, from_sequence)

  def _process_events(self) -> None:
    """Process incoming SSE events according to SSE specification"""
    if not self._response:
      return

    try:
      event_buffer = {"event": None, "data": [], "id": None, "retry": None}

      for line in self._response.iter_lines():
        if self.closed:
          break

        line = line.strip()

        # Empty line indicates end of event
        if not line:
          if event_buffer["data"] or event_buffer["event"]:
            self._dispatch_event(event_buffer)
          event_buffer = {"event": None, "data": [], "id": None, "retry": None}
          continue

        # Skip comment lines
        if line.startswith(":"):
          continue

        # Parse field
        if ":" in line:
          field, value = line.split(":", 1)
          field = field.strip()
          value = value.lstrip()  # Remove leading space but keep others

          if field == "data":
            event_buffer["data"].append(value)
          elif field == "event":
            event_buffer["event"] = value
          elif field == "id":
            event_buffer["id"] = value
            self.last_event_id = value
          elif field == "retry":
            try:
              event_buffer["retry"] = int(value)
            except ValueError:
              pass  # Ignore invalid retry values
        else:
          # Field with no value
          if line == "data":
            event_buffer["data"].append("")
          elif line in ["event", "id", "retry"]:
            event_buffer[line] = ""

      # Handle final event if stream ends without empty line
      if event_buffer["data"] or event_buffer["event"]:
        self._dispatch_event(event_buffer)

    except Exception as error:
      if not self.closed:
        self.emit("error", error)

  def _dispatch_event(self, event_buffer: Dict[str, Any]) -> None:
    """Dispatch a complete SSE event"""
    # Join data lines with newlines as per SSE spec
    data_str = "\n".join(event_buffer["data"])

    if not data_str and not event_buffer["event"]:
      return  # Skip empty events

    event_type = event_buffer["event"] or "message"

    # Parse JSON data if possible
    parsed_data = data_str
    try:
      if data_str:
        parsed_data = json.loads(data_str)
    except json.JSONDecodeError:
      # Keep as string if not valid JSON
      pass

    sse_event = SSEEvent(
      event=event_type,
      data=parsed_data,
      id=event_buffer["id"],
      timestamp=datetime.now(),
    )

    # Emit generic event
    self.emit("event", sse_event)

    # Emit typed event
    self.emit(event_type, parsed_data)

    # Check for completion events
    if event_type in [
      EventType.OPERATION_COMPLETED.value,
      EventType.OPERATION_ERROR.value,
      EventType.OPERATION_CANCELLED.value,
    ]:
      self.close()

  def _handle_error(
    self, error: Exception, operation_id: str, from_sequence: int
  ) -> None:
    """Handle connection errors with retry logic"""
    if self.closed:
      return

    if self.reconnect_attempts < self.config.max_retries:
      self.reconnect_attempts += 1
      delay_ms = self.config.retry_delay * (2 ** (self.reconnect_attempts - 1))
      delay_seconds = delay_ms / 1000

      self.emit(
        "reconnecting",
        {
          "attempt": self.reconnect_attempts,
          "delay": delay_ms,
          "last_event_id": self.last_event_id,
        },
      )

      time.sleep(delay_seconds)

      # Resume from last event if available
      resume_from = 0
      if self.last_event_id:
        try:
          resume_from = int(self.last_event_id) + 1
        except ValueError:
          resume_from = from_sequence
      else:
        resume_from = from_sequence

      self.connect(operation_id, resume_from)
    else:
      self.emit("max_retries_exceeded", error)
      self.close()

  def on(self, event: str, listener: Callable[[Any], None]) -> None:
    """Add event listener"""
    if event not in self.listeners:
      self.listeners[event] = set()
    self.listeners[event].add(listener)

  def off(self, event: str, listener: Callable[[Any], None]) -> None:
    """Remove event listener"""
    if event in self.listeners:
      self.listeners[event].discard(listener)

  def emit(self, event: str, data: Any) -> None:
    """Emit event to all listeners"""
    if event in self.listeners:
      for listener in self.listeners[event]:
        try:
          listener(data)
        except Exception as e:
          # Log error but don't stop other listeners
          print(f"Error in event listener for {event}: {e}")

  def close(self):
    """Close the SSE connection"""
    self.closed = True

    if self._response:
      try:
        self._response.__exit__(None, None, None)
      except Exception:
        pass
      self._response = None

    if self.client:
      self.client.close()
      self.client = None

    self.emit("closed", None)
    self.listeners.clear()

  def is_connected(self) -> bool:
    """Check if the connection is active"""
    return self.client is not None and not self.closed


class AsyncSSEClient:
  """Async version of SSE client"""

  def __init__(self, config: SSEConfig) -> None:
    if not httpx:
      raise ImportError(
        "httpx is required for async SSE client. Install with: pip install httpx"
      )

    self.config = config
    self.client: Optional[AsyncClient] = None
    self.reconnect_attempts = 0
    self.last_event_id: Optional[str] = None
    self.closed = False
    self.listeners: Dict[str, Set[Callable]] = {}
    self._response = None

  async def connect(self, operation_id: str, from_sequence: int = 0) -> None:
    """Connect to SSE stream for the given operation (async)"""
    url = urljoin(self.config.base_url, f"/v1/operations/{operation_id}/stream")
    params = {"from_sequence": from_sequence}

    headers = {
      "Accept": "text/event-stream",
      "Cache-Control": "no-cache",
      **(self.config.headers or {}),
    }

    try:
      self.client = httpx.AsyncClient(timeout=self.config.timeout)
      self._response = await self.client.stream(
        "GET", url, params=params, headers=headers
      )
      await self._response.__aenter__()

      self.reconnect_attempts = 0
      self.emit("connected", None)

      # Start processing events
      await self._process_events()

    except Exception as error:
      if not self.closed:
        await self._handle_error(error, operation_id, from_sequence)

  async def _process_events(self) -> None:
    """Process incoming SSE events according to SSE specification (async)"""
    if not self._response:
      return

    try:
      event_buffer = {"event": None, "data": [], "id": None, "retry": None}

      async for line in self._response.aiter_lines():
        if self.closed:
          break

        line = line.strip()

        # Empty line indicates end of event
        if not line:
          if event_buffer["data"] or event_buffer["event"]:
            self._dispatch_event(event_buffer)
          event_buffer = {"event": None, "data": [], "id": None, "retry": None}
          continue

        # Skip comment lines
        if line.startswith(":"):
          continue

        # Parse field
        if ":" in line:
          field, value = line.split(":", 1)
          field = field.strip()
          value = value.lstrip()

          if field == "data":
            event_buffer["data"].append(value)
          elif field == "event":
            event_buffer["event"] = value
          elif field == "id":
            event_buffer["id"] = value
            self.last_event_id = value
          elif field == "retry":
            try:
              event_buffer["retry"] = int(value)
            except ValueError:
              pass
        else:
          # Field with no value
          if line == "data":
            event_buffer["data"].append("")
          elif line in ["event", "id", "retry"]:
            event_buffer[line] = ""

      # Handle final event if stream ends without empty line
      if event_buffer["data"] or event_buffer["event"]:
        self._dispatch_event(event_buffer)

    except Exception as error:
      if not self.closed:
        self.emit("error", error)

  def _dispatch_event(self, event_buffer: Dict[str, Any]):
    """Dispatch a complete SSE event (same as sync version)"""
    # Join data lines with newlines as per SSE spec
    data_str = "\n".join(event_buffer["data"])

    if not data_str and not event_buffer["event"]:
      return  # Skip empty events

    event_type = event_buffer["event"] or "message"

    # Parse JSON data if possible
    parsed_data = data_str
    try:
      if data_str:
        parsed_data = json.loads(data_str)
    except json.JSONDecodeError:
      # Keep as string if not valid JSON
      pass

    sse_event = SSEEvent(
      event=event_type,
      data=parsed_data,
      id=event_buffer["id"],
      timestamp=datetime.now(),
    )

    # Emit generic event
    self.emit("event", sse_event)

    # Emit typed event
    self.emit(event_type, parsed_data)

    # Check for completion events
    if event_type in [
      EventType.OPERATION_COMPLETED.value,
      EventType.OPERATION_ERROR.value,
      EventType.OPERATION_CANCELLED.value,
    ]:
      asyncio.create_task(self.close())

  async def _handle_error(
    self, error: Exception, operation_id: str, from_sequence: int
  ) -> None:
    """Handle connection errors with retry logic (async)"""
    if self.closed:
      return

    if self.reconnect_attempts < self.config.max_retries:
      self.reconnect_attempts += 1
      delay_ms = self.config.retry_delay * (2 ** (self.reconnect_attempts - 1))
      delay_seconds = delay_ms / 1000

      self.emit(
        "reconnecting",
        {
          "attempt": self.reconnect_attempts,
          "delay": delay_ms,
          "last_event_id": self.last_event_id,
        },
      )

      await asyncio.sleep(delay_seconds)

      resume_from = 0
      if self.last_event_id:
        try:
          resume_from = int(self.last_event_id) + 1
        except ValueError:
          resume_from = from_sequence
      else:
        resume_from = from_sequence

      await self.connect(operation_id, resume_from)
    else:
      self.emit("max_retries_exceeded", error)
      await self.close()

  def on(self, event: str, listener: Callable[[Any], None]) -> None:
    """Add event listener"""
    if event not in self.listeners:
      self.listeners[event] = set()
    self.listeners[event].add(listener)

  def off(self, event: str, listener: Callable[[Any], None]) -> None:
    """Remove event listener"""
    if event in self.listeners:
      self.listeners[event].discard(listener)

  def emit(self, event: str, data: Any) -> None:
    """Emit event to all listeners"""
    if event in self.listeners:
      for listener in self.listeners[event]:
        try:
          listener(data)
        except Exception as e:
          print(f"Error in event listener for {event}: {e}")

  async def close(self):
    """Close the SSE connection (async)"""
    self.closed = True

    if self._response:
      try:
        await self._response.__aexit__(None, None, None)
      except Exception:
        pass
      self._response = None

    if self.client:
      await self.client.aclose()
      self.client = None

    self.emit("closed", None)
    self.listeners.clear()

  def is_connected(self) -> bool:
    """Check if the connection is active"""
    return self.client is not None and not self.closed
