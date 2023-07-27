"""
Takes a phrase from a user and translates it to piglatin for them.
"""

VOWELS = ("a", "e", "i", "o", "u", "y")


def main():
    message = input()
    translated = []

    for word in message.split():
        pre_non_letters = ""
        while len(word) > 0 and not word[0].isalpha():
            pre_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            translated.append(pre_non_letters)
            continue
        suff_non_letters = ""
        while len(word) > 0 and not word[-1].isalpha():
            suff_non_letters = word[-1] + suff_non_letters
            word = word[:-1]

        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower()

        consonants = ""

        while len(word) > 0 and not word[0] in VOWELS:
            consonants += word[0]
            word = word[1:]
        if consonants != "":
            word += consonants + "ay"
        else:
            word += "yay"

        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        translated.append(pre_non_letters + word + suff_non_letters)

    print(" ".join(translated))


if __name__ == "__main__":
    main()
