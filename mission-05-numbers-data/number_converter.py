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
