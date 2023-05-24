import customUtils as utils
import sys


def delete_items():
    print("Please enter the name of the list you would like to delete items from: ", end="")
    utils.read_files("lists")
    list_name = input()

    print("You list currently has the following items on it: ")
    items = utils.open_file(list_name)
    utils.print_list(items)

    print("Enter the one you would like to delete: ", end="")
    remove_these = []
    while True:
        to_delete = input()
        remove_these.append(to_delete)
        print("Would you like to delete any more items? [y/n]")
        if utils.getAns(input(), ['y', 'n']) == "n":
            file = open(f"lists/{list_name}.txt", "w")
            for item in items:
                if item.strip("\n") not in remove_these:
                    file.write(f"{item}")
            file.close()
            break


def update_list():
    view_lists()
    print("Enter the name of the one you would like to add items to: ")
    list_name = input()
    print("Your list already has the following items on it: ")
    utils.print_list(utils.open_file(list_name))
    list_items = add_items()
    utils.save_list(list_name, list_items)
    print("Your list has been saved")


def add_items():
    list_items = []
    print("\nEnter the items you would like to add to your list: ")
    print("To complete and save your list enter 'q'")
    while True:
        item = input()
        if item == 'q':
            return list_items
        else:
            list_items.append(item)


def check_available(list_name):
    if list_name in utils.read_files(r"lists"):
        while True:
            print("I'm sorry, that list name is already taken.")
            print("Please enter another list name.")
            print("To go back to the main menu enter '*'")
            list_name = input()

            if list_name == '*':
                return


def create_list():
    print("Enter a name for your list: ")
    list_name = input()
    check_available(list_name)
    list_items = add_items()
    print("Would you like to save your list? [y/n]")
    if utils.getAns(input(), ['y', 'n']) == 'y':
        utils.save_list(list_name, list_items)
        print("Your list has been saved")
        return
    else:
        print(
            "By not entering a list name you have chosen not to save your list.")
        print("Are you sure? [y/n]")
        if utils.getAns(input(), ['y', 'n']) == "y":
            return


def open_list():
    print("Enter the name of the list you would like to read: ", end="")
    file_name = input()
    contents = utils.open_file(file_name)
    utils.print_list(contents)


def view_lists():
    print("The lists available are: ")
    files = utils.read_files(r"lists")
    utils.print_list(files)


def main():
    while True:
        choice = utils.greet_user(
            ["Create list", "View lists", "See list", "Add list items", "Delete list items", "Quit"])
        match choice:
            case '0':
                create_list()
            case '1':
                view_lists()
            case '2':
                open_list()
            case '3':
                update_list()
            case '4':
                delete_items()
            case '5':
                break


if __name__ == "__main__":
    main()
