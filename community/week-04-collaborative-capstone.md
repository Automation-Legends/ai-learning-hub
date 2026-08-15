# Week 4 Capstone — Build a Community Resource Review Assistant

## Capstone mission

In Week 4, beginner members and intermediate builders collaborate on a real-world automation tool for the Automation Legends community: a **Community Resource Review Assistant**. The tool helps prepare a structured review draft when someone suggests an AI-learning resource. It does not publish content, approve a resource, access private data, or make final decisions. A human moderator remains responsible for every external action.

> **Capstone principle:** The team is not building an autonomous publisher. It is building a transparent, draft-and-review workflow that makes community knowledge easier to organize and evaluate.

## The real-world problem

Community members discover useful guides, tools, tutorials, and examples. Without a consistent intake process, good suggestions can be lost, duplicate resources can accumulate, and weak or unsupported claims can be shared too quickly. The capstone creates a repeatable process that turns an authorized suggestion into a clear draft for moderator review.

| Current challenge | Capstone response |
|---|---|
| Suggestions arrive in different formats | Use a simple, structured intake form or test spreadsheet row. |
| Resource quality is difficult to assess quickly | Create a review draft with summary, tags, source questions, and concerns. |
| AI may invent facts or endorse a source too strongly | Require uncertainty flags and prohibit publication decisions. |
| Sensitive or incomplete submissions may appear | Route exceptions to a human; do not process or publish them automatically. |
| Different members have different skill levels | Pair beginner research, prompt, and testing roles with intermediate workflow and API roles. |

## Team roles

Every member contributes meaningful work. Teams of three to six people work well, but the roles may be combined for smaller groups.

| Role | Beginner contribution | Intermediate contribution | Shared responsibility |
|---|---|---|---|
| **Community researcher** | Defines what makes a resource useful to a learner and drafts a simple review rubric. | Helps translate the rubric into structured fields. | Keeps the learner need visible. |
| **Prompt designer** | Writes and tests plain-language instructions and examples. | Converts the prompt into a reusable, versioned workflow step. | Requires clear output and uncertainty flags. |
| **Workflow builder** | Maps the member experience and identifies confusing steps. | Configures the trigger, input validation, AI action, review queue, and exception route. | Limits the system to a draft-and-review scope. |
| **Quality reviewer** | Tests normal and confusing examples from a learner’s perspective. | Runs the five-case evaluation and records failure patterns. | Approves no output automatically. |
| **Documentarian** | Creates a short user guide and explains the workflow in plain language. | Records technical boundaries, credentials policy, and fallback process. | Publishes only sanitized documentation. |
| **Moderator owner** | Explains the community standard and review expectations. | Confirms the approval and escalation process. | Owns final decisions and future maintenance. |

## Four-session capstone plan

The capstone can run over four days, four weekly meetings, or one structured sprint. Each session should finish with a visible artifact.

| Session | Focus | Activities | Deliverable |
|---|---|---|---|
| **1. Discover** | Define the problem and boundaries | Review the mission, choose roles, write the user journey, define what the workflow must never do, and agree on a resource-review rubric. | One-page project brief and review rubric. |
| **2. Build** | Create the draft-and-review workflow | Map trigger, inputs, output schema, prompt, review queue, and exception path. Use safe sample data only. | Workflow canvas, versioned prompt, and output contract. |
| **3. Test** | Evaluate and improve | Run the typical, incomplete, ambiguous, boundary, and messy cases. Record corrections and make one focused improvement. | Completed evaluation sheet and revised workflow. |
| **4. Demonstrate** | Share, reflect, and hand off | Show the workflow with a safe example, explain human review, state limits, and document the next responsible improvement. | Five-minute demo, project showcase, and maintenance note. |

## Project contract

Complete this contract before connecting any automation platform or API.

| Field | Team decision |
|---|---|
| **Project name** | Community Resource Review Assistant |
| **User** | Community member suggesting a public AI-learning resource; moderator reviewing the suggestion |
| **Trigger** | A member submits an authorized resource title, public URL, and short description |
| **Minimum input** | Title, URL, description, optional suggested category; no credentials, private data, or unnecessary personal information |
| **AI-assisted step** | Create a structured draft: short summary, suggested tags, questions to verify, concerns, and `needs_review` value |
| **Human reviewer** | Named Automation Legends moderator or maintainer |
| **Output destination** | A private review queue, issue, spreadsheet, or dashboard—not a public page |
| **Approval rule** | A moderator confirms the source, description, tags, and suitability before publication |
| **Exception path** | Missing, suspicious, unrelated, private, or unclear submissions are routed for manual review or rejected |
| **Disallowed actions** | Publishing, deleting content, purchasing, contacting people, or accessing private accounts without separate authorization |
| **Success measures** | Clear review drafts, lower moderator preparation time, visible source questions, and no automatic publication |

## Build the workflow

### 1. Design the intake

