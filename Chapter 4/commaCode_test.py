from commaCode import list_to_string


def test_over_2():
    assert list_to_string(["Daniel", "Arbour", "Whaling Station", "sunset", "beach"]) == \
        "Daniel, Arbour, Whaling Station, sunset, and beach"


def test_2():
    assert list_to_string(["sunset", "beach"]) == "sunset and beach"


def test_none():
    assert list_to_string([]) == ""
