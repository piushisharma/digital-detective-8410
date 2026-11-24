# Mission 05 — Number Systems, Python and Text Encoding

## 1. Task / objective
The goal of this mission is to understand how numbers and text are represented digitally:
1. Complete manual, step-by-step conversions between decimal, binary, and hexadecimal number systems using the positional-value and successive division methods.
2. Programmatically verify each calculation using Python's built-in functions.
3. Build an interactive, beginner-friendly number converter (`number_converter.py`) in Python 3 and test it with multiple positive numbers.
4. Investigate character encoding schemes (ASCII and UTF-8), examine character code points, and explain the necessity of digital encodings.

---

## 2. Work completed

### Task 5.1 — Step-by-Step Manual Conversions

The **positional-value method** states that the value of any digit depends on its face value multiplied by its base raised to the power of its position index (counting from 0 starting on the right).
- In decimal (base 10), weights are $10^0, 10^1, 10^2, \dots$
- In binary (base 2), weights are $2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16, \dots$
- In hexadecimal (base 16), weights are $16^0 = 1, 16^1 = 16, 16^2 = 256, \dots$ where digits $10 \dots 15$ are represented by letters $\text{A} \dots \text{F}$.

#### 1. Decimal 13 to Binary
- Method: Successive division by 2, recording remainders:
  - $13 \div 2 = 6$ remainder **1** (Least Significant Bit, LSB)
  - $6 \div 2 = 3$ remainder **0**
  - $3 \div 2 = 1$ remainder **1**
  - $1 \div 2 = 0$ remainder **1** (Most Significant Bit, MSB)
- Reading remainders from bottom to top (MSB to LSB):
  $$\mathbf{13_{10} = 1101_2}$$
- *Check:* $(1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) = 8 + 4 + 0 + 1 = 13$.

#### 2. Decimal 25 to Binary
- Method: Successive division by 2:
  - $25 \div 2 = 12$ remainder **1** (LSB)
  - $12 \div 2 = 6$ remainder **0**
  - $6 \div 2 = 3$ remainder **0**
  - $3 \div 2 = 1$ remainder **1**
  - $1 \div 2 = 0$ remainder **1** (MSB)
- Reading remainders from bottom to top:
  $$\mathbf{25_{10} = 11001_2}$$
- *Check:* $(1 \times 16) + (1 \times 8) + (0 \times 4) + (0 \times 2) + (1 \times 1) = 16 + 8 + 0 + 0 + 1 = 25$.

