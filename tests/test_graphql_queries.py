"""Validate every GraphQL operation document against the backend schema.

The documents under ``robosystems_client/graphql/operations/`` are the
single source the facade reads run from: ariadne-codegen generates the
typed Pydantic models and the ``*_GQL`` constants in
``graphql/generated/operations.py`` from them. Nothing but this test
stops a document referencing a field or argument the schema doesn't
have. That is not hypothetical: five of the eight library documents once
shipped referencing `statementContext` / `derivationRole`, which have
never existed in the schema. Every call raised GraphQLError, so the
whole LibraryClient element surface was dead, and no test, type check or
lint caught it.

Validation runs against a checked-in SDL snapshot rather than a live backend so
it works offline, in the pre-commit hook, and in CI.

The snapshot's currency matters in one direction more than the other:

- Backend *adds* a field the snapshot lacks — a query using it fails here.
  Noisy, but safe.
- Backend *removes* a field the snapshot still lists — a query using it passes
  here and fails at runtime. Silent, and exactly the failure this test exists
  to prevent.

So the snapshot is refreshed as part of `just generate-sdk`, not left to be
remembered; `just refresh-schema` runs it standalone.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from graphql import build_schema, parse, validate

GRAPHQL_DIR = Path(__file__).resolve().parent.parent / "robosystems_client" / "graphql"
SCHEMA_PATH = GRAPHQL_DIR / "schema.graphql"
OPERATIONS_DIR = GRAPHQL_DIR / "operations"


def _load_schema():
  if not SCHEMA_PATH.exists():  # pragma: no cover - guard for a bad checkout
    pytest.fail(f"Schema snapshot missing at {SCHEMA_PATH}. Run `just refresh-schema`.")
  return build_schema(SCHEMA_PATH.read_text())


# Deliberately a recursive glob rather than a hand-listed set: a new
# document added to any domain directory is covered the moment it
# exists, with nothing to remember.
DOCUMENTS = sorted(OPERATIONS_DIR.rglob("*.graphql"))


def test_documents_were_discovered():
  """Guard the glob itself — a discovery bug would make every other
  assertion here vacuously pass."""
  assert len(DOCUMENTS) > 30, (
    f"Only found {len(DOCUMENTS)} GraphQL documents under {OPERATIONS_DIR}; "
    "discovery is probably broken."
  )


@pytest.mark.parametrize(
  "path",
  DOCUMENTS,
  ids=[str(p.relative_to(OPERATIONS_DIR)) for p in DOCUMENTS],
)
def test_document_is_valid_against_schema(path: Path):
  schema = _load_schema()
  errors = validate(schema, parse(path.read_text()))
  assert not errors, "\n".join(
    [f"{path.relative_to(OPERATIONS_DIR)} is invalid against the schema:"]
    + [f"  - {e.message}" for e in errors]
  )
