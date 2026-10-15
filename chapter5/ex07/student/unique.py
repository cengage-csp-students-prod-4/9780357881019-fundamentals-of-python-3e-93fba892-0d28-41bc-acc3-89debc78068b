# unique.py

"""
unique.py

This program reads a text file and prints each unique word in
alphabetical order. If a word appears more than once in the file
(for example, "apple" and "apple"), it is only printed once.
"""

# Ask the user for the name of the text file
filename = input("Enter the name of the text file: ")

# Open the file in read mode and store its contents as a string
with open(filename, "r") as file:
    text = file.read()

# Split the text into a list of words (separated by whitespace)
words = text.split()

# Convert the list to a set to remove duplicate words
unique_words = set(words)

# Sort the unique words alphabetically and print each one
for word in sorted(unique_words):
    print(word)