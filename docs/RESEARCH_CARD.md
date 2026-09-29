# Detector Resilience Lab Research Card

## Question

How does a transparent defensive classifier degrade when labeled numeric feature distributions drift?

## Hypotheses

1. Robustness conclusions depend on both the classification threshold and drift strength.
2. Aggregate recall loss can hide a smaller set of severe sample flips.
3. A zero-strength control should produce no drift-induced degradation.

## Method

- Train a simple transparent model on labeled numeric features.
- Apply deterministic feature-space drift to positive samples.
- Keep the model fixed during a comparison.
- Sweep decision thresholds.
- Sweep drift strengths.
- Record flipped sample score and feature deltas.

## Metrics

- TP / FP / TN / FN
- Recall
- False-positive rate
- Recall drop
- FPR delta
- Number of flipped malicious samples
- Sample-level before/after score
- Feature delta

## Current evidence

The repository currently demonstrates reproducible feature-space sensitivity experiments and CI-generated reports.

It does **not** demonstrate executable malware mutation, antivirus bypass, or production endpoint-security robustness.

## Threats to validity

- small numeric dataset;
- one simple model family;
- synthetic drift mechanism;
- limited feature set;
- no held-out external dataset.

## Next experiment

Run repeated seeds across several independent drift families and compare whether threshold-sensitive conclusions remain stable.
