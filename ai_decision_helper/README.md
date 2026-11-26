# AI Decision Helper

A small, dependency-free Python tool (standard library only, Python 3.8+) that helps a delivery
manager judge whether each "use AI" request really needs AI, and which kind.

## Project layout

```
main.py                      entry point
ai_triage/requirements_data.py  10 requirements stored as data with yes/no attributes
ai_triage/classifier.py         decision function: category + reasons + risks + next step
ai_triage/lifecycle.py          5-stage lifecycle map (task + role) for AI-suitable items
ai_triage/report.py             writes report.csv, report.md, lifecycle.md
tests/test_decision.py          assert-based tests
docs/concepts.md                AI vs ML vs Deep Learning vs Generative AI explained
```

## How to run

```bash
python main.py                    # writes ./output/report.csv, report.md, lifecycle.md
python main.py --out-dir results  # custom output folder
python tests/test_decision.py     # run tests (pytest also works: pytest tests/)
```

## Categories

No AI (rules/code), Analytics/BI, Classical ML, Deep Learning, Generative AI.
See `docs/concepts.md` for the definitions and the decision order.

## Adding your own requirement

Add a `Requirement(...)` to `REQUIREMENTS` in `ai_triage/requirements_data.py` and re-run.
Attributes: `rules_possible`, `learns_from_data`, `unstructured_input`, `generates_content`,
`data_available`, `descriptive_only`. Contradictory attributes raise a `ValueError`.

## Sample output

```
 #  Requirement                                          Decision
-------------------------------------------------------------------------------------
 1  Validate PAN number format                           No AI (rules/code)
 2  Predict which customers will cancel next month       Classical ML
 3  Summarise long support emails                        Generative AI
 4  Detect defects in product photos                     Deep Learning
 5  Calculate GST on an invoice                          No AI (rules/code)
 6  Forecast weekly product demand                       Classical ML
 7  Answer employee questions from the HR policy PDF     Generative AI
 8  Sort invoices by amount                              No AI (rules/code)
 9  Monthly sales dashboard by region and product        Analytics/BI
10  Draft personalised replies to customer complaints    Generative AI

6 of 10 requirements need AI; 4 do not.
```

Sample `report.csv` row (columns: id, requirement, decision, reasons, risks, first_next_step):

```
4,Detect defects in product photos,Deep Learning,"Input is unstructured ... | The decision must be learned from labelled examples. | ...","Blocker: no usable (labelled) training data exists today. | ...","Collect and label a pilot set of examples (with domain experts) before choosing a model."
```

Sample lifecycle excerpt (`output/lifecycle.md`):

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define the prediction target, decision it supports and success metric. | Product owner |
| Data | Build a clean historical training table and check for leakage and missing values. | Data engineer |
| Model | Train and compare a baseline and a tree-based model; validate on a time-based holdout. | Data scientist |
| Deployment | Ship the model as a scheduled batch job or API feeding the business system. | ML engineer |
| Monitoring | Track accuracy against actual outcomes and input drift; retrain on a schedule. | ML engineer |
