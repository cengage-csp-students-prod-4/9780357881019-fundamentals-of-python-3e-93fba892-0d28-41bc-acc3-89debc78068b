"""decrypt.py

Decrypt text encrypted with a Caesar-style shift cipher.

The cipher operates on the 95 printable ASCII characters (codes 32 through
126, from space to tilde). Each character is shifted by a fixed distance,
wrapping around within that range. Characters outside the range, such as
newlines or non-ASCII symbols, are passed through unchanged.

The program prompts for the encrypted text and the shift distance, then
prints the decrypted plaintext.
"""

# Prompt the user for the ciphertext to decrypt
text = input("Enter the encrypted text: ")

# The distance used during encryption. Positive values shift each character
# backward in the ASCII table; negative values shift it forward.
distance = int(input("Enter the distance value (positive shifts backward, negative shifts forward): "))

# Accumulates the decrypted characters
plaintext = ""

for ch in text:
    # Get the ASCII code of the current character
    code = ord(ch)

    # Only shift printable ASCII characters (space through tilde);
    # anything else is left as-is
    if 32 <= code <= 126:
        # Convert to a 0-94 range by subtracting 32, shift by the distance,
        # wrap around using modulo 95 (the number of printable characters),
        # then convert back to an ASCII code by adding 32 again
        code = (code - 32 - distance) % 95 + 32

    # Append the (possibly shifted) character to the result
    plaintext += chr(code)

# Display the decrypted text
print(plaintext)