Create a simple form, spreadsheet row, or manual test object. Keep it minimal. The project should collect only what the review process needs.

```text
Resource title: [required]
Public URL: [required]
Submitter description: [required]
Suggested category: [optional]

Confirmation: “I am authorized to share this public link and description.”
```

### 2. Define the output contract

A structured output makes review fast and makes missing information visible.

```json
{
  "summary": "A concise description based only on the supplied information.",
  "suggested_tags": ["prompting", "beginner"],
  "verification_questions": ["Does the source identify an author and update date?"],
  "concerns": ["The description makes a result claim that needs evidence."],
  "needs_review": true
}
```

### 3. Use a review-safe prompt

```text
# Purpose
Prepare a review draft for a proposed public AI-learning resource.

# Rules
- Use only the submitted title, public URL, description, and category.
- Do not state that the resource is accurate, safe, current, endorsed, or suitable.
- Do not invent an author, price, feature, result, source content, or update date.
- If required information is missing, conflicting, suspicious, or unclear, set needs_review to true.
- Do not make a publication decision or contact the submitter.

# Input
<resource_suggestion>
Title: [title]
URL: [url]
Description: [description]
Suggested category: [category]
</resource_suggestion>

# Output
Return the required JSON schema only.
```

### 4. Add human approval

Place every draft in a moderator-owned review queue. The moderator can edit, approve, reject, or request more information. The automation must never add an item to a public resource list by itself.

### 5. Record a minimal audit trail

Record the submission source, workflow version, reviewer decision, reason for rejection or escalation, and date of review. Do not retain information that is unnecessary for the review process.

## Test before demonstration

Use the [Evaluation Sheet](../templates/evaluation-sheet.md) to test the workflow. The team must explain what happens when information is incomplete or unreliable.

| Test case | Sample condition | Expected safe behavior |
|---|---|---|
| **Typical** | A clear title, public URL, and concise description | Creates a review draft and marks it for moderator review. |
| **Incomplete** | Missing URL or description | Stops the normal flow and identifies the missing field. |
| **Ambiguous** | Promotional language without evidence | Lists verification questions and avoids endorsement. |
| **Boundary** | Private, sensitive, unrelated, or potentially unsafe content | Routes the item for manual review; does not process or publish it. |
| **Messy** | Conflicting details, very long text, or strange formatting | Preserves uncertainty and flags the submission instead of guessing. |

## Demonstration format

Each team receives five minutes to demonstrate the capstone. Use fictional or authorized public data only.

| Minute | What to show |
|---:|---|
| **0–1** | The community problem and the team’s user-centered goal. |
| **1–2** | The workflow map, the input boundary, and the human-review step. |
| **2–3** | One safe test submission and the structured review draft. |
| **3–4** | One failure or exception case and how the workflow stopped safely. |
| **4–5** | What the team learned, the next improvement, and what will remain human-owned. |

## Capstone completion checklist

- [ ] Our team wrote a project contract before building.
- [ ] We named a human reviewer and an exception route.
- [ ] We used only fictional, anonymized, or authorized public test data.
- [ ] We created a structured output that flags uncertainty.
- [ ] We tested at least five representative cases.
- [ ] We documented one failure and one focused improvement.
- [ ] We did not expose credentials, private data, or unapproved sources.
- [ ] We did not configure automatic public publishing or another consequential action.
- [ ] We delivered a short demo and a sanitized [Project Showcase](../templates/project-showcase.md).
- [ ] We described one responsible next step and one limitation that remains.

## Assessment rubric

| Criterion | Emerging | Ready | Strong |
|---|---|---|---|
| **Problem definition** | The task is vague or tool-first. | The team names a practical community problem. | The team connects the problem to a clear learner or moderator need. |
| **Safety boundaries** | Boundaries are missing. | Inputs, review, and exceptions are documented. | Boundaries are tested and explain why specific actions remain human-owned. |
| **Collaboration** | Roles are unclear. | Beginner and intermediate contributions are visible. | The team uses each role to improve the workflow and documentation. |
| **Workflow quality** | The flow is incomplete or untestable. | The flow has trigger, output, review, and fallback. | The flow is structured, observable, and includes useful error handling. |
| **Evaluation** | Only a happy-path result is shown. | Five representative tests are recorded. | Failures lead to a specific, evidence-based improvement. |
| **Reflection** | The team only describes success. | The team names a limitation and next step. | The team explains how learning will improve the next community resource or workflow. |

## Recognition and next steps

Teams may use the [Week 1 and 2 Completion Badge System](week-1-and-2-completion-badges.md) to document individual learning progress. The Week 4 capstone is a team experience; it does not require a live public deployment. A completed design, tested prototype, and honest reflection are valuable outcomes.

When a capstone team decides to continue, expand cautiously. Review the evaluation data, confirm source governance and access rules, appoint an owner, add monitoring, and release only a small, reversible version with moderator approval.
