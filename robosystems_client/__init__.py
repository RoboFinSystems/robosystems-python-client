"""RoboSystems Python Client."""

__version__ = "0.1.0"

from .client import AuthenticatedClient, Client

__all__ = (
  "AuthenticatedClient",
  "Client",
  "RoboSystemsSDK",
)

# Convenience alias for the main SDK
RoboSystemsSDK = AuthenticatedClient
