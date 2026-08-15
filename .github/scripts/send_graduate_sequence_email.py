import json
import os
import smtplib
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from html import escape


STAGES = {
    "initial": {
        "subject": "Congratulations — You completed the AI Learning Hub",
        "heading": "Congratulations, {name}!",
        "text": "You have been recognized as an Automation Legends AI Learning Hub Graduate after completing the four-week curriculum and receiving maintainer approval. Your print-ready completion certificate is attached.",
        "html": "You have been recognized as an <strong>Automation Legends AI Learning Hub Graduate</strong> after completing the four-week curriculum and receiving maintainer approval. Your print-ready completion certificate is attached.",
        "attach_certificate": True,
    },
    "followup_7": {
        "subject": "Keep building after your AI Learning Hub graduation",
        "heading": "One week after graduation, {name}",
        "text": "Congratulations again on completing the AI Learning Hub. If you want a practical next step, choose one capstone artifact to improve, share a sanitized project showcase, or support a new member with one verification or workflow-design tip.",
        "html": "Congratulations again on completing the AI Learning Hub. If you want a practical next step, choose one capstone artifact to improve, share a sanitized project showcase, or support a new member with one verification or workflow-design tip.",
        "attach_certificate": False,
    },
    "followup_30": {
        "subject": "Share what the AI Learning Hub helped you practice",
        "heading": "One month after graduation, {name}",
        "text": "Your experience can improve the next cohort. If you are comfortable, share one learning outcome, one limitation you discovered, or one resource you would improve. You may also contribute a safe prompt, workflow example, or project-showcase update.",
        "html": "Your experience can improve the next cohort. If you are comfortable, share one learning outcome, one limitation you discovered, or one resource you would improve. You may also contribute a safe prompt, workflow example, or project-showcase update.",
        "attach_certificate": False,
    },
}


def require(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Missing required configuration: {name}")
    return value


def certificate_html(name: str, completion_date: str, issue_url: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>AI Learning Hub Certificate of Completion</title>
<style>
body {{ font-family: Arial, sans-serif; color: #111827; background: #ffffff; }}
.certificate {{ width: 900px; margin: 30px auto; border: 8px solid #4F46E5; padding: 60px; text-align: center; }}
h1 {{ font-size: 44px; margin: 0; }} h2 {{ font-size: 32px; margin: 28px 0 8px; }}
p {{ font-size: 18px; line-height: 1.6; }} .note {{ font-size: 13px; color: #4B5563; margin-top: 36px; }}
</style></head>
<body><main class="certificate">
<p><strong>AUTOMATION LEGENDS</strong><br>AI LEARNING HUB</p>
<h1>Certificate of Completion</h1><p>This certificate recognizes</p><h2>{escape(name)}</h2>
<p>for completing the four-week AI Learning Hub curriculum through evidence-based practice in foundations, workflow design, advanced-system boundaries, and collaborative capstone work.</p>
<p><strong>Completion date:</strong> {escape(completion_date)}</p>
<p><strong>Evidence record:</strong> <a href="{escape(issue_url)}">{escape(issue_url)}</a></p>
<p class="note">This certificate recognizes curriculum completion and community practice. It is not a professional certification, employment qualification, or authorization to deploy high-impact AI systems.</p>
</main></body></html>"""


def main() -> int:
    stage = os.getenv("GRADUATE_EMAIL_STAGE", "initial").strip()
    if stage not in STAGES:
        raise ValueError(f"Unsupported graduate email stage: {stage}")

    github_login = require("GRADUATE_GITHUB_LOGIN")
    registry_raw = os.getenv("GRADUATE_EMAIL_REGISTRY", "").strip()
    if not registry_raw:
        print("Graduate email registry is not configured; no email sent.")
        return 0

    try:
        registry = json.loads(registry_raw)
    except json.JSONDecodeError as error:
        raise ValueError("GRADUATE_EMAIL_REGISTRY must be valid JSON.") from error

    recipient = registry.get(github_login, {})
    if not recipient.get("opt_in") or not recipient.get("email"):
        print(f"No opt-in email recipient is configured for GitHub user '{github_login}'; no email sent.")
        return 0

    smtp_host = require("SMTP_HOST")
    smtp_port = int(require("SMTP_PORT"))
    smtp_username = require("SMTP_USERNAME")
    smtp_password = require("SMTP_PASSWORD")
    smtp_from = require("SMTP_FROM")
    issue_url = require("GRADUATE_ISSUE_URL")
    display_name = recipient.get("certificate_name") or recipient.get("display_name") or github_login
    completion_date = os.getenv("GRADUATE_COMPLETION_DATE", "").strip() or datetime.now(timezone.utc).strftime("%B %d, %Y")
    stage_copy = STAGES[stage]

    message = EmailMessage()
    message["Subject"] = stage_copy["subject"]
    message["From"] = smtp_from
    message["To"] = recipient["email"]
    message.set_content(
        f"""{stage_copy['heading'].format(name=display_name)}

{stage_copy['text']}

Your approved evidence record is available here: {issue_url}

This communication recognizes evidence-based community practice. It is not a professional certification, employment qualification, or authorization to deploy high-impact AI systems.

To stop these optional graduate follow-ups, ask an Automation Legends maintainer to remove your notification opt-in.

Automation Legends AI Learning Hub"""
    )
    message.add_alternative(
        f"""<html><body><h1>{escape(stage_copy['heading'].format(name=display_name))}</h1>
<p>{stage_copy['html']}</p>
<p>Your approved evidence record is available <a href="{escape(issue_url)}">here</a>.</p>
<p>This communication recognizes evidence-based community practice. It is not a professional certification, employment qualification, or authorization to deploy high-impact AI systems.</p>
<p>To stop these optional graduate follow-ups, ask an Automation Legends maintainer to remove your notification opt-in.</p>
<p>Automation Legends AI Learning Hub</p></body></html>""",
        subtype="html",
    )

    if stage_copy["attach_certificate"]:
        message.add_attachment(
            certificate_html(display_name, completion_date, issue_url).encode("utf-8"),
            maintype="text",
            subtype="html",
            filename="automation-legends-ai-learning-hub-certificate.html",
        )

    use_tls = os.getenv("SMTP_USE_TLS", "true").strip().lower() != "false"
    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as smtp:
        if use_tls:
            smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(message)

    print(f"Graduate notification stage '{stage}' sent for GitHub user '{github_login}'.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Graduate notification failed: {error}", file=sys.stderr)
        raise
