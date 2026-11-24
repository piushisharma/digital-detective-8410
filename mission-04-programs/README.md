# Mission 04 — How Programs Run

## 1. Task / objective
The goal of this mission is to understand how computer software is translated into hardware instructions:
1. Write and execute a test program in Python 3 (`hello.py`) displaying `Hello from Python`.
2. Verify execution and capture genuine output.
3. Compare compilers and interpreters across translation methods, execution speed, output artifacts, language examples, and key trade-offs.
4. Explain hybrid compilation-interpretation models used by modern language runtimes (such as Python and Java).

## 2. Work completed

### Practical Execution: `hello.py`
A simple Python script was created at `mission-04-programs/hello.py`:
```python
print("Hello from Python")
```

Execution command and verification:
```bash
python3 mission-04-programs/hello.py
```
**Actual terminal output:**
```text
Hello from Python
```

---

### Comprehensive Comparison: Compiler vs. Interpreter

| Aspect | Compiler | Interpreter |
| :--- | :--- | :--- |
| **Translation Phase** | Translates the entire source code file at once before any execution begins. | Translates and executes the program instruction-by-instruction (line-by-line) at runtime. |
| **Execution Phase** | Execution happens separately after translation is 100% complete. | Translation and execution occur concurrently in a single runtime step. |
| **Typical Output Artifact** | Produces a standalone, platform-dependent binary executable file (e.g., `.exe` on Windows, Mach-O binary on macOS, ELF binary on Linux). | Does not generate a standalone binary file; executes instructions directly through the host interpreter process. |
| **Error Reporting** | Reports all syntax errors and type discrepancies during the compilation phase before running any code. | Halts execution immediately at runtime when the first encountering error line is hit. |
| **Execution Speed** | Very fast execution because instructions are already native machine code for the target CPU. | Slower execution because instructions must be parsed, checked, and translated while the program runs. |
| **Portability** | Lower binary portability; the binary must be recompiled for each target CPU architecture (x86_64 vs. arm64) and OS. | Higher source code portability; the same `.py` or `.js` script runs on any operating system with an installed interpreter. |
| **Language Examples** | C, C++, Rust, Go, Fortran | Python (standard CPython), Ruby, JavaScript (in simple engines), PHP |
| **Primary Advantages** | Optimized CPU execution performance, standalone distribution without shipping source code. | Rapid interactive debugging, immediate testing without compilation delays, platform flexibility. |

---

### Modern Hybrid Approaches (Bytecode & JIT)
Pure compilation and pure interpretation are two ends of a spectrum. Modern programming languages frequently combine both:

1. **Python (CPython):** When a Python program is run, CPython does not interpret raw text directly line-by-line. It first *compiles* the human-readable source code into intermediate **bytecode** (often cached in `__pycache__/*.pyc` files). The **Python Virtual Machine (PVM)** then *interprets* those bytecode instructions.
2. **Java:** The Java compiler (`javac`) compiles `.java` source code into intermediate bytecode (`.class` files). The Java Virtual Machine (JVM) interprets the bytecode, while a **Just-In-Time (JIT) compiler** detects frequently run loops ("hot spots") and compiles them dynamically into native CPU machine code at runtime.

---

## 3. Commands / tools used
- `python3`: Invoked Python 3.9.6 runtime to execute `hello.py`.
- Text editor: Created script and structured notes.

## 4. My understanding
- A CPU only understands native binary machine code (0s and 1s representing opcode instructions).
- Compilers act like a translator who converts an entire book from French to English in advance, allowing the reader to read it smoothly.
- Interpreters act like a live translator who translates speech sentence-by-sentence as words are spoken.
- Python sits comfortably in between: compiling to bytecode first so syntax errors are caught early, then using the PVM interpreter for execution flexibility.

## 5. Difficulties faced
Distinguishing whether Python should be classified strictly as an interpreted language given that it produces compiled bytecode (`.pyc`).

## 6. How I resolved them
Researched CPython's execution pipeline. Learned that bytecode is an intermediate, architecture-neutral format, and because execution relies on the virtual machine interpreting this bytecode rather than running native machine instructions directly on hardware, it is predominantly classified as an interpreted/virtual machine language.

## 7. Evidence / files
- Python program: [`hello.py`](./hello.py)
- Execution log: [`../evidence/hello-output.log`](../evidence/hello-output.log)
- Root README: [`../README.md`](../README.md)

## 8. Commit details
- **Commit Message:** `Add Python hello world example`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
