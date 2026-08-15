# Advanced Module: Multi-Agent Frameworks and Production Deployment

**Recommended audience:** Members who have completed the four-week AI Learning Hub pathway and can already define a bounded agent contract, retrieval plan, evaluation set, and human-review boundary.

**Estimated effort:** Two focused sessions plus a controlled pilot-design exercise.

> **Module principle:** A production-ready multi-agent system is not a collection of autonomous bots. It is a set of explicitly owned, observable, permission-bounded steps with safe stop conditions and accountable human control.

## What you will learn

By the end of this module, you should be able to decide whether a multi-agent design is justified, describe the responsibilities and permissions of each component, select a production deployment stage, and produce evidence that the system can be monitored, paused, reviewed, and improved.

| Capability | Completion evidence |
|---|---|
| Justify architecture | A one-page decision note explaining why one agent is sufficient or why specialist ownership makes a multi-agent design clearer. |
| Define specialist boundaries | An agent contract table that names each role, allowed inputs, tools, outputs, owner, escalation path, and prohibited actions. |
| Plan production controls | A staged deployment plan covering secrets, access, data minimization, logging, evaluation, cost, latency, incident response, and rollback. |
| Test collaboration safely | An eight-case evaluation set with results, failures, changes, and remaining limitations. |
| Operate responsibly | A named runbook owner, review queue, and release decision for the limited pilot. |

## Prerequisites and boundaries

Complete the [Week 3 custom-agents and vector-databases module](week-03-custom-agents-and-vector-databases.md) and the [Week 4 collaborative capstone](../community/week-04-collaborative-capstone.md) first. This module does not authorize deployment of high-impact systems or autonomous external actions. Use fictional, anonymized, or authorized public material in all exercises.

The capstone’s draft-and-review approach remains the baseline: no component may publish, purchase, delete, contact people, change access, or make a consequential decision without a separately reviewed design and an accountable human owner.

## Part 1 — Decide whether you need more than one agent

Multi-agent systems create coordination overhead. Prefer one well-scoped agent when a single instruction set, tool boundary, and evaluation set can safely handle the work. Add a specialist only when different ownership, tools, permissions, context, or evaluation standards make the workflow easier to understand and control.

| Use one bounded agent when… | Consider specialist agents when… |
|---|---|
| The workflow has one clear owner and one coherent output. | Distinct subproblems need different tools, data access, or approval rules. |
| The same evaluation criteria apply to every step. | Each specialist needs a separate contract and test set. |
| A single review queue can inspect the whole result. | A coordinator must assemble independently verified outputs. |
| Splitting tasks would add latency or obscure responsibility. | A named coordinator can route work without granting every specialist broad authority. |

OpenAI describes two common multi-agent approaches: agents used as tools under a manager and handoffs that transfer response ownership. The Agents SDK runner can manage tool loops, handoffs, approval pauses, state, traces, and evaluations.[1] The right pattern depends on who owns the final response and which component is allowed to act.

## Part 2 — Choose an orchestration pattern

### Pattern A: Coordinator with specialists as tools

A coordinator receives the request, selects a specialist, collects a structured result, and prepares a final draft. The coordinator owns the user-facing response and must not silently turn specialist output into an unreviewed action.

```text
Request → Coordinator → Specialist tool call(s) → Structured evidence → Coordinator draft → Human review
```

Use this pattern when specialists support one accountable owner. For example, a Resource Review Coordinator can call a source-check specialist, a taxonomy specialist, and a policy-check specialist. Each specialist returns evidence and uncertainty; the coordinator assembles a draft for a moderator.

### Pattern B: Explicit handoff

A triage agent routes a request to a specialist that takes responsibility for the next interaction or review step. Use this pattern only when the handoff boundary is observable and the new owner has a narrow, documented mandate.

```text
Request → Triage → Handoff to specialist → Specialist draft → Approval or escalation
```

### Pattern C: State-machine or graph workflow

A graph defines possible states, transitions, stop conditions, retries, and approval interruptions. This is often useful for a production workflow with several asynchronous or resumable steps. LangGraph describes support for single-, multi-agent, and hierarchical control flows, plus memory and human-in-the-loop controls.[3]

### Pattern D: Parallel research with a controlled merge

Run independent read-only specialists in parallel only when their work does not share mutable state and the coordinator can verify disagreements. The merge step must preserve evidence, sources, uncertainty, and conflict rather than choosing the most fluent answer.

> **Do not use a debate loop as a substitute for a policy, test set, or human decision.** More agents do not automatically produce better or safer results.

## Part 3 — Write the multi-agent system contract

Create this contract before selecting a framework or deployment service.

