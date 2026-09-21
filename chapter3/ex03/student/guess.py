import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
userNumberANS = int(input("Enter yout number: "))
cheat = False
##if userNumber < smaller or userNumber > larger:
##    print("you cheated")
count = 0
guess = random.randint(smaller, larger)
print(guess)
while count <= 10:
    count += 1
    win = False
    userNumber = input("Enter <, >, or = ")
    if userNumber == "<":
        larger = guess
        print(str(smaller)+", "+str(larger))
        guess = random.randint(smaller, larger)
        print(guess)
    elif userNumber == ">":
        smaller = guess
        print(str(smaller)+", "+str(larger))
        guess = random.randint(smaller, larger)
        print(guess)
    elif userNumberANS == guess and userNumber == "=":
        print("Congratulations! I've got it in", count, "tries!")
        win = True
        break
    else:
        cheat = True
    if guess == userNumberANS:
        cheat = True
    elif userNumberANS < smaller:
        cheat = True
    elif userNumberANS > larger:
        cheat = True
    if cheat == True:
        break
if win != True:
    if cheat == True:
        print("you cheated, game over!")
    else:
        print("I'm out of guesses, you win!")