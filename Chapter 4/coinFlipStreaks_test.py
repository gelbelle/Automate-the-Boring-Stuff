from coinFlipStreaks import count_streaks


def test_greater_than_1():
    assert count_streaks("HH", "THHTHTHTTHH") == 2


def test_none():
    assert count_streaks("HHH", "THTHTHT") == 0


def test_empty_sub_string():
    assert count_streaks("", "HTHTH") == 0


def test_empty_string():
    assert count_streaks("T", "") == 0
