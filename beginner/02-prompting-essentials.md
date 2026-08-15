# Beginner 2 — Prompting Essentials

## Goal

By the end of this module, you will be able to turn a vague request into a clear prompt that gives an AI assistant enough direction to produce a useful first draft.

## The five-part prompt

A strong everyday prompt usually answers five questions. You do not need every part every time, but adding the missing information is the fastest way to improve a weak result.

| Part | Question to answer | Example |
|---|---|---|
| **Goal** | What should the AI help you accomplish? | Create a meeting agenda. |
| **Context** | What background does it need? | The meeting is for a volunteer team planning a community event. |
| **Constraints** | What limits or rules matter? | Keep it to 30 minutes and do not invent dates or budgets. |
| **Output format** | What should the result look like? | Use a table with agenda item, owner, and time. |
| **Quality check** | How should uncertainty or missing information be handled? | Ask me two questions before drafting if key details are missing. |

This structure reflects widely used prompting guidance: clearer instructions, relevant context, and examples or requested formats make it easier for a model to produce an output you can review and use. [1]

## From vague to useful

| Vague request | Improved prompt |
|---|---|
| “Write an email about our event.” | “Draft a friendly email inviting volunteers to our community clean-up. The event is Saturday, 10:00–12:00. Keep the email under 180 words, include a subject line and a three-item checklist of what to bring. Do not invent a location; use `[location]` as a placeholder.” |
| “Help me study biology.” | “Create ten practice questions about photosynthesis for a high-school learner. Use a mix of multiple-choice and short-answer questions. Put answers after the questions and explain each answer in one sentence.” |
| “Make this better.” | “Rewrite the text below for a professional but warm tone. Preserve all facts, reduce it to 120 words or fewer, and list any unclear claims that need my confirmation.” |

## Activity — Improve three prompts

Choose three real tasks. Draft a prompt for each task using the [prompt template](../templates/prompt-template.md). Run each prompt, inspect the output, and improve the prompt once. Keep both versions so you can see which added detail made the largest difference.

### Starter prompt

```text
Goal: [What I want to accomplish]
Context: [Background the AI needs]
Constraints: [Rules, limits, exclusions]
Output: [Format, length, audience, tone]
Quality check: [Ask questions, mark assumptions, cite sources, or flag uncertainty]
```

## Prompt improvement moves

When the first answer is not useful, do not start over with a longer request by default. Identify the missing direction and make one deliberate change.

| Problem | Improvement move |
|---|---|
| The output is too general | Add the audience, purpose, and success criteria. |
| The output is too long or too short | Specify the length, sections, and exact format. |
| The output makes assumptions | Tell the AI to list assumptions or ask questions first. |
| The tone is wrong | Name the audience and provide a small example of the desired voice. |
| The output misses key details | Add reference material or a concise checklist of must-include items. |

## Completion check

You have completed this module when you can explain how the goal, context, constraints, and output format change the result, and you have improved at least three prompts using those elements.

## Reflection

Which prompt change gave you the biggest improvement: more context, a clearer format, a constraint, or a question-first instruction? Why?

## Continue

A well-written prompt can still produce a wrong answer. Next, learn how to review outputs: [Verify before you trust](03-verify-before-you-trust.md).

## References

[1]: https://developers.openai.com/api/docs/guides/prompt-engineering "OpenAI — Prompt engineering"
