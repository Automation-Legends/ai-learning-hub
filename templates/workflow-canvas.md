# Workflow Canvas

Use this canvas to understand a recurring task before you introduce an AI step or connect an automation platform. Complete it with a real but non-sensitive example whenever possible.

> **Design principle:** A workflow should be understandable by a teammate who did not create it. If a step is unclear, simplify or document it before automating.

## Canvas

| Field | Your notes |
|---|---|
| **Workflow name** |  |
| **Owner** |  |
| **Problem to solve** |  |
| **User or beneficiary** |  |
| **Trigger** | What event starts the work? |
| **Current inputs** | What information is received, and who is authorized to use it? |
| **Current process** | List the current steps in order. |
| **Current output** | What does “done” look like? |
| **Pain point** | Where does the task take too long, create inconsistency, or lose useful information? |
| **AI opportunity** | What single bounded transformation could AI assist with? |
| **AI input boundary** | What is necessary to send? What must be removed, anonymized, or excluded? |
| **Expected AI output** | What exact structure would make the result checkable? |
| **Human reviewer** | Who approves, corrects, or rejects the result? |
| **Approval criteria** | What must be true before an output can proceed? |
| **Exception conditions** | What uncertainty, missing data, or result should stop the normal flow? |
| **Exception route** | Who or what process handles the exception? |
| **Destination** | Where does an approved result go? |
| **Fallback** | What happens if the AI step or connected service is unavailable? |
| **Success measures** | What will show that the workflow improved? |
| **Review date** | When will the owner assess results and decide whether to expand, revise, or stop? |

## One-sentence workflow statement

Use this statement after completing the canvas.

```text
When [trigger] happens, use AI to [bounded transformation] from [authorized, minimal input] and create [checkable output] for [human reviewer]. If [exception], route the item to [person or fallback process].
```

## Example

| Field | Example |
|---|---|
| Workflow name | Weekly project-update draft |
| Trigger | A team member submits approved weekly notes. |
| AI opportunity | Extract milestones, blockers, and open questions into a standard table. |
| Input boundary | Use only the notes; remove personal details that are not needed for the project update. |
| Expected AI output | Table with milestone, status, blocker, owner, evidence, and `needs_confirmation`. |
| Human reviewer | Project lead. |
| Exception route | If notes conflict or an owner is absent, flag the row and send it to the project lead. |
| Success measure | Fewer omitted blockers and less time spent preparing updates. |
