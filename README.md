CRSB V2 — Clinical Reasoning Stability Benchmark

CRSB V2 (Clinical Reasoning Stability Benchmark) is a benchmark-centered evaluation framework designed to measure metacognitive reliability in AI reasoning systems.

While grounded in clinical diagnostic scenarios, CRSB V2 is not intended as a narrow domain benchmark. Its core purpose is to isolate and measure general cognitive and metacognitive faculties that remain difficult to assess with conventional accuracy-driven evaluations.

CRSB V2 focuses on whether a model not only produces a correct answer, but also:

calibrates confidence appropriately,
detects when critical information is missing,
revises beliefs when confronted with contradiction,
and identifies flawed reasoning instead of merely accepting plausible surface patterns.

In this sense, CRSB V2 is a metacognitive stress-testing framework: it is designed to reveal behavioral failure modes that standard benchmarks often miss.

Why CRSB V2

Many current AI systems can achieve strong performance on benchmark tasks while remaining:

overconfident when evidence is incomplete,
unstable under contradiction,
weak at belief revision,
or unable to detect reasoning flaws behind plausible conclusions.

Traditional evaluations often compress all of this into a single accuracy score. As a result, two systems may appear similarly strong while differing substantially in reliability, safety, and reasoning stability.

CRSB V2 is designed to expose that gap.

Its central question is:

What can we learn about model behavior beyond correctness alone?

More specifically, CRSB V2 helps answer questions such as:

Does the model defer when critical information is missing?
Does it revise its belief when new evidence conflicts with prior assumptions?
Is its confidence aligned with correctness?
Can it detect reasoning flaws instead of accepting plausible but incorrect conclusions?
Key Contribution

CRSB V2 reveals that a model can remain apparently accurate while still exhibiting metacognitive instability.

In particular, it is designed to surface failure modes that are often invisible in conventional evaluations, including:

correct answers produced with unsafe confidence,
failure to defer under missing information,
failure to revise under contradiction,
and acceptance of superficially plausible but logically flawed reasoning.

This makes CRSB V2 useful not only for profiling model performance, but also for distinguishing between systems that may look similar under standard benchmarks yet behave very differently under stress.

Cognitive Focus

CRSB V2 is primarily centered on metacognition, while also probing adjacent cognitive faculties in a structured and interpretable way.

Primary faculty
Metacognition
confidence calibration,
uncertainty handling,
belief revision,
logic-aware self-monitoring.
Secondary or proxy coverage
Executive functions
action selection under uncertainty (answer, revise, request_info),
controlled response adjustment after contradiction.
Attention
detection of missing critical information,
sensitivity to evidence relevance rather than surface plausibility.
Learning (proxy)
behavioral adaptation when new evidence invalidates a prior conclusion.
Social cognition (limited / proxy)
safe uncertainty communication,
appropriate deferral rather than overclaiming.

CRSB V2 therefore contributes to the broader effort of building interpretable cognitive profiles of frontier AI systems, rather than relying on broad static scores alone.

Benchmark Design Principle

CRSB V2 is designed around a simple principle:

Correctness is necessary, but not sufficient.

A robust reasoning system should also:

know when it may be wrong,
update its conclusions when warranted,
avoid unjustified certainty,
and expose reasoning flaws rather than conceal them behind fluent outputs.

For that reason, CRSB V2 does not operate as a conventional accuracy benchmark. Instead, it evaluates reasoning stability across controlled task families that isolate specific metacognitive behaviors.

Core Task Families

CRSB V2 includes four main task families:

1. Clean Baseline Reasoning

Standard diagnostic reasoning on structured clinical cases.

Purpose:

establish baseline item-level correctness,
measure reasoning under relatively stable conditions.
2. Information Gap Recognition

Tasks in which critical information is missing or insufficient.

Purpose:

test whether the model defers appropriately,
distinguish safe uncertainty handling from unsupported guessing.
3. Belief Revision Under Contradiction

Tasks in which new evidence conflicts with an earlier plausible conclusion.

Purpose:

test whether the model updates its conclusion,
distinguish genuine revision from stubbornness or superficial consistency.
4. Logic Audit

Tasks in which the model must evaluate reasoning quality rather than merely produce an answer.

Purpose:

test whether the system detects flawed reasoning,
distinguish logical monitoring from surface acceptance.
Main Evaluation Signals

CRSB V2 reports interpretable signals rather than a single opaque score.

Key outputs include:

Item Score
Measures task-level correctness.
Calibration Gap / Calibration Signal
Measures alignment between confidence and correctness.
Uncertainty Handling Signal
Measures whether the model defers appropriately when evidence is insufficient.
Belief Revision Signal
Measures whether the model updates conclusions under contradiction.
Logic Audit Signal
Measures whether the model detects reasoning flaws rather than accepting plausible but incorrect claims.
Failure Modes
Structured identification of model weaknesses.
Cognitive Profile / Radar Plot
A compact representation of behavioral strengths and weaknesses across abilities.

These outputs are intended to make system comparison more meaningful, more interpretable, and more informative for downstream safety-oriented analysis.

What CRSB V2 Reveals That Conventional Benchmarks Often Miss

CRSB V2 is built to expose distinctions that standard evaluations frequently fail to capture.

For example, two models may have similar accuracy while differing sharply in:

confidence discipline,
contradiction handling,
deferral behavior,
and logical self-monitoring.

A model that answers correctly for the wrong reasons, fails to revise when evidence changes, or remains overconfident under ambiguity may still look strong on conventional leaderboards.

CRSB V2 is designed to make those differences visible.

Why Clinical Scenarios

Clinical reasoning provides a strong testbed because it naturally contains:

incomplete information,
evolving evidence,
contradictory findings,
and high-stakes decisions under uncertainty.

These properties make it possible to probe metacognitive behavior in a rigorous and interpretable way.

However, the broader value of CRSB V2 is not limited to medicine. The benchmark’s underlying design targets general reasoning reliability, and its core logic can inform evaluations in other high-stakes domains where confidence, revision, and safe uncertainty handling matter.

Project Structure

CRSB V2 is a benchmark-centered framework composed of:

benchmark tasks,
evaluation and analysis code,
a Kaggle Benchmark,
a Kaggle Notebook,
and a Kaggle Writeup.

It is designed to support:

reproducible model evaluation,
interpretable cognitive profiling,
and structured comparison across systems and model variants.
Project Assets

This project is associated with:

a Kaggle Writeup,
a Kaggle Benchmark,
a Kaggle Notebook,
structured benchmark tasks,
evaluation and analysis code.
Status

Current public-facing project version: CRSB V2

Note: some Kaggle benchmark or task asset names may retain earlier labels for continuity during the submission cycle, while the current public writeup and notebook reflect the CRSB V2 framing.

Summary

CRSB V2 is a benchmark for evaluating reasoning stability, not just answer accuracy.

It is designed to measure whether AI systems:

reason correctly,
calibrate confidence appropriately,
handle uncertainty safely,
revise beliefs under contradiction,
and detect logical inconsistencies.

By doing so, CRSB V2 helps reveal behavioral failure modes that conventional evaluations often overlook, and contributes to the broader goal of building more precise and interpretable cognitive profiles of AI systems.

License

Apache 2.0
