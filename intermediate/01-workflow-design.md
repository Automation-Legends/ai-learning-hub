# Intermediate 1 — Workflow Design

## Goal

By the end of this module, you will be able to map a recurring task as a workflow, identify a narrow AI opportunity, and specify the human review and data boundaries before you automate anything.

## Start with the work, not the tool

The strongest AI workflows begin with a real process that is already understood. Before choosing a model or automation platform, map what starts the task, what information is used, what transformations occur, who reviews the result, and what happens when information is missing.

> **Automating an unclear process can make confusion faster.** First make the work visible; then decide where AI is genuinely helpful.

## The workflow canvas

Use the [workflow canvas](../templates/workflow-canvas.md) to document the following elements.

| Element | Question to answer | Example |
|---|---|---|
| Trigger | What starts the workflow? | A new form submission arrives. |
| Input | What information is needed? | An authorized, minimized copy of the form response. |
| Transformation | What work needs to happen? | Extract the request, classify the topic, and draft a reply. |
| Output | What should be produced? | A structured draft in a review queue. |
| Review | Who approves, corrects, or rejects it? | A support coordinator. |
| Destination | Where does the approved output go? | A help-desk system or email draft. |
| Exception | What happens when confidence is low or data is missing? | Route the item to a person without sending a draft. |
| Measure | How will you know it is helping? | Review time, correction rate, and response completeness. |

## Find a bounded AI opportunity

Good AI workflow candidates tend to involve unstructured text, recurring patterns, a clear human-defined goal, and an affordable review step. Begin with an **assistive** action rather than an autonomous decision.

| Candidate task | Appropriate AI boundary | Avoid at first |
|---|---|---|
| Incoming-message triage | Suggest a category and a concise summary for review | Automatically deny, approve, or commit on behalf of a person |
| Meeting follow-up | Extract draft action items from approved notes | Assign ownership or deadlines without confirmation |
| Content preparation | Create a draft outline from an approved brief | Publish without factual and editorial review |
| Feedback analysis | Suggest themes from anonymized feedback | Make people-impacting conclusions without review |

## Activity — Map your workflow

Select one recurring task and complete the workflow canvas. Then write a one-sentence AI opportunity statement using this pattern:

```text
When [trigger] happens, use AI to [bounded transformation] from [approved input] and create [checkable output] for [human reviewer]. If [exception], route the item to [person or process].
```

### Example

> When a team member submits weekly project notes, use AI to extract draft milestones, blockers, and questions from the approved notes and create a table for the project lead. If the notes are ambiguous or contain a missing owner, flag the item rather than guessing.

## Data boundaries

Document what the AI should receive and what it should never receive. Minimize inputs to only what is necessary for the transformation. Replace names, identifiers, or sensitive details with placeholders whenever possible. Confirm that your organization’s policies and the selected tool’s data practices permit the intended use.

## Completion check

You have completed this module when you have a one-page workflow canvas, a narrow AI opportunity, a named human reviewer, a defined exception path, and at least one measurable success signal.

## Reflection

Where does the workflow depend on human judgment? What would be the consequence if the AI output were wrong, incomplete, or sent to the wrong destination?

## Continue

Next, make the AI step more consistent: [Reliable prompting](02-reliable-prompting.md).
