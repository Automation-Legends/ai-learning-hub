import os
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]


def load_yaml(relative_path: str):
    return yaml.safe_load((REPO / relative_path).read_text(encoding="utf-8"))


def trigger(workflow):
    return workflow.get("on", workflow.get(True))


def front_matter(relative_path: str):
    text = (REPO / relative_path).read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def simulate_graduation(labels, notifications_enabled):
    labels = list(labels)
    actions = []
    is_claim = "type: four-week completion claim" in labels
    has_approval = "status: graduation approved" in labels
    has_badge = "badge: four-week AI Learning Hub graduate" in labels

    if not (is_claim and has_approval):
        return {"badge_awarded": False, "email_runs": False, "actions": actions}
    if has_badge:
        return {"badge_awarded": False, "email_runs": False, "actions": actions}

    actions.append("add:badge: four-week AI Learning Hub graduate")
    if "status: graduation review" in labels:
        actions.append("remove:status: graduation review")
    actions.append("comment:four-week completion approved")
    return {
        "badge_awarded": True,
        "email_runs": notifications_enabled,
        "actions": actions,
    }


def simulate_capstone_tracker(labels):
    labels = list(labels)
    if "type: capstone team" in labels:
        actions = []
        if "status: capstone team forming" not in labels:
            actions.append("add:status: capstone team forming")
        actions.append("comment:team orientation")
        return actions
    if "type: capstone progress" in labels:
        actions = []
        if "status: capstone review" not in labels:
            actions.append("add:status: capstone review")
        actions.append("comment:progress orientation")
        return actions
    return []


class CommunityAutomationSandboxTests(unittest.TestCase):
    def test_workflows_have_expected_events_and_permissions(self):
        graduation = load_yaml(".github/workflows/award-graduation-badge.yml")
        tracker = load_yaml(".github/workflows/capstone-tracking-runner.yml")
        followups = load_yaml(".github/workflows/send-graduate-followups.yml")

        self.assertEqual(trigger(graduation)["issues"]["types"], ["labeled"])
        self.assertEqual(graduation["permissions"]["issues"], "write")
        self.assertEqual(trigger(tracker)["issues"]["types"], ["opened", "labeled"])
        self.assertEqual(tracker["permissions"]["issues"], "write")
        self.assertIn("schedule", trigger(followups))
        self.assertIn("GRADUATE_EMAIL_NOTIFICATIONS_ENABLED", (REPO / ".github/workflows/send-graduate-followups.yml").read_text())

    def test_issue_templates_apply_tracking_types(self):
        completion = front_matter(".github/ISSUE_TEMPLATE/four-week-completion-claim.md")
        team = front_matter(".github/ISSUE_TEMPLATE/capstone-team-formation.md")
        progress = front_matter(".github/ISSUE_TEMPLATE/capstone-progress-update.md")

        self.assertIn("type: four-week completion claim", completion["labels"])
        self.assertIn("status: graduation review", completion["labels"])
        self.assertIn("type: capstone team", team["labels"])
        self.assertIn("type: capstone progress", progress["labels"])

    def test_approved_completion_awards_badge_and_runs_email_when_enabled(self):
        result = simulate_graduation(
            [
                "type: four-week completion claim",
                "status: graduation review",
                "status: graduation approved",
            ],
            notifications_enabled=True,
        )
        self.assertTrue(result["badge_awarded"])
        self.assertTrue(result["email_runs"])
        self.assertEqual(
            result["actions"],
            [
                "add:badge: four-week AI Learning Hub graduate",
                "remove:status: graduation review",
                "comment:four-week completion approved",
            ],
        )

    def test_unapproved_or_already_badged_completion_does_not_send_email(self):
        unapproved = simulate_graduation(
            ["type: four-week completion claim", "status: graduation review"],
            notifications_enabled=True,
        )
        already_badged = simulate_graduation(
            [
                "type: four-week completion claim",
                "status: graduation approved",
                "badge: four-week AI Learning Hub graduate",
            ],
            notifications_enabled=True,
        )
        self.assertFalse(unapproved["badge_awarded"])
        self.assertFalse(unapproved["email_runs"])
        self.assertFalse(already_badged["badge_awarded"])
        self.assertFalse(already_badged["email_runs"])

    def test_capstone_team_and_progress_records_receive_only_orientation_actions(self):
        team_actions = simulate_capstone_tracker(["type: capstone team"])
        progress_actions = simulate_capstone_tracker(["type: capstone progress"])
        unrelated_actions = simulate_capstone_tracker(["documentation"])

        self.assertEqual(team_actions, ["add:status: capstone team forming", "comment:team orientation"])
        self.assertEqual(progress_actions, ["add:status: capstone review", "comment:progress orientation"])
        self.assertEqual(unrelated_actions, [])

    def test_email_scripts_exit_safely_without_a_private_registry(self):
        base_environment = os.environ.copy()
        base_environment.pop("GRADUATE_EMAIL_REGISTRY", None)
        base_environment["GRADUATE_GITHUB_LOGIN"] = "sandbox-user"

        initial = subprocess.run(
            [sys.executable, ".github/scripts/send_graduate_sequence_email.py"],
            cwd=REPO,
            env=base_environment,
            capture_output=True,
            text=True,
            check=True,
        )
        followups = subprocess.run(
            [sys.executable, ".github/scripts/send_due_graduate_followups.py"],
            cwd=REPO,
            env=base_environment,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("no email sent", initial.stdout.lower())
        self.assertIn("no follow-up emails sent", followups.stdout.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
