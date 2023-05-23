import sys
import os


def greet_user(options):
    print("\nWhat would you like to do?")
    for i in range(len(options)):
        print(f"{i}: {options[i]}")

    ans = input()
    # List from range https://www.geeksforgeeks.org/range-to-a-list-in-python/
    return getAns(ans, str([*range(len(options))]))


def getAns(ans, options):
    while ans not in options:
        print(f"You must choose one of the following: {options}")
        ans = input()
    return ans


def save_game(game, score):
    fileName = "scores.txt"
    print("Would you like to save your score? [y/n]")
    ans = getAns(input(), ['y', 'n'])
    if ans == 'y':
        print("Please enter your name")
        name = input()
        try:
            file = open(fileName, "a+")
            file.writelines(f"{game}:: {name}: {score}\n")
            file.close()
            sortFile(fileName)
        except FileNotFoundError as err:
            print(f"Something has gone wrong: {err}")


def open_file(file_name):
    try:
        file = open(file_name, "r+")
        contents = file.readlines()
        return contents
    except FileNotFoundError as err:
        print(f"Something has gone wrong: {err}")


def print_list(name):
    items = open_file(name)
    for item in items:
        print(item, end="")


def save_list(name, items):
    try:
        file = open(f"lists/{name}.txt", "a+")
        for item in items:
            if item.strip():
                file.write(f"{item}\n")
        file.close()
    except FileNotFoundError as err:
        print(f"Something has gone wrong: {err}")


def ask_save(msg):
    print(f"{msg} [y/n]")
    ans = getAns(input(), ['y', 'n'])
    if ans == 'y':
        print("Please enter a name for your list: ", end="")
        return input()


def sortFile(fileName):
    with open(fileName, 'r') as reader:
        lines = reader.readlines()
    with open(fileName, "w") as writer:
        for score in sorted(lines):
            writer.write(score)


def playAgain(game, score):
    print("Would you like to play again? [y/n]")
    if getAns(input(), ['y', 'n']) == 'n':
        save_game(game, score)
        sys.exit(0)


def read_files(dir_name):
    for entry in os.scandir(dir_name):
        if entry.is_file():
            idx = entry.name.index(".")
            print(entry.name[:idx])
