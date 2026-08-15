# Intermediate 3 — Evaluation and Safeguards

## Goal

By the end of this module, you will be able to define what success means for an AI workflow, test it with representative cases, measure errors, and set practical safeguards for exceptions and higher-risk situations.

## Define success before tuning

Do not judge a workflow by whether one example looked impressive. Decide what a successful result means before you change the prompt or model. A simple evaluation gives you a repeatable way to compare versions and notice regressions.

> **A workflow is reliable when it performs well on representative cases and fails safely when it cannot.**

This approach aligns with primary-source guidance to establish success criteria and ways to test them before refining prompts. [1]

## Select success criteria

Use measures that match the workflow’s real purpose. Keep the first evaluation small and observable.

| Workflow purpose | Possible success criterion | Possible failure signal |
|---|---|---|
| Summary or extraction | Required facts are captured accurately | Important item omitted or invented |
| Classification | Category matches the review standard | Misclassification affects the next action |
| Drafting | Draft meets the brief and needs minimal correction | Wrong tone, unsupported claim, or missing section |
| Information routing | Correct reviewer receives a clear, complete item | Item is sent to the wrong queue or lacks key context |
| Structured output | All required fields are present in the requested format | Invalid structure, guessed field, or missing exception flag |

## Build a five-case test set

Create a compact set of examples that represents real conditions. Do not use live confidential data unless you are authorized and the environment is approved. Use sanitized or fictional cases when possible.

| Test case | Why it matters |
|---|---|
| **Typical case** | Confirms the workflow can handle the normal task. |
| **Incomplete case** | Checks that it flags missing data instead of guessing. |
| **Ambiguous case** | Checks that it describes uncertainty and asks for review. |
| **Boundary case** | Checks that it follows a non-negotiable rule or exclusion. |
| **Adversarial or messy case** | Checks resilience to conflicting, irrelevant, or badly formatted input. |

Use the [evaluation sheet](../templates/evaluation-sheet.md) to document the expected outcome, actual outcome, reviewer decision, and improvement idea for each case.

## Safeguards that matter

A safeguard is a planned control that reduces harm when the workflow encounters uncertainty, sensitive information, unexpected input, or a consequential decision. The appropriate safeguard depends on the use case, but most early workflows benefit from clear data boundaries, visible review, and a stop path.

| Safeguard | What it does | Example |
|---|---|---|
| **Data minimization** | Limits the information sent to the AI step | Pass only the support request text, not the full customer record. |
| **Structured output** | Makes omissions and deviations easier to detect | Require a fixed table with a `needs_review` field. |
| **Human approval** | Keeps a person responsible before an external action | A coordinator approves each drafted reply before it is sent. |
| **Exception routing** | Stops automation when information is missing or unclear | Send low-confidence or contradictory cases to a review queue. |
| **Audit trail** | Records input source, prompt version, output, and decision | Store a review log without retaining unnecessary sensitive content. |
| **Fallback process** | Keeps work moving when the AI step fails | Use the existing manual procedure when the service is unavailable. |

NIST’s AI Risk Management Framework is a voluntary framework for incorporating trustworthiness considerations in AI design, development, use, and evaluation. [2]

## Activity — Evaluate a prompt version

Run your Module 2 prompt on five representative cases. Score each case using a three-point scale: **pass**, **needs revision**, or **unsafe/unusable**. For any failure, identify whether the cause is a missing rule, poor input quality, an unclear success criterion, an inappropriate task boundary, or a need for human escalation.

Then make **one** change to create version 1.1. Run the same five cases again and compare the results. Avoid changing several variables at once; you want to understand which change helped.

## Completion check

You have completed this module when you have a five-case test set, written success criteria, a completed evaluation sheet, one documented prompt revision, and an exception path for outputs that should not proceed automatically.

## Reflection

Which failure was most surprising? Which safeguard would have caught it earliest? Does the workflow need a narrower task boundary rather than a more complex prompt?

## Continue

Now turn your evaluated workflow into a build-ready plan: [Build an AI automation](04-build-an-ai-automation.md).

## References

[1]: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview "Anthropic — Prompt engineering overview"
[2]: https://www.nist.gov/itl/ai-risk-management-framework "NIST — AI Risk Management Framework"
