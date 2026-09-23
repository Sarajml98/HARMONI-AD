# Implementation notes

## Why this cleaned version differs from the archived thesis workspace

The supplied thesis-code archive contains a Streamlit integration prototype plus local copies of external research repositories. Several adapter functions in the prototype include fallback heuristics or proxy probabilities when a real trained model cannot be executed.

For a public portfolio repository, those fallback values are intentionally removed. A missing model, missing input, or unavailable dependency must result in an explicit **skipped/error** state rather than a synthetic disease probability.

This cleaned repository therefore preserves the thesis's strongest reproducible software idea: controlled multimodal orchestration under partial data availability. It does **not** claim to reproduce every modality-specific model or the numerical evaluation run from the thesis.

## Thesis evaluation snapshot

The thesis reports an evaluation run in which the Clinical Predictor and GSP-EEG components executed, while PET/3DCNN, MRI/AD-DL, and GPMKL were skipped because required inputs/resources were unavailable. The available probabilities were combined using a transparent arithmetic mean. This repository implements that aggregation behavior without embedding the original third-party models.
