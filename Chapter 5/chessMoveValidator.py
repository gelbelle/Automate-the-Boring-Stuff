def validate_col(col):
    return col >= 'a' and col <= 'h'


def validate_row(row):
    return row > 0 and row < 9


def validate_square(square):
    return validate_row(int(square[0])) and validate_col(square[1])


def validate_color(color):
    return color in ['b', 'w']


def validate_piece(piece):
    return piece in ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']


def valid_move(square, piece):
    valid_square = validate_square(square)
    valid_color = validate_color(piece[1])
    valid_piece = validate_piece(piece[1:])

    return all([valid_square, valid_color, valid_piece])


def main():
    moves = {'1h': 'bking', '6c': 'wqueen',
             '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    for key, val in moves.items():
        if not valid_move(key, val):
            print(f"I'm sorry, moving {val[1:]} to {key} is not valid.")
            return False

    print("All moves valid")


if __name__ == "__main__":
    main()
