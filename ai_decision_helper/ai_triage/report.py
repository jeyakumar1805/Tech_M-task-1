"""Write the decision report (CSV + Markdown) and the lifecycle map (Markdown)."""

import csv
import os

from .classifier import classify
from .lifecycle import lifecycle_for
from .requirements_data import REQUIREMENTS

COLUMNS = ["id", "requirement", "decision", "reasons", "risks", "first_next_step"]


def build_rows(requirements=REQUIREMENTS):
    rows = []
    for req in requirements:
        d = classify(req)
        rows.append({
            "id": req.id,
            "requirement": req.name,
            "decision": d.category,
            "reasons": " | ".join(d.reasons),
            "risks": " | ".join(d.risks),
            "first_next_step": d.next_step,
        })
    return rows


def _md_cell(text):
    return str(text).replace("|", "/").replace("\n", " ")


def write_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows, path):
    lines = ["# AI Decision Report", "",
             "| " + " | ".join(COLUMNS) + " |",
             "|" + "---|" * len(COLUMNS)]
    for r in rows:
        lines.append("| " + " | ".join(_md_cell(r[c]) for c in COLUMNS) + " |")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_lifecycle(path, requirements=REQUIREMENTS):
    lines = ["# Lifecycle map for AI-suitable requirements", ""]
    count = 0
    for req in requirements:
        d = classify(req)
        stages = lifecycle_for(d.category, req.name)
        if not stages:
            continue
        count += 1
        lines += [f"## {req.id}. {req.name} ({d.category})", "",
                  "| Stage | Task | Role |", "|---|---|---|"]
        lines += [f"| {s} | {_md_cell(t)} | {r} |" for s, t, r in stages]
        lines.append("")
    if not count:
        lines.append("No requirement needs an AI lifecycle.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_all(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    rows = build_rows()
    write_csv(rows, os.path.join(out_dir, "report.csv"))
    write_markdown(rows, os.path.join(out_dir, "report.md"))
    write_lifecycle(os.path.join(out_dir, "lifecycle.md"))
    return rows
