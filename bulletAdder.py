#! python3
# A multi-clipboard program.

import pyperclip

original = pyperclip.paste()  # Get list to add bullets to

items = original.split()
new_list = []
for item in items:
    new_list.append(f"* {item}")
pyperclip.copy("\n".join(new_list))  # Copy list with bullets
print(pyperclip.paste())
