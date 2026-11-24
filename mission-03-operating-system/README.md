# Mission 03 — Operating System, Processes and Permissions

## 1. Task / objective
The goal of this mission is to investigate the host operating system (macOS) using native CLI diagnostics:
1. Examine operating system release details, kernel architecture, user identity (sanitized), and filesystem disk utilization.
2. Inspect active processes, process hierarchies, and Process Identifiers (PIDs).
3. Analyze Unix file permissions (read, write, execute) and absolute vs. relative path models.
4. Explain six core operating system responsibilities: process management, memory management, device management, file management, user interface/shell, and security/permissions.

## 2. Work completed

### Practical System Investigations

#### A. Operating System and Kernel Information
Commands executed on macOS:
```bash
sw_vers
uname -srm
```
**Observations:**
- **Product Name & Version:** macOS 27.2.1 (Build `26B131`).
- **Kernel & Architecture:** Darwin Kernel 27.2.0 on `arm64` (Apple Silicon architecture).

#### B. User Identity (Sanitized)
Commands executed:
```bash
id -u
id -gn
```
**Observations:**
- The current user belongs to user ID `501` and group `staff`.
- *Privacy safeguard:* Username and device hostname have been scrubbed from documentation.

#### C. Filesystem Storage Utilization
Command executed:
```bash
df -h /
```
**Observations:**
- **Root filesystem mount:** `/dev/disk3s1s1` on `/` (APFS container).
- **Total capacity:** 460 GiB.
- **Used storage:** 13 GiB (system boot volume snapshot).
- **Available storage:** 353 GiB available for user applications and files.
- Demonstrates how the operating system manages non-volatile secondary storage across APFS volume sharing.

#### D. Running Processes and Process Hierarchy
Command executed:
```bash
ps -eo pid,ppid,%cpu,%mem,comm | head -n 10
```
**Observations:**
| PID | PPID | %CPU | %MEM | Command / Daemon | Purpose |
| :---: | :---: | :---: | :---: | :--- | :--- |
| `1` | `0` | `0.0` | `0.1` | `/sbin/launchd` | The root ancestor process of macOS user space; initializes daemons and coordinates the process tree. |
| `531` | `1` | `0.5` | `0.3` | `/usr/libexec/logd` | System logging daemon collecting diagnostic logs. |
| `534` | `1` | `0.0` | `0.1` | `/usr/libexec/UserEventAgent` | Manages system-level user events and triggers. |
| `536` | `1` | `0.0` | `0.0` | `.../fseventsd` | File System Events Daemon notifying apps when files change. |

Every running program has a unique Process Identifier (PID) and tracks the PID of the process that spawned it (Parent Process ID, PPID).

#### E. File Permissions Breakdown
Examined file and directory permissions:
```bash
ls -ld . terminal-practice/notes.txt
```
- Directory `.` (`drwxr-xr-x`):
  - `d`: Directory type indicator.
  - `rwx` (Owner = 7): User has full read (4), write (2), and traverse/execute (1) rights.
  - `r-x` (Group = 5): `staff` members can read and traverse into the folder, but cannot create or delete files inside.
  - `r-x` (Others = 5): All other accounts can read and traverse, but not modify.
- File `terminal-practice/notes.txt` (`-rw-r--r--`):
  - `-`: Regular file.
  - `rw-` (Owner = 6): User can read (4) and write (2).
  - `r--` (Group = 4): Group members have read-only access.
  - `r--` (Others = 4): World read-only access.

---

### Core Operating System Responsibilities

1. **Process Management:** The OS schedules CPU time across active tasks using preemptive multitasking. It creates, monitors, and terminates processes, allocating time slices so the system remains responsive even under load.
2. **Memory Management:** The OS manages RAM by tracking which memory addresses belong to which process. It implements virtual memory and paging to keep processes isolated so a crash in one app does not corrupt another.
3. **Device Management:** The OS communicates with hardware peripherals (keyboard, trackpad, display, Wi-Fi chip) using device drivers. It abstracts raw electronic signals into clean software interfaces.
4. **File Management:** Using the Apple File System (APFS), the OS organizes data blocks into a hierarchical directory tree of files and folders, tracking metadata (file sizes, access dates, permissions).
5. **Shell and User Interface:** The OS provides user interfaces for human interaction: graphical interfaces (Aqua/Finder) for visual clicking, and command line interpreters (zsh shell) for fast, direct command execution.
6. **Security and Permissions:** The OS enforces Unix access control lists (UAC/ACL) and privilege separation. Only root (superuser) can modify system-critical files, preventing unauthorized software from altering essential binaries.

---

## 3. Commands / tools used
- `sw_vers`: Displayed macOS software release and build information.
- `uname -srm`: Checked Darwin kernel version and Apple Silicon `arm64` hardware architecture.
- `id -u`, `id -gn`: Examined user and group numerical IDs.
- `df -h /`: Inspected root disk volume total capacity, used space, and free space.
- `ps -eo pid,ppid,%cpu,%mem,comm`: Filtered process list to inspect process IDs and parent hierarchies.
- `ls -ld`: Examined permissions string on directory and file targets.

## 4. My understanding
- The OS is the master coordinator of the entire computer. Without it, software would have to interact directly with raw CPU registers and disk sectors.
- Process ID 1 (`launchd` on macOS, similar to `systemd` or `init` on Linux) is the parent of all user-space processes.
- Permissions follow an owner-group-others model. Each category has separate read (4), write (2), and execute (1) values.

## 5. Difficulties faced
Understanding why directory permissions need the execute bit (`x`) even though directories are not runnable programs like `.py` or binary files.

## 6. How I resolved them
Learned that on Unix-like operating systems, the execute permission on a directory represents the ability to enter ("traverse" / `cd` into) the directory and access metadata for files stored inside.

## 7. Evidence / files
- Sanitized OS log: [`../evidence/os-investigation.log`](../evidence/os-investigation.log)
- Mission 3 documentation: [`README.md`](./README.md)
- Root README: [`../README.md`](../README.md)

## 8. Commit details
- **Commit Message:** `Add operating system observations`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
