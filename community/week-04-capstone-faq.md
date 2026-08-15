# Week 4 Capstone FAQ

This FAQ answers common questions about the **Community Resource Review Assistant** capstone and the associated feedback and grading rubric. The capstone helps Automation Legends members turn the first three weeks of learning into a collaborative, evidence-based project.

> **Core idea:** The capstone builds a safe draft-and-review workflow. It prepares a structured review draft for a human moderator; it does not publish content automatically or make final decisions.

## Getting started

### What is the Week 4 capstone?

The Week 4 capstone is a mixed-skill project in which members design and test a **Community Resource Review Assistant**. The assistant helps prepare a review draft when someone suggests a public AI-learning resource. The draft can include a concise summary, suggested tags, verification questions, concerns, and a `needs_review` flag. A human moderator decides whether anything is approved, edited, or published.

Read the full [Week 4 Collaborative Capstone](week-04-collaborative-capstone.md) module before choosing a role.

### Why does the project focus on resource review?

Community resource suggestions are a realistic, low-risk use case. They require clear inputs, structured outputs, source checking, uncertainty handling, and human review. These are the same design habits that make AI workflows more useful in many other settings, without requiring the team to automate a high-impact decision.

### Do we need to build a live working application?

No. A clear project contract, workflow canvas, review-safe prompt, structured output, five-case test set, demonstration, and honest reflection are valid capstone outcomes. A live deployment is optional and should not be attempted until the team has documented boundaries, ownership, testing, and a review process.

### Is the capstone only for members with technical experience?

No. The capstone is designed for beginner and intermediate contributors. It needs learner research, prompt design, quality review, testing, documentation, workflow design, and moderation. Technical complexity is not the goal and is not rewarded by itself.

### How do I join the capstone?

Read the project module, choose a role you would like to practice, and share your interest in the community space or with the named facilitator. You may start with a role you already know or choose one that helps you learn a new skill.

## Roles and collaboration

### What roles can beginner members take?

Beginner members can contribute as community researchers, prompt designers, quality reviewers, or documentarians. Useful artifacts include a learner-needs statement, a resource-review rubric, a prompt revision, safe test cases, verification questions, plain-language instructions, or a project reflection.

### What roles can intermediate builders take?

Intermediate members can contribute as workflow builders, evaluators, technical documentarians, or review-queue designers. Useful artifacts include a workflow canvas, input-validation plan, structured-output schema, safe API or no-code integration boundary, exception path, five-case evaluation, maintenance note, or credential-storage guidance.

### Can one member hold more than one role?

Yes, particularly in a small team. However, keep the project scope narrow. It is better to complete a clear contribution, explain its limits, and hand it off well than to take on too many roles without documenting the work.

### How should teams divide work fairly?

Begin by assigning a named owner for each artifact: project contract, prompt and output schema, workflow canvas, evaluation sheet, demonstration, and maintenance note. Then identify handoffs. For example, a beginner prompt designer may pass a revised output format to an intermediate workflow builder; the builder returns a testable draft to a quality reviewer.

### What if the team disagrees about a tool or approach?

Return to the project contract. Ask which option best supports the intended user, minimizes inputs, preserves human review, and can be tested safely. When two approaches are reasonable, choose the one that is easier to explain, evaluate, and reverse. Record the decision and the reason.

### What if a team member cannot complete a contribution?

Communicate early, document the incomplete handoff, and narrow the project rather than silently filling the gap. A team can still demonstrate strong collaboration by identifying an unfinished item, assigning a new owner, and explaining the limitation honestly.

## Workflow, data, and safety

### What information may the resource intake include?

Use only what the review process needs: a public resource title, public URL, short description, and optional suggested category. Do not include passwords, API keys, private documents, client information, sensitive personal data, or other information that the team is not authorized to use.

### What should the AI-assisted step do?

The AI-assisted step should prepare a review draft from the supplied material. It may create a short summary, suggest categories, identify questions to verify, identify possible concerns, and set a `needs_review` flag. It must not declare that a resource is accurate, safe, current, endorsed, or suitable unless a human reviewer independently establishes that conclusion.

### What must the automation not do?

The capstone workflow must not automatically publish or delete content, buy anything, contact people, access private accounts, grant permissions, or make final decisions. It should prepare information for a reviewer, not replace accountable human judgment.

### Why is human review required?

AI output can be incomplete, misleading, or wrong even when it looks plausible. A named moderator is responsible for deciding whether a resource is appropriate, whether claims are supported, and whether content is ready for the community. The reviewer also owns exceptions and escalation.

### Where should API keys or credentials be stored?

Do not place secrets in the repository, an issue, a screenshot, a prompt, or a chat message. If the team experiments with an integration, keep credentials in an approved secret manager, environment variable, or automation-platform credential store with the narrowest necessary permissions. A written design without live credentials is a valid capstone outcome.

### What is an exception path?

An exception path defines what happens when the normal workflow should stop. For this capstone, missing, unclear, suspicious, unrelated, private, or potentially unsafe submissions should enter a manual-review queue or be rejected by a human moderator. The workflow should not guess its way through uncertainty.

### How can we work safely with a public repository?

Use fictional, anonymized, or clearly authorized public examples. Remove private details before sharing an artifact. Explain the general workflow rather than exposing real records. Ask permission before sharing another member’s name, result, or screenshot.

## Testing and improvement

### Which test cases are required?

Each team must test five conditions:

