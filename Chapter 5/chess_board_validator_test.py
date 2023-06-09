import chess_board_validator


def test_piece_type_true():
    assert chess_board_validator.check_num_pieces(
        ['bking',  'wqueen', 'bbishop', 'bqueen', 'wking']) == True


def test_piece_type_false():
    assert chess_board_validator.check_num_pieces(
        ['wking',  'wqueen', 'bbishop', 'bqueen', 'wking']) == False


def test_total_pieces_true():
    assert chess_board_validator.check_num_pieces(
        ['bking',  'wqueen', 'bbishop', 'bqueen', 'wking']) == True
