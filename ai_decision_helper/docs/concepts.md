# AI vs ML vs Deep Learning vs Generative AI

These terms are nested, like Russian dolls:

```
AI
└── Machine Learning (ML)
    └── Deep Learning (DL)
        └── Generative AI (GenAI)
```

| Term | Plain meaning | Typical input | Typical output | Example |
|---|---|---|---|---|
| **AI** | Umbrella: software doing tasks that normally need human judgement | any | any | All below |
| **Machine Learning** | Rules are *learned from historical data*, not hand-written | Tables (structured) | A number or label | Churn prediction, demand forecast |
| **Deep Learning** | ML with many-layered neural networks; learns its own features | Images, audio, text | A label or number | Defect detection in photos |
| **Generative AI** | Deep models that *create new content* | Prompts, documents | Text, answers, images | Summarising emails, HR policy Q&A |

Two non-AI categories complete the picture:

- **No AI (rules/code)**: logic is fully known and deterministic (GST, PAN format, sorting).
  Cheaper, exact and explainable. Always prefer this when it works.
- **Analytics/BI**: describes what already happened (dashboards, aggregates). No prediction.

## How the helper decides (first match wins)

1. Output is newly generated content -> **Generative AI**
2. Unstructured input and (must be learned, or no rules possible) -> **Deep Learning**
3. Must be learned from data -> **Classical ML**
4. Descriptive reporting only -> **Analytics/BI**
5. Rules can express it -> **No AI (rules/code)**

Rule of thumb for a delivery manager: *if you can write the rule down, don't use AI.*
