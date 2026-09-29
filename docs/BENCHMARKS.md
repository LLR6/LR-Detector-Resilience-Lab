# Benchmarks

## Threshold sensitivity

```bash
detector-resilience examples/features.csv \
  --seed 7 \
  --strength 1.0 \
  --threshold 0.5 \
  --thresholds 0.3,0.5,0.7
```

## Drift-strength sensitivity

```bash
detector-resilience examples/features.csv \
  --seed 7 \
  --threshold 0.5 \
  --strengths 0,0.5,1,1.5
```

The report tracks baseline recall, post-drift recall, recall drop, post-drift FPR and flipped malicious samples.

`strength=0` acts as a sanity check: it should not introduce drift degradation.

## Boundary

All experiments operate on non-executable numeric feature vectors. Results must not be interpreted as real-world malware-evasion capability.
