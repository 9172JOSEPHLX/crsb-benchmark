# 🧠 CRSB V2 — Clinical Reasoning Stability Benchmark

> **A metacognitive benchmark for evaluating reasoning stability beyond accuracy**

---

## 🎯 What is CRSB V2?

CRSB V2 is a **benchmark-centered evaluation framework** designed to measure  
**metacognitive reliability** in AI reasoning systems.

Unlike traditional benchmarks, CRSB V2 does not ask:

> *“Is the answer correct?”*

It asks:

> **“Is the reasoning reliable, calibrated, and stable under stress?”**

---

## ⚠️ The Core Problem

Modern AI systems often:
- achieve high accuracy  
- appear confident  
- produce fluent explanations  

👉 **But still fail in critical ways:**
- ❌ Overconfidence under missing information  
- ❌ Failure to revise under contradiction  
- ❌ Acceptance of flawed reasoning  
- ❌ Instability across similar cases  

Traditional benchmarks compress all of this into a **single score**.

➡️ **CRSB V2 is designed to expose that hidden gap.**

---

## 🔍 What CRSB V2 Evaluates

CRSB V2 measures whether a model:

- 🎯 **Answers correctly**
- 📏 **Calibrates confidence appropriately**
- ⚠️ **Detects missing critical information**
- 🔄 **Revises beliefs under contradiction**
- 🧪 **Identifies flawed reasoning**

---

## 🧠 Cognitive Focus

### Primary Faculty
- **Metacognition**
  - Calibration  
  - Uncertainty handling  
  - Belief revision  
  - Logic monitoring  

### Secondary (Proxy) Faculties
- **Executive Functions** → action selection (`answer / revise / defer`)  
- **Attention** → detection of missing information  
- **Learning (proxy)** → adaptation under contradiction  
- **Social Cognition (proxy)** → safe deferral behavior  

---

## 🧪 Benchmark Design Principle

> **Correctness is necessary — but not sufficient.**

A reliable model must also:
- know when it may be wrong  
- update its beliefs  
- avoid unjustified confidence  
- detect reasoning flaws  

---

## 🧩 Core Task Families

### 1. 🟢 Clean Baseline Reasoning
Standard structured clinical cases  
→ Measures baseline correctness

---

### 2. 🟡 Information Gap Recognition
Incomplete or ambiguous cases  
→ Tests safe deferral vs guessing

---

### 3. 🔴 Belief Revision Under Contradiction
Conflicting evidence introduced  
→ Tests adaptive reasoning

---

### 4. 🔵 Logic Audit
Evaluate reasoning quality  
→ Tests detection of flawed logic

---

## 📊 Evaluation Signals

CRSB V2 produces **interpretable outputs**, not just a single score:

- **Item Score** → correctness  
- **Calibration Signal** → confidence vs accuracy  
- **Uncertainty Handling** → safe vs unsafe decisions  
- **Belief Revision Score** → adaptability  
- **Logic Audit Score** → reasoning quality  
- **Failure Modes** → structured weaknesses  
- **Radar Profile** → cognitive fingerprint  

---

## 💡 Key Insight

> A model can be **accurate but unreliable**.

CRSB V2 reveals:
- hidden instability under contradiction  
- unsafe confidence behavior  
- reasoning flaws masked by fluency  

👉 These are **invisible in standard benchmarks**.

---

## 🏥 Why Clinical Scenarios?

Clinical reasoning naturally includes:
- incomplete information  
- evolving evidence  
- contradictions  
- high-stakes decisions  

➡️ Ideal for **metacognitive stress testing**

⚠️ However:

> CRSB V2 targets **general cognitive behavior**, not just healthcare.

---

## 🏗️ Project Structure

- 📦 Kaggle Benchmark  
- 📓 Kaggle Notebook  
- 📝 Writeup  
- 🧪 Structured tasks  
- ⚙️ Evaluation pipeline  

---

## 🚀 What Makes CRSB V2 Different?

| Traditional Benchmarks | CRSB V2 |
|----------------------|--------|
| Accuracy-focused | Reasoning-focused |
| Static scoring | Behavioral profiling |
| Single metric | Multi-signal analysis |
| Surface-level success | Failure-mode detection |

---

## 📌 Summary

CRSB V2 evaluates whether AI systems:
- reason correctly  
- calibrate confidence  
- handle uncertainty safely  
- revise beliefs  
- detect logical inconsistencies  

➡️ Moving from **performance measurement**  
➡️ to **cognitive behavior analysis**

---

## 📜 License
Apache 2.0
