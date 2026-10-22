"""
commandinterpreter.py

A simple text-based command interpreter.
The main function displays a menu, accepts a command, performs it,
and repeats until the user selects the "Quit" command (the last menu item).
"""


def printMenu(menu):
    """Displays the menu options, each prefixed with a number."""
    print("\nMenu:")
    for i in range(len(menu)):
        print(str(i + 1) + ". " + menu[i])


def acceptCommand(length):
    """
    Repeatedly prompts the user for a number between 1 and length
    (inclusive). Displays an error message for invalid input and
    returns the number once it is valid.
    """
    while True:
        try:
            response = input("Enter a command number (1-" + str(length) + "): ")
        except EOFError:
            print()
            return length  # no more input: fall back to Quit (last item)

        try:
            number = int(response)
        except ValueError:
            print("Error: '" + response + "' is not a number. Please try again.")
            continue

        if 1 <= number <= length:
            return number
        print("Error: " + str(number) + " is out of range. "
              "Please enter a number from 1 to " + str(length) + ".")


def performCommand(number, menu):
    """Displays the command in the menu that corresponds to the number."""
    print("Command = " + menu[number - 1])


def main(menu):
    """
    Runs the interpreter loop for the given menu.
    The last item in the menu must be "Quit".
    """
    while True:
        printMenu(menu)
        number = acceptCommand(len(menu))
        performCommand(number, menu)
        if menu[number - 1] == "Quit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    # Required test menu
    fileMenu = ["Open", "Save", "Compile", "Run", "Quit"]

    # Second test menu (Quit is still last). To try it, change the
    # call below to main(musicMenu).
    musicMenu = ["Play", "Pause", "Next Track", "Previous Track", "Shuffle", "Quit"]

    main(fileMenu)