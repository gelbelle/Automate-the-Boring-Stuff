import chessUtils
import operator


def check_num_pieces(pieces):
    valid_pieces = {
        "king": 1,
        "queen": 1,
        "bishop": 2,
        "knight": 2,
        "rook": 2,
        "pawn": 8
    }
    white = [piece for piece in pieces if piece[0] == 'w']
    black = [piece for piece in pieces if piece[0] == 'b']

    white_pieces = {}
    black_pieces = {}

    for piece in white:
        white_pieces[piece[1:]] = white.count(piece)

    for piece in black:
        black_pieces[piece[1:]] = black.count(piece)

    for key, val in valid_pieces.items():
        if white_pieces.get(key):
            if white_pieces[key] > val:
                print(f"You have too many {key}s")
                return False
        if black_pieces.get(key):
            if black_pieces[key] > val:
                print(f"You have too many {key}s")
                return False

    return len(white) <= 16 and len(black) <= 16


def main():
    board = {'1h': 'bking', '6c': 'wqueen',
             '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    for key in board.keys():
        if not chessUtils.validate_square(key):
            print(f"{key} is not a valid square")
            return False

    if not check_num_pieces(list(board.values())):
        print("There are too many pieces on the board")
        return False


if __name__ == "__main__":
    main()
