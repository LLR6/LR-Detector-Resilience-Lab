# Detector Resilience Lab Architecture

```text
labeled feature CSV
       ↓
simple detector training
       ↓
baseline scores
       ↓
safe deterministic feature drift
       ↓
post-drift scores
      ↙        ↘
threshold      strength
 sweep          sweep
      \        /
       degradation report
```

## Experimental controls

- explicit random seed;
- fixed model during a drift comparison;
- threshold sweep for operating-point sensitivity;
- strength sweep for perturbation-magnitude sensitivity;
- `strength=0` as a no-drift sanity check.

## Boundary

Only numeric feature vectors are modified. The project does not process, transform, or generate executable samples.

## Non-goals

- operational evasion;
- antivirus bypass;
- claims of real-world endpoint-security performance without appropriate datasets.
