# Week 1 and Week 2 Completion Checklist and Badge System

This interactive system helps Automation Legends members turn learning into visible progress. Complete the checklists, share a **sanitized** reflection, and request a maintainer review. Badges recognize completed practice; they are not a professional certification, a guarantee of technical skill, or authorization to deploy an automation without appropriate review.

> **Recognition principle:** Evidence matters more than perfection. A member earns a badge by showing a thoughtful process, clear boundaries, and honest reflection—not by producing an impressive-looking output alone.

## Available badges

| Badge label | Meaning | How to earn it |
|---|---|---|
| **`badge: week-1 explorer`** | You completed the foundational AI-learning practices. | Complete the Week 1 checklist and share a sanitized reflection. |
| **`badge: week-2 workflow builder`** | You designed and tested a safe, reviewable automation workflow. | Complete the Week 2 checklist and share a workflow summary plus test evidence. |
| **`badge: learning-hub pathfinder`** | You completed both Week 1 and Week 2 and connected the habits across a real project. | Earn the first two badges and submit a short project reflection. |

Maintainers apply the labels to an approved badge-claim issue or discussion. A badge remains associated with the contribution that shows the learning evidence.

## How to use this checklist

1. Work through the linked learning materials at your own pace.
2. Check a box only after you have completed the practice activity.
3. Share a safe summary: use fictional, anonymized, or explicitly authorized examples. Never include credentials, private data, client details, or information you are not allowed to share.
4. Open a [badge-claim issue](https://github.com/Automation-Legends/ai-learning-hub/issues/new/choose) or community discussion using the template below.
5. A maintainer checks that the reflection demonstrates the required learning habits and then applies the relevant label.

## Week 1 — Explorer checklist

Week 1 focuses on foundations, prompt clarity, verification, and a first practical project.

- [ ] I read the [New-Member Onboarding Guide](new-member-onboarding.md) and the [Code of Conduct](../CODE_OF_CONDUCT.md).
- [ ] I completed [AI Foundations](../beginner/01-ai-foundations.md) and wrote personal rules for privacy, verification, and accountability.
- [ ] I chose one low-risk, real task that I want AI to assist with.
- [ ] I used the [Prompt Template](../templates/prompt-template.md) to write a prompt with a goal, context, constraints, output format, and quality check.
- [ ] I tested the prompt with a safe example and improved it at least once.
- [ ] I completed the SCOPE review activity in [Verify Before You Trust](../beginner/03-verify-before-you-trust.md).
- [ ] I independently checked at least three meaningful claims, numbers, dates, or output details.
- [ ] I completed a small AI-assisted workflow using [Your First AI Project](../beginner/04-first-ai-project.md).
- [ ] I recorded what AI helped with, what I changed or verified myself, and what I would improve next time.
- [ ] I shared a sanitized reflection using the [Project Showcase Template](../templates/project-showcase.md) or the badge-claim template below.

### Week 1 evidence checklist

A Week 1 claim is ready for review when it includes all of the following.

| Required evidence | Example |
|---|---|
| One defined task | “Turn approved weekly notes into a priority list.” |
| One prompt improvement | “I added a table format and `[confirm]` placeholders for missing deadlines.” |
| One review action | “I checked the dates against the source notes and removed an invented task.” |
| One learning reflection | “Next time, I will include audience and tone in the prompt.” |

## Week 2 — Workflow Builder checklist

Week 2 builds on Week 1. It focuses on workflow design, APIs, webhooks, credential safety, structured outputs, and test cases.

- [ ] I completed [Week 2: Automation Workflows and APIs](../intermediate/week-02-automation-workflows-and-apis.md).
- [ ] I mapped one recurring task using the [Workflow Canvas](../templates/workflow-canvas.md).
- [ ] I defined the trigger, authorized input, bounded AI transformation, expected output, human reviewer, destination, and fallback.
- [ ] I can explain the difference between an API request and a webhook in my own words.
- [ ] I identified the least-privilege credential or permission the workflow would need, without sharing an actual secret.
- [ ] I documented where the credential would be stored safely, such as an approved secret manager or platform credential store.
- [ ] I wrote a structured output contract that makes the AI result easy to review.
- [ ] I defined at least one exception that stops the normal flow and routes the item for human review.
- [ ] I tested the design with typical, incomplete, ambiguous, boundary, and messy inputs using the [Evaluation Sheet](../templates/evaluation-sheet.md).
- [ ] I recorded at least one workflow improvement based on a test result.
- [ ] I shared a sanitized workflow summary and named the human-review step.

### Week 2 evidence checklist

A Week 2 claim is ready for review when it includes all of the following.

| Required evidence | Example |
|---|---|
| Workflow statement | “When a resource suggestion arrives, create a review draft for a moderator.” |
| Boundaries | “The workflow uses only title, link, and description; it does not access private member data.” |
| Review step | “A moderator approves every draft before publication.” |
| Exception path | “Missing or suspicious sources enter a manual-review queue.” |
| Test result | “An incomplete input was flagged instead of receiving an invented summary.” |
| Improvement | “I added a required `needs_review` field to the output.” |

## Pathfinder recognition

After earning the Week 1 Explorer and Week 2 Workflow Builder badges, you may request the **Learning Hub Pathfinder** badge. This badge recognizes that you connected foundational prompting and verification habits to a repeatable workflow design.

To request it, include the following in your claim:

- [ ] Links to or references for the Week 1 and Week 2 evidence.
- [ ] A short description of how the Week 1 review habit changed the Week 2 workflow.
- [ ] One remaining limitation or risk you would address before any live deployment.
- [ ] One way you will help another community member learn from your experience.

## Badge-claim template

Use the [guided GitHub badge-claim form](https://github.com/Automation-Legends/ai-learning-hub/issues/new/choose) when available, or copy this template into a new issue or community discussion. Remove or replace any sensitive information before posting.

```text
## Badge requested
[ ] Week 1 Explorer
[ ] Week 2 Workflow Builder
[ ] Learning Hub Pathfinder

## My project or learning task
[One or two sentences]

## What I completed
[Brief list of the checklist items completed]

## Safe evidence
[Link to a sanitized project showcase, workflow canvas, evaluation summary, or clearly described example]

## What I verified or changed myself
[One or more specific review actions]

## Boundaries and human review
[What data was excluded, who reviews the result, and what stops automation]

## What I learned
[One concise reflection]

## What I will improve next
[One specific next step]
```

## Maintainer review checklist

Maintainers apply a badge only after confirming that the claim demonstrates the appropriate level of practice. The review should be constructive, short, and consistent.

| Review question | Week 1 | Week 2 |
|---|---|---|
| Is the member’s example safe to share? | Required | Required |
| Is the learning task concrete and appropriately scoped? | Required | Required |
| Did the member show a verification or correction step? | Required | Required |
| Did the member identify a limitation or uncertainty? | Required | Required |
| Is there a named human-review or escalation point? | Encouraged | Required |
| Did the member test exceptions or edge cases? | Encouraged | Required |
| Is the reflection honest and sufficiently specific? | Required | Required |

If a claim is incomplete, a maintainer should explain the missing evidence and invite the member to update it. The goal is to help members finish the learning loop, not to reject early attempts.

## Suggested GitHub labels

| Label | Color | Description |
|---|---|---|
| `badge: week-1 explorer` | `0E8A16` | Completed Week 1 foundations, prompting, verification, and a first AI-assisted project. |
| `badge: week-2 workflow builder` | `1D76DB` | Completed Week 2 workflow design, API safety, exception planning, and tests. |
| `badge: learning-hub pathfinder` | `5319E7` | Completed Week 1 and Week 2 with a connected project reflection. |
| `status: badge review` | `FBCA04` | A maintainer review is needed before a badge is applied. |

## Share your progress

A badge claim becomes more useful when it teaches another member something. Share one clear prompt improvement, one workflow safeguard, one test result, or one limitation you discovered. This turns recognition into a reusable community resource.
