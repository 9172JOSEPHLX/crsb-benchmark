\# CRSB Mammo External35 — Full35 Real Run Ledger



Date: 2026-05-08  

Notebook: `new-benchmark-task-f1439-35-mammo-adapter-070526 (4).ipynb`  

Role: hybrid f1439 notebook + Mammo External35 adapter-070526  

Status: PASS STRONG  



\## Dataset



File: `mammo\_crsb\_external35\_v1.json`  

SHA256: `731e90cd85c3636eec591f131e20bf5e62c6a0c63c6eea4db052b57de9652c7d`



\## Run



Model/run name: `kbench\_llm\_mammo35\_full35`  

Cases: 35  



\## Results



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



\## Clinical safety counts



| Counter | Value |

|---|---:|

| undercall\_456\_to\_0123\_count | 0 |

| overcall\_12\_to\_56\_count | 0 |

| birads5\_pred\_as\_6\_count | 0 |

| birads6\_pred\_as\_5\_count | 0 |

| birads0\_missed\_count | 0 |



\## Interpretation



PASS STRONG. The model achieved perfect BI-RADS classification with zero severe clinical errors and zero parse failures.



Residual CRSB weaknesses are confidence overstatement and incomplete rationale-anchor coverage, especially on medium-confidence and context-rich cases.



\## Decision



Keep Mammo35 as an external clinical semantic-stability probe.



Do not overwrite or update the official `crsb\_v2\_metacognitive\_eval\_f1439\_r58.v3` task with this adapter notebook.

