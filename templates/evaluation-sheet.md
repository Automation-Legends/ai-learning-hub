# Evaluation Sheet

Use this sheet to test an AI-assisted task against representative examples. An evaluation does not need to be large to be useful. Start with five cases, define what success means, review every output, and make one deliberate improvement at a time.

## Workflow and version

| Field | Value |
|---|---|
| Workflow name |  |
| Owner |  |
| Prompt or workflow version |  |
| Date evaluated |  |
| Reviewer |  |
| Success criteria |  |
| Approval rule |  |
| Exception rule |  |

## Test cases

| Case | Type | Input description | Expected result | Actual result | Score | Reviewer notes | Improvement idea |
|---|---|---|---|---|---|---|---|
| 1 | Typical |  |  |  | Pass / Needs revision / Unsafe |  |  |
| 2 | Incomplete |  |  |  | Pass / Needs revision / Unsafe |  |  |
| 3 | Ambiguous |  |  |  | Pass / Needs revision / Unsafe |  |  |
| 4 | Boundary |  |  |  | Pass / Needs revision / Unsafe |  |  |
| 5 | Messy or adversarial |  |  |  | Pass / Needs revision / Unsafe |  |  |

## What the scores mean

| Score | Meaning | Required action |
|---|---|---|
| **Pass** | The output meets the defined success criteria and followed the required guardrails. | Keep the result as evidence; continue testing. |
| **Needs revision** | The output is usable only after material correction, clarification, or restructuring. | Diagnose the cause and make a focused improvement. |
| **Unsafe** | The output invents material facts, violates a boundary, misroutes a consequential item, or would cause harm if used as intended. | Stop the normal flow, route for human review, and revise the task boundary or safeguards. |

## Evaluation summary

| Measure | Result |
|---|---|
| Pass rate |  |
| Needs-revision rate |  |
| Unsafe/unusable count |  |
| Common failure pattern |  |
| Safeguard that caught the issue |  |
| Safeguard still missing |  |
| Change to test next |  |
| Decision | Continue / revise / narrow scope / pause |

## Improvement discipline

Change one important variable at a time when possible: the task boundary, instructions, output schema, example, input preparation, human-review rule, or exception condition. Then rerun the same test set. This creates evidence for whether the change helped rather than relying on a single impressive example.

## Review reminder

For tasks involving safety, health, finances, legal rights, employment, access to services, or a person’s reputation, use review standards appropriate to the real-world consequence. AI output should support—not replace—authorized human judgment.
