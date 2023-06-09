import chessMoveValidator
import chessUtils


def test_valid_row_false():
    assert chessUtils.validate_row(9) == False


def test_valid_row_true():
    assert chessUtils.validate_row(1) == True


def test_valid_row_true9():
    assert chessUtils.validate_row(8) == True


def test_valid_col_false():
    assert chessUtils.validate_col('z') == False


def test_valid_col_true():
    assert chessUtils.validate_col('h') == True


def test_valid_square_true():
    assert chessUtils.validate_square('2g') == True


def tet_valid_square_false():
    assert chessUtils.validate_square("0g") == False


def test_valid_color_true():
    assert chessMoveValidator.validate_color('b') == True


def test_valid_color_false():
    assert chessMoveValidator.validate_color('e') == False


def test_valid_piece_true():
    assert chessMoveValidator.validate_piece("queen") == True


def test_valid_piece_false():
    assert chessMoveValidator.validate_piece("qween") == False


def test_valid_move_true():
    assert chessMoveValidator.valid_move('2g', 'bbishop') == True


def test_valid_move_false():
    assert chessMoveValidator.valid_move("9g", "rbishop") == False
