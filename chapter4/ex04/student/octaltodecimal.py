"""octaltodecimal.py

Converts a string of octal digits (0-7) to its decimal integer value
by processing one digit at a time, without using int(x, 8).
"""

# Read the octal number as a string so we can loop over each digit
octal = input('Enter a string of octal digits: ')

decimal = 0
for digit in octal:
    # Shift the value so far one octal place to the left (multiply by 8),
    # then add the value of the new digit
    decimal = decimal * 8 + int(digit)

print('The integer value is', decimal)