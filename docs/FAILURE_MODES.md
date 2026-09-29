# Known Failure Modes

- Drift result depends strongly on one threshold.
  - Use threshold sweep.
- Drift result depends strongly on one perturbation magnitude.
  - Use strength sweep.
- `strength=0` changes metrics.
  - Treat as implementation regression.
- Dataset labels/features change between runs.
  - Version the dataset/report semantics before comparing.
- Feature-space results are misinterpreted as executable evasion.
  - Re-state the non-executable boundary.
