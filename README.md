<<<<<<< HEAD
# CRSB Benchmark    Mars 28th, 2026 

# CRSB V1 — Clinical Reasoning Stability Benchmark

CRSB V1 is a benchmark for evaluating the stability and reliability of clinical AI reasoning across diagnostic tasks.

It is designed to go beyond raw accuracy by measuring whether models:
- reason correctly,
- calibrate confidence appropriately,
- handle uncertainty safely,
- revise beliefs under contradiction,
- and detect logical inconsistencies.

## Core task types

CRSB V1 includes four task families:

1. **Clean Baseline Reasoning**  
   Standard diagnostic reasoning on structured clinical cases.

2. **Information Gap Recognition**  
   Detecting when critical information is missing instead of guessing.

3. **Belief Revision Under Contradiction**  
   Updating conclusions when new evidence conflicts with prior assumptions.

4. **Logic Audit**  
   Identifying flawed reasoning rather than accepting plausible but incorrect conclusions.

## Main evaluation signals

The benchmark reports interpretable metrics including:
- **Item Score**
- **Calibration Gap**
- **Failure Modes**
- **Cognitive Profile / Radar Plot**

## Why this benchmark matters

Many AI systems can produce correct answers while remaining poorly calibrated, overconfident, or unstable under uncertainty.

CRSB V1 is designed to reveal this gap between:
- **performance**
- and
- **metacognitive reliability**

## Project assets

This project is associated with:
- a Kaggle Benchmark
- a Kaggle Notebook
- structured benchmark tasks and evaluation code

## Status

Current version:
- **Task**: `crsb_v1_metacognitive_eval`
- **Benchmark**: `CRSB V1 — Clinical Reasoning Stability Benchmark`

## License

Apache 2.0
=======
# crsb-benchmark
CRSB V1 is a benchmark for evaluating the stability and reliability of clinical AI reasoning across diagnostic tasks.
>>>>>>> cbdfa274891d9526750b474b61259cfc8cba95a6
