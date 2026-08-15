# Week 4 Capstone Slide Deck — Detailed Presentation Script

Use this script with the **Week 4 Collaborative Capstone** presentation. It is designed for a 35-minute presentation followed by up to 10 minutes of questions. The goal is to help members understand the project, choose an appropriate role, recognize the safety boundaries, and understand how evidence-based grading works.

> **Facilitator outcome:** Every participant should leave able to name one role, one project boundary, one test case, and one piece of evidence they can contribute.

## Timing guide

| Slide | Topic | Suggested time |
|---:|---|---:|
| 1 | Welcome to the capstone | 2 minutes |
| 2 | Why the capstone matters | 3 minutes |
| 3 | Community problem | 3 minutes |
| 4 | Collaboration roles | 4 minutes |
| 5 | Project contract | 4 minutes |
| 6 | Draft-and-review safety pattern | 4 minutes |
| 7 | Five-case testing | 4 minutes |
| 8 | Shared-artifact rubric | 4 minutes |
| 9 | Individual contribution and fairness | 4 minutes |
| 10 | Commitment and next steps | 3 minutes |
| — | Questions and role matching | 10 minutes |

## Before presenting

- [ ] Open the [Week 4 capstone module](week-04-collaborative-capstone.md), [grading rubric](week-04-capstone-feedback-and-grading-rubric.md), and [capstone FAQ](week-04-capstone-faq.md).
- [ ] Confirm the current kickoff date, team-signup method, and facilitator contact before stating them.
- [ ] Prepare one fictional or authorized public sample resource suggestion; do not use private submissions in a live session.
- [ ] Enable captions and ensure a moderator can collect questions in chat.
- [ ] Prepare a chat prompt: **“My first capstone role or contribution will be ________.”**
- [ ] Keep the [Workflow Canvas](../templates/workflow-canvas.md) and [Evaluation Sheet](../templates/evaluation-sheet.md) available for follow-up.

# Slide-by-slide script

## Slide 1 — Week 4 Collaborative Capstone

**Time:** 2 minutes

**Purpose:** Welcome members and state the project’s learning value and practical boundary.

**Say:**

> Welcome to Week 4 of the Automation Legends AI Learning Hub. This is our collaborative capstone: the point where individual lessons become a shared, practical project.
>
> We are building a Community Resource Review Assistant. Its job is intentionally narrow. When a member suggests a public AI-learning resource, the workflow prepares a structured draft for a moderator. It does not publish a resource automatically, decide whether a claim is true, or replace the person responsible for approval.
>
> Today we will cover the community problem, the roles, the project contract, the safety pattern, the required tests, and the grading rubric. By the end, you should be able to choose a role and identify the first artifact you can help create.

**Ask in chat:**

> In one word, what do you want to strengthen during this capstone: prompting, workflow, testing, documentation, collaboration, or review?

**Transition:**

> The capstone matters because learning is strongest when it helps a real community process.

## Slide 2 — Week 4 turns AI learning into useful community practice

**Time:** 3 minutes

**Purpose:** Explain why the capstone is practical without overpromising autonomy or deployment.

**Say:**

> Up to this point, members have practiced individual skills: clear prompts, verification, workflow design, evaluation, and system boundaries. Week 4 connects those skills to one shared problem.
>
> The project is real-world because communities receive resource suggestions in many formats, with different levels of context and reliability. But the project remains low-risk because the output is a review draft. A moderator remains accountable for any public action.
>
> Beginners and intermediate builders contribute different skills, but those skills are equally important. A better prompt, clearer review rubric, safer test case, or stronger user guide can improve the project as much as a workflow diagram or integration design.
>
> You do not have to deploy a live system to succeed. A clear, tested design and an honest reflection are successful outcomes.

**Facilitator action:** Pause after “equally important” and ask for one example of a nontechnical contribution that could improve the project.

**Transition:**

> Let us look at the specific problem the team is solving.

## Slide 3 — One focused problem creates a meaningful project

**Time:** 3 minutes

**Purpose:** Connect each capstone component to a concrete community need.

**Say:**

> The project starts with a simple observation: good resource suggestions can arrive without enough context, while weak or unclear suggestions can look convincing at first glance.
>
> The assistant does not solve the entire moderation problem. It solves one narrow part: preparing a consistent draft that helps a human reviewer see what was submitted, what needs checking, and where uncertainty remains.
>
> A structured intake makes submissions easier to compare. Verification questions make unsupported claims visible. A review queue prevents drafts from moving directly to public publication. And uncertainty flags remind us that an AI-generated summary is not an endorsement.

**Ask:**

