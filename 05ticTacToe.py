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
    keys = list(board.keys())
    square = utils.create_options(
        "Please select which spot you would like to play in", keys)
    print("You have chosen your location")
    board[keys[square]] = player

    return board


def get_next_player(current):
    return "O" if current == "X" else "X"


# TODO check if length is three for any of the potential lines
def check_win(board):
    players = ["X", "O"]
    plays = set()
    for [key, val] in board.items():
        if val != " ":
            plays.add(key)

    lines = []
    lines.append((play for play in plays if "top" in play))
    lines.append((play for play in plays if "mid" in play))
    lines.append((play for play in plays if "low" in play))

    lines.append((play for play in plays if "L" in play))
    lines.append((play for play in plays if "M" in play))
    lines.append((play for play in plays if "R" in play))

    checked = any(len(line) == 3 for line in lines)
    for line in lines:
        print(line)

    print(checked)

    # lines = [["top-L", "top-M", "top-R"], ["mid-L", "mid-M", "mid-R"], ["low-L", "low-M", "low-R"], ]
    if board['top-L'] in players and board['top-L'] == ['top-M'] == board['top-R']:
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
        return True
    return False


def check_game_over(board):
    start_pos = 0
    sum = 0
    plays = "".join(list(board.values()))
    while start_pos < len(board):
        pos = plays.find("XXX", start_pos)

        if pos != -1:
            start_pos = pos + 1
            sum += 1
        else:
            print(sum)


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
            break
        current_player = get_next_player(current_player)
        print(f"\n**************\nYour turn {current_player}")


def main():
    """Generates a Tic Tac Toe board and prints it to the screen
    """
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print_board(board)

    play_game(board)


if __name__ == "__main__":
    main()