| Component | Required decision |
|---|---|
| User and workflow goal | Who benefits, what task is being completed, and what outcome is useful? |
| Coordinator owner | Who owns routing, final assembly, and the user-facing draft? |
| Specialists | What single capability does each specialist own? |
| Inputs | What is the minimum authorized information each component receives? |
| Tool permission | Which read or action tools may each component invoke? What is explicitly forbidden? |
| State | What may persist across steps, where is it stored, and when is it deleted? |
| Structured output | Which fields must be returned, including sources, confidence limits, and `needs_review`? |
| Human control | Which transition pauses for approval, and who decides? |
| Failure handling | How do timeouts, tool errors, prompt injection, missing inputs, and conflicting outputs stop or escalate? |
| Observability | Which trace, event, latency, cost, tool-call, and review records are retained? |
| Operational owner | Who monitors alerts, changes prompts, approves releases, and can disable the system? |

OpenAI’s practical guide frames an agent around three components—model, tools, and instructions—and recommends clear tool definitions, model baselines, evaluation, and guardrails.[2] Treat each specialist as its own smaller contract rather than inheriting broad authority from the coordinator.

## Part 4 — Reference architecture: Community Resource Publication Planner

Use this **read-only, draft-only** reference project for the exercise. It extends the Week 4 capstone without automating community publication.

```text
Authorized public resource suggestion
        ↓
Intake validator ──→ manual review if missing, private, or out of scope
        ↓
Review coordinator
   ├── Source-check specialist (read-only evidence and missing-source flags)
   ├── Taxonomy specialist (suggested tags with uncertainty)
   └── Policy-check specialist (policy questions and concerns)
        ↓
Structured review packet: summary, sources, tags, concerns, conflicts, needs_review
        ↓
Named moderator reviews, edits, approves, rejects, or escalates
```

### Specialist contract example

| Specialist | Allowed inputs | Allowed tools | Required output | Never allowed to |
|---|---|---|---|---|
| Intake validator | Title, public URL, description, category | Schema check only | Valid / incomplete / out-of-scope with reason | Fetch private links or infer missing facts |
| Source check | Validated public URL and description | Read-only approved-source lookup | Evidence, missing details, source-quality questions | Endorse a resource or publish a verdict |
| Taxonomy | Validated description and source metadata | Approved taxonomy lookup | Suggested tags and uncertainty | Create public categories or modify shared taxonomy |
| Policy check | Draft packet and community policy | Read-only policy retrieval | Policy questions, concerns, escalation flag | Override a moderator or grant approval |
| Coordinator | Structured specialist outputs | Specialist calls only | Review packet with conflicts and `needs_review` | Publish, message users, or suppress disagreement |

## Part 5 — Production deployment ladder

Do not move directly from a working demo to broad production access. Use a staged release with entry and exit criteria.

| Stage | Scope | Required controls before moving forward |
|---|---|---|
| **0. Offline design** | Contract, synthetic examples, no live tools | Named owner, prohibited actions, structured outputs, initial evaluation set |
| **1. Local sandbox** | Fictional or authorized public data, read-only tools | Tests for ordinary and failure cases; trace review; no credentials in code |
| **2. Staging** | Isolated environment and controlled test account | Secret storage, least-privilege access, monitoring, rollback, runbook, alert route |
| **3. Limited pilot** | Small group, draft-only output, mandatory human approval | Release criteria, review queue, feedback path, latency and cost budget, incident owner |
| **4. Controlled production** | Defined eligible users and narrow use case | Ongoing evaluations, version control, audit records, access review, incident drills |
| **5. Expansion decision** | Proposed additional scope or action authority | Evidence that current controls work; new risk review and explicit owner approval |

Production deployment is an operating commitment, not a hosting event. The operational owner must be able to answer: What changed? Which system version ran? Which tools were called? Which approval occurred? What happened when a tool failed? How can the workflow be paused or rolled back?

## Part 6 — Production control checklist

### Access, secrets, and data

- [ ] Give every specialist the narrowest possible tool and data permissions.
- [ ] Store secrets in an approved secret manager or environment configuration; never in prompts, source code, issues, logs, or screenshots.
- [ ] Separate staging from production credentials and data.
- [ ] Minimize inputs, redact sensitive content where appropriate, and define retention and deletion rules.
- [ ] Log an identifier and decision metadata, not unnecessary private prompt content.

### Reliability and operations

- [ ] Define timeout, retry, fallback, and circuit-breaker behavior for every tool.
- [ ] Give each run a trace or correlation identifier across coordinator and specialists.
- [ ] Record structured outputs, tool-call status, latency, model/version, review outcome, and safe error category.
- [ ] Set a latency budget, cost budget, and maximum tool-call or handoff limit.
- [ ] Publish a runbook that names the operational owner, escalation contacts, pause switch, and rollback procedure.

### Evaluation and release control

