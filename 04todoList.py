import customUtils as utils
import sys

list_items = []
print("Enter something you would like to add to your list: ")
print("To complete and save your list enter 'q'")
while True:
    item = input()
    if item == 'q':
        utils.save_list(list_items)
        print("Your list has been saved")
        sys.exit(0)
    else:
        list_items.append(item)
