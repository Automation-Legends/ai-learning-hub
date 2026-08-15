# Intermediate 2 — Reliable Prompting

## Goal

By the end of this module, you will be able to create a reusable prompt that separates instructions from input data, includes an output schema, and uses examples to make the result easier to evaluate.

## From a chat request to a workflow prompt

An everyday prompt may be enough for a one-off task. A repeatable workflow needs more structure. The prompt should make clear what never changes, what changes for each run, what a successful output looks like, and what the AI should do when required information is missing.

| Prompt layer | Purpose | Example |
|---|---|---|
| **Role and purpose** | Establish the task and intended standard | “You prepare a concise project-update draft for a project lead.” |
| **Rules** | Define boundaries and must-follow behavior | “Do not invent owners, dates, or status. Mark missing facts as `[needs confirmation]`.” |
| **Input data** | Provide the specific material for this run | `<project_notes>…</project_notes>` |
| **Output schema** | Make the result checkable and reusable | “Return a table with milestone, status, blocker, owner, and evidence.” |
| **Examples** | Demonstrate a desired pattern for a representative case | Input/output pair showing a correctly flagged missing owner |
| **Review instruction** | Surface uncertainty and route exceptions | “List assumptions and unanswered questions after the table.” |

Organized prompt sections and examples can help a model distinguish task rules from reference material and follow a desired output pattern. [1]

## A reusable prompt template

Use the [prompt template](../templates/prompt-template.md) and keep it under version control or in a shared document with a simple change log. A prompt version should include the date, intended use, owner, sample input, expected output, and known limitations.

```text
# Purpose
Create a review-ready project-update draft from approved weekly notes.

# Rules
- Do not invent facts, owners, dates, or status.
- Use only the supplied notes.
- Mark any missing required field as [needs confirmation].
- If the notes conflict, place the conflict in the questions section.

# Input
<weekly_notes>
[Paste authorized notes here]
</weekly_notes>

# Output format
1. A Markdown table: milestone | status | blocker | owner | supporting note
2. A section named “Questions for review” with unresolved issues.
3. A section named “Assumptions made” with any interpretation that needs confirmation.
```

## Examples are specifications

If a task has a precise style or classification rule, provide one or two representative input/output examples. Select examples that demonstrate a decision the model could otherwise misinterpret. Do not rely on examples alone; keep the core rules explicit.

| Example type | What it teaches |
|---|---|
| Normal case | The expected structure and level of detail |
| Incomplete case | How to flag missing information instead of guessing |
| Ambiguous case | How to describe uncertainty and request review |
| Edge case | A boundary the model must not cross |

## Activity — Build a versioned prompt

Create version 1 of the AI step you mapped in Module 1. Include a purpose, rules, input section, output schema, and at least one example. Then test it with two inputs: one normal case and one incomplete or ambiguous case.

Record the following table in your notes.

| Field | Record |
|---|---|
| Prompt version | e.g., `v1.0 — 2026-08-14` |
| Intended task | The exact workflow step it supports |
| What worked | A specific behavior you want to preserve |
| What failed | A concrete error, omission, or undesirable behavior |
| Change for v1.1 | One deliberate edit to test next |

## Completion check

You have completed this module when your prompt has separate sections for rules and input, a requested output format, at least one review instruction, and a test case that demonstrates how it handles missing or ambiguous information.

## Reflection

What must never change between runs? What is specific to each input? How can your output format make it easier for another person to review the AI’s work quickly?

## Continue

A structured prompt is only a hypothesis. Next, test it against defined success criteria: [Evaluation and safeguards](03-evaluation-and-safeguards.md).

## References

[1]: https://developers.openai.com/api/docs/guides/prompt-engineering "OpenAI — Prompt engineering"
