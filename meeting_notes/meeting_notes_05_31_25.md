# Meeting Minutes – 05/31/2025

**Meeting Time:** 7:00 AM – 8:00 AM PST  
**Location:** Google Meet  
**Attendees:**

- Kervens Louis  
- Olumide Kolawole  
- Dorcas Njeri  

---

## 1. Overview

1. Reviewed repository changes and updates made by team members.  
2. Olumide demoed key Git/GitHub workflows as a refresher.

---

## 2. Git Refresher: Key Concepts Covered

### 2.1 `git switch -c branch-name`

**What it does:**  
Creates a new branch named `branch-name` and immediately switches
(checks out) to it.

**Why use it:**  

- Keeps new features or fixes isolated from the `main` (or `master`)
branch until they’re ready to merge.  
- Prevents accidental commits on the primary integration branch.

**How it works under the hood:**  

1. `git branch branch-name` – Creates a new branch pointer at the current commit.
2. `git switch branch-name` – Moves `HEAD` to the new branch so subsequent
commits go there.  
3. By combining those two steps, `git switch -c branch-name` does both in one command:

\`\`\`
$ git switch -c feature/login-form
 → Creates “feature/login-form” at the current commit, then checks it out
\`\`\`

**Best practices / Tips:**  

- **Naming conventions:**  
  - `feature/xxx` for new features  
  - `bugfix/yyy` for bug fixes  
  - `hotfix/zzz` for urgent production fixes  
- **Always start from an up-to-date base:**

  \`\`\`
  $ git checkout main
  $ git pull origin main
  $ git switch -c feature/your-thing
  \`\`\`

---

### 2.2 `git checkout main`

**What it does:**  
Switches (checks out) your working directory to the `main` branch.

**Why use it:**  

- Returns to your primary integration branch (often named `main` or `master`).  
- Pulls the latest upstream changes:

  \`\`\`
  $ git pull origin main
  \`\`\`

- Starts a new branch from a clean, up-to-date `main`.  
- Merges completed feature branches back into `main`.

> **Note:** As of Git 2.23+, you can also use `git switch main`. However, `git
> checkout main` remains valid for switching branches.

**Typical workflow context:**

\`\`\`

## 1) Ensure no uncommitted changes (or stash them)

$ git status

## If there are changes, either commit them or run

$ git stash

## 2) Switch back to main

$ git checkout main

## 3) Fetch and merge remote updates

$ git pull origin main

## 4) Create a new branch if needed

$ git switch -c feature/new-stuff
\`\`\`

---

### 2.3 `git branch`

**What it does (no arguments):**  
Lists all local branches, showing which one is currently checked out
(marked with an asterisk `*`).

**With arguments, you can:**  

- **Create** a new branch:

  \`\`\`
  git branch branchname
  \`\`\`

- **Delete** a branch:

  \`\`\`
  git branch -d branchname
  \`\`\`

- **Rename** the current branch:

  \`\`\`
  git branch -m new-name
  \`\`\`

**How to interpret the output:**

\`\`\`
$ git branch
  develop

- feature/login-form
  main
  release/v1.2
\`\`\`

- The `*` indicates the branch you’re “on” (where `HEAD` is pointing).  
- Other lines list all local branches.

**Why use it:**  

- Quickly see which branches exist locally and identify the active one.  
- Confirm that a new branch was created successfully.  
- Find old or merged branches that can be cleaned up.

---

### 2.4 `git add .`

**What it does:**  
Stages all changes—new files, modifications, and deletions—in the current
directory and its subdirectories, preparing them for commit.

**Why use it:**  

- After editing files, creating new ones, or deleting files, you must
stage those changes before committing.  

- `git add .` is a convenient way to include everything at once.

**Important nuances:**  

- **New (untracked) files:**  
  - `git add .` picks up new files and stages them.  
- **Modified files:**  
  - Any tracked files that were changed get staged.  
- **Deleted files:**  
  - If you ran `rm filename.txt`, `git add .` stages that deletion as well.  

**Caution:** Because it stages *every* change under the current directory,
double-check that you want to commit everything.
If you only want specific files, use:

\`\`\`
git add path/to/file1 path/to/file2
\`\`\`

or interactively:

\`\`\`
git add -p
\`\`\`

This lets you review hunks of changes before staging.

**Example workflow:**

\`\`\`

## 1) Make changes in your working directory

## - Edit src/app.js

## - Create tests/app.test.js

## - Delete old_config.json

$ git status

## Shows

## modified:   src/app.js

## untracked:  tests/app.test.js

## deleted:    old_config.json

## 2) Stage everything

$ git add .

## 3) Verify staged changes

$ git status

## Shows under “Changes to be committed”

## modified:  src/app.js

## new file:   tests/app.test.js

## deleted: old_config.json

\`\`\`

---

### 2.5 `git commit -m "commit message"`

**What it does:**  
Records a new snapshot (a commit) in your local repository.
The `-m` flag provides the commit message inline, avoiding the need to open an editor.

**Why use it:**  

- Every time you reach a logical milestone—e.g.,
“Finished login form validation” or “Fixed date-format bug”—you create a commit.
- A clear, concise commit message helps your teammates
(and your future self)understand what changed and why.

**Anatomy of a good commit message:**

\`\`\`
$ git commit -m "Add login form validation and error messages"
\`\`\`

- **Verb (imperative mood):** Start with a short action word
(Add, Fix, Refactor, etc.).  

- **Scope (optional):** You can include a scope in parentheses, e.g.,

- **Detail (optional):** After a blank line, explain *why* you made the change,
if it isn’t obvious from the diff.

> **Tip:** If you omit `-m "..."`, Git opens your default editor so you
> can write a multi-line message.

**Typical workflow context:**

1. Stage your changes:

 \`\`\`
 $ git add .
 \`\`\`
2. Commit them:

 \`\`\`
 $ git commit -m "Implement initial login form UI and validation"
 \`\`\`
3. After this command, your local branch contains a new commit that the remote
(e.g., GitHub) doesn’t have—yet.

---

### 2.6 `git push origin branch`

**What it does:**  

Uploads the commits on your local `branch` to the remote repository
named `origin`. In other words, it shares your work with
teammates (or triggers CI).

**Why use it:**  

- Once you’ve committed locally and want others to
see your feature/fix, use `git push`.  
- This updates `origin/branch` (creating it if it doesn’t exist)
to match your local branch.

**Syntax breakdown:**

\`\`\`
git push origin feature/login-form
\`\`\`

- `origin`: The default name for the remote repo you cloned from
(e.g., `https://github.com/your-org/your-repo.git`).

