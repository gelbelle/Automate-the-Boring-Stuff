

def list_to_string(to_format: list) -> str:
    """ Take a list and return a string formatted based on the length of the string

    :param to_format -- the list to be formatted
    :type to_format: str
    :returns: a string formatted based on the length of to_format
    [item1, item2, item3] -> "item1, item2, and item3"
    [item1, item2] -> "item1 and item2"
    [item1] -> "item1
    [] -> ""
    :rtype: str

    """

    try:
        if len(to_format) > 2:
            return ", and ".join((", ".join(to_format[:-1]), to_format[-1]))
        if len(to_format) == 2:
            return f"{to_format[0]} and {to_format[1]}"
        else:
            return to_format[0]
    except IndexError:
        return ""


def main():
    to_format = ["Daniel", "Arbour"]
    list_to_string(to_format)


if __name__ == "__main__":
    print(main())
