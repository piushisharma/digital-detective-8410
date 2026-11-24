# Mission 02 — Terminal and File Management

## 1. Task / objective
The goal of this mission is to become confident with the command-line interface (CLI) in macOS Terminal:
1. Practice foundational navigation and file-manipulation commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
2. Understand differences between file creation and content modification, overwriting (`>`) vs. appending (`>>`), and copying (`cp`) vs. moving/renaming (`mv`).
3. Explore common command flags (`-l`, `-a`, `-h`) and command chaining via pipes (`|`).
4. Check package manager status (Homebrew) without installing or modifying packages.

## 2. Work completed

### Practical Experiments in `terminal-practice/`
A dedicated practice directory (`terminal-practice/`) was created inside the repository to safely perform all file operations without affecting the rest of the project.

#### A. Directory Navigation and Path Inspection
- `pwd`: Showed current working directory (`/Users/.../digital-detective-8410`).
- `cd terminal-practice`: Navigated into the subfolder using a relative path.
- Absolute vs. Relative paths:
  - **Relative Path:** `terminal-practice` refers to a folder relative to where the terminal currently is.
  - **Absolute Path:** `/Users/<username>/digital-detective-8410/terminal-practice` specifies the unambiguous location starting from the root directory `/`.

#### B. File Creation, Overwrite and Append
- Created a file using output redirection:
  ```bash
  echo "Initial file content" > notes.txt
  ```
- Checked contents with `cat notes.txt`, confirming `Initial file content`.
- Appended a second line using `>>`:
  ```bash
  echo "Appended second line" >> notes.txt
  ```
- Re-inspected contents with `cat notes.txt`, demonstrating both lines were present:
  ```text
  Initial file content
  Appended second line
  ```
- **Difference:** Single chevron `>` truncates and replaces existing file content, while double chevron `>>` preserves existing data and adds new text at the end of the file.

#### C. Copying vs. Moving Files
- Copied `notes.txt` to `copied_notes.txt` using `cp notes.txt copied_notes.txt`. Both files existed independently.
- Moved/renamed `copied_notes.txt` to `moved_notes.txt` using `mv copied_notes.txt moved_notes.txt`. The original name ceased to exist.
- **Difference:** `cp` creates an exact duplicate in another location, doubling the disk footprint. `mv` relocates the file or changes its directory entry without duplicating the underlying data blocks.

#### D. Listing Flags Explored
| Command / Flag | Purpose | Observation |
| :--- | :--- | :--- |
| `ls` | Basic listing | Shows only regular filenames horizontally. |
| `ls -l` | Long format listing | Shows permissions, link count, owner, group, size in bytes, modification time, and name. |
| `ls -a` | All files | Reveals hidden files beginning with a dot (`.` and `..`). |
| `ls -lh` | Human-readable sizes | Formats byte counts into legible units (e.g., `42B`, `1.9K`). |
| `ls -lah` | Combined flags | Displays long format with all hidden files and human-readable units. |

#### E. Command Pipeline Demonstration
Connected the output of `ls` to `head` using the pipe symbol `|`:
```bash
ls -lah .. | head -n 5
```
**Observation:** Instead of scrolling through the entire directory listing, the pipeline intercepted standard output and displayed only the top 5 lines.

#### F. Package Manager Verification
Checked for Homebrew on macOS:
```bash
which brew
brew --version
```
**Result:** Homebrew was found at `/opt/homebrew/bin/brew` (version `6.0.20`). In accordance with assignment instructions, no packages were installed or removed.

---

## 3. Commands / tools used
- `pwd`: Print name of current/working directory.
- `ls`, `ls -l`, `ls -a`, `ls -lh`, `ls -lah`: Directory listing utilities with flags.
- `cd`: Change directory.
- `mkdir -p`: Create directory hierarchy safely.
- `touch`: Update timestamp or create empty file.
- `echo >` and `echo >>`: Standard output redirection (overwrite and append).
- `cat`: Concatenate and print file contents to terminal.
- `cp`: Copy files.
- `mv`: Move or rename files.
- `head -n 5`: Filter output to first 5 lines.
- `|` (Pipe): Stream data from stdout of one process into stdin of another.
- `which brew`, `brew --version`: Safe package manager status verification.

## 4. My understanding
- The CLI allows direct, scriptable control over the computer without relying on graphical windows or mouse clicks.
- The pipeline (`|`) is a core Unix philosophy concept: small, specialized tools (like `ls` and `head`) can be combined together to accomplish complex filtering tasks efficiently.
- Distinguishing between overwriting (`>`) and appending (`>>`) is critical to avoid accidental data loss when redirecting program outputs.

## 5. Difficulties faced
Remembering the exact order of source and destination arguments for `cp` and `mv`, and being cautious not to accidentally overwrite files with `>`.

## 6. How I resolved them
Adopted the mental rule "from here to there" (`cp source destination`). Verified file contents with `cat` after each operation to ensure no data was overwritten unintentionally.

## 7. Evidence / files
- Sanitized terminal log: [`../evidence/terminal-practice.log`](../evidence/terminal-practice.log)
- Practice folder: [`../terminal-practice/`](../terminal-practice/)
- Root README: [`../README.md`](../README.md)

## 8. Commit details
- **Commit Message:** `Document Terminal commands and file operations`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
