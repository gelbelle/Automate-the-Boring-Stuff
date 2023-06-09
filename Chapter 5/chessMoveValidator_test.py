import chessValidator


def test_valid_row_false():
    assert chessValidator.validate_row(9) == False


def test_valid_row_true():
    assert chessValidator.validate_row(1) == True


def test_valid_row_true9():
    assert chessValidator.validate_row(8) == True


def test_valid_col_false():
    assert chessValidator.validate_col('z') == False


def test_valid_col_true():
    assert chessValidator.validate_col('h') == True


def test_valid_color_true():
    assert chessValidator.validate_color('b') == True


def test_valid_color_false():
    assert chessValidator.validate_color('e') == False


def test_valid_piece_true():
    assert chessValidator.validate_piece("queen") == True


def test_valid_piece_false():
    assert chessValidator.validate_piece("qween") == False


def test_valid_square_true():
    assert chessValidator.validate_square('2g') == True


def tet_valid_square_false():
    assert chessValidator.validate_square("0g") == False


def test_valid_move_true():
    assert chessValidator.valid_move('2g', 'bbishop') == True


def test_valid_move_false():
    assert chessValidator.valid_move("9g", "rbishop") == False
