"""Library Client for RoboSystems API.

Read-only facade for the taxonomy library — the shared reference material
(sfac6, fac, rs-gaap, …, mapping taxonomies) in the extensions DB public
schema.

**Two access modes** — picked by the caller's ``graph_id``:

- ``"library"`` (sentinel, default) → canonical browse of the public
  schema. Route: ``POST /extensions/library/graphql``.
- Any tenant ``graph_id`` (``"kg…"``) → tenant schema + public fallback
  via search_path. Returns the tenant's library copy plus any tenant
  extensions of library tables. Route: ``POST /extensions/{graph_id}/graphql``.

**Read-only**: the library is immutable at the DB level (triggers block
UPDATE/DELETE on rows whose ``created_by='library-seeder'``), so there is
no write surface here. Tenant-scope writes go through ``LedgerClient``.
"""

from __future__ import annotations

from typing import Any

from ..graphql.client import GraphQLClient, strip_none_vars
from ..graphql.generated.get_library_element import (
  GetLibraryElement,
)
from ..graphql.generated.get_library_element import (
  GetLibraryElementLibraryElement as LibraryElement,
)
from ..graphql.generated.get_library_element_arcs import (
  GetLibraryElementArcs,
  GetLibraryElementArcsLibraryElementArcs,
)
from ..graphql.generated.get_library_element_equivalents import (
  GetLibraryElementEquivalents,
)
from ..graphql.generated.get_library_element_equivalents import (
  GetLibraryElementEquivalentsLibraryElementEquivalents as LibraryElementEquivalents,
)
from ..graphql.generated.get_library_taxonomy import (
  GetLibraryTaxonomy,
)
from ..graphql.generated.get_library_taxonomy import (
  GetLibraryTaxonomyLibraryTaxonomy as LibraryTaxonomy,
)
from ..graphql.generated.list_library_elements import (
  ListLibraryElements,
  ListLibraryElementsLibraryElements,
)
from ..graphql.generated.list_library_taxonomies import (
  ListLibraryTaxonomies,
  ListLibraryTaxonomiesLibraryTaxonomies,
)
from ..graphql.generated.list_library_taxonomy_arcs import (
  ListLibraryTaxonomyArcs,
)
from ..graphql.generated.operations import (
  GET_LIBRARY_ELEMENT_ARCS_GQL,
  GET_LIBRARY_ELEMENT_EQUIVALENTS_GQL,
  GET_LIBRARY_ELEMENT_GQL,
  GET_LIBRARY_TAXONOMY_GQL,
  LIST_LIBRARY_ELEMENTS_GQL,
  LIST_LIBRARY_TAXONOMIES_GQL,
  LIST_LIBRARY_TAXONOMY_ARCS_GQL,
  SEARCH_LIBRARY_ELEMENTS_GQL,
)
from ..graphql.generated.search_library_elements import (
  SearchLibraryElements,
  SearchLibraryElementsSearchLibraryElements,
)

LIBRARY_GRAPH_ID = "library"
"""Sentinel graph_id for the canonical library read surface.

Passing this to any LibraryClient method routes the GraphQL request to
``/extensions/library/graphql`` and reads from the public schema only.
"""


