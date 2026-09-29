# Compatibility

## Runtime

- Python: **3.10+**
- CI target: **3.10 / 3.11 / 3.12**
- CLI: `detector-resilience`

## Data boundary

Input remains non-executable numeric feature data.

## Report schemas

- experiment report: `lr-detector-resilience/v2`

Threshold and strength sweep fields may be extended in minor releases.

Changing mutation semantics, feature definitions or metric meaning requires CHANGELOG documentation because it changes experiment comparability.
