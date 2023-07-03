#! python3
# A multi-clipboard program.

import sys
import pyperclip
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'profile': """
        Angeleah Hoeppner
        Research Assistant,
        Community Profiles Project
        250 335-2037
        """}

# Handles command line arguments

if len(sys.argv) < 2:
    print("Usage: python 06customClipboard.py [keyphrase] - copy phrase text")
    sys.exit()
keyphrase = sys.argv[1]  # First command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}")
