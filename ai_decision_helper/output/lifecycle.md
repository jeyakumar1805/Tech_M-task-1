# Lifecycle map for AI-suitable requirements

## 2. Predict which customers will cancel next month (Classical ML)

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define the prediction target, decision it supports and success metric for 'Predict which customers will cancel next month'. | Product owner |
| Data | Build a clean historical training table and check for leakage and missing values. | Data engineer |
| Model | Train and compare a baseline and a tree-based model; validate on a time-based holdout. | Data scientist |
| Deployment | Ship the model as a scheduled batch job or API feeding the business system. | ML engineer |
| Monitoring | Track accuracy against actual outcomes and input drift; retrain on a schedule. | ML engineer |

## 3. Summarise long support emails (Generative AI)

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define allowed outputs, quality bar and human-review rules for 'Summarise long support emails'. | Product owner |
| Data | Collect and clean source documents/examples; add access controls and remove sensitive data. | Data engineer |
| Model | Choose an LLM, design prompts/retrieval, and score outputs on a gold evaluation set. | Data scientist |
| Deployment | Deploy behind an API with guardrails, logging, cost limits and a feedback button. | ML engineer |
| Monitoring | Review sampled outputs for hallucination, cost and user feedback; re-run evals on every change. | Product owner |

## 4. Detect defects in product photos (Deep Learning)

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define classes, acceptable miss/false-alarm rates and the human fallback for 'Detect defects in product photos'. | Product owner |
| Data | Collect and label representative images/audio/text with domain experts; version the dataset. | Data engineer |
| Model | Fine-tune a pre-trained network and test on a held-out set including hard cases. | Data scientist |
| Deployment | Serve the model on suitable hardware (GPU/edge) with a review queue for low-confidence cases. | ML engineer |
| Monitoring | Sample production predictions for re-labelling; watch for new defect types or lighting/camera drift. | Data scientist |

## 6. Forecast weekly product demand (Classical ML)

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define the prediction target, decision it supports and success metric for 'Forecast weekly product demand'. | Product owner |
| Data | Build a clean historical training table and check for leakage and missing values. | Data engineer |
| Model | Train and compare a baseline and a tree-based model; validate on a time-based holdout. | Data scientist |
| Deployment | Ship the model as a scheduled batch job or API feeding the business system. | ML engineer |
| Monitoring | Track accuracy against actual outcomes and input drift; retrain on a schedule. | ML engineer |

## 7. Answer employee questions from the HR policy PDF (Generative AI)

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define allowed outputs, quality bar and human-review rules for 'Answer employee questions from the HR policy PDF'. | Product owner |
| Data | Collect and clean source documents/examples; add access controls and remove sensitive data. | Data engineer |
| Model | Choose an LLM, design prompts/retrieval, and score outputs on a gold evaluation set. | Data scientist |
| Deployment | Deploy behind an API with guardrails, logging, cost limits and a feedback button. | ML engineer |
| Monitoring | Review sampled outputs for hallucination, cost and user feedback; re-run evals on every change. | Product owner |

## 10. Draft personalised replies to customer complaints (Generative AI)

| Stage | Task | Role |
|---|---|---|
| Problem framing | Define allowed outputs, quality bar and human-review rules for 'Draft personalised replies to customer complaints'. | Product owner |
| Data | Collect and clean source documents/examples; add access controls and remove sensitive data. | Data engineer |
| Model | Choose an LLM, design prompts/retrieval, and score outputs on a gold evaluation set. | Data scientist |
| Deployment | Deploy behind an API with guardrails, logging, cost limits and a feedback button. | ML engineer |
| Monitoring | Review sampled outputs for hallucination, cost and user feedback; re-run evals on every change. | Product owner |
