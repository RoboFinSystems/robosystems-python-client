## Summary

<!-- What this PR does and why. Ground it in the actual change, not the diff mechanics. -->

## Changes

<!-- The substantive changes, grouped by area: regenerated api/ and models/ vs. the hand-written
     facades under robosystems_client/clients/ vs. tooling/packaging. Summarize generated churn by
     its net effect on the public surface rather than enumerating it — and never describe generated
     output as authored work. Note whether both the sync and async paths were covered. -->

-

## Compatibility

<!-- Required judgment, not an optional section. This package is post-1.0 on PyPI and integrators
     pin against it.
     - BREAKING: a removed or renamed export, a changed signature, a model field that became
       required or was dropped, changed runtime semantics. Forces a major; must be coordinated with
       the API. Say what a consumer has to change.
     - ADDITIVE: new endpoints, new optional model fields, new exports.
     - INTERNAL: generation tooling, tests, packaging that does not alter the emitted surface.
     A regeneration is NOT automatically additive — an API schema change can turn a field required
     with no hand-written line involved. Compare the emitted models before classifying. -->

ADDITIVE

## Testing

<!-- How the change was verified. Run `just test-all` (pytest -> format -> lint -> typecheck) before
     opening. Note it never builds a distribution, so packaging changes need `just build-package`
     too. SDK regeneration needs a reachable API and often is not runnable in-session — say so
     plainly if you could not. "Not run" is a valid answer. -->