- `feature/login-form`: The branch you want to push.
If `origin/feature/login-form` doesn’t exist yet,
this command creates it (assuming you have permission).

**Common variations:**  

- **Set upstream in one shot:**  

For a brand-new branch, run:
\`\`\`
git push --set-upstream origin feature/login-form
\`\`\`

This tells Git to record that `feature/login-form`
should track `origin/feature/login-form`.
Afterward, you can simply run `git push` on that branch.

- **Force push (⚠️ use with caution):**  

\`\`\`
git push --force origin branch
\`\`\`  

Overwrites the remote branch to match your local history,
even if the remote has commits you don’t. Only use this after
rebasing or if the team agrees.  

- **Push tags:**  
If you’ve tagged a commit locally (`git tag v1.0`), you can push that tag with:
\`\`\`
git push origin v1.0
\`\`\`  
Or push all tags at once:
\`\`\`
git push origin --tags
\`\`\`

---

### 2.7 Typical End-to-End Feature-Branch Workflow

1. **Start from `main` (or your integration branch):**  
 \`\`\`
 $ git checkout main
 $ git pull origin main
 \`\`\`

2. **Create and switch to a new feature branch:**  
 \`\`\`
 $ git switch -c feature/amazing-widget
 \`\`\`

3. **Work locally:**  

- Edit existing files  
- Create new files  
- Delete old files  

**Stage changes:**  

 \`\`\`
 $ git add .
 \`\`\`

**Commit:**  
 \`\`\`
 $ git commit -m "Add initial implementation of amazing widget"
 \`\`\`

**Push your feature branch to the remote:**  
 \`\`\`
 $ git push --set-upstream origin feature/amazing-widget
 \`\`\`  
 (After this initial push, you can simply use `git push` next time.)

**Create a Pull Request (PR)/Merge Request (MR):**

- Most hosting platforms (GitHub, GitLab, Bitbucket) will prompt you
with a “Compare & pull request” button once you push a new branch.
- Open the PR, request reviews, and assign labels as appropriate.

**Merge back into `main`:**

- Once the PR is approved, merge it.  
- Then update your local `main`:  
   \`\`\`
   $ git checkout main
   $ git pull origin main
   \`\`\`

**Clean up old feature branches:**  
 \`\`\`
 $ git branch -d feature/amazing-widget
 $ git push origin --delete feature/amazing-widget
 \`\`\`

---

## GitHub & Project Board Topics

- **Pull Requests:**  
- How to open a PR, assign reviewers, and add labels.  
- Best practices for writing a clear description and linking to issue/ticket numbers.

- **Project Board Updates:**  
- Move cards between columns (e.g., “To Do,” “In Progress,” “Review,” “Done”).  
- Add any relevant notes or checklists to each card.  

---

## 4. Team Decision: Standard Time Zone

Since each member is in a different time zone, we agreed to adopt
**MIT/Boston time(EDT, UTC –4 hours)** as the team standard for all scheduled
stand-ups, deadlines, and deliverables.  

> **Time Zone:** EDT (Eastern Daylight Time) UTC –4 hours

---

## 5. Deliverables & Next Steps

- **Deliverable Due Monday (06/02/2025):**  
- Finalize our current feature branch and merge into `main`.  
- Ensure code review is complete and any outstanding comments are addressed.  
- Update the project board, moving cards to “Done” for completed tasks.  

- **By Monday:**  
- Get additional team members involved in the overall process
(assign new sub-tasks, onboard them to the repo, and walk them through the Git
workflow).

---
<!-- markdownlint-enable MD013 -->

### 5.1 Action Items

| Owner   | Task                                                                                     | Due Date    |
| ------- | ---------------------------------------------------------------------------------------- | ----------- |
| Olumide | Merge feature branch into `main` after final review.                                     | 06/02/2025  |
| Kervens | Assign new team members to specific project-board cards and schedule a brief orientation. | 06/02/2025  |
| Dorcas  | Update project board to reflect merged work and prepare any remaining tasks for Monday.  | 06/02/2025  |

<!-- markdownlint-disable MD013 -->
---

**Minutes prepared by:** Olumide Kolawole  
**Date:** 05/31/2025

## Problem Identification Deliverables

As a team, we’ll submit the following items under `0_domain_research/` and in our main README:

1. **Problem-Statement (Personal Context)**
   - A concise statement of the problem, grounded in your own experiences.

2. **Domain Background Review** (`0_domain_research/`)
   - Collate relevant literature, articles, and notes about our chosen domain.
   - Explain why this domain matters and how our problem fits into it.

3. **Group’s Summary of Domain Understanding**
   - A high-level overview of how we see the domain’s structure, stakeholders, and workflows.
   - (Bonus) Apply systems thinking—map out key actors, processes, and dependencies.

4. **Actionable Research Question**
   - One clear, data-science–oriented question that we can realistically answer given our tools and timeline.
   - Ensure it’s specific, measurable, and grounded in the constraints we’re facing (data access, team bandwidth, etc.).

5. **Planning Documents** (in the repository)
   - **Group Norms**: How we’ll collaborate, make decisions, and resolve conflicts.
   - **Learning Goals**: What each member hopes to achieve (skills, knowledge, etc.) by this milestone.
   - **Constraints & Assumptions**: Time, tools, data availability, technology stack, etc.
   - **Communication Plan**: Preferred channels (Slack, email, GitHub), meeting cadence, and response expectations.

6. **Milestone Retrospective**
   - Reflect on what worked, what didn’t, and any adjustments needed for the next phase.
   - Keep it candid—identify blockers, successes, and lessons learned.

7. **Milestone Survey**
   - Complete the required survey form (link provided by the instructor).
   - Summarize any key takeaways or feedback in our README.

---

### Where to Put Everything

- **`README.md`** (root)
  - Add a “Problem Identification” heading (the checklist above), with links to any subfolders or files.
  - Include brief summaries for items 1, 4, 6, and 7 directly under their respective headings.

- **`0_domain_research/`** (new folder)
  - Place all background review materials (articles, notes, slides).
  - Include a `domain_understanding.md` with your systems-thinking diagram or summary.

- **`planning/`** (new folder)
  - `group_norms.md`
  - `learning_goals.md`
  - `constraints_assumptions.md`
  - `communication_plan.md`

- **`retrospective/`** (new folder)
  - `milestone_retrospective.md`

> Once each document is complete, be sure to commit and push to the repo so everyone can review and contribute.
