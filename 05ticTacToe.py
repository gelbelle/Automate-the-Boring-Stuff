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

# TODO count streaks of 3 to determine if line? Maybe just do by hand right now


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

    while plays < 9:
        new_board = get_move(current_player, board)
        check_game_over(new_board)
        print_board(new_board)
        current_player = get_next_player(current_player)
        print(f"\n**************\nYour turn {current_player}")
        plays += 1


def main():
    """Generates a Tic Tac Toe board and prints it to the screen
    """
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print_board(board)

    play_game(board)
    print("Game over")


if __name__ == "__main__":
    main()
