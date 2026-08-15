# Week 2 — Automation Workflows and APIs

## Goal

By the end of Week 2, you will be able to describe a safe automation workflow, explain the basic role of an API and a webhook, identify where credentials belong, and prepare a small **draft-and-review** automation for a real task.

This module is for intermediate members who already know how to write a prompt and want to connect work across tools without losing human judgment. You do not need to code to complete the planning exercises. If you do write code, begin with a low-risk, read-only request and never place an API key in public code, a browser-only application, a screenshot, or a community post.

> **Week 2 principle:** Automate a narrow, repeatable transformation. Keep people responsible for approvals, exceptions, high-impact decisions, and anything that leaves your system.

## What you will build this week

| Outcome | What it means |
|---|---|
| **Workflow map** | A visible description of the trigger, input, AI step, output, review, destination, and fallback. |
| **API request sketch** | A plain-language description of the service, endpoint, method, input, output, and permission needed. |
| **Safety plan** | A decision about what data may be sent, where credentials are stored, and which outcomes stop for human review. |
| **Five-case test set** | Typical, incomplete, ambiguous, boundary, and messy inputs that test whether the workflow fails safely. |

## Part 1 — Understand the workflow before connecting tools

An automation workflow turns a repeatable event into a sequence of controlled steps. The basic pattern is not “AI does everything.” It is **trigger → preparation → bounded transformation → review → destination → monitoring**.

| Component | Question to answer | Community example |
|---|---|---|
| **Trigger** | What event starts the work? | A member submits a resource suggestion form. |
| **Preparation** | What authorized, minimal information is needed? | The title, link, short description, and category—not private member data. |
| **AI transformation** | What narrow task can AI assist with? | Create a concise summary and suggest tags. |
| **Output contract** | What must the result look like? | A table with title, summary, tags, source link, and `needs_review`. |
| **Human review** | Who checks, edits, or approves it? | A community moderator. |
| **Destination** | Where does an approved item go? | A repository issue, discussion draft, or resource backlog. |
| **Exception path** | What stops the normal flow? | Missing source, unclear claim, sensitive information, or low-quality output. |
| **Measure** | How will you know it helps? | Moderator review time, correction rate, and number of valid submissions. |

Start with the [Workflow Canvas](../templates/workflow-canvas.md). If the task cannot be described clearly before automation, it is not ready to be connected to an API.

## Part 2 — APIs in plain language

An **API**, or application programming interface, is a documented way for one system to request information or ask another system to perform an authorized action. GitHub’s REST API, for example, supports integrations that retrieve data and automate workflows. [1]

A typical API request has the following parts.

| Part | Plain-language meaning | Example |
|---|---|---|
| **Endpoint** | The specific address for one type of resource or action | `https://api.github.com/repos/Automation-Legends/ai-learning-hub` |
| **Method** | The kind of request | `GET` reads data; `POST` creates something; `PATCH` updates something; `DELETE` removes something. |
| **Headers** | Context sent with the request | Content type, API version, or authorization information. |
| **Parameters or body** | The specific input the service needs | A search term, form fields, or JSON data. |
| **Response** | What the service sends back | A status code and usually structured data such as JSON. |
| **Permission** | The access granted to the request | Read-only access, specific project access, or another limited scope. |

### A read-only API example

The following request asks GitHub’s public API for basic information about this repository. It does not create, change, or delete anything.

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/Automation-Legends/ai-learning-hub
```

Read the response as data. Look for fields such as the repository name, description, default branch, and visibility. This is a useful first experiment because it teaches the request-and-response pattern without requiring a secret or changing a system.

## Part 3 — Webhooks versus API requests

An API request asks a service for information or an action. A **webhook** sends information to your chosen URL when a subscribed event happens. GitHub describes webhooks as event-driven deliveries that can be used instead of repeatedly polling an API. [2]

| Use case | Better first choice | Why |
|---|---|---|
| You need repository details once | API request | You can ask for the data when you need it. |
| You need to react whenever a new issue is opened | Webhook | The event can notify your system when it occurs. |
| You need a daily digest of approved content | Scheduled workflow plus API request | A scheduled run can fetch only the information needed for the digest. |
| You need a person to approve an AI draft | Workflow with a review queue | The approval should occur before the external action. |

For a first build, it is usually safer to start with a manual trigger or scheduled test run. Add webhooks only after you understand the incoming data, validation, security, and failure behavior.

## Part 4 — The credential rule

An API key or token is a secret that grants access. Treat it like a password. The OpenAI API documentation, for example, states that API keys are secrets and should not be exposed in client-side code; use server-side environment variables or a key-management service instead. [3]

| Do | Do not |
|---|---|
| Store keys in an approved secret manager, environment variable, or automation platform credential store | Paste a key into GitHub, a chat message, a screenshot, or a shared document |
| Grant the narrowest permissions the workflow needs | Use an all-powerful account or a token with unnecessary permissions |
| Rotate or revoke a key if you believe it was exposed | Wait for a problem or assume a public key is harmless |
| Use test data and a low-privilege test account when possible | Test a new workflow on sensitive live records |
| Review the provider’s current documentation, limits, and terms | Assume a tutorial’s pricing, fields, permissions, or behavior are permanent |

## Part 5 — Design a draft-and-review automation

This exercise uses a community resource-suggestion workflow. You can adapt it to your work, study, or project context.

### Workflow statement

```text
When an authorized resource suggestion is submitted, prepare a structured review draft from the title, link, and description. The draft must contain a summary, suggested category, verification questions, and a needs-review flag. A moderator approves or rejects the draft before it is added to the resource backlog. If the source is missing, suspicious, or incomplete, create no public item and route it for manual review.
```

### Step-by-step build plan

| Step | Action | Completion check |
|---|---|---|
| **1. Define the trigger** | Use a manual form submission or a test spreadsheet row. | You can identify exactly when the workflow starts. |
| **2. Minimize the input** | Pass only the title, URL, description, and submitter-approved contact method if needed. | No unnecessary personal or confidential information is included. |
| **3. Validate basic fields** | Check that title and URL exist and that the URL uses a safe expected format. | Missing or malformed entries enter the exception path. |
| **4. Run the AI step** | Ask for a structured summary, tags, limitations, and a `needs_review` value. | The output follows a predictable schema. |
| **5. Create a review queue** | Send the draft to a moderator-owned place, such as a private issue, spreadsheet, or dashboard. | No item is published automatically. |
| **6. Add the approval action** | Let a moderator edit, approve, or reject the draft. | A human is accountable for the external action. |
| **7. Log the result** | Record the input source, workflow version, reviewer decision, and reason for exceptions. | You can evaluate performance later. |
| **8. Test five cases** | Run normal, incomplete, ambiguous, boundary, and messy examples. | You know how the workflow behaves outside the ideal path. |

### Sample AI instruction for the review step

```text
# Purpose
Prepare a review draft for a proposed AI learning resource.

