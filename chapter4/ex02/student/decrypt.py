text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value (positive shifts backward, negative shifts forward): "))

plaintext = ""
for ch in text:
    code = ord(ch)
    if 32 <= code <= 126:
        # shift back by distance, wrapping within the 95 printable characters
        code = (code - 32 - distance) % 95 + 32
    plaintext += chr(code)

print(plaintext)