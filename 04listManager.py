import customUtils as utils
import sys


def delete_items():
    print("Please enter the name of the list you would like to delete items from: ", end="")
    utils.read_files("lists")
    list_name = f"lists/{input()}.txt"
    print("You list currently has the following items on it: ")
    items = utils.open_file(list_name)
    for item in items:
        print(item, end="")

    print("Enter the one you would like to delete: ", end="")
    to_delete = []
    while True:
        to_delete.append(input())
        print("Would you like to delete any more items? [y/n]")
        if utils.getAns(input(), ['y', 'n']) == "n":
            file = open(list_name, "w")
            for item in items:
                if item.strip("\n") not in to_delete:
                    file.write(f"{item}")
            file.close()
            break


def add_items():
    list_items = []
    print("Enter the items you would like to add to your list: ")
    print("To complete and save your list enter 'q'")
    while True:
        item = input()
        if item == 'q':
            while True:
                name = utils.ask_save("Would you like to save your list?")
                if name:
                    utils.save_list(name, list_items)
                    print("Your list has been saved")
                    return
                else:
                    print(
                        "By not entering a list name you have chosen not to save your list.")
                    print("Are you sure? [y/n]")
                    if utils.getAns(input(), ['y', 'n']) == "y":
                        return
        else:
            list_items.append(item)


def read_list():
    print("Enter the name of the list you would like to read: ", end="")
    list_name = input()
    utils.print_list(f"lists/{list_name}.txt")


def view_lists():
    print("The lists available are: ")
    utils.read_files(r"lists")


def main():
    while True:
        choice = utils.greet_user(
            ["View lists", "See list", "Add list items", "Delete an item from your list", "Quit"])
        match choice:
            case '0':
                view_lists()
            case '1':
                read_list()
            case '2':
                add_items()
            case '3':
                delete_items()
            case '4':
                sys.exit(0)


if __name__ == "__main__":
    main()