# Rules
- Use only the supplied title, URL, and description.
- Do not claim that the source is accurate, safe, current, or endorsed.
- Do not invent an author, price, result, feature, or source content.
- If the URL, title, or description is missing or unclear, set needs_review to true.
- Do not make a publication decision.

# Input
<resource_suggestion>
Title: [title]
URL: [url]
Description: [description]
</resource_suggestion>

# Output
Return JSON with: summary, suggested_tags, verification_questions, concerns, and needs_review.
```

## Part 6 — Test for safe failure

Use the [Evaluation Sheet](../templates/evaluation-sheet.md) to test the workflow before connecting it to a real destination.

| Test case | Input condition | Expected behavior |
|---|---|---|
| Typical | A clear title, valid URL, and concise description | Creates a structured review draft and marks it for human review. |
| Incomplete | No description or missing URL | Stops the normal flow and flags missing information. |
| Ambiguous | Marketing language with no source details | Lists verification questions and does not endorse the claim. |
| Boundary | A link that appears to contain sensitive or unrelated content | Routes the item for manual review; does not process or publish it. |
| Messy | Conflicting titles, very long text, or unusual formatting | Preserves uncertainty and records an exception instead of guessing. |

## Part 7 — Common workflow errors

| Error | Why it is risky | Better pattern |
|---|---|---|
| Automating a decision instead of a draft | An incorrect output can cause harm or reputational damage. | Automate preparation; require approval before the action. |
| Sending too much data | It increases privacy, compliance, and security risk. | Minimize inputs and remove personal or sensitive details. |
| Hiding a key in the workflow or code | A leak can grant unauthorized access. | Use approved secret storage and least-privilege credentials. |
| Assuming a successful response means a correct result | An API can succeed technically while the output is wrong or incomplete. | Validate outputs, review important fields, and test edge cases. |
| Ignoring errors and rate limits | Requests can fail, be delayed, or exceed service limits. | Capture errors, add a safe fallback, and monitor the workflow. |
| Publishing without a review queue | It removes the chance to correct an AI-generated mistake. | Hold drafts for a named person to approve or reject. |

## Week 2 challenge

Complete a one-page automation design for a real, low-risk task. Do **not** connect any live credentials or publish a workflow until you have completed the test set.

Use the [Workflow Canvas](../templates/workflow-canvas.md), then share a sanitized summary in the community using this format:

```text
Workflow name: [name]
Trigger: [event]
AI-assisted step: [narrow transformation]
Human review: [person or role]
Exception path: [what stops automation]
One test case: [what you tried and what happened]
One question: [where you need feedback]
```

## Completion check

You have completed Week 2 when you can explain the difference between an API request and a webhook, identify where credentials should be stored, show a workflow with a human review step, and document how it behaves for five test cases.

## Continue learning

For a deeper workflow foundation, revisit [Workflow Design](01-workflow-design.md), [Reliable Prompting](02-reliable-prompting.md), and [Evaluation and Safeguards](03-evaluation-and-safeguards.md). When your process is defined, continue to [Build an AI Automation](04-build-an-ai-automation.md).

## References

[1]: https://docs.github.com/en/rest "GitHub Docs — REST API documentation"
[2]: https://docs.github.com/en/webhooks/about-webhooks "GitHub Docs — About webhooks"
[3]: https://developers.openai.com/api/reference/overview "OpenAI API — API Overview"
