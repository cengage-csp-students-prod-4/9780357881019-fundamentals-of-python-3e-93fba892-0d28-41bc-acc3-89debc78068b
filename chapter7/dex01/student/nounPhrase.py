import random
articles = ["the", "a", "one", "some", "any"]
adjectives = ["big", "small", "blue", "green", "yellow", "red", "purple", "orange", "brown", "black", "white"]
nouns = ["apple", "peach", "banana", "pear", "orange", "grape", "strawberry", "blueberry", "raspberry", "cherry", "watermelon", "cantaloupe", "honeydew"]
#nounphrase = article [adjectivephrase] noun
def nounPhrase():
    """Builds and returns a noun phrase."""
    if random.randint(0, 1) == 0:
        return random.choice(articles) + " " + random.choice(nouns)
    return random.choice(articles) + " " + \
        adjectivePhrase() + " " + random.choice(nouns)

#adjectivephrase = adjective [adjectivephrase]
def adjectivePhrase():
    """Builds and returns an adjective phrase."""
    if random.randint(0, 1) == 0:
        return random.choice(adjectives)
    return random.choice(adjectives) + " " + adjectivePhrase()

print(nounPhrase())