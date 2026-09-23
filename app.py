"""HARMONI-AD workflow demonstrator.

Portfolio-safe reconstruction: demonstrates controlled execution, explicit skipping,
and transparent aggregation without inventing model outputs when a trained component
is unavailable.
"""
import streamlit as st
from src.harmoni_ad.workflow import ModalityResult, aggregate_available

st.set_page_config(page_title="HARMONI-AD", layout="wide")
st.title("HARMONI-AD")
st.caption("Multimodal Alzheimer’s disease workflow demonstrator — research prototype, not a clinical device")

st.markdown("""
This interface demonstrates the thesis workflow principle: each modality is validated
independently, unavailable components are explicitly skipped, and only genuine
successful outputs may contribute to aggregation.
""")

st.subheader("Modality status")
clinical_ok = st.checkbox("Clinical predictor output available")
eeg_ok = st.checkbox("EEG/GSP output available")
pet_ok = st.checkbox("PET/3DCNN output available")
mri_ok = st.checkbox("MRI/AD-DL output available")
gpmkl_ok = st.checkbox("GPMKL output available")

configs = [
    ("Clinical", clinical_ok), ("GSP-EEG", eeg_ok), ("3DCNN-PET", pet_ok),
    ("AD-DL MRI", mri_ok), ("GPMKL", gpmkl_ok),
]
results = []
for name, enabled in configs:
    if enabled:
        p = st.number_input(f"{name}: externally produced AD probability", 0.0, 1.0, 0.5, 0.01, key=name)
        results.append(ModalityResult(name, "executed", p))
    else:
        results.append(ModalityResult(name, "skipped", message="No validated model output supplied"))

if st.button("Aggregate available outputs"):
    agg = aggregate_available(results)
    st.subheader("Execution trace")
    for r in results:
        st.json(r.to_dict())
    st.subheader("Aggregation")
    if agg["status"] == "insufficient_data":
        st.warning("At least two validated modality outputs are required for aggregation.")
    else:
        st.metric("Mean probability across available modalities", f'{agg["probability"]:.3f}')
        st.info("Interpret as a research workflow output only; no clinical diagnosis is produced.")
