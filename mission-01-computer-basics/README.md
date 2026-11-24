# Mission 01 — Computer Fundamentals and IPOS

## 1. Task / objective
The objective of this mission is to understand foundational computer architecture concepts:
1. Examine the Input-Processing-Output-Storage (IPOS) model using a real everyday computing activity.
2. Identify and classify hardware and software components, clearly distinguishing between system software and application software.
3. Explore dedicated computer-based embedded systems outside standard personal computers and smartphones.

## 2. Work completed

### Task 1.1 — The IPOS Cycle in an Everyday Activity
**Selected Activity:** Typing and saving a college assignment in a text editor (e.g., VS Code or Notes).

| IPOS Stage | Description of Action | Hardware / Components Involved |
| :--- | :--- | :--- |
| **Input** | Keystrokes are entered by typing on the keyboard; cursor navigation and selections are made via the trackpad. | Built-in Apple Magic Keyboard, multi-touch trackpad, USB/Bluetooth controller |
| **Processing** | The CPU translates electrical keypress scan codes into digital character representations (Unicode/ASCII), updates the editor's text buffer in memory, and recalculates document layout. | CPU (Apple Silicon 10-core SoC), L1/L2/L3 CPU Cache, Memory Controller |
| **Output** | Characters appear visually on the screen in real-time as font glyphs; backlight adjustments provide visibility. | Liquid Retina Display, Display Controller / Integrated GPU |
| **Storage** | **Primary (Volatile):** The active unsaved document is held in RAM.<br>**Secondary (Non-volatile):** When pressing `Cmd + S`, the operating system writes the document file permanently to flash storage. | Primary: 16 GB Unified RAM<br>Secondary: Internal NVMe Solid-State Drive (SSD) |

---

### Task 1.2 — Hardware and Software Classification

#### A. Hardware Components (Physical units)
| Component | Classification | Primary Role in System |
| :--- | :--- | :--- |
| **Central Processing Unit (CPU)** | Processing Unit | Executes program instructions, performs arithmetic and logic operations, coordinates system tasks. |
| **Random Access Memory (RAM)** | Primary Storage (Volatile) | Holds actively running programs, operating system kernel data, and working data for quick CPU access. |
| **Solid-State Drive (SSD)** | Secondary Storage (Non-volatile) | Retains files, installed applications, and the operating system even when the computer is turned off. |
| **Liquid Retina Display** | Output Device | Converts digital pixel data from the GPU into visible light and user interfaces. |

#### B. Software Components
| Software Name | Category | Exact Sub-type | Purpose and Why It Fits This Category |
| :--- | :--- | :--- | :--- |
| **macOS Darwin Kernel** | System Software | Operating System (OS) | Manages hardware resources, CPU scheduling, memory allocation, and provides file system access to all programs. |
| **Python 3 Interpreter** | System Software | Language Runtime / Translator | Translates human-written Python source code into bytecode and machine instructions so the computer can execute it. |
| **Git Version Control** | System Software | Developer Tool / CLI Utility | Tracks line-by-line file history, manages branches, and records project evolution across commits. |
| **Visual Studio Code** | Application Software | Text Editor / Code Editor | User-facing application designed to let students and developers write, edit, and organize code. |

---

### Task 1.3 — Dedicated Computer-Based Systems

Beyond general-purpose personal computers and smartphones, computers are embedded into everyday machines to perform specific automated functions:

| System Name | Main Purpose | Input(s) | Output(s) |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Provides 24/7 self-service banking such as cash withdrawals and balance inquiries. | Card reader (chip/NFC), PIN numeric keypad, touch screen buttons, deposit slot sensors. | Cash dispenser motor, physical receipt printer, transaction screen UI, audio speaker/beeper. |
| **Smart Traffic Light Controller** | Manages traffic flow safely at busy road intersections and adapts signals to congestion. | Inductive loop vehicle sensors in the road pavement, pedestrian crossing buttons, optical traffic cameras. | Red, Amber, Green light signals; pedestrian countdown displays; audible crossing signal for visually impaired people. |
| **Modern Microwave Oven** | Regulates cooking and heating of food accurately based on power level and time. | Number keypad or dial knob, start/stop buttons, door safety interlock switch, internal temperature sensor. | Magnetron microwave emitter, rotating turntable motor, interior light bulb, digital 7-segment timer display, audible completion beep. |

---

## 3. Commands / tools used
- `system_profiler SPHardwareDataType`: Inspected local Mac hardware architecture (confirmed 10-core CPU and 16 GB unified memory).
- Text editor (VS Code): Formatted and validated the comparison tables and assignment notes.

## 4. My understanding
- **The IPOS Cycle:** Every computing task, no matter how simple or complex, follows the four-step cycle: receiving raw data (Input), manipulating and calculating it (Processing), presenting human-readable results (Output), and preserving it for future use (Storage).
- **System Software vs. Application Software:** System software acts as the foundation and bridge between physical hardware and users (e.g., OS kernel, device drivers, compilers). Application software sits on top of system software to solve specific end-user problems (e.g., writing notes, playing games, browsing the web).
- **General-purpose vs. Dedicated Systems:** A laptop is a general-purpose computer that can run thousands of different software programs. An ATM or microwave controller is a dedicated embedded system optimized to perform a single set of tasks with high reliability and safety.

## 5. Difficulties faced
Initially, it was tricky to decide whether RAM should be classified under "Processing" or "Storage" in the IPOS cycle because it is located directly next to the CPU and changes rapidly.

## 6. How I resolved them
Clarified through standard computer science fundamentals that memory is categorized under Primary Storage. Although volatile, it stores active program instructions and variables so the CPU does not have to wait on the slower secondary SSD.

## 7. Evidence / files
- Root README: [`../README.md`](../README.md)
- Mission 1 documentation: [`README.md`](./README.md)

## 8. Commit details
- **Commit Message:** `Add computer basics and IPOS notes`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
