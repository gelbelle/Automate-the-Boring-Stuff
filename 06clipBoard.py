import pyperclip as pc

"""
This program allows the user to create custom snippets.
The user can set keywords for each snippet for fast pasting.
"""


def main():
    snippet_names = {'agree': """Yes, I agree. That sounds fine to me.""",
                     'busy': """Sorry, can we do this later this week or next week?""",
                     'upsell': """Would you consider making this a monthly donation?"""}
    snippet_names["agree"] = pc.copy("Hello")


if __name__ == "__main__":
    main()
