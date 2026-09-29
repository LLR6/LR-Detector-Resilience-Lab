# Engineering Decisions

## D1 — Feature-space only

Experiments modify numeric feature vectors, never executable files.

## D2 — Keep the model simple

The current detector is intentionally understandable so drift effects can be attributed more easily.

## D3 — Separate threshold sensitivity from drift strength

A model can look fragile because of one operating threshold or because its ranking truly changes under drift. Both axes are reported.

## D4 — Include a zero-strength sanity point

`strength=0` should produce no drift degradation and acts as a basic experimental control.

## D5 — Report flipped samples

Aggregate metrics are paired with sample-level score and feature deltas.