class LibraryClient:
  """Read-only facade for the RoboSystems taxonomy library."""

  def __init__(self, config: dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.timeout = config.get("timeout", 60)

  def _get_graphql_client(self) -> GraphQLClient:
    if not self.token:
      raise RuntimeError("No API key provided. Set token in config.")
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
    cleaned = strip_none_vars(variables) if variables else None
    return self._get_graphql_client().execute(graph_id, query, cleaned)

  # ── Taxonomies ──────────────────────────────────────────────────────

  def list_library_taxonomies(
    self,
    graph_id: str = LIBRARY_GRAPH_ID,
    *,
    standard: str | None = None,
    include_element_count: bool = False,
  ) -> list[ListLibraryTaxonomiesLibraryTaxonomies]:
    """List every taxonomy visible at this graph_id."""
    data = self._query(
      graph_id,
      LIST_LIBRARY_TAXONOMIES_GQL,
      {"standard": standard, "includeElementCount": include_element_count},
    )
    return ListLibraryTaxonomies.model_validate(data).library_taxonomies

  def get_library_taxonomy(
    self,
    graph_id: str = LIBRARY_GRAPH_ID,
    *,
    id: str | None = None,
    standard: str | None = None,
    version: str | None = None,
    include_element_count: bool = False,
  ) -> LibraryTaxonomy | None:
    """Fetch one taxonomy by id or by (standard, version). Returns None if not found."""
    data = self._query(
      graph_id,
      GET_LIBRARY_TAXONOMY_GQL,
      {
        "id": id,
        "standard": standard,
        "version": version,
        "includeElementCount": include_element_count,
      },
    )
    return GetLibraryTaxonomy.model_validate(data).library_taxonomy

  # ── Elements ────────────────────────────────────────────────────────

  def list_library_elements(
    self,
    graph_id: str = LIBRARY_GRAPH_ID,
    *,
    taxonomy_id: str | None = None,
    source: str | None = None,
    classification: str | None = None,
    activity_type: str | None = None,
    element_type: str | None = None,
    is_abstract: bool | None = None,
    limit: int = 50,
    offset: int = 0,
    include_labels: bool = False,
    include_references: bool = False,
  ) -> list[ListLibraryElementsLibraryElements]:
    """List library elements with filters and pagination."""
    data = self._query(
      graph_id,
      LIST_LIBRARY_ELEMENTS_GQL,
      {
        "taxonomyId": taxonomy_id,
        "source": source,
        "classification": classification,
        "activityType": activity_type,
        "elementType": element_type,
        "isAbstract": is_abstract,
        "limit": limit,
        "offset": offset,
        "includeLabels": include_labels,
        "includeReferences": include_references,
      },
    )
    return ListLibraryElements.model_validate(data).library_elements

  def search_library_elements(
    self,
    query: str,
    graph_id: str = LIBRARY_GRAPH_ID,
    *,
    source: str | None = None,
    limit: int = 50,
  ) -> list[SearchLibraryElementsSearchLibraryElements]:
    """Substring search across qname, name, and standard label text."""
    data = self._query(
      graph_id,
      SEARCH_LIBRARY_ELEMENTS_GQL,
      {"query": query, "source": source, "limit": limit},
    )
    return SearchLibraryElements.model_validate(data).search_library_elements

  def get_library_element(
    self,
    graph_id: str = LIBRARY_GRAPH_ID,
    *,
    id: str | None = None,
    qname: str | None = None,
  ) -> LibraryElement | None:
    """Get a single element by id or qname. Returns None if not found."""
    data = self._query(
      graph_id,
      GET_LIBRARY_ELEMENT_GQL,
      {"id": id, "qname": qname},
    )
    return GetLibraryElement.model_validate(data).library_element

  # ── Arcs / Equivalence ──────────────────────────────────────────────

  def list_library_taxonomy_arcs(
    self,
    taxonomy_id: str,
    graph_id: str = LIBRARY_GRAPH_ID,
    *,
    association_type: str | None = None,
    limit: int = 200,
    offset: int = 0,
  ) -> ListLibraryTaxonomyArcs:
    """All arcs contributed by a taxonomy plus their total count.

    Returns the typed response carrying both root fields:
    ``library_taxonomy_arcs`` (the page of arcs) and
    ``library_taxonomy_arc_count`` (total before pagination).
    """
    data = self._query(
      graph_id,
      LIST_LIBRARY_TAXONOMY_ARCS_GQL,
      {
        "taxonomyId": taxonomy_id,
        "associationType": association_type,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListLibraryTaxonomyArcs.model_validate(data)

  def get_library_element_arcs(
    self,
    id: str,
    graph_id: str = LIBRARY_GRAPH_ID,
  ) -> list[GetLibraryElementArcsLibraryElementArcs]:
    """All mapping arcs where this element is source or target."""
    data = self._query(graph_id, GET_LIBRARY_ELEMENT_ARCS_GQL, {"id": id})
    return GetLibraryElementArcs.model_validate(data).library_element_arcs

  def get_library_element_equivalents(
    self,
    id: str,
    graph_id: str = LIBRARY_GRAPH_ID,
  ) -> LibraryElementEquivalents | None:
    """Equivalence fan-out (FAC ↔ us-gaap collapse). Returns None if not found."""
    data = self._query(graph_id, GET_LIBRARY_ELEMENT_EQUIVALENTS_GQL, {"id": id})
    return GetLibraryElementEquivalents.model_validate(data).library_element_equivalents
