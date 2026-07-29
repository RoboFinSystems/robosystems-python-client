#!/usr/bin/env python3
"""Refresh the checked-in GraphQL SDL snapshot by introspecting the backend.

`tests/test_graphql_queries.py` validates every hand-written query document
against this snapshot. That check is only as good as the snapshot is current:

- Backend *adds* a field the snapshot lacks -> a query using it fails
  validation. Noisy, but safe.
- Backend *removes* a field the snapshot still lists -> a query using it
  validates clean and fails at runtime. Silent, and exactly the failure the
  test exists to prevent.

So the snapshot has to be refreshed whenever the SDK is regenerated, which is
why `just generate-sdk` calls this. Introspecting the same running backend the
REST generation already targets keeps both halves of the SDK generated from one
source, and mirrors how the TypeScript client's codegen introspects live.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from graphql import build_client_schema, get_introspection_query, print_schema

DEFAULT_URL = "http://localhost:8000/extensions/kg00000000000000000000/graphql"
OUT_PATH = (
  Path(__file__).resolve().parent.parent
  / "robosystems_client"
  / "graphql"
  / "schema.graphql"
)


def introspect(url: str) -> dict:
  payload = json.dumps({"query": get_introspection_query()}).encode()
  request = urllib.request.Request(
    url, data=payload, headers={"Content-Type": "application/json"}
  )
  with urllib.request.urlopen(request, timeout=60) as response:
    body = json.loads(response.read())
  if "errors" in body and body["errors"]:
    raise RuntimeError(f"Introspection returned errors: {body['errors']}")
  return body["data"]


def main() -> int:
  url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
  try:
    data = introspect(url)
  except (urllib.error.URLError, TimeoutError) as exc:
    # Fail loudly rather than leaving a stale snapshot in place looking fresh.
    print(f"Could not introspect {url}: {exc}", file=sys.stderr)
    print("Is the backend running? Start it, then re-run.", file=sys.stderr)
    return 1

  sdl = print_schema(build_client_schema(data))
  previous = OUT_PATH.read_text() if OUT_PATH.exists() else None
  OUT_PATH.write_text(sdl)

  if previous is None:
    print(f"Wrote {OUT_PATH.name} ({len(sdl.splitlines())} lines)")
  elif previous == sdl:
    print(f"{OUT_PATH.name} already current ({len(sdl.splitlines())} lines)")
  else:
    print(
      f"{OUT_PATH.name} updated ({len(previous.splitlines())} -> "
      f"{len(sdl.splitlines())} lines) — re-run `just test-all`"
    )
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
