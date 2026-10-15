# unique.py

filename = input("Enter the name of the text file: ")

with open(filename, "r") as file:
    text = file.read()

words = text.split()

unique_words = set(words)

for word in sorted(unique_words):
    print(word)