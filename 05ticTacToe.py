import customUtils as utils
import random


def print_board(board):
    """Prints the tic tac toe board.
    Code from Automate the Boring Stuff Ch 5
    """
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def get_move(player, board):
    # Only display options that are available for play
    keys = [key for key in board.keys() if board[key] == " "]

    square = utils.create_options(
        "Please select which spot you would like to play in", keys)
    print("You have chosen your location")
    board[keys[square]] = player

    return board


def get_next_player(current):
    return "O" if current == "X" else "X"


def check_win(board):
    # players = ["X", "O"]
    plays = set()
    for [key, val] in board.items():
        if val != " ":
            plays.add(key)

    lines = [["top-L", "top-M", "top-R"], ["mid-L", "mid-M", "mid-R"], ["low-L", "low-M", "low-R"],
             ["top-L", "mid-L", "low-L"], ["top-M", "mid-M",
                                           "low-M"], ["top-R", "mid-R", "low-R"],
             ["top-L", "mid-M", "low-R"], ["top-R", "mid-M", "low-L"]]

    # Implementation loop from https://www.scaler.com/topics/tic-tac-toe-python/
    for line in lines:
        if all(check in plays for check in line):
            return True
    return False


def play_game(board):
    current_player = random.choice(["X", "O"])
    print(f"\n************\n{current_player} you go first")
    plays = 0

    while plays <= 9:
        new_board = get_move(current_player, board)
        print_board(new_board)
        plays += 1
        if check_win(new_board):
            print(f"Congratulations {current_player}! You won!")
            return current_player
        current_player = get_next_player(current_player)
        print(f"\n**************\nYour turn {current_player}")


def update_score(winner, Xs, Os):
    if winner == "X":
        Xs["wins"] += 1
        Os["losses"] += 1
    elif winner == "O":
        Os["wins"] += 1
        Xs["losses"] += 1
    else:
        Xs["ties"] += 1
        Os["ties"] += 1

    return [Xs, Os]


def new_board():
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    return board


def main():
    """Generates a Tic Tac Toe board and prints it to the screen
    """
    board = new_board()

    Xs = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }
    Os = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }

    while True:
        print_board(board)
        winner = play_game(board)
        print(f"Winner is {winner}")
        new_score = update_score(winner, Xs, Os)
        Xs = new_score[0]
        Os = new_score[1]

        utils.playAgain("Tic Tac Toe", [Xs, Os])

        board = new_board()


if __name__ == "__main__":
    main()
