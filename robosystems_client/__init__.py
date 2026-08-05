"""RoboSystems Python Client."""

from .client import AuthenticatedClient, Client
from .clients import (
  InvestorClient,
  LedgerClient,
  LibraryClient,
  RoboSystemsClientConfig,
  RoboSystemsClients,
  get_clients,
)
from .graphql.client import GraphQLError

# Convenience aliases for the main SDK
RoboSystemsClient = AuthenticatedClient
RoboSystemsSDK = AuthenticatedClient

__all__ = (
  "AuthenticatedClient",
  "Client",
  "GraphQLError",
  "InvestorClient",
  "LedgerClient",
  "LibraryClient",
  "RoboSystemsClient",
  "RoboSystemsClientConfig",
  "RoboSystemsClients",
  "RoboSystemsSDK",
  "get_clients",
)


def _get_version() -> str:
  """Get version from package metadata."""
  try:
    from importlib.metadata import version

    return version("robosystems-client")
  except Exception:
    return "0.0.0+development"


__version__ = _get_version()
