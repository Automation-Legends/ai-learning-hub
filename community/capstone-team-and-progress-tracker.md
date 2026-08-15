# Capstone Team and Progress Tracker

The capstone tracker uses GitHub issues to make team formation, artifact ownership, safe testing, blockers, and demonstration readiness visible. It is a coordination aid—not a grading system or a substitute for human facilitation.

> **Tracker boundary:** Automation creates orientation labels and comments. Maintainers decide team membership, move status labels, review evidence, approve credentials, and confirm project completion.

## Start a capstone team

1. Open the [Capstone Team Formation](../.github/ISSUE_TEMPLATE/capstone-team-formation.md) issue template.
2. Give the team a clear name and list every participant with one role and one initial artifact.
3. Record the project contract: trigger, minimum input, AI-assisted task, structured output, human reviewer, destination, stop conditions, and disallowed actions.
4. Assign owners for the five required test cases.
5. The tracker adds **`status: capstone team forming`** and posts an orientation comment.
6. A maintainer checks that roles, scope, and the human-review boundary are clear. The maintainer can then apply **`status: capstone active`**.

## Record progress

Open a [Capstone Progress Update](../.github/ISSUE_TEMPLATE/capstone-progress-update.md) issue for a substantial milestone, such as a completed project contract, test-set review, workflow revision, or demo preparation. Link the team-formation issue so the project record remains connected.

A good progress update shows what was completed, who owned it, the result of the five tests, one blocker or decision request, and the next focused milestone. The tracker adds **`status: capstone review`** and an orientation comment. A maintainer then reviews the evidence and changes labels deliberately.

## Status labels

| Label | Maintainer use |
|---|---|
| `type: capstone team` | Identifies the team-formation record. |
| `type: capstone progress` | Identifies a linked milestone or progress update. |
| `status: capstone team forming` | Roles, artifact owners, and the initial project contract are being confirmed. |
| `status: capstone active` | The team is actively building and testing. |
| `status: capstone blocked` | A decision, resource, handoff, or facilitator review is needed. |
| `status: capstone review` | Evidence is ready for facilitator or maintainer review. |
| `status: capstone ready to demo` | The project has a safe demonstration plan and clear limitations. |
| `status: capstone complete` | A maintainer has confirmed that the project record meets the capstone completion standard. |

## Suggested status flow

```text
Team forming → Active → Review → Ready to demo → Complete
                     ↘ Blocked → Active
```

Apply only the status that best describes the current project state. Remove obsolete statuses when the team moves forward. Keep the `type:` label throughout the project.

## What the tracker does automatically

| Event | Automated action |
|---|---|
| A team-formation issue opens or receives `type: capstone team` | Adds `status: capstone team forming` and posts a setup reminder. |
| A progress-update issue opens or receives `type: capstone progress` | Adds `status: capstone review` and posts an evidence-and-safety reminder. |
| Any other issue | No tracker action. |

The tracker does **not** form a team, select a project, evaluate test quality, assign a score, award a credential, or declare a team complete. Those decisions remain with community members and maintainers.

## Safe collaboration rules

- Use only fictional, anonymized, or authorized public examples in issues.
- Do not place private documents, credentials, client information, or sensitive personal data in a team or progress issue.
- Record limitations and failures as useful learning evidence.
- Request help using the smallest relevant context; link a safe artifact rather than copying unnecessary content.
- Keep every workflow in the capstone’s draft-and-review boundary. No automation may publish, purchase, delete, contact people, or make final decisions without a separate, reviewed design.

## Preparing for demonstration

Before a maintainer applies **`status: capstone ready to demo`**, confirm that the team can show the problem, contract, role contributions, one typical test, one failure or boundary case, the human-review step, one improvement, one limitation, and one next responsible action.

Use the [feedback and grading rubric](week-04-capstone-feedback-and-grading-rubric.md), [capstone FAQ](week-04-capstone-faq.md), and [project showcase template](../templates/project-showcase.md) to prepare the evidence.
