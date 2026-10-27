"""
File: newton.py
Approximates the square root of a number using Newton's method,
decomposed into three cooperating functions.
"""

TOLERANCE = 0.000001


def limitReached(estimate, x):
    """Returns True if the estimate is close enough to the square root of x."""
    return abs(x - estimate ** 2) <= TOLERANCE


def improveEstimate(estimate, x):
    """Returns a new, improved approximation of the square root of x."""
    return (estimate + x / estimate) / 2


def newton(x, estimate=1.0):
    """Recursively approximates the square root of x."""
    if limitReached(estimate, x):
        return estimate
    return newton(x, improveEstimate(estimate, x))


def main():
    """Allows the user to compute square roots until they press Enter."""
    while True:
        text = input("Enter a positive number or press Enter to quit: ")
        if text == "":
            break
        x = float(text)
        if x < 0:
            print("The number must be positive.")
            continue
        print("Newton's estimate:", newton(x))
        print("Python's estimate:", x ** 0.5)


if __name__ == "__main__":
    main()