import sys


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
        file = open(fileName, "a+")
        file.writelines(f"{game}:: {name}: {score}\n")
        file.close()
        sortFile(fileName)


def save_list(items):
    print("Would you like to save your list? [y/n]")
    ans = getAns(input(), ['y', 'n'])
    if ans == 'y':
        print("Please enter a name for your list: ", end="")
        name = input()
        file = open(f"{name}.txt", "a+")
        for item in items:
            file.write(f"{item}\n")
        file.close()


def sortFile(fileName):
    with open(fileName, 'r') as reader:
        lines = reader.readlines()
    with open(fileName, "w") as writer:
        for score in sorted(lines):
            writer.write(score)
    """     writeFile = open(fileName, "w")
    writeFile.writelines(lines)
    writeFile.close() """


def playAgain(game, score):
    print("Would you like to play again? [y/n]")
    if getAns(input(), ['y', 'n']) == 'n':
        save_game(game, score)
        sys.exit(0)
