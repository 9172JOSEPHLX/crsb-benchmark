# CRSB V2 — Clinical Reasoning Stability Benchmark

CRSB V2 (Clinical Reasoning Stability Benchmark) is a metacognitive evaluation framework for assessing how reliably AI systems reason in clinical diagnostic scenarios.

Unlike traditional benchmarks focused primarily on accuracy, CRSB V2 evaluates reasoning stability, including:

- Correctness (item score)
- Calibration (confidence vs correctness)
- Uncertainty handling (deferral vs overconfidence)
- Belief revision under contradiction
- Logic audit (error detection vs surface acceptance)

---

## Key Idea

CRSB V2 isolates clinically relevant cognitive and metacognitive abilities rather than relying only on aggregate performance.

It is designed to answer questions such as:
- Does the model defer when critical information is missing?
- Does it revise its belief when confronted with contradictory evidence?
- Is its confidence aligned with correctness?
- Can it detect reasoning flaws instead of accepting plausible but incorrect conclusions?

---

## Project Structure

CRSB V2 is a benchmark-centered framework for evaluating the stability and reliability of clinical AI reasoning across diagnostic tasks.

It is designed to go beyond raw accuracy by measuring whether models:
- reason correctly,
- calibrate confidence appropriately,
- handle uncertainty safely,
- revise beliefs under contradiction,
- and detect logical inconsistencies.

---

## Core Task Types

CRSB V2 includes four task families:

1. **Clean Baseline Reasoning**  
   Standard diagnostic reasoning on structured clinical cases.

2. **Information Gap Recognition**  
   Detecting when critical information is missing instead of guessing.

3. **Belief Revision Under Contradiction**  
   Updating conclusions when new evidence conflicts with prior assumptions.

4. **Logic Audit**  
   Identifying flawed reasoning rather than accepting plausible but incorrect conclusions.

---

## Main Evaluation Signals

The benchmark reports interpretable signals including:
- **Item Score**
- **Calibration Gap**
- **Failure Modes**
- **Cognitive Profile / Radar Plot**

Tasks are designed to yield verifiable outcomes and interpretable failure modes, enabling meaningful comparison across systems and model variants.

---

## Why This Benchmark Matters

Many AI systems can produce correct answers while remaining poorly calibrated, overconfident, or unstable under uncertainty.

CRSB V2 is designed to reveal the gap between:
- **performance**
- and
- **metacognitive reliability**

It is intended not only to profile model behavior, but also to discriminate between systems that may appear similarly accurate on conventional benchmarks.

---

## Project Assets

This project is associated with:
- a Kaggle Writeup
- a Kaggle Benchmark
- a Kaggle Notebook
- structured benchmark tasks
- evaluation and analysis code

---

## Status

Current public-facing project version: **CRSB V2**

Note: some Kaggle benchmark or task asset names may retain earlier labels for continuity during the submission cycle, while the current public writeup and notebook reflect the CRSB V2 framing.

---

## License

Apache 2.0
