# Contributing

Contributions should improve measurement of defensive model robustness under safe feature drift.

## Expectations

- keep experiments in numeric / tabular feature space;
- preserve deterministic seeds;
- document the drift transformation;
- include threshold- or strength-sensitivity tests where relevant;
- report negative and flat results, not only degradation;
- do not claim AV/EDR bypass from feature simulations.

## Checks

```bash
python -m pip install -e .
python -m unittest discover -s tests
detector-resilience examples/features.csv --seed 7 --thresholds 0.3,0.5,0.7 --strengths 0,0.5,1,1.5
```
