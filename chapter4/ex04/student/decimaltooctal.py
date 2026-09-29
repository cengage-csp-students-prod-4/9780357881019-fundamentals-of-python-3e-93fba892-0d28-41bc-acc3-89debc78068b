"""decimaltooctal.py

Converts a non-negative decimal integer to its octal representation
using repeated division by 8, without using oct() or format().
"""

# Read the decimal integer from the user
decimal = int(input('Enter a decimal integer: '))

# Zero is a special case: the loop below would never run and leave an empty string
if decimal == 0:
    octal = '0'
else:
    octal = ''
    # Keep dividing by 8 until nothing is left
    while decimal > 0:
        # The remainder is the next octal digit, starting from the rightmost
        # Prepend it so the digits end up in the correct order
        octal = str(decimal % 8) + octal
        # Integer-divide to drop the digit we just extracted
        decimal //= 8

print('The octal representation is', octal)