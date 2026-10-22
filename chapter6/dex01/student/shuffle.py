import random
def shuffleString(theString):
    print("".join(random.sample(list(theString), len(theString))))
shuffleString("Apples are red")