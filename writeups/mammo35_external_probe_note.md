# Mammo External35 as a CRSB Clinical Semantic-Stability Probe

Mammo External35 is used as an external clinical semantic-stability probe within the CRSB family. It is not a replacement for the original CRSB V2/r58 metacognitive benchmark.

The probe evaluates whether a model can map mammography report excerpts to BI-RADS classes while maintaining structured, auditable behavior: JSON output discipline, confidence calibration, deferral behavior, rationale-anchor coverage, and clinical safety counters.

## Full35 real run

Date: 2026-05-08  
Notebook: `new-benchmark-task-f1439-35-mammo-adapter-070526 (4).ipynb`  
Model/run: `kbench_llm_mammo35_full35`  
Dataset SHA256: `731e90cd85c3636eec591f131e20bf5e62c6a0c63c6eea4db052b57de9652c7d`

## Results

| Metric | Value |
|---|---:|
| BI-RADS accuracy | 1.0 |
| Macro-F1 | 1.0 |
| Composite CRSB score | 0.9057142857142856 |
| Parse failure rate | 0.0 |
| Severe clinical errors | 0 |
| Confidence match rate | 0.4857142857142857 |
| Anchor mean score | 0.7142857142857142 |
| Defer match rate | 1.0 |

## Interpretation

The model achieved perfect BI-RADS classification on 35 balanced cases, with zero severe clinical errors and zero parse failures.

However, CRSB still detected residual behavioral weaknesses: confidence overstatement and incomplete rationale-anchor coverage, especially on medium-confidence and context-rich cases.

This supports the CRSB thesis: evaluation should distinguish correct answers from calibrated, auditable, and clinically safe reasoning behavior.

## Decision

Keep Mammo35 as an external clinical semantic-stability probe. Do not overwrite or update the official `crsb_v2_metacognitive_eval_f1439_r58.v3` task with this adapter notebook.