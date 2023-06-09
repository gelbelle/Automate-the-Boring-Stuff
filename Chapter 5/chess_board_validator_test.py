import chess_move_validator

board = ['king',  'wqueen', 'bbishop', 'bqueen', 'wking']


def test_total_pieces_true():
    assert chess_move_validator.check_num_pieces(board) == True
