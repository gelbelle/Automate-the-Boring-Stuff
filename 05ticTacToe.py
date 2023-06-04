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


# TODO check if length is three for any of the potential lines
def check_win(board):
    # players = ["X", "O"]
    plays = set()
    for [key, val] in board.items():
        if val != " ":
            plays.add(key)

    """ lines = []
    top = []
    mid = []
    low = []
    left = []
    middle = []
    right = []

    for play in plays:
        if "top" in play:
            top.append(play)
        elif "mid" in play:
            mid.append(play)
        elif "low" in play:
            low.append(play)
        if "L" in play:
            left.append(play)
        if "R" in play:
            right.append(play)
        if "M" in play:
            middle.append(play)

    lines.append([top, mid, low, left, middle, right])

    for line in lines:
        for row in line:
            if len(row) == 3:
                return True """

    """ lines.append((play for play in plays if "top" in play))
    lines.append((play for play in plays if "mid" in play))
    lines.append((play for play in plays if "low" in play))

    lines.append((play for play in plays if "L" in play))
    lines.append((play for play in plays if "M" in play))
    lines.append((play for play in plays if "R" in play))

    checked = any(line for line in lines if len(line) == 3) """
    """  for line in lines:
        print(line)  """

    # print(checked)

    lines = [["top-L", "top-M", "top-R"], ["mid-L", "mid-M", "mid-R"], ["low-L", "low-M", "low-R"],
             ["top-L", "mid-L", "low-L"], ["top-M", "mid-M",
                                           "low-M"], ["top-R", "mid-R", "low-R"],
             ["top-L", "mid-M", "low-R"], ["top-R", "mid-M", "low-L"]]
    """if board['top-L'] in players and board['top-L'] == ['top-M'] == board['top-R']:
        return True
    if board['mid-L'] in players and board['mid-L'] == board['mid-M'] == board['mid-R']:
        return True
    if board['low-L'] in players and board['low-M'] == board['low-L'] == board['low-R']:
        return True
    if board['top-L'] in players and board['top-L'] == board['mid-L'] == board['low-L']:
        return True
    if board['top-M'] in players and board['top-M'] == board['mid-M'] == board['low-L']:
        return True
    if board['top-R'] in players and board['top-R'] == board['mid-R'] == board['low-R']:
        return True
    if board['top-L'] in players and board['top-L'] == board['mid-M'] == board['low-R']:
        return True
    if board['top-R'] in players and board['top-R'] == board['mid-M'] == board['low-L']:
        return True """

    for line in lines:
        if all(check in plays for check in line):
            return True
    return False


""" def check_game_over(board):
    start_pos = 0
    sum = 0
    plays = "".join(list(board.values()))
    while start_pos < len(board):
        pos = plays.find("XXX", start_pos)

        if pos != -1:
            start_pos = pos + 1
            sum += 1
        else:
            print(sum) """


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
    # print_board(board)
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
