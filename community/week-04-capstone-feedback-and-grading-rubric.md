# Week 4 Capstone Feedback and Grading Rubric

This rubric assesses the **Community Resource Review Assistant** capstone. It is designed for mixed-skill teams in which beginner members and intermediate builders make different, equally valuable contributions. The assessment rewards problem clarity, safety, evidence, collaboration, and reflection—not technical complexity, tool choice, speed, or a live production deployment.

> **Fairness principle:** A beginner who designs a strong review rubric, improves a prompt through testing, documents a limitation, and supports the team can earn the same high score as an intermediate builder who creates a sound workflow specification. Both must show clear evidence, responsible boundaries, and useful collaboration.

## Assessment at a glance

| Assessment area | Points | What is assessed |
|---|---:|---|
| **Shared capstone artifact** | 60 | The team’s problem definition, workflow, safety boundaries, testing, and documentation |
| **Individual role contribution** | 25 | Role-specific evidence, handoffs, and personal reflection |
| **Team demonstration and peer learning** | 15 | Clear demo, evidence of testing, honest limitations, and learning transfer |
| **Total** | **100** | A safe, useful, collaborative capstone outcome |

A team does not need to deploy a live system to receive a strong score. A complete design, safe prototype, thoughtful test results, and clear handoff plan are valid capstone outcomes.

## Required evidence

Before grading, ensure the team has submitted a sanitized project package. It may be a repository folder, shared document, presentation, or project showcase that contains the following materials.

- [ ] One-page project contract with problem, user, scope, human reviewer, and disallowed actions.
- [ ] Workflow canvas showing trigger, minimum input, AI-assisted step, structured output, review queue, destination, and exception path.
- [ ] Versioned review-safe prompt and output contract.
- [ ] Five-case evaluation sheet: typical, incomplete, ambiguous, boundary, and messy inputs.
- [ ] Record of at least one change made after testing.
- [ ] Sanitized demonstration or screenshot using only fictional, anonymized, or authorized public material.
- [ ] Individual role reflections.
- [ ] Maintenance note identifying owner, human approval step, and one limitation.

Do not submit credentials, private documents, client data, passwords, API keys, personal contact details, or information that the team is not authorized to share.

## Shared capstone artifact — 60 points

### 1. Problem definition and member value — 10 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 9–10** | Defines a specific community problem, identifies the intended member and moderator experience, and explains why the proposed workflow is preferable to the current approach. The scope is narrow and achievable. |
| **Meets expectations: 7–8** | States a relevant community problem and intended user. The scope is mostly clear and feasible. |
| **Developing: 4–6** | Names a general problem, but the user need, workflow purpose, or scope needs clarification. |
| **Not yet demonstrated: 0–3** | Starts with a tool rather than a problem, or provides no clear user need or scope. |

**Feedback prompts:** What specific friction does this project reduce? Which member or moderator benefit is easiest to verify? What scope should be removed to make the project safer and clearer?

### 2. Workflow and output design — 15 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 13–15** | Maps a complete, understandable workflow with a clear trigger, minimized input, bounded AI step, structured output, destination, human reviewer, and fallback. The output makes uncertainty visible. |
| **Meets expectations: 10–12** | Includes the main workflow steps and structured output. Most handoffs are clear, though one boundary or fallback may need refinement. |
| **Developing: 6–9** | Shows a partial workflow but omits important transitions, output requirements, or the review process. |
| **Not yet demonstrated: 0–5** | The workflow is unclear, untestable, or depends on AI making an undefined final decision. |

**Feedback prompts:** Can another team reproduce the workflow from the map? Is the output easy for a moderator to review? Where does the workflow need a more explicit stop condition?

### 3. Safety, privacy, and human accountability — 15 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 13–15** | Minimizes data, explicitly excludes private or unauthorized content, protects credentials, names a human reviewer, documents a clear exception path, and prevents automatic public publication or other consequential actions. |
| **Meets expectations: 10–12** | Includes a human review step, basic privacy boundary, and exception route. One safeguard may need more detail. |
| **Developing: 6–9** | Recognizes a safety concern but does not translate it into a workflow control or named owner. |
| **Not yet demonstrated: 0–5** | Includes unreviewed publication, excessive data, exposed secrets, or no meaningful human accountability. |

**Feedback prompts:** What data is necessary—and what must be excluded? Who decides whether a draft is approved? What happens when the source, input, or output is uncertain?

### 4. Testing and evidence-based improvement — 10 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 9–10** | Tests all five required cases, documents the actual behavior, identifies a meaningful failure or limitation, and makes a focused improvement based on the evidence. |
| **Meets expectations: 7–8** | Tests most required cases and documents at least one improvement or follow-up question. |
| **Developing: 4–6** | Tests only normal inputs or records results without explaining what changed. |
| **Not yet demonstrated: 0–3** | Provides only a happy-path example or makes unsupported claims about reliability. |

**Feedback prompts:** Which test revealed the most useful weakness? What changed after the test? Which unresolved failure needs human review rather than another prompt revision?

### 5. Documentation and maintainability — 10 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 9–10** | Produces clear, concise, sanitized documentation that explains the purpose, workflow, prompt, review process, known limits, owner, and next safe step. A new maintainer can understand the project. |
| **Meets expectations: 7–8** | Documents the main purpose, workflow, and review process. Some details may need expansion for handoff. |
| **Developing: 4–6** | Documentation describes the idea but not how to review, maintain, or limit it. |
| **Not yet demonstrated: 0–3** | Documentation is missing, unsafe to share, or too incomplete for another member to understand. |

**Feedback prompts:** Could a moderator understand the workflow without attending the demo? Does the documentation state what the project cannot do? Who owns the next review or update?

