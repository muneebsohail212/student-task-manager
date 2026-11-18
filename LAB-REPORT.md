# LAB REPORT – Lab Assignment 4

**Course:** CSC418 – DevOps for Cloud Computing
**Name:** _______Muhammad Muneeb Sohail_______________  **Reg. No.:** FA23-BSE-__212__
**Repository:** https://github.com/muneebsohail212/student-task-manager
**Release:** https://github.com/muneebsohail212/student-task-manager/releases/tag/v1.0.0

## 1. Git vs GitHub; purpose of add, commit and push

Git is a version control tool that runs on my own computer and records the history of my files. GitHub is an online service that hosts Git repositories and adds teamwork features such as Issues, Pull Requests and Actions.

- `git add` puts chosen changes into the staging area, so I decide what goes into the next commit.
- `git commit` saves the staged changes as a snapshot in my local history, with a message that explains the change.
- `git push` uploads my local commits to the remote repository on GitHub so others can see them and the work is backed up.

## 2. Why branches and Pull Requests are used; what causes merge conflicts

Branches let me work on one feature or fix separately from `main`, so unfinished or broken code does not affect the stable version and several people can work in parallel. A Pull Request asks to merge a branch into `main`; it gives a place to review the changed files, discuss them, run automated tests and link the related Issue before merging.

A merge conflict happens when two branches change the same lines of the same file (or one edits a file the other deletes) and Git cannot decide which version to keep. In this lab both branches changed the `Project status:` line in `README.md` differently, so I had to choose the final text myself.

## 3. Fetch vs pull; merge vs rebase

- `git fetch` downloads new commits from the remote but does not change my working files or current branch. `git pull` is fetch followed by merging those commits into my current branch.
- `git merge` joins two branches by creating a merge commit that keeps both histories as they happened. `git rebase` replays my commits on top of another branch, giving a straight, linear history but rewriting those commits, so it should not be used on commits that are already shared.

## 4. How GitHub Issues and Actions help a team

Issues track tasks, bugs and ideas in one place, with descriptions, labels and assignees, and can be linked to Pull Requests so everyone knows why a change was made and when it is finished. GitHub Actions automatically runs workflows, such as unit tests, on every push or Pull Request, so mistakes are found early and only code that passes the checks is merged.

## 5. One difficulty I faced and how I solved it

The hardest part was the merge conflict in `README.md`. After merging the first branch, merging the second one stopped with `CONFLICT (content)`. I opened the file, read the `<<<<<<<`, `=======` and `>>>>>>>` markers, understood that they show my current version and the incoming version, and replaced the whole block with one final line. Then I ran `git add README.md` and `git commit` to complete the merge, and checked with `git log --graph` that nothing else was lost.

## Why branches are useful (Part B, item 5)

Each feature branch (`feature/add-task`, `feature/complete-task`, `feature/delete-task`) kept its work isolated, so I could commit and test one feature at a time without breaking `main`. The commit graph (`git log --oneline --graph --all`) shows the branches splitting from `main` and later merging back, which makes the history easy to follow and review.

## Evidence

Screenshots for every step are in the `lab-evidence/` folder.
