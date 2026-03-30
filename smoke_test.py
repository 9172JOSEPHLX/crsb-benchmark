from crsb import (
    analyze_scenario_uncertainty,
    apply_validity_guard,
    heuristic_calibrate_confidence,
)

scenario = analyze_scenario_uncertainty(
    task_type="information_gap_recognition",
    clinical_context="radiology",
    input_text="[MARGIN DESCRIPTION MISSING]",
)

guard = apply_validity_guard(
    task_type="information_gap_recognition",
    prediction_answer="Benign",
    prediction_confidence=0.95,
    prediction_defer=False,
    missing_critical_info=scenario.missing_critical_info,
    contradiction_detected=scenario.contradiction_detected,
    revision_trigger=scenario.revision_trigger,
)

cal = heuristic_calibrate_confidence(
    raw_confidence=0.95,
    item_score=0.0,
    missing_critical_info=True,
)

print("SCENARIO:", scenario.to_dict())
print("GUARD:", guard.to_dict())
print("CALIBRATION:", cal.to_dict())
