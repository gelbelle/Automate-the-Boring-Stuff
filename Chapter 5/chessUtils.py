def validate_col(col):
    return col >= 'a' and col <= 'h'


def validate_row(row):
    return row > 0 and row < 9


def validate_square(square):
    return validate_row(int(square[0])) and validate_col(square[1])