> Which challenge on this slide feels most familiar in your own work: inconsistent input, checking claims, maintaining a review process, or handling uncertainty?

**Facilitator note:** If a member gives an example involving private material, thank them and ask them to restate it with fictional or generalized details.

**Transition:**

> Solving this problem requires multiple kinds of expertise, so the capstone deliberately assigns complementary roles.

## Slide 4 — Every skill level has a meaningful role

**Time:** 4 minutes

**Purpose:** Make role selection accessible and prevent technical-status hierarchy.

**Say:**

> There is no “helper” role in this capstone. Every role owns an artifact that can improve the team’s final work.
>
> Beginner members can define what makes a resource useful, improve the review prompt, design safe examples, identify confusing outputs, and document the member experience. These tasks make the workflow more usable and more trustworthy.
>
> Intermediate builders can map the trigger and flow, define the structured output, design the review queue and exception path, and evaluate how the workflow behaves across different test cases.
>
> Everyone shares the same responsibilities: keep the scope narrow, use only authorized and minimized data, preserve human approval, and state limits honestly.

**Role-selection interaction:**

> In the chat, choose one role you would like to try: community researcher, prompt designer, quality reviewer, documentarian, workflow builder, evaluator, or moderator owner. You may choose a role you want to learn, not only one you already know.

**Facilitator guidance:** If a participant says “I am just a beginner,” respond:

> Beginner perspective is essential. You can help the team decide whether an input form is understandable, whether a prompt is clear, whether the output makes uncertainty visible, and whether the documentation is usable.

**Transition:**

> Once the team chooses roles, the first artifact is the project contract.

## Slide 5 — The project contract protects people and progress

**Time:** 4 minutes

**Purpose:** Explain how the project contract prevents scope creep and unsafe implementation.

**Say:**

> Before selecting a tool or writing a prompt, the team writes a project contract. This is how we decide what the project is—and what it is not.
>
> The minimum input is limited to a public title, URL, description, and optional category. The AI step prepares a summary, tags, verification questions, concerns, and a `needs_review` flag. The human owner is a named moderator who reviews every draft before any public action.
>
> The stop conditions are equally important. If an input is missing, unclear, private, unrelated, or suspicious, the normal flow stops and the issue goes to manual review. The team does not solve uncertainty by guessing.
>
> A strong project contract lets the team say no to unnecessary features. It helps us make a useful workflow that remains understandable and safe.

**Micro-activity:**

> Take one minute in pairs or chat: What is one input you would explicitly exclude from this workflow, and why?

**Expected examples:** passwords, API keys, private documents, client data, sensitive personal information, unverified screenshots.

**Transition:**

> The contract leads directly to the capstone’s central operational pattern: draft and review.

## Slide 6 — Draft-and-review is the central safety pattern

**Time:** 4 minutes

**Purpose:** Show the safe workflow sequence and reinforce accountable human decision-making.

**Say:**

> The safety pattern is simple: Suggest, Validate, Draft, Human Review, then Approve or Escalate.
>
> Suggest means a member provides an authorized public resource suggestion. Validate checks that the required fields exist and the submission is within scope. Draft uses the approved prompt to prepare structured information. Human Review is the point where a moderator checks the source, the claims, the tags, and any concerns. The final action is either approval or escalation—not silent automatic publication.
>
> The automation must not publish content, delete content, buy anything, contact people, or make final decisions. It must also use minimized inputs and keep credentials in approved secret storage.
>
> Notice that this does not make the project less valuable. It makes the value clearer. The automation saves preparation time while the human keeps responsibility.

**Ask:**

> Where in this sequence would you want a person to pause and ask a question before moving forward?

**Facilitator note:** Reinforce that a human reviewer must be named, not implied.

**Transition:**

> We cannot know whether the pattern works by showing one perfect example. We need tests that reveal uncertainty.

## Slide 7 — Five tests turn uncertainty into improvement

**Time:** 4 minutes

**Purpose:** Explain the evaluation standard and normalize failure as learning evidence.

**Say:**

> Every team runs five tests. The typical case checks whether the workflow can create a useful review draft. The incomplete case checks whether missing information stops the process. The ambiguous case checks whether marketing language creates verification questions rather than endorsement. The boundary case checks whether private, unsafe, or unrelated material is routed to a human. The messy case checks whether conflicting or unusually formatted input preserves uncertainty rather than triggering a guess.
>
> When a test fails, that is not a reason to hide the result. It is a reason to document the observed behavior, explain why it matters, and make the smallest focused improvement. A test may tell us to add an input requirement, a `needs_review` field, a stop condition, or a clearer reviewer instruction.
>
> A capstone team is not being graded on whether AI is perfect. It is being graded on whether the team can observe, test, and improve the process responsibly.

