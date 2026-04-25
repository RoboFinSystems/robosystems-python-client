"""Library-domain GraphQL queries and parsers.

Read-only facade for the taxonomy library — the shared reference material
(sfac6, fac, rs-gaap, …, mapping taxonomies) in the extensions DB public
schema.

Same pattern as the investor queries: one constant + one ``parse_*``
helper per query, returning camelCase → snake_case dicts.
"""

from __future__ import annotations

from typing import Any

from ...client import keys_to_snake


# ── Taxonomies ─────────────────────────────────────────────────────────

LIST_LIBRARY_TAXONOMIES_QUERY = """
query ListLibraryTaxonomies($standard: String, $includeElementCount: Boolean! = false) {
  libraryTaxonomies(standard: $standard, includeElementCount: $includeElementCount) {
    id
    name
    description
    standard
    version
    namespaceUri
    taxonomyType
    isShared
    isActive
    isLocked
    elementCount
  }
}
""".strip()


def parse_library_taxonomies(data: dict[str, Any]) -> list[dict[str, Any]]:
  items = data.get("libraryTaxonomies") or []
  return [keys_to_snake(t) for t in items]


GET_LIBRARY_TAXONOMY_QUERY = """
query GetLibraryTaxonomy(
  $id: ID
  $standard: String
  $version: String
  $includeElementCount: Boolean! = false
) {
  libraryTaxonomy(
    id: $id
    standard: $standard
    version: $version
    includeElementCount: $includeElementCount
  ) {
    id
    name
    description
    standard
    version
    namespaceUri
    taxonomyType
    isShared
    isActive
    isLocked
    elementCount
  }
}
""".strip()


def parse_library_taxonomy(data: dict[str, Any]) -> dict[str, Any] | None:
  t = data.get("libraryTaxonomy")
  return keys_to_snake(t) if t is not None else None


# ── Elements ───────────────────────────────────────────────────────────

LIST_LIBRARY_ELEMENTS_QUERY = """
query ListLibraryElements(
  $taxonomyId: ID
  $source: String
  $classification: String
  $statementContext: String
  $derivationRole: String
  $elementType: String
  $isAbstract: Boolean
  $limit: Int! = 50
  $offset: Int! = 0
  $includeLabels: Boolean! = false
  $includeReferences: Boolean! = false
) {
  libraryElements(
    taxonomyId: $taxonomyId
    source: $source
    classification: $classification
    statementContext: $statementContext
    derivationRole: $derivationRole
    elementType: $elementType
    isAbstract: $isAbstract
    limit: $limit
    offset: $offset
    includeLabels: $includeLabels
    includeReferences: $includeReferences
  ) {
    id
    qname
    namespace
    name
    trait
    statementContext
    derivationRole
    balanceType
    periodType
    isAbstract
    isMonetary
    elementType
    source
    taxonomyId
    parentId
    labels @include(if: $includeLabels) {
      role
      language
      text
    }
    references @include(if: $includeReferences) {
      refType
      citation
      uri
    }
  }
}
""".strip()


def parse_library_elements(data: dict[str, Any]) -> list[dict[str, Any]]:
  items = data.get("libraryElements") or []
  return [keys_to_snake(e) for e in items]


SEARCH_LIBRARY_ELEMENTS_QUERY = """
query SearchLibraryElements($query: String!, $source: String, $limit: Int! = 50) {
  searchLibraryElements(query: $query, source: $source, limit: $limit) {
    id
    qname
    namespace
    name
    trait
    statementContext
    derivationRole
    balanceType
    periodType
    isAbstract
    isMonetary
    elementType
    source
    taxonomyId
    parentId
    labels {
      role
      language
      text
    }
    references {
      refType
      citation
      uri
    }
  }
}
""".strip()


def parse_library_search_results(data: dict[str, Any]) -> list[dict[str, Any]]:
  items = data.get("searchLibraryElements") or []
  return [keys_to_snake(e) for e in items]


GET_LIBRARY_ELEMENT_QUERY = """
query GetLibraryElement($id: ID, $qname: String) {
  libraryElement(id: $id, qname: $qname) {
    id
    qname
    namespace
    name
    trait
    statementContext
    derivationRole
    balanceType
    periodType
    isAbstract
    isMonetary
    elementType
    source
    taxonomyId
    parentId
    labels {
      role
      language
      text
    }
    references {
      refType
      citation
      uri
    }
  }
}
""".strip()


def parse_library_element(data: dict[str, Any]) -> dict[str, Any] | None:
  e = data.get("libraryElement")
  return keys_to_snake(e) if e is not None else None


# ── Arcs / Equivalence ─────────────────────────────────────────────────

LIST_LIBRARY_TAXONOMY_ARCS_QUERY = """
query ListLibraryTaxonomyArcs(
  $taxonomyId: ID!
  $associationType: String
  $limit: Int! = 200
  $offset: Int! = 0
) {
  libraryTaxonomyArcCount(taxonomyId: $taxonomyId)
  libraryTaxonomyArcs(
    taxonomyId: $taxonomyId
    associationType: $associationType
    limit: $limit
    offset: $offset
  ) {
    id
    structureId
    structureName
    fromElementId
    fromElementQname
    fromElementName
    toElementId
    toElementQname
    toElementName
    associationType
    arcrole
    orderValue
    weight
  }
}
""".strip()


def parse_library_taxonomy_arcs(data: dict[str, Any]) -> dict[str, Any]:
  return {
    "arcs": [keys_to_snake(a) for a in (data.get("libraryTaxonomyArcs") or [])],
    "count": data.get("libraryTaxonomyArcCount", 0),
  }


GET_LIBRARY_ELEMENT_ARCS_QUERY = """
query GetLibraryElementArcs($id: ID!) {
  libraryElementArcs(id: $id) {
    id
    direction
    associationType
    arcrole
    taxonomyId
    taxonomyStandard
    taxonomyName
    structureId
    structureName
    peer {
      id
      qname
      name
      trait
      statementContext
      derivationRole
      source
    }
  }
}
""".strip()


def parse_library_element_arcs(data: dict[str, Any]) -> list[dict[str, Any]]:
  items = data.get("libraryElementArcs") or []
  return [keys_to_snake(a) for a in items]


GET_LIBRARY_ELEMENT_EQUIVALENTS_QUERY = """
query GetLibraryElementEquivalents($id: ID!) {
  libraryElementEquivalents(id: $id) {
    element {
      id
      qname
      name
      trait
      statementContext
      derivationRole
      source
    }
    equivalents {
      id
      qname
      name
      trait
      statementContext
      derivationRole
      source
    }
  }
}
""".strip()


def parse_library_element_equivalents(data: dict[str, Any]) -> dict[str, Any] | None:
  eq = data.get("libraryElementEquivalents")
  return keys_to_snake(eq) if eq is not None else None
