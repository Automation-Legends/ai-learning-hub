# Beginner 4 — Your First AI Project

## Goal

By the end of this module, you will convert one recurring task into a small AI-assisted workflow that saves effort while preserving human review.

## Choose a safe, useful project

Pick a task that is frequent enough to matter but low-risk enough to experiment with. Your project should have a clear before-and-after state. Avoid projects that require sharing confidential data or making important decisions without human review.

| Good first project | AI-assisted step | Human review step |
|---|---|---|
| Weekly meeting preparation | Turn notes into an agenda and action list | Confirm owners, deadlines, and missing topics |
| Study guide creation | Create questions from your approved notes | Check answers against course material |
| Content planning | Generate a month of draft topic ideas | Select topics and verify factual claims before publishing |
| Customer-feedback sorting | Categorize anonymized feedback into themes | Review categories and decide what action to take |
| Job-search organization | Turn your own experience into draft accomplishment bullets | Ensure every statement is accurate and truthful |

## Project method: MAPS

Use **MAPS** to keep the project focused.

| Step | Question | Deliverable |
|---|---|---|
| **M — Map the current task** | What triggers it, what inputs does it use, and what does “done” look like? | A three- to five-step description of the current process |
| **A — Assist one step** | Which drafting, organizing, or transformation step could AI help with? | A clear AI task boundary |
| **P — Prompt and protect** | What prompt, data boundary, and output format are needed? | A reusable prompt and privacy check |
| **S — Score the result** | How will you know whether it actually improved the task? | A short comparison of quality, time, and review effort |

## Activity — Build the workflow

Use the steps below for a task you selected in Module 1.

### 1. Describe the current process

Write the trigger, inputs, actions, final output, and the person responsible for reviewing the work. Keep the description short and specific.

### 2. Select one AI-assisted step

Start with a single step, such as drafting an outline, extracting action items from approved notes, grouping feedback themes, or converting source material into practice questions. Do not attempt to automate every step at once.

### 3. Create a reusable prompt

Use the [prompt template](../templates/prompt-template.md). Include exact rules about what the AI must not invent, the output format, and what uncertainty it should flag.

### 4. Test with two examples

Try the prompt on two representative, non-sensitive examples. Compare the AI-assisted output with the way you previously completed the task. Check facts and important details.

### 5. Record the result

Use the [project showcase template](../templates/project-showcase.md) to note what changed. Measure a meaningful signal such as time saved, fewer missed steps, clearer structure, or better preparation for human review.

## Example project brief

| Field | Example |
|---|---|
| Problem | Weekly volunteer meetings begin without a consistent agenda. |
| AI-assisted step | Convert approved coordinator notes into a 30-minute agenda draft. |
| Inputs | Anonymized notes from the coordinator. |
| Output | Table with agenda item, objective, owner, and timebox. |
| Guardrails | Do not invent decisions, names, dates, or deadlines; mark missing owners as `[confirm owner]`. |
| Human review | Coordinator confirms all items before sharing the agenda. |
| Success measure | Agenda preparation takes less time and has fewer missing action items. |

## Completion check

You have completed the Beginner Path when you have documented one AI-assisted workflow, tested it with two examples, completed a human review, and recorded what you would improve next.

## Reflection

What did AI make faster or clearer? What still required your judgment? What guardrail would you add before using this workflow again?

## Next step

When you are ready to make your workflow more reliable and repeatable, begin the [Intermediate Path](../intermediate/README.md).