**Prompt for teams:**

> Choose one test case your team will run first. What evidence will show that the workflow behaved safely?

**Transition:**

> The grading rubric is designed to reward that evidence rather than tool complexity.

## Slide 8 — The rubric rewards evidence—not technical complexity

**Time:** 4 minutes

**Purpose:** Explain the shared 60-point artifact score.

**Say:**

> Sixty points come from the shared capstone artifact. These points are not about whether the team used code, a no-code tool, or a particular AI model.
>
> Ten points assess whether the team defined a real member or moderator problem. Fifteen assess workflow and structured-output design. Fifteen assess safety, privacy, and human accountability. Ten assess testing and an evidence-based improvement. Ten assess documentation and maintainability.
>
> The highest scores come from a narrow, clear scope; a visible human-review step; meaningful tests; and documentation that another member can understand. A live deployment does not add points by itself.

**Facilitator action:** Display or link the rubric. Ask teams to identify which of the five shared-artifact categories they feel most prepared for and which needs early attention.

**Transition:**

> The next section ensures that grading remains fair even when individual roles differ.

## Slide 9 — Individual contribution makes grading fair across roles

**Time:** 4 minutes

**Purpose:** Explain individual and team assessment so beginners and builders understand how their work is recognized.

**Say:**

> The remaining points recognize the work each person brings to the team. Fifteen points assess role-specific contribution. Five points assess collaboration and handoffs. Five points assess reflection and a responsible next step. Fifteen points assess the team demonstration and what other members can learn from it.
>
> A beginner is not expected to produce an integration design. An intermediate builder is not expected to perform every user-research task. Each member should show evidence of the role they performed, one decision they influenced, one thing they verified or changed, one limitation, and one next step.
>
> This is why we ask for project evidence and reflection. A team’s demo can look polished, but the evidence shows whether the work is safe, understood, and transferable.

**Invite reflection:**

> Complete this sentence in your notes: “The artifact I can own is ________. The evidence I can show is ________.”

**Transition:**

> Let us close by turning this information into one concrete next action.

## Slide 10 — Choose a role. Build safely. Share what you learn.

**Time:** 3 minutes, then questions

**Purpose:** Secure a commitment and direct participants to the right resources.

**Say:**

> Your next step is small and specific. Choose a role. Read the project contract. Create one artifact. Test one workflow step. Show one honest limitation.
>
> If you are starting today, select a role that fits your learning goal and send a short message to the team or facilitator. If you are already in a team, agree on the first artifact and the first test case. If you are facilitating, make sure every role has a named owner and that the human-review boundary is documented.
>
> Remember the community standard: build safely, verify what matters, and share what you learn in a way that helps the next member.

**Commitment prompt:**

```text
My first capstone role or contribution will be ________.
```

Invite participants to post their commitment in chat.

## Question-and-answer guidance

Use the final ten minutes to answer questions and match members to roles. Keep answers tied to the project boundary and concrete next actions.

| Question | Response approach |
|---|---|
| “Can we use a different tool?” | Yes, if the tool supports the project contract, safe data handling, review queue, and testability. The tool is secondary to the workflow. |
| “Can a beginner join the workflow team?” | Yes. Beginners can own prompts, test cases, input clarity, output review, documentation, and learner research. |
| “Can we add automatic publishing?” | Not in the capstone scope. Start with the draft-and-review pattern. Any later expansion needs new safeguards, ownership, and testing. |
| “What if our test fails?” | Document it, explain the risk, make the smallest focused improvement, and show what you learned. |
| “How do we get a high score?” | Show evidence of a useful problem, clear workflow, safety boundary, test-driven improvement, role contribution, and honest reflection. |
| “Can we earn the four-week graduate badge?” | Yes, after submitting evidence for all four weeks and receiving maintainer approval through the completion-claim process. |

## Post-presentation follow-up

Post this message within 24 hours.

```text
Thank you for joining the Week 4 capstone briefing.

Your next action is to choose a role and create one safe, visible artifact.

Start here:
- Capstone module: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/week-04-collaborative-capstone.md
- Feedback and grading rubric: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/week-04-capstone-feedback-and-grading-rubric.md
- Capstone FAQ: https://github.com/Automation-Legends/ai-learning-hub/blob/main/community/week-04-capstone-faq.md
- Workflow canvas: https://github.com/Automation-Legends/ai-learning-hub/blob/main/templates/workflow-canvas.md
- Evaluation sheet: https://github.com/Automation-Legends/ai-learning-hub/blob/main/templates/evaluation-sheet.md

Reply with your role, first artifact, or one question about the workflow boundary.
```
