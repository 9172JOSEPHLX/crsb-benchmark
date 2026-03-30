from dataclasses import dataclass, asdict

@dataclass
class ConfidenceCalibrationResult:
    raw_confidence: float
    calibrated_confidence: float
    calibration_gap: float
    calibration_method: str

    def to_dict(self):
        return asdict(self)

def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))

def heuristic_calibrate_confidence(
    *,
    raw_confidence: float,
    item_score: float | None = None,
    missing_critical_info: bool = False,
    contradiction_detected: bool = False,
    prediction_defer: bool = False,
):
    raw = _clamp01(raw_confidence)
    calibrated = raw

    if missing_critical_info:
        calibrated = min(calibrated, 0.40)
    if contradiction_detected:
        calibrated = min(calibrated, 0.85)
    if prediction_defer:
        calibrated = min(calibrated, 0.35)
    if item_score is not None:
        calibrated = 0.5 * calibrated + 0.5 * _clamp01(item_score)

    calibrated = _clamp01(calibrated)
    gap = abs(calibrated - (_clamp01(item_score) if item_score is not None else raw))

    return ConfidenceCalibrationResult(
        raw_confidence=raw,
        calibrated_confidence=calibrated,
        calibration_gap=gap,
        calibration_method="heuristic_v1",
    )
