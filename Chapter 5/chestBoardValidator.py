def check_num_pieces(pieces):
    print(pieces)
    num_white = len([piece for piece in pieces if piece[0] == 'w'])
    num_black = len([piece for piece in pieces if piece[0] == 'b'])
    if num_white > 16 or num_black > 16:
        return False


def main():
    board = {'1h': 'bking', '6c': 'wqueen',
             '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    check_num_pieces(list(board.values()))


if __name__ == "__main__":
    main()
