# Week 4 Capstone Video Walkthrough Script

This script supports a **12–15 minute recorded walkthrough** for new Week 4 participants. It explains the Community Resource Review Assistant project, team tracking, evidence submission, grading, and graduation process without exposing private member data or suggesting that automation makes final decisions.

> **Audience:** Beginner and intermediate AI Learning Hub members, including those joining their first collaborative automation project.

## Production notes

| Element | Guidance |
|---|---|
| Screen capture | Use a clean browser profile and fictional or authorized public examples only. Blur or exclude private notifications, open tabs, and account details. |
| Captions | Publish captions and provide the script in the video description or linked resource. |
| Pace | Pause after each action so viewers can follow the repository navigation. |
| On-screen style | Use readable, high-contrast callouts. Keep important UI details away from video edges. |
| Links | Add the capstone module, grading rubric, FAQ, team tracker, and completion guide in the description. |
| Safety reminder | Repeat that the project creates drafts for human review; it does not publish or make final decisions automatically. |

## At-a-glance run of show

| Time | Segment | Viewer outcome |
|---:|---|---|
| 0:00–0:40 | Welcome and project purpose | Understand the capstone’s goal and safe boundary. |
| 0:40–2:00 | Open the project resources | Know where to find the module, rubric, FAQ, and templates. |
| 2:00–3:30 | Read the project contract | Understand the minimum input, output, reviewer, and stop conditions. |
| 3:30–5:00 | Choose a team role | Select a beginner or intermediate contribution. |
| 5:00–6:30 | Form a capstone team | Create a team issue and assign initial artifacts. |
| 6:30–8:15 | Build and test safely | Use the five-case evaluation approach. |
| 8:15–9:45 | Post a progress update | Record evidence, blockers, and the next milestone. |
| 9:45–11:30 | Understand grading and submission | Know how shared and individual evidence are assessed. |
| 11:30–13:00 | Complete the graduation process | Understand the claim, review, badge, and opt-in notification process. |
| 13:00–14:00 | Close and next action | Choose one first contribution. |

# Full script

## 0:00–0:40 — Welcome and project purpose

**On screen:** The AI Learning Hub README, then the Week 4 capstone title.

**Say:**

> Welcome to the Week 4 collaborative capstone for the Automation Legends AI Learning Hub. In this walkthrough, you will see how to join the Community Resource Review Assistant project, work with a mixed-skill team, test your workflow safely, submit evidence, and complete the graduation process.
>
> The project has one important boundary from the start: it prepares a structured draft for a human moderator. It does not publish content automatically, make final decisions, or replace accountable review.

**On-screen callout:**

> Build drafts. Keep humans accountable.

## 0:40–2:00 — Open the project resources

**On screen:** Navigate from the repository README to the Week 4 capstone module, grading rubric, FAQ, and team tracker.

**Say:**

> Start at the AI Learning Hub homepage. In the community resources section, open four pages before beginning work.
>
> First, the Week 4 Collaborative Capstone explains the project problem, the roles, the project contract, and the test cases. Second, the Feedback and Grading Rubric shows how shared work and individual contributions are assessed. Third, the Capstone FAQ answers practical questions about roles, tools, testing, revisions, and credentials. Fourth, the Capstone Team and Progress Tracker explains how to coordinate work through GitHub issues.
>
> You do not need to memorize every detail now. Keep these pages open as your working references.

**Show links:**

- `community/week-04-collaborative-capstone.md`
- `community/week-04-capstone-feedback-and-grading-rubric.md`
- `community/week-04-capstone-faq.md`
- `community/capstone-team-and-progress-tracker.md`

## 2:00–3:30 — Read the project contract

**On screen:** Scroll to the project contract section. Highlight each field in sequence.

**Say:**

> Before choosing a tool, read the project contract. A project contract keeps the scope useful, clear, and safe.
>
> For this capstone, the minimum input is a public resource title, URL, short description, and optional category. The AI-assisted step can prepare a summary, suggest tags, identify verification questions, identify concerns, and set a `needs_review` flag.
>
> The named human reviewer is a moderator. That person checks the source, claims, tags, and concerns before anything happens publicly.
>
> The contract also states when the workflow must stop. Missing, unclear, private, unrelated, suspicious, or unsafe material goes to manual review. The workflow does not guess its way through uncertainty.

**Pause and ask viewers:**

> What is one input you would explicitly keep out of this project? Pause the video and write it down.

**On-screen examples:** passwords, private documents, API keys, client data, sensitive personal information.

## 3:30–5:00 — Choose a team role

**On screen:** The capstone role table. Use a split view between beginner and intermediate roles.

**Say:**

> Next, choose a role. You do not need to be a programmer to make a meaningful contribution.
>
> Beginner members can define learner needs, improve prompts, write safe test cases, review outputs, and document the project. Intermediate builders can map the workflow, define structured outputs, set safe integration boundaries, build a review queue, and evaluate exception handling.
>
> Every role contributes to a shared responsibility: use only authorized and minimized data, preserve human review, and state limitations honestly.
>
> Choose one role you want to practice, not only one you already know. Then identify the first artifact you can own. That could be a prompt revision, a test case, a workflow canvas section, or a documentation outline.

**On-screen prompt:**

> My role: ________  
> My first artifact: ________

## 5:00–6:30 — Form a capstone team

**On screen:** Open **New issue** and select the Capstone Team Formation template. Use fictional names and a fictional project example.

**Say:**