#### 3. Binary 1010 to Decimal
- Method: Positional expansion using powers of 2:
  $$\text{Value} = (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$$
  $$\text{Value} = (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$$
  $$\text{Value} = 8 + 0 + 2 + 0 = \mathbf{10_{10}}$$

#### 4. Binary 1101 to Decimal
- Method: Positional expansion using powers of 2:
  $$\text{Value} = (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$$
  $$\text{Value} = (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$$
  $$\text{Value} = 8 + 4 + 0 + 1 = \mathbf{13_{10}}$$

#### 5. Hexadecimal A to Decimal
- Hexadecimal uses digits $0\text{--}9$ and letters $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$.
  $$\text{Value} = 10 \times 16^0 = 10 \times 1 = \mathbf{10_{10}}$$

#### 6. Hexadecimal 1F to Decimal
- Method: Positional expansion using powers of 16:
  $$\text{Value} = (1 \times 16^1) + (\text{F} \times 16^0)$$
  $$\text{Value} = (1 \times 16) + (15 \times 1)$$
  $$\text{Value} = 16 + 15 = \mathbf{31_{10}}$$

#### 7. Binary 1111 to Hexadecimal
- In binary-to-hexadecimal grouping, each group of 4 bits corresponds to exactly one hexadecimal digit:
  $$1111_2 = (1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$$
- Decimal 15 in base 16 is the symbol **F**.
  $$\mathbf{1111_2 = F_{16}} \quad (\text{or } \mathbf{0xF})$$

---

### Task 5.2 — Python Verification

Each manual calculation was verified in Python using the built-in functions:

| Problem | Manual Result | Python Verification Expression | Python Result | Status |
| :--- | :---: | :--- | :---: | :---: |
| Decimal 13 to binary | $1101_2$ | `bin(13)` | `'0b1101'` | Verified |
| Decimal 25 to binary | $11001_2$ | `bin(25)` | `'0b11001'` | Verified |
| Binary 1010 to decimal | $10_{10}$ | `int('1010', 2)` | `10` | Verified |
| Binary 1101 to decimal | $13_{10}$ | `int('1101', 2)` | `13` | Verified |
| Hex A to decimal | $10_{10}$ | `int('A', 16)` | `10` | Verified |
| Hex 1F to decimal | $31_{10}$ | `int('1F', 16)` | `31` | Verified |
| Binary 1111 to hex | $\text{F}_{16}$ | `hex(0b1111)` | `'0xf'` | Verified |

All manual calculations match Python's output exactly.

---

### Task 5.3 — Python Number Converter (`number_converter.py`)

A beginner-friendly script was created at `mission-05-numbers-data/number_converter.py`:

```python
# Number Converter
# A beginner-friendly program to convert a decimal integer to binary and hexadecimal.

def main():
    print("=== Number Converter ===")
    user_input = input("Enter a positive decimal integer: ")
    decimal_number = int(user_input)

    binary_result = bin(decimal_number)
    hex_result = hex(decimal_number)

    print("\n--- Conversion Results ---")
    print("Decimal input:     ", decimal_number)
    print("Binary (with 0b):  ", binary_result)
    print("Binary (raw bits): ", binary_result[2:])
    print("Hexadecimal:       ", hex_result.upper().replace("0X", "0x"))
    print("Hex (raw digits):  ", hex_result[2:].upper())

if __name__ == "__main__":
    main()
```

#### Explanation of Core Python Built-in Functions:
- `input()`: Pauses program execution and reads a line of text entered by the user from standard input (stdin) as a string.
- `int()`: Parses and converts the string into an integer numerical type so arithmetic and base transformations can be computed.
- `bin()`: Converts an integer to its binary string representation prefixed with `'0b'`.
- `hex()`: Converts an integer to its hexadecimal string representation prefixed with `'0x'`.

#### Real Program Test Runs:
1. **Test 1 (Input: `13`):**
   - Binary: `0b1101` (raw bits: `1101`)
   - Hexadecimal: `0xD` (raw digit: `D`)
2. **Test 2 (Input: `25`):**
   - Binary: `0b11001` (raw bits: `11001`)
   - Hexadecimal: `0x19` (raw digits: `19`)
3. **Test 3 (Input: `42`):**
   - Binary: `0b101010` (raw bits: `101010`)
   - Hexadecimal: `0x2A` (raw digits: `2A`)

---

### Task 5.4 — Character Encoding

1. **ASCII (American Standard Code for Information Interchange):**
   - A 7-bit character encoding system developed in the 1960s.
   - Defines 128 characters ($0 \dots 127$), covering uppercase and lowercase English letters, numbers $0\text{--}9$, basic punctuation, and control characters (like newline and tab).
2. **UTF-8 (8-bit Unicode Transformation Format):**
   - A variable-length character encoding capable of encoding all 1,112,064 valid character code points in Unicode.
   - Uses between 1 and 4 bytes per character.
   - **Backwards compatibility:** For characters $0\text{--}127$, UTF-8 uses exactly 1 byte identical to ASCII.
3. **ASCII Values of Uppercase 'A' and Lowercase 'a':**
   - `'A'` = **65** in decimal $\rightarrow 01000001_2$ in binary.
   - `'a'` = **97** in decimal $\rightarrow 01100001_2$ in binary.
   - *Observation:* The difference is $97 - 65 = 32$ ($2^5$). Flipping bit 5 changes an uppercase ASCII letter to lowercase.
4. **Why Character Encoding is Necessary:**
   - Computer hardware, registers, and memory only store electrical states representing binary 0s and 1s.
   - Computers cannot store letters directly. An agreed-upon encoding standard ensures that when one computer saves the binary sequence `01000001`, another computer anywhere in the world interprets it as the letter 'A' rather than random gibberish.
5. **Character Outside Basic ASCII:**
   - **Euro Currency Symbol (`€`):**
     - Unicode Code Point: `U+20AC` (decimal `8364`).
     - UTF-8 Encoded Representation: 3 bytes: `0xE2 0x82 0xAC` (decimal values `[226, 130, 172]`).
   - **Hindi Character (`क`):**
     - Unicode Code Point: `U+0915` (decimal `2325`).
     - UTF-8 Encoded Representation: 3 bytes: `0xE0 0xA4 0x95` (decimal values `[224, 164, 149]`).

---

## 3. Commands / tools used
- `python3`: Executed inline calculations and ran `number_converter.py`.
- `bin()`, `hex()`, `int()`, `ord()`, `encode('utf-8')`: Built-in Python tools for number base and byte encoding conversions.

## 4. My understanding
- Base systems represent identical quantities using different counting groupings: binary uses groups of 2, decimal groups of 10, and hexadecimal groups of 16.
- Hexadecimal is widely used in computer science because one hex character precisely represents 4 binary bits (a nibble), making long 32-bit or 64-bit addresses compact and human-readable.
- UTF-8 solved the limitation of ASCII by allocating 1 byte for English and up to 4 bytes for other global scripts and symbols while remaining completely backwards-compatible with existing ASCII files.

## 5. Difficulties faced
Initially remembering whether the remainder from successive division by 2 is read top-to-bottom or bottom-to-top.

## 6. How I resolved them
Verified by calculating the positional sum: the first remainder obtained from dividing an odd number by 2 represents the $2^0 = 1$ place (the LSB), which means the remainders must be read in reverse (bottom-to-top) to place the MSB on the far left.

## 7. Evidence / files
- Python converter script: [`number_converter.py`](./number_converter.py)
- Test runs log: [`../evidence/number-converter-runs.log`](../evidence/number-converter-runs.log)
- Root README: [`../README.md`](../README.md)

## 8. Commit details
- **Commit Message:** `Build decimal number converter`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
