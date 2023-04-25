import random
import customUtils

def main():
    number = random.randint(1,100)
    numGuesses = 0
    scores = []
    
    while True:
        print("Guess a number between 1 and 100")
        try:
            guess = int(input())
            numGuesses += 1

            if guess < number:
                print(f"{guess} is too low.\nGuess again")
            elif guess > number:
                print(f"{guess} is too high.\nGuess again")
            else:
                print(f"Congratulations, {guess} is correct.\nIt took you {numGuesses} guesses")
                scores.append(numGuesses)
                customUtils.playAgain("Guess the Number", scores)
                number = random.randint(1,100)
                numGuesses = 0
        except ValueError:
            print("You must enter a number")

if __name__ == "__main__":
    main()