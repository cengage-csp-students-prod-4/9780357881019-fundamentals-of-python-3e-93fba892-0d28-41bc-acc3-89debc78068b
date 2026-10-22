"""
testinputfunctions.py

Robust input functions for integers and floating-point numbers.
"""


def inputInt(prompt):
    """Prompts the user for an integer (digits only).
    Repeats until the input is valid, then returns the integer."""
    while True:
        text = input(prompt)
        if text.isdigit():
            return int(text)
        print("Error: input must contain digits only. Please try again.")


def inputFloat(prompt):
    """Prompts the user for a floating-point number.
    The input may contain digits only, or digits and a single
    decimal point. Repeats until the input is valid, then
    returns the number as a float."""
    while True:
        text = input(prompt)

        # Remove at most one decimal point, then check what is left
        if text.count(".") <= 1:
            digits = text.replace(".", "")
            if digits.isdigit():
                return float(text)

        print("Error: input must contain digits only or digits "
              "and a single decimal point. Please try again.")


def main():
    """Tests inputInt and inputFloat."""
    print("Testing inputInt:")
    number = inputInt("Enter an integer: ")
    print("You entered the integer", number)

    print("\nTesting inputFloat:")
    number = inputFloat("Enter a floating-point number: ")
    print("You entered the float", number)


if __name__ == "__main__":
    main()