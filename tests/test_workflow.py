from src.harmoni_ad.workflow import ModalityResult, aggregate_available

def test_skipped_modalities_do_not_contribute():
    results = [
        ModalityResult("Clinical", "executed", 0.52),
        ModalityResult("EEG", "executed", 0.64),
        ModalityResult("PET", "skipped"),
    ]
    out = aggregate_available(results)
    assert out["status"] == "aggregated"
    assert out["n_modalities"] == 2
    assert abs(out["probability"] - 0.58) < 1e-9

def test_insufficient_data():
    out = aggregate_available([ModalityResult("Clinical", "executed", 0.52)])
    assert out["status"] == "insufficient_data"
