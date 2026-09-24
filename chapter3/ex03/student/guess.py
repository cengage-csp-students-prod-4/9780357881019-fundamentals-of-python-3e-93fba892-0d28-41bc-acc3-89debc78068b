import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# Minimum number of guesses needed for a range of this size
maxGuesses = int(math.log(larger - smaller + 1, 2)) + 1

count = 0
win = False
while count < maxGuesses:
    guess = (smaller + larger) // 2
    print(guess)
    count += 1
    userNumber = input("Enter <, >, or = ")
    if userNumber == "=":
        print("Congratulations! I've got it in", count, "tries!")
        win = True
        break
    elif userNumber == "<":
        larger = guess - 1
    elif userNumber == ">":
        smaller = guess + 1
    else:
        break  # invalid hint
    if smaller > larger:
        break  # no numbers left: the hints contradict each other

if not win:
    print("I'm out of guesses, and you cheated!")