"""RoboSystems Python SDK."""

__version__ = "0.1.0"

from .client import AuthenticatedClient, Client

__all__ = (
  "AuthenticatedClient",
  "Client",
  "RoboSystemsClient",
)

# Convenience alias for the main client
RoboSystemsClient = AuthenticatedClient
