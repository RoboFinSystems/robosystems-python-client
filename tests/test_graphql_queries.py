"""Validate every hand-written GraphQL document against the backend schema.

These query strings are hand-maintained (see the `python-client-graphql`
RFC for the codegen replacement), which means nothing but this test stops a
document referencing a field or argument the schema doesn't have. That is not
hypothetical: five of the eight library documents shipped referencing
`statementContext` / `derivationRole`, which have never existed in the schema.
Every call raised GraphQLError, so the whole LibraryClient element surface was
dead, and no test, type check or lint caught it.

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

import importlib
import pkgutil
from pathlib import Path

import pytest
from graphql import build_schema, parse, validate

SCHEMA_PATH = (
  Path(__file__).resolve().parent.parent
  / "robosystems_client"
  / "graphql"
  / "schema.graphql"
)

QUERY_PACKAGE = "robosystems_client.graphql.queries"


def _load_schema():
  if not SCHEMA_PATH.exists():  # pragma: no cover - guard for a bad checkout
    pytest.fail(f"Schema snapshot missing at {SCHEMA_PATH}. Run `just refresh-schema`.")
  return build_schema(SCHEMA_PATH.read_text())


def _iter_documents():
  """Yield (module, attribute, document) for every GraphQL string we ship.

  Deliberately reflective rather than a hand-listed set: a new query added to
  any domain module is covered the moment it exists, with nothing to remember.
  """
  package = importlib.import_module(QUERY_PACKAGE)
  for info in pkgutil.walk_packages(package.__path__, f"{QUERY_PACKAGE}."):
    module = importlib.import_module(info.name)
    for attr in dir(module):
      if attr.startswith("_"):
        continue
      value = getattr(module, attr)
      if not isinstance(value, str):
        continue
      # Module docstrings and prose constants are strings too; only treat a
      # value as a document if it actually declares an operation.
      stripped = value.lstrip()
      if stripped.startswith(("query ", "mutation ", "subscription ", "fragment ")):
        yield info.name, attr, value


DOCUMENTS = sorted(_iter_documents())


def test_documents_were_discovered():
  """Guard the reflection itself — a discovery bug would make every other
  assertion here vacuously pass."""
  assert len(DOCUMENTS) > 30, (
    f"Only found {len(DOCUMENTS)} GraphQL documents; discovery is probably broken."
  )


@pytest.mark.parametrize(
  "module_name,attr,document",
  DOCUMENTS,
  ids=[f"{m.rsplit('.', 1)[-1]}.{a}" for m, a, _ in DOCUMENTS],
)
def test_document_is_valid_against_schema(module_name: str, attr: str, document: str):
  schema = _load_schema()
  errors = validate(schema, parse(document))
  assert not errors, "\n".join(
    [f"{module_name}.{attr} is invalid against the schema:"]
    + [f"  - {e.message}" for e in errors]
  )
