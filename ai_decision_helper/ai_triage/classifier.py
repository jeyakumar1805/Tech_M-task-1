"""Decision function: does a requirement need AI, and which kind?

Concept ladder the categories are based on (see docs/concepts.md for more):

* AI  (umbrella)   : any technique that lets software do tasks that normally need
                     human judgement. Includes ML, DL and GenAI.
* Machine Learning : the rules are *learned from historical data* instead of being
                     written by hand. Typically tabular data (churn, demand, fraud).
* Deep Learning    : ML using many-layered neural networks; shines on unstructured
                     data (images, audio, text) where features cannot be hand-built.
* Generative AI    : deep models (LLMs, diffusion) that *create new content* - text,
                     summaries, answers, images - rather than output a label or number.

Two non-AI categories sit below the ladder:

* No AI (rules/code): the logic is fully known and deterministic.
* Analytics/BI      : describing what already happened (aggregations, dashboards).

Decision order (first match wins):
  1. Output is generated content                   -> Generative AI
  2. Unstructured input AND (learned OR no rules)  -> Deep Learning
  3. Must be learned from data                     -> Classical ML
  4. Descriptive reporting only                    -> Analytics/BI
  5. Rules can express it                          -> No AI (rules/code)
"""

from dataclasses import dataclass, field

from .requirements_data import Requirement

NO_AI = "No AI (rules/code)"
BI = "Analytics/BI"
ML = "Classical ML"
DL = "Deep Learning"
GENAI = "Generative AI"

CATEGORIES = [NO_AI, BI, ML, DL, GENAI]
AI_CATEGORIES = [ML, DL, GENAI]  # categories that need an AI project lifecycle


@dataclass
class Decision:
    category: str
    reasons: list = field(default_factory=list)
    risks: list = field(default_factory=list)
    next_step: str = ""

    @property
    def is_ai(self):
        return self.category in AI_CATEGORIES


_BASE_RISKS = {
    NO_AI: ["Using AI here would add cost and non-deterministic errors for no benefit.",
            "Rules can go stale (e.g. law or rate changes), so keep them configurable and tested."],
    BI: ["Teams may define metrics differently, so agree one definition per metric.",
         "Dashboards are only as good as the underlying data quality."],
    ML: ["Model accuracy degrades as customer/market behaviour drifts.",
         "Predictions are probabilistic, so a business owner must accept some error rate."],
    DL: ["Needs a lot of good labelled examples and compute.",
         "Hard to explain individual predictions; failure cases can be surprising."],
    GENAI: ["Hallucination: output may be fluent but wrong, so evaluation and human review are needed.",
            "Data privacy: prompts may contain personal or confidential data.",
            "Ongoing per-use model cost and vendor dependence."],
}


def classify(req: Requirement) -> Decision:
    reasons = []

    if req.generates_content:
        category = GENAI
        reasons.append("Output is newly generated content (text), which only generative models produce.")
        if req.unstructured_input:
            reasons.append("Input is free text/documents, which large language models handle natively.")
        if not req.rules_possible:
            reasons.append("No fixed rules can produce the right wording for every case.")
        if not req.learns_from_data:
            reasons.append("A pre-trained model can be used, so no model training is needed from scratch.")

    elif req.unstructured_input and (req.learns_from_data or not req.rules_possible):
        category = DL
        reasons.append("Input is unstructured (images/audio/text), so features cannot be hand-coded.")
        if req.learns_from_data:
            reasons.append("The decision must be learned from labelled examples.")
        reasons.append("Output is a label/number, not new content, so this is discriminative deep learning, not generative.")

    elif req.learns_from_data:
        category = ML
        reasons.append("Logic must be learned from historical data; nobody can write the rule by hand.")
        reasons.append("Input is structured/tabular, so classical ML is enough and cheaper than deep learning.")
        if req.rules_possible:
            reasons.append("Some rules exist, so use them as a baseline to beat.")

    elif req.descriptive_only:
        category = BI
        reasons.append("Need is to summarise or visualise what already happened, not predict or generate.")
        reasons.append("Aggregations and charts on existing data need no model.")

    elif req.rules_possible:
        category = NO_AI
        reasons.append("The logic is fully known and deterministic, so it can be written as explicit rules.")
        reasons.append("No learning from data is needed; the exact same input must always give the same output.")
        if req.unstructured_input:
            reasons.append("Input looks unstructured but follows a fixed layout that code can parse.")

    else:
        raise ValueError(
            f"Requirement '{req.name}' cannot be classified: no rules, no learning need, "
            "no generation and not descriptive. Clarify the requirement."
        )

    risks = list(_BASE_RISKS[category])
    if category in (ML, DL) and not req.data_available:
        risks.insert(0, "Blocker: no usable (labelled) training data exists today.")
    if category == GENAI and not req.data_available:
        risks.insert(0, "Blocker: no source documents/examples available to ground the model.")

    return Decision(category, reasons, risks, _next_step(category, req))


def _next_step(category: str, req: Requirement) -> str:
    if category == NO_AI:
        return "Write the rule as a spec with worked examples, implement in code and unit-test it."
    if category == BI:
        return "Agree metric definitions with the business owner and build the dashboard on the existing data source."
    if category == ML:
        if req.data_available:
            return "Pull historical data, define the target and success metric, and build a simple baseline."
        return "Start collecting and logging the data needed; revisit once enough history exists."
    if category == DL:
        if req.data_available:
            return "Audit volume and quality of labelled data and try a pre-trained model as a baseline."
        return "Collect and label a pilot set of examples (with domain experts) before choosing a model."
    # GENAI
    if req.data_available:
        return "Build a small evaluation set of real examples with expected outputs and prototype with an off-the-shelf LLM."
    return "Gather source documents/examples first, then prototype with an off-the-shelf LLM."
