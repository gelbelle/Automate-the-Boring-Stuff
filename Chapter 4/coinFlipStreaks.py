import random

HEADS = "H"
TAILS = "T"


def count_streaks(sub: str, string: str) -> int:
    """ Takes in a substringand a string to search in. It returns the number of 
    times the substring appears in the string

    :param sub -- The substring to search for
    :type sub: str
    :param string -- The string to search in
    type string: str
    :return -- The total number of times the substring is found in the string, including
    overlapping iterations
    :rtype int
    """
    start_pos = 0
    sum = 0

    # If either sub or string is empty return 0
    if not sub or not string:
        return 0

    # Algorithm drawn from examples from Geeks for Geeks
    # https://www.geeksforgeeks.org/python-count-overlapping-substring-in-a-given-string/
    while start_pos < len(string):
        pos = string.find(sub, start_pos)

        if pos != -1:
            start_pos = pos + 1
            sum += 1
        else:
            return sum


def main():
    """Simulates flipping a coin a specified number of times then counts how many streaks of
    specified length appear in the coin flips.
    """
    flips = ""
    streak_length = 6

    for _ in range(1000):
        flips += random.choice([HEADS, TAILS])

    total_streaks = count_streaks(HEADS*streak_length)
    + count_streaks(TAILS*streak_length)

    print(
        f"Total number of streaks of {HEADS} and {TAILS} of length {streak_length} is {total_streaks}")


if __name__ == "__main__":
    main()