## Individual role contribution — 25 points

Each member submits a short reflection and links to the evidence they created or improved. Assess the contribution against the role the member actually performed, not against an assumed technical level.

### 6. Role-specific contribution — 15 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 13–15** | Shows substantial, role-appropriate work that improved the team’s project. Explains the reasoning, revisions, and evidence behind the contribution. |
| **Meets expectations: 10–12** | Shows a clear, useful contribution aligned with the assigned or chosen role. |
| **Developing: 6–9** | Shows participation but provides limited evidence of ownership, revision, or impact. |
| **Not yet demonstrated: 0–5** | Provides no clear evidence of an individual contribution. |

Use the following role examples when reviewing evidence.

| Role | Examples of strong evidence |
|---|---|
| **Beginner community researcher** | Learner need statement, resource-review rubric, plain-language usability feedback, or a source-quality checklist. |
| **Beginner prompt designer** | A prompt version history, test examples, an improved output format, or a documented uncertainty instruction. |
| **Beginner quality reviewer** | A safe test case, a correction found during review, a SCOPE check, or feedback that improved the member experience. |
| **Beginner documentarian** | Clear onboarding instructions, a project showcase, a help guide, or a sanitized explanation of limits. |
| **Intermediate workflow builder** | Workflow canvas, input-validation plan, API/no-code integration boundary, structured-output schema, or review-queue design. |
| **Intermediate evaluator** | Five-case test plan, exception handling, success criteria, evaluation results, or an evidence-based iteration. |
| **Intermediate technical documentarian** | Credential-storage guidance, source inventory, maintenance note, owner and escalation policy, or configuration handoff. |
| **Moderator owner** | Approval criteria, escalation process, community-standard alignment, or a sustainable review policy. |

### 7. Collaboration and handoffs — 5 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 5** | Proactively made another member’s contribution easier through clear handoffs, respectful feedback, shared documentation, or role-appropriate support. |
| **Meets expectations: 4** | Participated reliably and completed the agreed handoff. |
| **Developing: 2–3** | Participated inconsistently or needed clarification to complete the handoff. |
| **Not yet demonstrated: 0–1** | Collaboration evidence is missing or behavior made the team’s work less safe or inclusive. |

### 8. Reflection and next step — 5 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 5** | Identifies a specific learning insight, a limitation, and a responsible next improvement. Connects the reflection to evidence. |
| **Meets expectations: 4** | Names a learning insight and a plausible next step. |
| **Developing: 2–3** | Offers a general reflection without evidence or a clear next action. |
| **Not yet demonstrated: 0–1** | Reflection is missing or only claims success without acknowledging a limitation. |

## Team demonstration and peer learning — 15 points

### 9. Demonstration clarity — 5 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 5** | Delivers a concise, accessible demonstration that shows the community problem, workflow, human-review step, and a safe example. |
| **Meets expectations: 4** | Explains the project and shows most major workflow elements. |
| **Developing: 2–3** | Shows a result but leaves the problem, workflow, or review process unclear. |
| **Not yet demonstrated: 0–1** | No coherent demonstration is provided. |

### 10. Evidence, limits, and learning transfer — 10 points

| Performance level | Evidence standard |
|---|---|
| **Exceeds expectations: 9–10** | Shares test evidence, one limitation, a failed or uncertain case, and a specific lesson that another team can reuse. |
| **Meets expectations: 7–8** | Shares at least one test or limitation and a useful takeaway. |
| **Developing: 4–6** | Focuses on feature claims with limited evidence, limitation, or reusable learning. |
| **Not yet demonstrated: 0–3** | Makes unsupported performance claims or does not acknowledge a limitation. |

## Grade bands

| Total score | Descriptor | Interpretation |
|---:|---|---|
| **90–100** | Exemplary collaborative practice | The team created a safe, well-tested, maintainable project and made learning reusable for the community. |
| **80–89** | Strong, ready-to-share prototype | The team met the capstone expectations and has a few defined improvements before expanding scope. |
| **70–79** | Complete with targeted revisions | The core project is present, but one or more areas need clearer testing, boundaries, or documentation. |
| **60–69** | Developing evidence | The team has a promising start but must supply missing evidence or revise unsafe/unclear elements. |
| **Below 60** | Rebuild the learning loop | The team should narrow scope, restore safety boundaries, complete testing, and resubmit the project package. |

## Feedback protocol

Feedback should be specific, kind, and actionable. Reviewers should not reward a more technical tool choice over a stronger user-centered, safe, and well-documented contribution.

### Facilitator feedback format

Use this short structure for every team.

```text
Strength: [Name one evidence-backed practice that should continue.]
Question: [Ask one question that helps the team identify a boundary, assumption, or missing evidence.]
Next step: [Name one focused revision that is achievable before the next review.]
```

### Peer-feedback checklist

- [ ] I commented on evidence, not personal style or technical status.
- [ ] I named one useful strength before suggesting a revision.
- [ ] I asked whether the workflow preserves human review and safe data boundaries.
- [ ] I checked whether the team tested an incomplete, ambiguous, or boundary case.
- [ ] I suggested one practical next step rather than adding unbounded scope.

### Individual reflection prompt

```text
My role: [role]
My contribution: [link or description]
One decision I influenced: [decision]
What I verified, corrected, or tested: [evidence]
One limitation I discovered: [limitation]
My next responsible improvement: [next step]
```

## Regrade and revision path

A revision is a learning opportunity, not a penalty. When a team receives a developing score, the reviewer should identify the smallest high-value change needed: for example, adding a human-review step, completing the five-case test set, narrowing the input data, or documenting a limitation. Teams may resubmit the updated evidence package with a brief note explaining what changed and why.
