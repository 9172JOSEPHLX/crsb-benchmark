from dataclasses import dataclass, asdict

@dataclass
class ScenarioUncertaintyResult:
    missing_critical_info: bool
    contradiction_detected: bool
    revision_trigger: bool
    uncertainty_mode: str

    def to_dict(self):
        return asdict(self)

def analyze_scenario_uncertainty(*, task_type: str, clinical_context: str, input_text: str, expected_behavior: str | None = None):
    text = input_text.upper()
    missing = "MISSING" in text or "NOT DESCRIBED" in text
    contradiction = task_type in {"belief_revision_under_contradiction", "logic_audit"} or "REASSESS" in text or "ADDITIONAL EVIDENCE" in text
    revision_trigger = task_type == "belief_revision_under_contradiction" and contradiction
    mode = "missing_info" if missing else ("contradiction" if contradiction else "none")
    return ScenarioUncertaintyResult(
        missing_critical_info=missing,
        contradiction_detected=contradiction,
        revision_trigger=revision_trigger,
        uncertainty_mode=mode,
    )
