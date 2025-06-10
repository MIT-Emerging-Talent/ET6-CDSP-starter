# Contribution Guidelines

Welcome, and thank you for your interest in contributing to our project!

This document outlines how we work as a team, how we manage contributions via
GitHub, and how we communicate. Please take a moment to read through these
guidelines before starting any task or submitting a pull request.

---

## General Workflow

- We use **GitHub Issues** and a **project board** to track progress.
- All issues in the **To Do** list are open to anyone, unless explicitly assigned.
- If you want to take an issue:
  1. Assign it to yourself.
  2. Leave a comment in the issue: `"I'll take this one"` (or similar).
  3. Move the issue to the **In Progress** column on the board.
- Once the task is complete and reviewed, move it to **Done**.

---

## GitHub Flow

### Issues

- Always add issues to the project board.
- Write a clear description of the problem or task.
- If possible, create a branch directly from the issue.
- If you created the branch separately, link it to the issue manually.
- Use labels when appropriate, especially:
  - `team-input-needed` – when you need help or feedback.
  - `discussion` – to raise questions or suggestions.

### Pull Requests

- Every change must go through a **Pull Request**.
- Every PR must be **linked to an issue**.
- Every PR must be **reviewed by at least one team member** before being merged.
- In your PR description, briefly explain what was done and why.
- Keep your branches up to date with the base branch before requesting a review.

---

## Markdown & Linting

- Before committing Markdown files, run a linter (e.g., `markdownlint`).
- Pay attention to common rule violations:
  - `MD013` – Line length too long (keep it under 120 chars).
  - `MD024` – Duplicate headings at the same level.
  - `MD031` – Blank lines before/after headings.
  - `MD001` – Headings should be incremented just by one level at a time.
  - `MD022` – Headings should be surrounded by blank lines.
  - `MD041` – First line should be an H1 heading.
- If you see markdown warnings, fix them as part of your contribution.

---

## Communication

- Our **primary communication platform is Slack**.
  - For quick pings or informal coordination, we have a **WhatsApp group**.
  - If you need help or think your work might interest others, feel free to share
  it or mention someone in Slack.
- We have **two team calls per week**. The meeting link is pinned in our Slack workspace.
- If you're working on a task, keep the issue and board updated — that helps
  everyone stay on the same page.

---

## Contribution Checklist

Before creating or merging a PR, make sure you:

- [ ] Created an issue with a clear description.
- [ ] Linked the issue to the project board.
- [ ] Created a branch from or linked it to the issue.
- [ ] Left a comment if you self-assigned an issue from the To Do list.
- [ ] Ran markdown linter and fixed any issues.
- [ ] Requested review from at least one team member.
- [ ] Updated the issue status on the board (In Progress / Done).
- [ ] Used labels like `team-input-needed` if collaboration is required.
- [ ] Confirmed that all comments, suggestions, or change requests have been addressed before merging.

---

Thank you for helping us build a better project, together 💙
