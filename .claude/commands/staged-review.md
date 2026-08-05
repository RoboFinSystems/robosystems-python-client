---
description: Review the staged diff against this SDK's compatibility, generation, and packaging rules.
---

Review all staged changes (`git diff --cached`) with focus on the contexts below. Read the diff first — if nothing is staged, say so rather than reviewing the working tree.

This is `robosystems-client`: a **published, post-1.0 Python SDK**, largely generated from the RoboSystems API's OpenAPI document and GraphQL schema, consumed by internal tooling and external integrators. It is a **public repository**.

## Before anything else: is this file generated?

```bash
git diff --cached --name-only
```

`robosystems_client/api/`, `robosystems_client/models/`, and `robosystems_client/graphql/generated/` are **generation output**. A hand edit there is erased by the next `just generate-sdk` / `just generate-graphql` — that's a blocking finding regardless of how correct the edit is. The fix belongs in one of:

- `bin/generate-sdk.sh` — the post-generation patches applied to `openapi-python-client` output
- `[tool.ariadne-codegen]` in `pyproject.toml`, or the operation documents under `robosystems_client/graphql/operations/` — GraphQL generation inputs
- `robosystems_client/graphql/schema.graphql` — the checked-in schema snapshot, refreshed with `just refresh-schema` against a running backend
- the API's OpenAPI or GraphQL schema, in `RoboFinSystems/robosystems` — where wrong types actually originate

If the staged diff mixes regenerated output with hand-written change, say which files are which; that distinction drives the rest of the review.

## Compatibility (the section that decides the verdict)

Post-1.0, the emitted type surface **is** the contract. For anything staged here:

- Is an export removed or renamed? A signature or return type changed? An input type narrowed? Runtime semantics altered? Each is a **major**, requires coordination with the API and every consuming app, and must be stated explicitly rather than discovered by an integrator.
- Is it additive — new endpoints, new optional fields, new exports? Free, but name it.
- **A regeneration is not automatically safe.** An API schema change can turn an optional field required, or drop one, so the diff reaches consumers as a break with no hand-written line involved. Compare the emitted model and signature surface, not the diff shape.
- Does new surface appear in the package `__init__.py` exports, importable from where the README says it is? Unexported surface may as well not exist.
- Is the change applied to **both** the sync and async paths? A fix landed on one is a half-fix.

## SDK implementation

- Are new methods fully typed, with no `Any` used to silence `basedpyright`?
- Do the typed facades under `robosystems_client/clients/` follow the existing patterns rather than inventing a second style?
- Is error handling consistent — are API errors mapped to something a consumer can branch on, not swallowed into a generic throw?
- Are request/response types the generated models rather than hand-redeclared shapes that will drift?

## Auth and secrets

- Token and header handling: is anything logged, stringified into an exception message, or attached where it could surface in a consumer's traceback? An httpx error that carries request headers is a credential leak downstream.
- Are credentials read from configuration rather than defaulted to anything real?
- No API keys, JWTs, real graph IDs, or customer payloads in tests, fixtures, or comments. Fixtures should be invented.

## Packaging

- Changes to `pyproject.toml` — dependency pins, optional extras, `requires-python`, included packages, `py.typed` — change **what ships and who can install it**. A dropped `py.typed` silently turns a typed SDK into an untyped one for every consumer; a narrowed `requires-python` locks out supported versions (3.11–3.13).
- Never stage a version bump in `pyproject.toml` in a feature branch: `create-release.yml` owns the bump on `main`, and pushing `release/**` is what triggers `publish.yml`.

## Testing

- Do new methods have tests, including the error paths?
- Do tests exercise the public surface as a consumer would import it, rather than reaching into internals?
- Is the test asserting correct behavior, or just asserting what the code currently does?

## Documentation

- Is the README updated for new or changed surface? For a published package this is the primary integrator documentation.
- Are JSDoc comments present on new public methods, and accurate on changed ones? They surface in consumers' editors.
- Does a breaking change come with the migration line an integrator needs?

## Public-repo hygiene

- No customer names, graph IDs, internal cost/pricing detail, or real financial payloads in code, comments, or fixtures.
- If the change fixes a security issue, keep commit messages and comments terse and non-actionable — the area hardened, never the mechanism. Remember the vulnerable version stays installable from PyPI until a patch is published.

## Output

Provide a summary with:

1. **Compatibility**: BREAKING / ADDITIVE / INTERNAL, with what a consumer must change if breaking
2. **Issues**: Problems that should be fixed before commit
3. **Suggestions**: Improvements that aren't blocking
4. **Questions**: Anything unclear that needs clarification

Anchor each finding to `file:line`. If the staged diff is clean, say so plainly rather than manufacturing findings.
