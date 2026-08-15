# Graduate Email Notification Sequence

This resource explains the **opt-in** graduate notification sequence for the Automation Legends AI Learning Hub. It sends a congratulatory email and print-ready certificate only after a maintainer approves a valid four-week completion claim and the repository awards the graduate badge.

> **Default state:** Notification workflows are published but **inactive** until a maintainer explicitly enables them and configures private email settings. The public repository never stores or displays member email addresses.

## Sequence at a glance

| Stage | Trigger | Message | Certificate |
|---|---|---|---|
| **Day 0** | A maintainer applies `status: graduation approved` to a valid completion claim, which awards the graduate badge | Congratulates the member and links their approved evidence record | Attached as a print-ready HTML certificate |
| **Day 7** | Optional daily follow-up check finds a member who graduated seven days earlier and opted in | Invites a small next step: improve an artifact, share a safe showcase, or help another member | No attachment |
| **Day 30** | Optional daily follow-up check finds a member who graduated 30 days earlier and opted in | Invites feedback, a safe contribution, or a reflection on learning | No attachment |

The system does not make eligibility decisions, infer contact information, grade evidence, or email anyone without an opt-in record.

## How the Day 0 workflow works

1. A member opens a four-week completion claim.
2. The claim receives `type: four-week completion claim` and `status: graduation review`.
3. A maintainer checks the evidence and, only when it meets the standard, applies `status: graduation approved`.
4. The graduation workflow adds `badge: four-week AI Learning Hub graduate`, removes the review label, and leaves an auditable GitHub comment.
5. If notifications are enabled and the approved GitHub user appears in the private opt-in registry, the workflow sends the Day 0 email and attaches a print-ready certificate.
6. If notification settings or an opt-in registry entry are missing, no email is sent. The credential approval remains valid and visible on GitHub.

## Required private configuration

Set these values in repository or organization settings. Never place them in issues, commits, Markdown files, screenshots, or chat messages.

| Type | Name | Purpose |
|---|---|---|
| Repository variable | `GRADUATE_EMAIL_NOTIFICATIONS_ENABLED` | Set to `true` only after testing and privacy review; leave unset or `false` to disable all sends. |
| Repository variable | `SMTP_USE_TLS` | Set to `true` for a TLS-enabled SMTP connection unless the mail provider documents another requirement. |
| Secret | `SMTP_HOST` | Mail server hostname. |
| Secret | `SMTP_PORT` | Mail server port. |
| Secret | `SMTP_USERNAME` | SMTP account username. |
| Secret | `SMTP_PASSWORD` | SMTP account password or provider-issued application password. |
| Secret | `SMTP_FROM` | Approved sender address. |
| Secret | `GRADUATE_EMAIL_REGISTRY` | Private JSON mapping of GitHub user names to opted-in recipient data. |

## Private opt-in registry format

Store the following JSON in the **`GRADUATE_EMAIL_REGISTRY`** secret. Replace all placeholders before saving it. The values in this example are not real addresses.

```json
{
  "example-github-user": {
    "email": "member@example.invalid",
    "opt_in": true,
    "followup_opt_in": true,
    "display_name": "Example Member",
    "certificate_name": "Example Member",
    "graduated_on": "2026-08-14",
    "issue_url": "https://github.com/Automation-Legends/ai-learning-hub/issues/123"
  }
}
```

| Field | Required for | Meaning |
|---|---|---|
| GitHub username key | All messages | Must match the username that opened the approved completion claim. |
| `email` | All messages | Private recipient address. |
| `opt_in` | All messages | Must be `true`; otherwise no message is sent. |
| `followup_opt_in` | Day 7 and Day 30 only | Must be `true` to receive optional follow-ups. |
| `display_name` | All messages | Friendly name for the email; GitHub username is used if omitted. |
| `certificate_name` | Day 0 certificate | Approved name shown on the attached certificate; `display_name` is used if omitted. |
| `graduated_on` | Day 7 and Day 30 only | Approval date in `YYYY-MM-DD` format. |
| `issue_url` | All messages | Link to the approved evidence record. |

## Privacy and consent rules

- Ask a member for an email address and notification preference through a private, consent-aware process—not a public GitHub issue.
- Add a recipient only after they opt in. Record the date and source of consent in a private maintainer-controlled record.
- Set `opt_in` to `false` or remove the member from the private registry immediately when they withdraw consent.
- Keep public issue comments free of email addresses, certificates that contain personal information, and other private data.
- Do not use the notification workflow for marketing messages outside the documented Day 0, Day 7, and Day 30 learning-community sequence without renewed consent.
- Treat the certificate as a record of course completion and community practice, not a professional certification or deployment authorization.

## Maintainer activation checklist

- [ ] A mail provider and sender address have been approved.
- [ ] SMTP credentials are stored only as secrets.
- [ ] `GRADUATE_EMAIL_REGISTRY` uses placeholder-free, valid JSON and contains only opted-in recipients.
- [ ] `GRADUATE_EMAIL_NOTIFICATIONS_ENABLED` remains `false` during setup.
- [ ] A test account with explicit consent is added to the private registry.
- [ ] The Day 0 workflow is tested on a disposable test completion claim.
- [ ] The attached certificate renders correctly and the evidence-record link is correct.
- [ ] The Day 7 and Day 30 scheduled workflow is tested with a test recipient before enabling routine use.
- [ ] `GRADUATE_EMAIL_NOTIFICATIONS_ENABLED` is set to `true` only after the checks above pass.

## Pause, repair, or disable delivery

To stop all sends immediately, set **`GRADUATE_EMAIL_NOTIFICATIONS_ENABLED`** to `false`. To stop one person’s messages, set their `opt_in` value to `false` or remove their registry entry. If an email fails because a secret or mapping is missing, correct the private configuration and rerun the relevant workflow only after confirming that the recipient has consented.

## Files used by the sequence

| File | Role |
|---|---|
| [Graduation workflow](../.github/workflows/award-graduation-badge.yml) | Awards the graduate badge after maintainer approval and sends the Day 0 email when enabled. |
| [Follow-up workflow](../.github/workflows/send-graduate-followups.yml) | Checks daily for opted-in Day 7 and Day 30 follow-ups when enabled. |
| [Sequence email sender](../.github/scripts/send_graduate_sequence_email.py) | Creates the message and attaches the Day 0 certificate. |
| [Follow-up scheduler](../.github/scripts/send_due_graduate_followups.py) | Finds opted-in graduates due a follow-up message. |
