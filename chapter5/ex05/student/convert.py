"""
File: convert.py

Converts a string representation of a number in any base (2-16)
to its decimal (base 10) integer value.
"""

# Lookup table: maps each digit character to the integer it represents.
# Initialized before the function is defined.
DIGITS = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
}


def repToDecimal(rep, base):
    """Returns the decimal integer value of the string rep,
    interpreted as a number in the given base."""
    decimal = 0
    exponent = len(rep) - 1
    for digit in rep:
        # Convert to uppercase, look up its value, and weight it
        # by the proper power of the base.
        decimal += DIGITS[digit.upper()] * base ** exponent
        exponent -= 1
    return decimal


def main():
    """Tests repToDecimal with numbers in several bases."""
    tests = [
        ("10", 8, 8),
        ("10", 16, 16),
        ("101", 2, 5),
        ("1111", 2, 15),
        ("777", 8, 511),
        ("FF", 16, 255),
        ("ff", 16, 255),
        ("1A3", 16, 419),
        ("ABC", 16, 2748),
        ("123", 10, 123),
        ("21", 3, 7),
    ]
    for rep, base, expected in tests:
        result = repToDecimal(rep, base)
        status = "OK" if result == expected else "FAIL"
        print("repToDecimal(\"" + rep + "\", " + str(base) + ") = "
              + str(result) + "  (expected " + str(expected) + ")  " + status)


if __name__ == "__main__":
    main()