| Test case | What it checks |
|---|---|
| **Typical** | The workflow creates a clear review draft when required information is present. |
| **Incomplete** | Missing information stops the normal flow and is flagged. |
| **Ambiguous** | Marketing language or unclear claims produce verification questions rather than endorsement. |
| **Boundary** | Private, unsafe, unrelated, or unauthorized input routes to manual review. |
| **Messy** | Conflicting, unusually long, or oddly formatted input preserves uncertainty rather than causing a guess. |

### What should we do when a test fails?

Treat the failure as evidence. Record the input condition, the observed behavior, why it is a problem, and the smallest focused improvement. The improvement may be an input check, a clearer output requirement, a stricter stop condition, a better review question, or a decision to keep a task manual.

### Do we need perfect results to pass?

No. The capstone rewards honest testing and responsible improvement. A team that discovers a limitation, prevents an unsafe action, and documents a focused next step can demonstrate stronger learning than a team that shows only a polished happy-path example.

### What does “structured output” mean?

Structured output is a predictable format that makes a result easier to review. For example, the review assistant can return fields for summary, suggested tags, verification questions, concerns, and `needs_review`. A moderator can check these fields more quickly than an unstructured paragraph.

## Grading and feedback

### How is the capstone graded?

The [feedback and grading rubric](week-04-capstone-feedback-and-grading-rubric.md) uses a 100-point scale. Sixty points assess the shared artifact: problem definition, workflow design, safety, testing, and documentation. Twenty-five points assess individual role contribution, collaboration, and reflection. Fifteen points assess the team demonstration and peer-learning value.

### Will beginner members be graded against intermediate builders?

No. Individual contributions are assessed against the member’s actual role and evidence. A beginner who improves a prompt through testing, identifies a missing detail, documents a boundary, and supports a handoff can earn the same high score as an intermediate builder who creates a safe workflow specification.

### Does building a live application earn extra credit?

No. The rubric does not award additional points for complexity, tool brand, coding language, or live deployment. A live system may create additional risks. The highest scores come from a useful scope, clear evidence, safe boundaries, thoughtful testing, collaboration, and honest reflection.

### What evidence should I submit for my individual contribution?

Submit a sanitized artifact or concise description of your work, one decision you influenced, one thing you verified or changed, one limitation, and one responsible next step. Link to a prompt version, workflow section, test case, documentation page, review rubric, or project showcase when possible.

### What if I disagree with feedback or my score?

Ask for clarification using the rubric category and evidence. A useful request might be: “Which additional evidence would demonstrate a clear human-review boundary?” The rubric includes a revision path. Focus on the smallest high-value change rather than arguing for points without evidence.

### Can we revise and resubmit?

Yes. A revision is part of the learning process. The reviewer should identify the smallest focused improvement needed, such as adding an exception path, completing the test set, minimizing the input, or documenting a limitation. Resubmit the revised artifact with a note about what changed and why.

## Graduation badge and certificate

### What is required for the four-week completion badge?

A member needs evidence for Week 1 foundations, Week 2 workflow design, Week 3 advanced-system boundaries, and a Week 4 capstone contribution. The evidence must show practice, verification, collaboration, and reflection. Review the [Four-Week Completion Badge and Certificate](four-week-completion-badge-and-certificate.md) guide for the complete checklist.

### Does a four-week badge mean I am professionally certified?

No. The badge recognizes completion of the Automation Legends AI Learning Hub curriculum and evidence-based community practice. It is not a professional certification, an employment qualification, or authorization to deploy high-impact AI systems without appropriate governance and expertise.

### How does graduation-label automation work?

When a member opens a completion claim, it is automatically labeled as a four-week claim and sent to graduation review. A maintainer reviews the evidence. Only after the maintainer applies **`status: graduation approved`** does the repository workflow add **`badge: four-week AI Learning Hub graduate`**, remove the review label, and leave an auditable confirmation comment.

### Why is approval required before the badge is added?

A checked box or written claim is not enough to establish that the submitted work meets the evidence standard. Approval preserves the meaning of the credential and prevents the automation from judging evidence, interpreting private material, or awarding a credential based only on issue text.

### Can I request a printable certificate?

Yes. Choose the printable-certificate option in the completion claim. An authorized facilitator can use the certificate wording template after the evidence is approved. The facilitator should assign a unique credential ID and keep any private issuing record outside the public repository unless you consent to public sharing.

## Support and next steps

### Where should I start if I feel stuck?

Start with one small, visible artifact. Choose a role. Read the project contract. Create a safe test input. Improve one prompt field. Map one workflow step. Or write one verification question. Then ask the community a specific question such as: “What should the exception path be when the URL is missing?”

### Which resources should I keep open while working?

Keep these resources available:

- [Week 4 Collaborative Capstone](week-04-collaborative-capstone.md)
- [Feedback and Grading Rubric](week-04-capstone-feedback-and-grading-rubric.md)
- [Workflow Canvas](../templates/workflow-canvas.md)
- [Evaluation Sheet](../templates/evaluation-sheet.md)
- [Project Showcase Template](../templates/project-showcase.md)
- [Contribution Guide](../CONTRIBUTING.md)

### What should our team demonstrate at the end?

Show the community problem, the project contract, the workflow map, one safe example, one failure or exception case, the human-review step, one improvement based on testing, one limitation, and one next responsible step. Keep the demonstration concise and use only sanitized material.

### How can I help another member succeed?

Offer feedback on evidence, not status or tool choice. Ask whether the member has a clear user, minimal input, review point, exception path, and test case. Share one practical suggestion and one strength you observed. The strongest community contributions make safe learning easier for the next person.
