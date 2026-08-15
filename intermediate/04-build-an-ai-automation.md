# Intermediate 4 — Build an AI Automation

## Goal

By the end of this module, you will be able to specify a small AI-assisted automation that has a clear trigger, authorized input, bounded AI task, human review, destination, exception route, and measurement plan.

## Automation is a system

An AI automation is more than a prompt connected to another app. It is a system with data flowing through it, decisions about what should happen, people who remain accountable, and planned behavior when the normal path fails.

> **Begin with “draft and review,” not “decide and send.”** Earn greater automation only after your workflow demonstrates reliable performance and appropriate controls.

## The minimum viable automation

| Component | Question | Example |
|---|---|---|
| **Trigger** | What event starts the workflow? | A new approved form response is received. |
| **Input preparation** | What authorized, minimal data is passed onward? | Request text with names and identifiers removed where possible. |
| **AI action** | What narrow transformation does AI perform? | Extract topic, urgency cues, and a concise summary. |
| **Output contract** | What exact structure should the AI return? | JSON or table with `topic`, `summary`, `questions`, and `needs_review`. |
| **Decision rule** | What controls the next step? | If `needs_review` is true, do not create a draft. |
| **Human review** | Who approves or corrects the result? | A support coordinator checks the review queue. |
| **Destination** | Where does an approved item go? | A ticket system, spreadsheet, or email draft. |
| **Exception path** | What happens on missing data, failure, or ambiguity? | Create a manual-review task with the source link. |
| **Monitoring** | What will you measure? | Completion rate, correction rate, exception rate, and review time. |

## Build specification

Complete this specification before connecting tools.

```text
Workflow name:
Owner:
Purpose and user benefit:

Trigger:
Authorized input and data boundary:

AI task:
Prompt version:
Expected output schema:

Human reviewer:
Approval criteria:

Destination after approval:
Exception conditions:
Fallback procedure:

Measures to review weekly:
Launch scope and date:
```

## Example: Meeting follow-up draft

| Field | Example specification |
|---|---|
| Workflow name | Weekly meeting follow-up draft |
| Trigger | The meeting note is marked “approved for processing.” |
| AI task | Extract draft decisions, action items, owners, and open questions from the note. |
| Output | A table with action, owner, due date, evidence, and `needs_confirmation`. |
| Review | The meeting facilitator confirms every action item before it is sent. |
| Exception | If no owner or due date is stated, use `[confirm]`; do not assign one. |
| Destination | An email draft and a review queue. |
| Measures | Missing-item rate, corrections per draft, and time to prepare follow-up. |

## Activity — Create your automation specification

Use your workflow canvas, versioned prompt, and evaluation results from the prior modules. Complete the build specification for a **draft-and-review** automation. Then invite a peer to inspect it and ask the following questions.

1. Is the AI task narrow enough to describe in one sentence?
2. Is every input authorized and necessary?
3. Does the output format make review quick?
4. Can the workflow avoid acting when information is missing or unclear?
5. Is there a named human owner and a manual fallback?
6. Would the workflow’s measures reveal a quality problem after launch?

## Launch gradually

Start with a small number of low-impact cases. Compare the automation with the existing manual process and review every output at first. Keep a record of corrections and exceptions. Expand only after the workflow consistently meets its success criteria and your review process is working as intended.

## Completion check

You have completed the Intermediate Path when you have a written automation specification, a tested prompt, five evaluation cases, defined approval criteria, an exception route, and a plan for measuring performance after launch.

## Reflection

What is the smallest safe first release? What evidence would persuade you that the automation is ready to handle a wider scope? What event should immediately pause or roll back the workflow?

## Next step

Share your sanitized learning project with the community using the [project showcase template](../templates/project-showcase.md). Then contribute an improvement, an example, or a new exercise through the [contribution guide](../CONTRIBUTING.md).
