"""Assert-based tests. Run with: python tests/test_decision.py  (or: pytest)"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from ai_triage import (REQUIREMENTS, classify, lifecycle_for, STAGES,
                       NO_AI, BI, ML, DL, GENAI, Requirement)

BY_NAME = {r.name: r for r in REQUIREMENTS}


def decision(name):
    return classify(BY_NAME[name])


def test_at_least_ten_requirements():
    assert len(REQUIREMENTS) >= 10


def test_gst_is_no_ai():
    assert decision("Calculate GST on an invoice").category == NO_AI


def test_pan_validation_is_no_ai():
    assert decision("Validate PAN number format").category == NO_AI


def test_sorting_is_no_ai():
    assert decision("Sort invoices by amount").category == NO_AI


def test_photo_defects_is_deep_learning():
    assert decision("Detect defects in product photos").category == DL


def test_tabular_prediction_is_classical_ml():
    assert decision("Predict which customers will cancel next month").category == ML
    assert decision("Forecast weekly product demand").category == ML


def test_text_generation_is_genai():
    assert decision("Summarise long support emails").category == GENAI
    assert decision("Answer employee questions from the HR policy PDF").category == GENAI


def test_dashboard_is_bi():
    assert decision("Monthly sales dashboard by region and product").category == BI


def test_every_decision_has_reasons_risks_and_next_step():
    for req in REQUIREMENTS:
        d = classify(req)
        assert d.reasons and d.risks and d.next_step, req.name


def test_missing_data_is_flagged_as_blocker():
    assert decision("Detect defects in product photos").risks[0].startswith("Blocker")


def test_lifecycle_only_for_ai_and_has_five_stages():
    for req in REQUIREMENTS:
        d = classify(req)
        stages = lifecycle_for(d.category, req.name)
        if d.is_ai:
            assert [s for s, _, _ in stages] == STAGES
            assert all(task and role for _, task, role in stages)
        else:
            assert stages == []


def test_contradictory_requirement_raises():
    bad = Requirement(99, "Vague ask", False, False, False, False, True)
    try:
        classify(bad)
    except ValueError:
        return
    raise AssertionError("expected ValueError")


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    for name, fn in tests:
        fn()
        print(f"PASS {name}")
    print(f"\nAll {len(tests)} tests passed.")
