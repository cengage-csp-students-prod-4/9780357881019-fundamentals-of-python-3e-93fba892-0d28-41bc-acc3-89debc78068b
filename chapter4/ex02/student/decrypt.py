text = input("Enter the text: ")
distance = int(input("Enter the distance value: "))
direction = input("Shift backward (decrypt) or forward (encrypt)? Enter b or f: ").lower()

if direction == "f":
    distance = -distance  # flip so the formula below shifts forward

result = ""
for ch in text:
    code = ord(ch)
    if 32 <= code <= 126:
        code = (code - 32 - distance) % 95 + 32
    result += chr(code)

print(result)