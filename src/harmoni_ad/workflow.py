"""Core workflow utilities for the portfolio-safe HARMONI-AD reconstruction.

This module intentionally does not reproduce heuristic pseudo-predictions from the
original prototype. It validates modality availability and aggregates only genuine
probabilities supplied by successfully executed external components.
"""
from dataclasses import dataclass, asdict
from typing import Optional, Iterable

@dataclass
class ModalityResult:
    modality: str
    status: str  # executed | skipped | error
    probability: Optional[float] = None
    label: Optional[str] = None
    message: str = ""

    def to_dict(self):
        return asdict(self)


def validate_probability(value: Optional[float]) -> Optional[float]:
    if value is None:
        return None
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError("Probability must be between 0 and 1.")
    return value


def aggregate_available(results: Iterable[ModalityResult], min_modalities: int = 2):
    """Average probabilities from executed modalities only.

    Mirrors the transparent aggregation principle described in the thesis evaluation.
    Returns an explicit insufficient-data state when too few real outputs are available.
    """
    usable = []
    for result in results:
        if result.status == "executed" and result.probability is not None:
            usable.append(validate_probability(result.probability))
    if len(usable) < min_modalities:
        return {"status": "insufficient_data", "n_modalities": len(usable), "probability": None}
    return {
        "status": "aggregated",
        "n_modalities": len(usable),
        "probability": sum(usable) / len(usable),
    }
