# The Digital Detective — Mini System Report
### Explore Your Computer • Build a Mini System Report

## Student Information
| Field | Details |
| :--- | :--- |
| **Name** | Piushi Sharma |
| **USN** | 2392608410 |
| **Campus / Section** | B.Tech CSE (First Year) |
| **GitHub username** | piushisharma |
| **GitHub repository name** | digital-detective-8410 |
| **GitHub repository URL** | https://github.com/piushisharma/digital-detective-8410 |

---

## About This Project
This repository contains my independent learning assignment for **SnAI: The Digital Detective — Explore Your Computer • Build a Mini System Report**.

The project investigates how personal computer systems operate under the hood, exploring:
1. Basic computer architecture and the Input-Processing-Output-Storage (IPOS) model.
2. Navigating and managing files safely using the macOS Terminal (CLI).
3. Operating system responsibilities (process management, memory, devices, storage, and permissions).
4. How code is translated and executed (compilers vs. interpreters) using Python 3.
5. Digital data representation, manual and programmatic conversions (decimal, binary, hexadecimal), and character encodings (ASCII and UTF-8).
6. Practical version control using Git and collaborative workflows on GitHub (branches and Pull Requests).
7. Foundational networking concepts, connectivity diagnostics, and DNS query resolution.

Each mission was undertaken sequentially with dedicated testing, evidence gathering, and distinct Git commits.

---

## Mission Navigation Index

| Folder / Mission | Title | Status | Focus / Highlights |
| :--- | :--- | :---: | :--- |
| [`mission-00-setup/`](./mission-00-setup/) | Repository and Workspace Setup | Completed | Environment check (Python 3.9.6, Git 2.50.1), repository structure |
| [`mission-01-computer-basics/`](./mission-01-computer-basics/) | Computer Fundamentals and IPOS | Pending | IPOS cycle trace, hardware vs. software classification, dedicated systems |
| [`mission-02-terminal/`](./mission-02-terminal/) | Terminal and File Management | Pending | Safe CLI practice, directory navigation, flags, and pipelines |
| [`mission-03-operating-system/`](./mission-03-operating-system/) | Operating System, Processes & Permissions | Pending | macOS system inspection, process IDs, file permissions |
| [`mission-04-programs/`](./mission-04-programs/) | How Programs Run | Pending | Python test program (`hello.py`), compiler vs. interpreter comparison |
| [`mission-05-numbers-data/`](./mission-05-numbers-data/) | Number Systems, Python and Text Encoding | Pending | Manual conversions with step-by-step working, Python verification, `number_converter.py` |
| [`mission-06-git-github/`](./mission-06-git-github/) | Git, GitHub, Branches and Pull Requests | Pending | Branching (`update-about`), Pull Request workflow, Git command glossary |
| [`mission-07-networking/`](./mission-07-networking/) | Computer Networks | Pending | Network topologies, DNS lookup, connectivity tests, web request lifecycle |
| [`mission-08-final-report/`](./mission-08-final-report/) | Final Review and Submission | Pending | Verification audit against rubric, final checks, submission summary |
| [`evidence/`](./evidence/) | Evidence & Artifacts | Active | Sanitized terminal logs and practical verification evidence |

---

## How to Run the Programs

All code in this repository requires standard Python 3 and runs directly from the terminal without external packages.

### 1. Hello World Program (Mission 04)
Run from the repository root:
```bash
python3 mission-04-programs/hello.py
```
**Expected Output:**
```text
Hello from Python
```

### 2. Number Converter Program (Mission 05)
Run from the repository root:
```bash
python3 mission-05-numbers-data/number_converter.py
```
Or run from inside the `mission-05-numbers-data/` directory:
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
The program interactively asks for any positive decimal integer and prints its binary and hexadecimal representations.

---

## Project Verification & Integrity
- All commands and code have been executed and tested directly on macOS.
- All terminal outputs have been scrubbed to protect personal privacy (local usernames, home paths, and IP addresses redacted).
- Commits are made sequentially after verifying each mission's deliverables.
