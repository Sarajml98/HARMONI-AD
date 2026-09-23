# HARMONI-AD

**A Harmonized Multimodal Machine Learning Framework for Early Alzheimer's Disease Detection**

Master's thesis project in Digital Health, developed by **Sara Jamali** at Deggendorf Institute of Technology.

> **Research prototype only.** This repository is not a medical device and must not be used for diagnosis or clinical decision-making.

## Overview

HARMONI-AD explores how heterogeneous Alzheimer's disease analysis components can be coordinated when patient data are incomplete. Instead of assuming that MRI, PET, EEG, clinical assessments, and other modalities are always simultaneously available, the framework emphasizes **modularity, controlled execution, missing-modality handling, and transparent output provenance**.

The thesis evaluation focused on system-level feasibility and workflow robustness rather than claiming a new state-of-the-art diagnostic model.

## Core contribution

The project focuses on the integration layer around modality-specific research components:

- independent validation of modality inputs;
- conditional execution of available components;
- explicit `executed`, `skipped`, and `error` states;
- aggregation using only successfully produced outputs;
- transparent reporting of which modalities contributed to a result;
- a unified Streamlit-based interaction concept.

## Architecture

```text
Patient / Research Inputs
        |
        v
+---------------------------+
| Modality availability &   |
| input validation          |
+---------------------------+
        |
        +----------+----------+----------+----------+
        |          |          |          |          |
     Clinical     EEG        PET        MRI       Features
        |          |          |          |          |
        v          v          v          v          v
   Predictor    GSP       3D CNN      AD-DL      GPMKL
        |          |          |          |          |
        +----------+----------+----------+----------+
                           |
                           v
                Available outputs only
                           |
                           v
                Transparent aggregation
                           |
                           v
                 Execution trace / result
```

## Thesis evaluation behavior

The thesis reports a representative partial-data execution in which the **Clinical Predictor** and **GSP-EEG** components executed, while **3DCNN-PET**, **AD-DL MRI**, and **GPMKL** were skipped because their required runtime inputs/resources were unavailable. The two available outputs were averaged as a simple, interpretable aggregation mechanism.

This public reconstruction deliberately does not fabricate predictions for unavailable components.

## Repository structure

```text
HARMONI-AD/
├── app.py                         # safe Streamlit workflow demonstrator
├── src/harmoni_ad/
│   └── workflow.py                # status model + transparent aggregation
├── tests/
│   └── test_workflow.py
├── docs/
│   ├── IMPLEMENTATION_NOTES.md
│   └── THIRD_PARTY_COMPONENTS.md
├── requirements.txt
└── .gitignore
```

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests with:

```bash
pytest
```

## Third-party research components

The thesis workspace evaluated/integrated research components for PET, MRI, EEG, clinical data, and feature-based modelling. The original workspace contains third-party implementations. They are **not copied into this cleaned repository**; see [`docs/THIRD_PARTY_COMPONENTS.md`](docs/THIRD_PARTY_COMPONENTS.md) for provenance notes.

## Data and model files

Medical/research datasets, ADNI-derived data, model weights, serialized models, and subject-level files are intentionally excluded from this repository. Users should obtain any external datasets directly from their official providers and comply with the applicable data-use agreements.

## Scope and limitations

HARMONI-AD was evaluated primarily as an integration and workflow prototype. The thesis did not benchmark all five modality-specific components simultaneously on a single complete multimodal cohort. The conceptual architecture also discusses more advanced fusion and explainability directions that go beyond what is reproduced in this cleaned public codebase.

## Thesis

**A Multimodal Machine Learning Framework for Early Alzheimer's Disease**  
Master of Science in Digital Health — Deggendorf Institute of Technology, 2026.

## License

No license is granted for third-party components referenced by this project. Before assigning a license to this repository, the ownership/licensing of any additional code copied from the original thesis workspace should be reviewed.
