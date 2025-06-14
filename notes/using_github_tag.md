# Git Tagging Instructions for Milestone Submission

For each milestone, we must create a **Git tag** so that reviewers know which
version of our project to review. Think of a tag like a "save point"
— it freezes our work at a specific stage.

Please follow the instructions below carefully.

---

## Step 1: Make Sure All Work Is Committed

Before tagging, make sure that everyone’s work (especially the research files
in the `0_domain_research/` folder) is already added, committed, and pushed
to the main branch.

To check:

- Did you see your name’s file inside the `0_domain_research/` folder?
- Did you commit and push your changes?

If yes, move to Step 2.

---

## Step 2: Create a Tag for the Milestone

Now we create a label for our current version.

In your terminal or GitHub desktop, create a tag called:

`milestone-1-submission`

If you're using the terminal:

- Type: git tag milestone-1-submission

You’ve now created a local tag for the current version of the project.

---

## Step 3: Push the Tag to GitHub

Creating a tag on your computer isn’t enough. You must push it to GitHub so
reviewers can see it.

To push your tag:

- Type: git push origin milestone-1-submission

This uploads the tag to GitHub.

---

## Step 4: Confirm Your Tag on GitHub

After pushing the tag, double-check it’s live on GitHub.

1. Go to our repository page on GitHub.
2. Click the “<> Code” tab if you’re not already there.
3. Find the dropdown near the top-left that says “main” or your branch name.
4. Click it and switch to the “Tags” tab.
5. You should see: milestone-1-submission

That means your submission is locked in and ready for review!

---

## Why This Matters

Reviewers will look *only* at the version of the project connected to the tag.  
If you miss this step, your submission may not be counted — even if you did the work.

---

## Quick Tips

- Don’t tag early — only after all final files are present.
- Don’t forget to push the tag after creating it.
- Tag from the main branch or whichever branch your team is using.

---

## Example Scenario

Let’s say your final edits are done. You’ve added and committed your file in
the `0_domain_research` folder.  
You then:

1. Create the tag: milestone-1-submission  
2. Push the tag to GitHub  
3. See the tag on GitHub under “Tags”  

You’re good to go!

---

## Questions?

If anything is unclear or you’re not sure what to do, ask your team lead or
check with an instructor before the deadline.
