"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
The vocabulary is read from text files at startup.
"""

import random

def getWords(filename):
    """Reads words from the given file (one per line)
    and returns them as a tuple."""
    words = []
    with open(filename, "r") as f:
        for line in f:
            word = line.strip()
            if word:                 # skip blank lines
                words.append(word)
    return tuple(words)

# Initialize the vocabulary from the input files
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()