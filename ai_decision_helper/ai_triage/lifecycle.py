"""Lifecycle map: 5 project stages per AI-suitable category, with a task and an owner each.

Only AI-suitable requirements (Classical ML, Deep Learning, Generative AI) get a lifecycle.
'{name}' is replaced with the requirement's name.
"""

from .classifier import ML, DL, GENAI, AI_CATEGORIES

STAGES = ["Problem framing", "Data", "Model", "Deployment", "Monitoring"]

# category -> list of (stage, concrete task, responsible role), in stage order
_LIFECYCLE = {
    ML: [
        ("Problem framing", "Define the prediction target, decision it supports and success metric for '{name}'.", "Product owner"),
        ("Data", "Build a clean historical training table and check for leakage and missing values.", "Data engineer"),
        ("Model", "Train and compare a baseline and a tree-based model; validate on a time-based holdout.", "Data scientist"),
        ("Deployment", "Ship the model as a scheduled batch job or API feeding the business system.", "ML engineer"),
        ("Monitoring", "Track accuracy against actual outcomes and input drift; retrain on a schedule.", "ML engineer"),
    ],
    DL: [
        ("Problem framing", "Define classes, acceptable miss/false-alarm rates and the human fallback for '{name}'.", "Product owner"),
        ("Data", "Collect and label representative images/audio/text with domain experts; version the dataset.", "Data engineer"),
        ("Model", "Fine-tune a pre-trained network and test on a held-out set including hard cases.", "Data scientist"),
        ("Deployment", "Serve the model on suitable hardware (GPU/edge) with a review queue for low-confidence cases.", "ML engineer"),
        ("Monitoring", "Sample production predictions for re-labelling; watch for new defect types or lighting/camera drift.", "Data scientist"),
    ],
    GENAI: [
        ("Problem framing", "Define allowed outputs, quality bar and human-review rules for '{name}'.", "Product owner"),
        ("Data", "Collect and clean source documents/examples; add access controls and remove sensitive data.", "Data engineer"),
        ("Model", "Choose an LLM, design prompts/retrieval, and score outputs on a gold evaluation set.", "Data scientist"),
        ("Deployment", "Deploy behind an API with guardrails, logging, cost limits and a feedback button.", "ML engineer"),
        ("Monitoring", "Review sampled outputs for hallucination, cost and user feedback; re-run evals on every change.", "Product owner"),
    ],
}


def lifecycle_for(category: str, name: str):
    """Return [(stage, task, role), ...] for an AI category, or [] if not AI-suitable."""
    if category not in AI_CATEGORIES:
        return []
    return [(stage, task.format(name=name), role) for stage, task, role in _LIFECYCLE[category]]
