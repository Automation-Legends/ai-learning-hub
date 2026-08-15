# Prompt Template

Use this template to create a clear, reviewable prompt for a one-off task or a repeated workflow. Remove sections that do not help your task; keep the rules that protect accuracy, privacy, and human accountability.

## Copyable template

```text
# Goal
Help me [specific outcome].

# Audience and context
The audience is [who will use the result].
Relevant background: [facts, definitions, source material, or constraints].

# Rules and boundaries
- Use only the information provided below unless I explicitly request research.
- Do not invent facts, dates, names, sources, calculations, or citations.
- If information is missing or unclear, [ask up to N questions / use a placeholder / flag it for review].
- Do not include or infer [sensitive or out-of-scope information].

# Task
[Describe the transformation, analysis, or draft needed.]

# Input
<input>
[Paste authorized, relevant material here.]
</input>

# Output format
Return [table, checklist, JSON, draft, sections, word limit, tone, language].
Include [required fields or headings].

# Quality check
Before finalizing, list:
1. Assumptions made;
2. Missing information;
3. Claims or numbers that require independent verification.
```

## When to use each section

| Section | Use it when | Example |
|---|---|---|
| Goal | Always | “Create a review-ready project update.” |
| Audience and context | The response depends on a user, organization, or situation | “This is for new volunteers with no prior knowledge.” |
| Rules and boundaries | Accuracy, policy, privacy, or completeness matters | “Do not invent deadlines; use `[confirm]` when absent.” |
| Input | The AI needs specific source material | Approved notes, an anonymized transcript, or product requirements |
| Output format | You need a result that can be checked or reused | “Return a five-row table with column headers.” |
| Quality check | The output will influence an important decision or publication | “Flag assumptions and unsupported claims.” |

## Example — Create a study guide

```text
# Goal
Create a study guide that helps a high-school learner review photosynthesis.

# Audience and context
The learner has completed a basic biology unit and needs practice before a quiz.

# Rules and boundaries
- Use only the notes in the input.
- Do not add facts that are not stated in the notes.
- If a key term is not explained in the notes, list it as a question rather than guessing.

# Task
Create a concise study guide and ten practice questions.

# Input
<input>
[Approved class notes go here.]
</input>

# Output format
Use the headings “Key ideas,” “Vocabulary,” and “Practice questions.”
Put the answer key after the questions. Keep each explanation to two sentences or fewer.

# Quality check
List any missing information that prevents a complete answer key.
```

## Improvement log

When a prompt is used more than once, save the following information. This helps you learn from actual results instead of guessing what changed.

| Version | Date | Change made | Test case | Result | Next action |
|---|---|---|---|---|---|
| v1.0 | YYYY-MM-DD | First draft | Typical input | Needed a clearer format | Add required columns |

## Review reminder

A structured prompt improves clarity; it does not guarantee correctness. Independently verify important information, calculations, sources, and decisions before using the output.
