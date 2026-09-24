smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
cheat = False
win = False
count = 0
guess = (smaller + larger) // 2
print(guess)
while count <= 10:
    count += 1
    userNumber = input("Enter <, >, or = ")
    if userNumber == "<":
        larger = guess - 1
        print(str(smaller)+", "+str(larger))
        guess = (smaller + larger) // 2
        print(guess)
    elif userNumber == ">":
        smaller = guess + 1
        print(str(smaller)+", "+str(larger))
        guess = (smaller + larger) // 2
        print(guess)
    elif userNumber == "=":
        print("Congratulations! I've got it in", count, "tries!")
        win = True
        break
    else:
        cheat = True
if win != True:
    if cheat == True:
        print("I'm out of guesses, and you cheated!")
    else:
        print("I'm out of guesses, you win!")