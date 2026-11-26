"""Business requirements stored as data.

Each requirement carries yes/no attributes that drive the decision function.

Attribute meanings
------------------
rules_possible      : A person can write the full logic as explicit rules/formulae.
learns_from_data    : The logic can only be discovered by learning patterns from
                      examples (prediction, classification, forecasting).
unstructured_input  : Input is free text, images, audio or documents, not tidy columns.
generates_content   : Output is new content (text, answers, drafts), not a label/number.
data_available      : Relevant historical / labelled data or source documents exist today.
descriptive_only    : The need is to summarise or visualise what already happened
                      (aggregates, charts, dashboards), with no prediction.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Requirement:
    id: int
    name: str
    rules_possible: bool
    learns_from_data: bool
    unstructured_input: bool
    generates_content: bool
    data_available: bool
    descriptive_only: bool = False


REQUIREMENTS = [
    # --- the 8 given requirements ---
    Requirement(1, "Validate PAN number format",
                rules_possible=True, learns_from_data=False, unstructured_input=False,
                generates_content=False, data_available=True),
    Requirement(2, "Predict which customers will cancel next month",
                rules_possible=False, learns_from_data=True, unstructured_input=False,
                generates_content=False, data_available=True),
    Requirement(3, "Summarise long support emails",
                rules_possible=False, learns_from_data=False, unstructured_input=True,
                generates_content=True, data_available=True),
    Requirement(4, "Detect defects in product photos",
                rules_possible=False, learns_from_data=True, unstructured_input=True,
                generates_content=False, data_available=False),  # no labelled photos yet
    Requirement(5, "Calculate GST on an invoice",
                rules_possible=True, learns_from_data=False, unstructured_input=False,
                generates_content=False, data_available=True),
    Requirement(6, "Forecast weekly product demand",
                rules_possible=False, learns_from_data=True, unstructured_input=False,
                generates_content=False, data_available=True),
    Requirement(7, "Answer employee questions from the HR policy PDF",
                rules_possible=False, learns_from_data=False, unstructured_input=True,
                generates_content=True, data_available=True),
    Requirement(8, "Sort invoices by amount",
                rules_possible=True, learns_from_data=False, unstructured_input=False,
                generates_content=False, data_available=True),
    # --- 2 requirements of our own ---
    Requirement(9, "Monthly sales dashboard by region and product",
                rules_possible=True, learns_from_data=False, unstructured_input=False,
                generates_content=False, data_available=True, descriptive_only=True),
    Requirement(10, "Draft personalised replies to customer complaints",
                rules_possible=False, learns_from_data=False, unstructured_input=True,
                generates_content=True, data_available=True),
]
