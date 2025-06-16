<!-- markdownlint-disable MD001 -->
<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD033 -->
<!--
Explanation:
- MD001: Disabled because HTML <details> tags are used for collapsible sections, which causes skipping heading levels.
- MD013: Disabled to allow longer lines for better-looking tables.
- MD033: Disabled because HTML (such as <details> and <summary> for collapsibles) is used in this file.

These rules are temporarily disabled to improve the visual quality and readability of this document.
-->
# CONTRIBUTING.md

Welcome to The Data Detectives! 👋

We are an international, interdisciplinary team working across time zones, cultures,
and communication styles. To ensure respectful, inclusive, and effective collaboration,
please follow these guidelines when contributing to this project. 👇

---

<details open>
<summary><h2>🏗️ Repository Structure</h2></summary>

Please take a moment to get acquainted with the key directories and files in this repository:

| Path                                   | Description                                                                          |
|-----------------------------------------|--------------------------------------------------------------------------------------|
| **/collaboration**                      | Materials for team communication, group norms, learning goals, constraints, and retrospectives. |
| **/notes**                              | Shared tools, guides, resources and useful references for the team.                            |
| **/0_domain_study → /6_final_presentation** | Project deliverables arranged by milestones |
| **README.md, CONTRIBUTING.md**          | Core documentation for understanding and contributing to the project.                 |

</details>

---

<details>
<summary><h2>🌍 Be Culturally Respectful</h2></summary>

- Assume positive intent — differences in expression or tone may reflect cultural backgrounds, not disrespect.
- Limit the use of idioms, slang, or culture-specific references, or explain them if used.
- Remember that holidays and weekends may vary across cultures and locations.

</details>

---

<details>
<summary><h2>🕓 Respect Time Zones and Asynchronous Work</h2></summary>

- Don’t expect instant responses; allow time for team members to reply.
- Use clear dates and specify time zones when coordinating meetings or deadlines.
- Document any decisions so collaborators in other time zones stay in the loop.
- Assign and track tasks on the GitHub Project Board for team-wide visibility.

</details>

---

<details>
<summary><h2>💬 Communicate Clearly</h2></summary>

- Keep your messages clear and to the point.
- Use lists, visuals, or brief summaries to break down complex ideas.
- Request clarification if you’re confused, and be patient with questions from others.

</details>

---

<details>
<summary><h2>🎯 Contribute Inclusively</h2></summary>

- Invite participation from everyone, especially those less comfortable with language or tools.
- Value different working styles, speeds, and levels of experience.
- Use shared docs and GitHub Issues to ensure everyone can contribute and stay informed.

</details>

---

<details>
<summary><h2>🛠 GitHub Workflow</h2></summary>

### 1. 🖇️ Cloning the Repository

- You can either:

  - Use VSCode → "Clone Git Repository"
  
  - Or use terminal with following command:

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-19-repo.git
cd ET6-CDSP-group-19-repo
```

---

### 2. 🌿 Creating & Updating a Branch

- Make a new branch for your feature or fix:

  ```bash
  git checkout -b your_branch_name
  ```

  ✔ Use clear names: `docs-collaboration`, `bug-fix`

- To keep your branch updated with main:

  ```bash
  git checkout main
  git pull origin main
  git checkout your_branch_name
  git merge main
  ```

---

### 3. 🚀 Making & Pushing Changes

- Only stage files you intend to change:

  ```bash
  git add specific_file.py      
  git commit -m "feat: add milestone summary"
  git push origin your_branch_name
  ```

  ❌ Avoid using 'git add .'

---

### 4. 🧩 Working with Issues

- Always check for an existing issue before creating a new one.
- Use issues for bugs, ideas, or questions; describe your suggestion, get feedback, and make sure it fits team priorities.
- Write clear titles and details.
- Assign yourself to an issue when you start.
- Reference issues in Pull Requests (e.g., `Closes #7`).

---

### 5. 📥 Creating a Pull Request (PR)

- After pushing your branch:

  - **Option 1:** Click **Compare & Pull Request** on the repo homepage.
  - **Option 2:**  
    1. Go to the Pull Requests tab → New Pull Request  
    2. Select your branch and `main`  
    3. Click **Create Pull Request**

- Your PR should include:

  - What you changed & why
  - Linked issue (e.g., `Closes #4`)
  - Screenshots or notes if helpful

❗ Every PR must be reviewed by **at least two members** before merging.

---

### 6. 🔁 Review & Merge

- Assign reviewers and move your task to **Ready for Review** on the Project Board.
- After approval, click **Merge pull request → Confirm merge.**
- Move the corresponding card to **Done** on the Project Board.

---

### 7. ⚔️ Resolving Merge Conflicts

- If your branch is behind `main`, follow these steps:

```bash
git checkout main
git pull origin main
git checkout your_branch_name
git merge main
```

- If there are conflicts:

  - VSCode will highlight the conflicting areas (`<<<<<<<`)
  - Manually edit files to resolve

- After fixing each file:

```bash
git add resolved_file.py
```

- Finalize the merge:

```bash
git commit -m "resolve merge conflict with main"
```

❗If you're unsure, don’t hesitate to ask the team before committing.

---

### 8. 📌 Using the Project Board

- The GitHub Project Board helps us stay organized.
- Every task should begin as an **Issue**.
- Move tasks to **In Progress** when you start.
- Move to **Ready for Review** with an open PR.
- Move to **Done** after merging.
- Keep the board updated for async teamwork.

</details>

---

## 🤝 Let’s Build Together

This is a learning environment—everyone brings something valuable.  
Let’s co-create a respectful and inclusive space where differences are strengths, and feedback is welcomed as a tool for collective growth.

---

Thank you for contributing! 💙
