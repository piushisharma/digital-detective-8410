# Mission 00 — Repository and Workspace Setup

## 1. Task / objective
Verify the local development environment on macOS, confirm tool installations (Python 3 and Git), create the project repository named `digital-detective-8410` (using the last four digits of USN `2392608410`), scaffold the required folder structure, write the root README, initialize Git tracking, connect the local repository to GitHub, and document the rationale for repository structure.

## 2. Work completed
- Checked installed versions of Python and Git via the macOS Terminal.
- Verified Python version: `Python 3.9.6`.
- Verified Git version: `git version 2.50.1 (Apple Git-155)`.
- Created the local repository root directory `digital-detective-8410`.
- Initialized local Git version control with default branch `main`.
- Created the project directory tree for all missions and the `evidence/` directory.
- Authored the root `README.md` providing an overview of the assignment, student identification, mission index, and run instructions.
- Configured `.gitignore` to avoid committing unwanted macOS system files (`.DS_Store`) and Python cache folders (`__pycache__/`).
- Configured local Git author details for `piushisharma` and added the GitHub remote: `https://github.com/piushisharma/digital-detective-8410.git`.
- Prepared the initial commit.

## 3. Commands / tools used
- `python3 --version`: Confirmed Python 3 installation and version (`Python 3.9.6`).
- `git --version`: Confirmed Git installation and version (`git version 2.50.1`).
- `mkdir -p digital-detective-8410`: Created the project directory.
- `cd digital-detective-8410 && git init`: Initialized the Git repository.
- `git config user.name "piushisharma"`: Set local commit author username.
- `git config user.email "piushi@users.noreply.github.com"`: Set local commit email.
- `git remote add origin https://github.com/piushisharma/digital-detective-8410.git`: Connected local repository to GitHub.
- `git status`: Checked working tree status before staging.
- `git add .`: Staged setup documentation and initial project structure.
- `git commit -m "Set up Digital Detective mission structure"`: Created the Mission 0 commit.

## 4. My understanding
- **What is a Git repository?** A Git repository is a digital ledger and storage structure that tracks the full history of a project. Instead of saving manual copies of files like `report_v1.txt` or `report_final.txt`, Git records snapshots (commits) of changes over time. It allows me to see what changed, when it changed, and roll back if something breaks.
- **Why organize files by mission?** The assignment covers multiple distinct domains: computer architecture, terminal operations, operating systems, programming language execution, number systems, version control, and computer networks. Organizing folders mission-by-mission keeps notes, evidence, and code isolated and cleanly mapped to the professor's evaluation rubric.
- **Why use version control from day one?** Setting up Git at the start ensures every phase of development is recorded chronologically, creating proof of independent and progressive learning.

## 5. Difficulties faced
Running in a fresh repository without a global Git configuration required explicitly setting local repository author configuration (`user.name` and `user.email`) so commits are attributed properly to my GitHub account.

## 6. How I resolved them
Configured local repository user identity settings directly in `.git/config` matching my GitHub account details prior to creating the first commit.

## 7. Evidence / files
- Root README: [`../README.md`](../README.md)
- Mission 0 README: [`README.md`](./README.md)
- Evidence directory: [`../evidence/`](../evidence/)
- Git configuration: `.git/config`

## 8. Commit details
- **Commit Message:** `Set up Digital Detective mission structure`
- **Branch:** `main`
- **Remote Push Status:** Pushed to `https://github.com/piushisharma/digital-detective-8410`
