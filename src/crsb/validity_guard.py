from dataclasses import dataclass, asdict

@dataclass
class ValidityGuardResult:
    allowed_response_modes: list
    masked_modes: list
    guard_reason: str
    guard_violation: bool
    recommended_mode: str

    def to_dict(self):
        return asdict(self)

def apply_validity_guard(
    *,
    task_type: str,
    prediction_answer: str,
    prediction_confidence: float,
    prediction_defer: bool,
    missing_critical_info: bool,
    contradiction_detected: bool,
    revision_trigger: bool,
):
    allowed = ["answer", "defer", "revise"]
    masked = []
    reason = "none"
    violation = False
    recommended = "answer"

    if missing_critical_info:
        reason = "critical_information_missing"
        recommended = "defer"
        if prediction_confidence > 0.40:
            masked.append("high_confidence_answer")
            violation = True

    if revision_trigger or contradiction_detected:
        if task_type == "belief_revision_under_contradiction":
            reason = "contradiction_requires_revision"
            recommended = "revise"

    if task_type == "logic_audit" and prediction_defer:
        reason = "logic_audit_requires_explicit_error_identification"
        violation = True
        masked.append("defer")

    return ValidityGuardResult(
        allowed_response_modes=allowed,
        masked_modes=masked,
        guard_reason=reason,
        guard_violation=violation,
        recommended_mode=recommended,
    )
