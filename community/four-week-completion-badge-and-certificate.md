# Four-Week Completion Badge and Certificate Template

The **Automation Legends AI Learning Hub Graduate** credential recognizes members who complete the four-week learning journey with visible evidence of practice, verification, collaboration, and reflection. It can be issued as a GitHub badge label, a project-completion record, and a printable certificate using the wording below.

> **Credential boundary:** This recognition confirms completion of the AI Learning Hub curriculum and evidence-based community practice. It is **not** a professional certification, employment qualification, or authorization to deploy high-impact AI systems without appropriate governance, review, and expertise.

## Recognition options

| Format | Purpose | Issued by |
|---|---|---|
| **GitHub badge label** | Visible community recognition on an approved completion claim | Automation Legends maintainer |
| **Completion record** | Links the member’s sanitized evidence and learning reflection | Automation Legends maintainer or facilitator |
| **Printable certificate** | A formal record for the member’s personal portfolio | Authorized Automation Legends facilitator |

## Eligibility requirements

A member is eligible when they submit evidence for each stage of the four-week journey. Evidence must be sanitized, authorized, and honest about limitations.

| Week | Completion evidence |
|---|---|
| **Week 1: Foundations** | A low-risk AI task, improved prompt, verification action, and reflection; normally associated with the `badge: week-1 explorer` label |
| **Week 2: Workflow Builder** | A workflow canvas, human-review step, five-case test set, and documented improvement; normally associated with the `badge: week-2 workflow builder` label |
| **Week 3: Advanced Systems** | A bounded agent contract or retrieval-system design, approved-source plan, eight-question evaluation set, and stated limitation |
| **Week 4: Collaborative Capstone** | Role-specific contribution, shared project evidence, safe-team practices, and a capstone reflection or demo contribution |

A facilitator may accept an equivalent artifact when it clearly demonstrates the same learning outcome. The standard is evidence of practice—not a particular tool, programming language, or deployment platform.

## Required completion claim

Use the [guided GitHub completion-claim form](https://github.com/Automation-Legends/ai-learning-hub/issues/new/choose) when available, or copy the following template into a new issue or community discussion. Do not include credentials, private data, client information, or unapproved screenshots.

```text
## Credential requested
[ ] badge: four-week AI Learning Hub graduate

## Member name for recognition
[Name or preferred display name]

## Week 1 evidence
[Link or short sanitized description]

## Week 2 evidence
[Link or short sanitized description]

## Week 3 evidence
[Link or short sanitized description]

## Week 4 capstone role and evidence
[Role, link or short sanitized description, and team contribution]

## What I verified or changed myself
[One or more specific actions]

## One limitation I discovered
[Concise reflection]

## One responsible next step
[What you will improve, test, or learn next]

## Certificate preference
[ ] GitHub badge only
[ ] Completion record
[ ] Printable certificate wording
```

## Maintainer review checklist

A maintainer should review the claim against the evidence rather than assuming that attendance, a tool choice, or a polished demo is enough.

- [ ] Evidence is present for all four weeks or an equivalent learning artifact has been approved.
- [ ] Submitted examples are authorized, sanitized, and free of secrets or sensitive material.
- [ ] Week 1 evidence includes an explicit verification action.
- [ ] Week 2 evidence includes a human-review or escalation point and relevant test cases.
- [ ] Week 3 evidence names system boundaries, source governance, and a limitation.
- [ ] Week 4 evidence shows a role-specific contribution to the collaborative capstone.
- [ ] Reflection is specific and acknowledges a limitation or uncertainty.
- [ ] The member does not make unsupported claims about professional competence or production readiness.
- [ ] The maintainer applies the recognition label and records the issue or discussion link.

## Badge label standard

| Label | Color | Description |
|---|---|---|
| `type: four-week completion claim` | `1D76DB` | Identifies an issue as a four-week credential claim. |
| `status: graduation review` | `FBCA04` | A maintainer must review the four-week completion evidence. |
| `status: graduation approved` | `0E8A16` | A maintainer approved the evidence; the badge workflow may now run. |
| `badge: four-week AI Learning Hub graduate` | `C69214` | Completed the four-week AI Learning Hub curriculum with evidence of practice, verification, and collaboration. |

### Recommended badge description

> **Automation Legends AI Learning Hub Graduate** — completed the four-week learning journey: foundations, workflow design, advanced system boundaries, and collaborative capstone practice.

## Printable certificate template

Copy this wording into a certificate design or official document. Confirm all placeholders and evidence before issuing it.

```text
AUTOMATION LEGENDS
AI LEARNING HUB

CERTIFICATE OF COMPLETION

This certificate recognizes

[MEMBER NAME]

for completing the four-week Automation Legends AI Learning Hub curriculum.

The member demonstrated evidence-based AI practice across:
• AI foundations, clear prompting, and verification;
• workflow design, testing, and human review;
• bounded advanced-system design and responsible knowledge use; and
• collaborative capstone contribution to the Community Resource Review Assistant.

Completion date: [MONTH DAY, YEAR]
Credential ID: [AL-AILH-YYYY-####]
Evidence record: [LINK TO APPROVED COMPLETION CLAIM]

Issued by: [FACILITATOR OR AUTHORIZED MAINTAINER NAME]
Automation Legends AI Learning Hub

This certificate recognizes learning completion and community practice. It is not a professional certification, employment qualification, or authorization to deploy high-impact AI systems.
```

## Certificate issue record

To maintain an accurate record, store the following fields in an approved facilitator-owned tracker. Do not expose personal information in public repositories without consent.

| Field | Record |
|---|---|
| Credential ID | `AL-AILH-[year]-[sequential number]` |
| Recipient display name | The name the member approves for the certificate |
| Completion date | Date the maintainer approved the evidence |
| Completion-claim link | URL of the reviewed claim or discussion |
| Issuer | Authorized facilitator or maintainer |
| Delivery method | Badge, completion record, printable certificate, or combination |
| Notes | Optional internal note about a resubmission or equivalent evidence |

## Issuing process

1. A member opens a completion claim with all four weeks of evidence.
2. A maintainer reviews the evidence against the checklist above.
3. If evidence is incomplete, the maintainer names the smallest focused revision needed.
4. Once approved, the maintainer applies **`status: graduation approved`**. The repository workflow then adds **`badge: four-week AI Learning Hub graduate`**, removes the review label, and posts an auditable confirmation comment.
5. If requested, the facilitator creates the printable certificate, assigns a unique credential ID, and records the issue link in the approved tracker.
6. The member may share the credential, provided they represent its completion-only boundary accurately.

## Quality and integrity

Recognition should celebrate genuine practice while preserving trust. Do not issue a credential for copied, fabricated, private, or unsafe evidence. When a claim includes mistakes but shows careful testing, correction, and reflection, guide the member through revision rather than treating the mistake as a failure of participation.
