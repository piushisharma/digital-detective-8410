# Mission 06 — Git, GitHub, Branches and Pull Requests

## 1. Task / objective
The goal of this mission is to understand and master version control using Git and collaborative workflows on GitHub:
1. Explain the purpose of version control and the role of Git (local tool) vs. GitHub (remote cloud platform).
2. Clarify the Git three-tree architecture: Working Directory, Staging Area (Index), and Repository (Commit History).
3. Explain and demonstrate essential Git commands: `git init`, `git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git push`, and `git pull`.
4. Perform a real branching and Pull Request exercise:
   - Create a dedicated feature branch named `update-about`.
   - Update the root `README.md` by adding a section titled "My Learning".
   - Commit and push the branch to GitHub.
   - Open a genuine Pull Request targeting `main`.
   - Inspect the PR, confirm changed files, and leave it open as instructed.
5. Provide a simple, clear Git command glossary for reference.

---

## 2. Work completed

### Git Architecture: Working Directory, Staging Area, and Repository
Git manages project files through three distinct states:
1. **Working Directory (Untracked / Modified):** The actual files on disk that you are currently editing. Changes here are local to your editor.
2. **Staging Area (Index):** A preparation buffer where you selectively mark which specific file changes should be bundled together into the next commit snapshot using `git add`.
3. **Repository (Committed History):** The permanent `.git` database storing cryptographic snapshots (commits) along with timestamps, author metadata, and commit messages.

#### Difference Between Staging and Committing:
- **Staging (`git add`):** Means "drafting" or preparing changes. It allows you to review and choose exactly which modifications belong together. Staged changes can still be unstaged or edited before finalizing.
- **Committing (`git commit`):** Takes the current snapshot in the staging area and permanently records it into the project history with a unique SHA-1 hash. It is the permanent "checkpoint" in your project.

---

### Demonstrating Core Git Commands

| Command | Exact Function | Real Project Example / Usage |
| :--- | :--- | :--- |
| `git init` | Initializes a brand-new Git repository in the current folder, creating the hidden `.git/` metadata directory. | Executed at project start to create `digital-detective-8410`. |
| `git status` | Displays working tree status: modified files, untracked files, and staged changes ready for commit. | Checked before every staging step to ensure only relevant files are staged. |
| `git add <file>` | Moves changes from the working tree into the staging area (index). | `git add mission-01-computer-basics/README.md` |
| `git commit -m "<msg>"` | Packages staged changes into a permanent snapshot with an informative single-line message. | `git commit -m "Add computer basics and IPOS notes"` |
| `git log` | Displays chronological list of commits, authors, dates, and commit hashes. | `git log --oneline -n 5` |
| `git branch` | Lists all local branches, or creates a new branch pointer when given a name argument. | `git branch` shows `* main` and `update-about`. |
| `git switch <branch>` | Safely switches the working directory files to the specified branch. | `git switch -c update-about` created and switched to the branch. |
| `git push` | Uploads local branch commits to the corresponding branch on the remote GitHub repository. | `git push -u origin update-about` |
| `git pull` | Fetches changes from the remote repository and immediately merges them into the current local branch. | `git pull origin main` |

---

### Branching and Pull Request Practical Activity

#### 1. Branch Creation and Switching
Created and checked out the feature branch:
```bash
git switch -c update-about
```
Verified with `git branch` that HEAD was pointing to `update-about`.

#### 2. Root README Update
Edited `README.md` to include a new section titled **"My Learning"**:
```markdown
## My Learning
Through the hands-on missions in this assignment, I learned:
1. **How hardware and software collaborate:** I traced an everyday typing activity through the IPOS cycle and saw how the CPU, volatile RAM, and persistent SSD work together under operating system coordination.
2. **Command line power and safety:** I learned to navigate files, use pipes to chain commands, and safely manage files using standard flags without relying on a graphical window.
3. **Data representation at the hardware level:** I learned how numbers are converted between decimal, binary, and hexadecimal, and why computers use UTF-8 encoding to represent human text using binary bytes.
```

#### 3. Commit and Push
- Staged and committed the change on the branch:
  ```bash
  git add README.md
  git commit -m "Add My Learning section to root README"
  ```
- Pushed branch to GitHub:
  ```bash
  git push -u origin update-about
  ```

#### 4. Pull Request Creation & Inspection
- Opened Pull Request targeting `main`:
  - **PR Number:** `#1`
  - **PR URL:** https://github.com/piushisharma/digital-detective-8410/pull/1
  - **Title:** `Add My Learning section to root README`
  - **Head Branch:** `update-about`
  - **Base Branch:** `main`
  - **Description:** *"This pull request adds the My Learning section to the root README on branch update-about, documenting key insights from the Digital Detective missions as required by Mission 06."*
  - **Changed Files:** 1 file (`README.md`, +9 lines additions, 0 deletions).
  - **PR State:** `Open` (kept unmerged as required by assignment guidelines).

---

### Simple Git Command Glossary

| Command | What it does in simple terms |
| :--- | :--- |
| `git init` | Starts tracking the current folder as a Git repository. |
| `git clone <url>` | Downloads an existing remote repository to your local computer. |
| `git status` | Shows which files are changed, staged, or untracked. |
| `git add <file>` | Stages a file for the next commit snapshot. |
| `git commit -m "msg"` | Saves staged changes permanently to history with a message. |
| `git branch <name>` | Creates a new branch (alternate timeline for code). |
| `git switch <name>` | Swaps your current workspace to a different branch. |
| `git merge <name>` | Combines history from another branch into your current branch. |
| `git push` | Sends your local commits to GitHub. |
| `git pull` | Downloads and merges the latest commits from GitHub to your computer. |
| `git diff` | Shows line-by-line differences between files and commits. |
| `git log --oneline` | Shows a clean, single-line summary of commit history. |

---

## 3. Commands / tools used
- `git switch -c`: Created and switched to `update-about`.
- `git diff`: Checked working tree differences on the branch.
- `git commit`: Created branch commit `6f7d1f2`.
- `git push -u origin update-about`: Published feature branch to GitHub remote.
- GitHub Pull Request API: Validated PR #1 details and changed files.
- `git switch main`: Returned to main branch for continuing assignment missions.

## 4. My understanding
- Git is the local tool that runs on my Mac to record changes and track history. GitHub is the cloud platform that hosts the remote repository so others can view and collaborate on the project.
- Branches allow developers to work on new features or experiments in isolation without risking the stability of the `main` branch.
- Pull Requests (PRs) provide a structured code review process: they let peers or instructors review the diff, comment on code, run automated tests, and approve changes before merging them into `main`.

## 5. Difficulties faced
Understanding the difference between pushing a commit directly to `main` versus creating a feature branch and opening a Pull Request.

## 6. How I resolved them
Walked through the complete branching lifecycle: created `update-about`, committed the `README.md` changes locally, pushed the branch to GitHub, and examined PR #1 in the GitHub web interface to verify how diffs are presented for review.

## 7. Evidence / files
- Pull Request details log: [`../evidence/pull-request-details.json`](../evidence/pull-request-details.json)
- Feature branch: `update-about`
- Root README: [`../README.md`](../README.md)
- Mission 6 documentation: [`README.md`](./README.md)

## 8. Commit details
- **Commit Message:** `Document Git branching and pull requests`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