- [ ] Test typical, incomplete, ambiguous, boundary, messy, contradictory, tool-failure, and prompt-injection cases.
- [ ] Define success measures before selecting a model or framework.
- [ ] Establish a capable-model baseline; then test lower-cost options against the same evaluation set.[2]
- [ ] Compare specialist and coordinator outputs against known-good criteria and record disagreements.
- [ ] Require human approval for release, high-impact transitions, and expansion of tool authority.

## Part 7 — Multi-agent evaluation set

Use the following eight cases for the Community Resource Publication Planner. Add domain-specific cases before a pilot.

| Case | Input condition | Expected safe behavior |
|---|---|---|
| Typical | Clear public resource suggestion | Coordinator prepares a structured review packet with source evidence and `needs_review`. |
| Incomplete | Missing URL or description | Intake validator stops the workflow and requests the missing field. |
| Ambiguous | Broad or promotional claim | Source specialist creates verification questions; coordinator avoids endorsement. |
| Boundary | Private, sensitive, or unauthorized content | Workflow rejects or escalates without passing data to specialists. |
| Messy | Long, conflicting, or malformed text | Preserve uncertainty, identify conflicts, and avoid invented details. |
| Contradictory | Specialists return incompatible tags or concerns | Coordinator exposes the disagreement in the packet and routes it to review. |
| Tool failure | A specialist tool times out or returns an error | Coordinator records the failure, avoids a fabricated substitute, and escalates. |
| Prompt injection | Input asks the system to ignore policy or perform a forbidden action | Treat the text as untrusted content, maintain the contract, and route to review. |

## Part 8 — Framework selection without framework lock-in

Start with the contract and evaluation set, then choose an implementation that makes the boundaries visible.

| Capability | Questions to ask | Example options |
|---|---|---|
| Orchestration | Can the system express coordination, handoffs, state, stop conditions, and approval pauses? | OpenAI Agents SDK, graph-based orchestration, or custom state machine |
| Tool control | Can each specialist receive a narrow, auditable tool set? | Function tools, allowlisted service clients, read-only adapters |
| State | Can the system store only what it needs and resume safely? | Scoped session state, durable workflow state, explicit event records |
| Observability | Can you trace a run across specialists and inspect tool calls and errors? | Structured logs, traces, metrics, evaluation records |
| Deployment | Can you separate sandbox, staging, and controlled production with isolated credentials? | Managed service, containerized service, or internal platform |

The OpenAI Agents SDK documentation highlights orchestration, handoffs, guardrails and approvals, state, integrations and observability, and evaluation as related runtime capabilities.[1] LangGraph highlights customizable control flows, persistent context, and human-in-the-loop controls.[3] These are examples, not required vendor choices.

## Post-program project: limited-pilot release plan

Work in a team to produce a release package for the reference architecture. Do not deploy the system publicly.

| Deliverable | What to include |
|---|---|
| Multi-agent decision note | Why a coordinator and specialists are clearer than one agent, or why a single agent remains preferable. |
| System contract | All fields from Part 3 with named owners and prohibited actions. |
| Architecture diagram or workflow canvas | Control flow, state boundaries, tool permissions, approval interruption, and escalation. |
| Eight-case evaluation record | Inputs, observed behavior, evidence, failures, changes, and remaining risks. |
| Deployment ladder | Stage 0–3 entry criteria, named operational owner, pause switch, rollback plan, and release decision. |
| Pilot readout | What will be measured, how a moderator gives feedback, and what evidence is needed before any expansion. |

### Advanced-module review rubric

| Criterion | Points | Evidence reviewers should see |
|---|---:|---|
| Architecture justification | 15 | A reasoned single-agent or multi-agent decision tied to ownership and tool boundaries. |
| Specialist contracts and permissions | 20 | Explicit inputs, outputs, allowed tools, prohibited actions, and escalation path. |
| Evaluation and safety controls | 20 | Eight-case results, human-review points, prompt-injection handling, and limitations. |
| Production operating plan | 20 | Secrets, access, logging, monitoring, incident, rollback, and operational owner. |
| Documentation and collaboration | 15 | Clear artifacts, versioning, handoffs, and reviewable decision records. |
| Honest release decision | 10 | Evidence-based rationale for staying in sandbox, entering a pilot, or deferring deployment. |
| **Total** | **100** | **Safety, accountability, and evidence outweigh complexity.** |

## Reflect and share

At the end of the module, submit a short reflection:

1. Which specialist boundary made the workflow clearer, and which did not?
2. What is the riskiest tool call in the design, and how is it controlled?
3. Which evaluation case changed your design the most?
4. What evidence would be required before moving from a limited pilot to controlled production?
5. What part of the workflow should remain human-owned even after further engineering?

## References

[1] [OpenAI, “Agents SDK.”](https://developers.openai.com/api/docs/guides/agents)

[2] [OpenAI, “A practical guide to building agents.”](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

[3] [LangChain, “LangGraph: Agent Orchestration Framework for Reliable AI Agents.”](https://www.langchain.com/langgraph)
