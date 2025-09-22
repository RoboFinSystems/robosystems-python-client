"""RoboSystems Python Client."""

from .client import AuthenticatedClient, Client

# Convenience alias for the main SDK
RoboSystemsSDK = AuthenticatedClient

__all__ = (
  "AuthenticatedClient",
  "Client",
  "RoboSystemsSDK",
)


def _get_version() -> str:
  """Get version from package metadata."""
  try:
    from importlib.metadata import version

    return version("robosystems-client")
  except Exception:
    return "0.0.0+development"


__version__ = _get_version()
