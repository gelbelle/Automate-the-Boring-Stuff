import sys

def getAns(ans, options):
    while ans not in options:
        print(f"You must choose one of the following: {options}")
        ans = input()
    return ans

def save(game, score):
    fileName = "scores.txt"
    print("Would you like to save your score? [y/n]")
    ans = getAns(input(), ['y','n'])
    if ans == 'y':
        print("Please enter your name")
        name = input()
        file = open(fileName, "a+")
        file.writelines(f"{game}:: {name}: {score}\n")
        file.close()
        sortFile(fileName)

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
    if getAns(input(), ['y','n']) == 'n':
        save(game, score)
        sys.exit(0)