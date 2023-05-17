import random
import customUtils


def main():
    possibilities = ["r", "p", "s"]
    words = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    wins = 0
    losses = 0
    ties = 0
    while True:
        computer = possibilities[random.randint(0, 2)]

        print("\nLets play rock, paper, scissors")
        print(f"\n{wins} wins, {losses} losses, {ties} ties\n")
        print("Enter your move: (r)ock, (p)aper, (s)cissors")

        player = customUtils.getAns(input(), possibilities)

        if player == computer:
            print(f"It's a tie, you both picked {words[player]}")
            ties += 1
        elif player == 'r':
            if computer == 's':
                print("You win! rock beats scissors")
                wins += 1
            else:
                print("You lost this one, paper beats rock")
                losses += 1
        elif player == 'p':
            if computer == 'r':
                print("You win! paper beats rock")
                wins += 1
            else:
                print("You lost this one, scissors beats paper")
                losses += 1
        else:
            if computer == 'r':
                print("You win! scissors beats paper")
                wins += 1
            else:
                print("You lost this one, rock beats scissors")
                losses += 1

        customUtils.playAgain("Rock Paper Scissors", [
                              f"wins: {wins}", f"losses: {losses}", f"ties: {ties}"])


if __name__ == "__main__":
    main()
