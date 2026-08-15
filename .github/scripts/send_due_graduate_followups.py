import json
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import send_graduate_sequence_email as notifier  # noqa: E402


def parse_graduated_on(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def main() -> int:
    registry_raw = os.getenv("GRADUATE_EMAIL_REGISTRY", "").strip()
    if not registry_raw:
        print("Graduate email registry is not configured; no follow-up emails sent.")
        return 0

    try:
        registry = json.loads(registry_raw)
    except json.JSONDecodeError as error:
        raise ValueError("GRADUATE_EMAIL_REGISTRY must be valid JSON.") from error

    today = date.today()
    stages_sent = 0
    for github_login, recipient in registry.items():
        if not recipient.get("opt_in") or not recipient.get("followup_opt_in"):
            continue
        if not recipient.get("graduated_on") or not recipient.get("issue_url"):
            continue

        graduated_on = parse_graduated_on(recipient["graduated_on"])
        if today == graduated_on + timedelta(days=7):
            stage = "followup_7"
        elif today == graduated_on + timedelta(days=30):
            stage = "followup_30"
        else:
            continue

        os.environ["GRADUATE_GITHUB_LOGIN"] = github_login
        os.environ["GRADUATE_ISSUE_URL"] = recipient["issue_url"]
        os.environ["GRADUATE_COMPLETION_DATE"] = recipient["graduated_on"]
        os.environ["GRADUATE_EMAIL_STAGE"] = stage
        notifier.main()
        stages_sent += 1

    print(f"Completed graduate follow-up check; sent {stages_sent} opt-in message(s).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Graduate follow-up processing failed: {error}", file=sys.stderr)
        raise