> When your team is ready, open a new issue and select the Capstone Team Formation template. Give the team a clear name. List each team member, their role, and the first artifact they own.
>
> Complete the project-contract table together. This is where you name the trigger, minimum authorized input, AI-assisted task, structured output, human reviewer, destination after review, stop conditions, and actions the workflow will not take.
>
> The template also assigns an owner for each required test case: typical, incomplete, ambiguous, boundary, and messy.
>
> When the issue opens, the tracker adds a team-forming status and an orientation comment. That automation does not approve the team or choose the project. A maintainer reviews the record and deliberately changes the status when the team is ready to begin active work.

**On-screen callout:**

> Never include private data, credentials, or client material in the issue.

## 6:30–8:15 — Build and test safely

**On screen:** The Workflow Canvas and Evaluation Sheet. Walk through one fictional resource suggestion.

**Say:**

> Now the team builds a narrow draft-and-review workflow. Start with a fictional or authorized public resource suggestion. Validate the minimum fields. Prepare a structured draft. Send the result to a human reviewer. Then either approve or escalate.
>
> Test more than the happy path. The typical case checks whether a useful draft is created. The incomplete case checks whether missing information stops the flow. The ambiguous case checks whether the workflow asks verification questions instead of making an endorsement. The boundary case checks whether private or unrelated material is routed away from the workflow. The messy case checks whether the system preserves uncertainty instead of guessing.
>
> If a test fails, record it. Explain what happened, why it matters, and the smallest focused improvement. A limitation that is found, documented, and addressed is valuable learning evidence.

**On-screen callout:**

> A safe “stop” is a successful workflow behavior.

## 8:15–9:45 — Post a progress update

**On screen:** Open the Capstone Progress Update issue template. Complete a fictional milestone.

**Say:**

> For a meaningful milestone, open a Capstone Progress Update issue and link the team-formation record. Record the artifact, its owner, a safe link or summary, and whether it is draft, reviewed, or revised.
>
> Add the results from all five test cases. If the team is blocked, describe only the smallest relevant context a facilitator needs to help. Avoid private documents, secrets, and unrelated personal information.
>
> Finally, name one next milestone, who owns it, and when the team will review it. The progress tracker adds a review status and a reminder. It does not grade the work or declare completion. Those decisions remain with the team and maintainer.

**On-screen prompt:**

> Next milestone: ________  
> Owner: ________  
> Review point: ________

## 9:45–11:30 — Understand grading and submission

**On screen:** The grading rubric, first shared-artifact categories, then individual contribution categories.

**Say:**

> The capstone uses a 100-point evidence-based rubric. Sixty points assess the shared artifact: the community problem, workflow and structured output, safety and accountability, testing and improvement, and documentation.
>
> The remaining points assess role-specific contribution, collaboration and handoffs, reflection and a responsible next step, and the team demonstration.
>
> This approach is designed to be fair across roles. A beginner who improves a prompt through testing, identifies a missing review step, and documents a clear limitation can earn the same high score as an intermediate builder who maps a safe workflow.
>
> Do not focus on complexity or a live deployment. Focus on evidence. Show what you contributed, what you verified, what you learned, and what should happen next.

**On-screen checklist:**

- Useful project contract
- Role-specific artifact
- Five-case test evidence
- Human-review boundary
- One limitation
- One responsible next step

## 11:30–13:00 — Complete the graduation process

**On screen:** Open the Four-Week Completion Claim template and the completion badge guide.

**Say:**

> After you complete all four weeks, open a Four-Week Completion Claim. Link or describe safe evidence from Week 1 foundations, Week 2 workflow design, Week 3 advanced-system boundaries, and your Week 4 capstone contribution.
>
> Include what you verified or changed yourself, one limitation you discovered, and one responsible next step. A maintainer reviews the evidence. If it meets the standard, the maintainer applies the graduation-approved status.
>
> The repository then adds the four-week graduate badge and leaves an auditable confirmation comment. This recognition celebrates curriculum completion and evidence-based community practice. It is not a professional certification or authorization to deploy high-impact AI systems.
>
> If you have privately opted in to graduate email notifications, the notification sequence can send a congratulations email and a print-ready certificate after the badge is awarded. Your email address is never placed in a public issue.

**On-screen callout:**

> Evidence → Maintainer review → Graduate badge → Optional private notification

## 13:00–14:00 — Close and next action

**On screen:** Return to the README and highlight the capstone links.

**Say:**

> You are ready to begin. Your first step is not to build the entire system. Choose a role, create one small artifact, test one workflow behavior, and record one honest limitation.
>
> Use the capstone module, tracker, rubric, and FAQ as your guides. If you need help, ask a specific question tied to the project contract or test evidence.
>
> Build safely, verify what matters, and share what you learn so the next member can build with more confidence.

**Final on-screen text:**

> Choose a role. Build safely. Share what you learn.  
> `github.com/Automation-Legends/ai-learning-hub`

## Video description template

```text
Week 4 turns individual AI learning into a collaborative, evidence-based community project.

In this walkthrough, you will learn how to:
• choose a capstone role;
• form a team and define a safe project contract;
• run the five required test cases;
• record progress and submit evidence;
• understand the grading rubric; and
• complete the four-week graduation process.

Resources:
• Capstone module: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/week-04-collaborative-capstone.md
• Team and progress tracker: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/capstone-team-and-progress-tracker.md
• Grading rubric: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/week-04-capstone-feedback-and-grading-rubric.md
• Capstone FAQ: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/week-04-capstone-faq.md
• Completion guide: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/four-week-completion-badge-and-certificate.md

Use only fictional, anonymized, or authorized public material in community work. The capstone prepares drafts for human review; it does not publish content or make final decisions automatically.
```
