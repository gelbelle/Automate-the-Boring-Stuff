import customUtils as utils
import sys
import os


def delete_list():
    files = view_lists()
    choice = utils.create_options(
        "\nChoose the list you would like to delete: ", files)
    print("Your list  has the following items on it: ")
    utils.print_list(utils.open_file(files[choice]))
    print(
        "Are you sure you want to delete this list? [y/n]\n**You will not be able to recover the list afterwards**")
    if utils.getAns(input(), ['y', 'n']) == 'y':
        os.remove(f"lists/{files[choice]}.txt")
        print(f"The list {files[choice]} has been deleted")
    else:
        print(f"The list {files[choice]} has not been deleted")


def delete_items():
    files = view_lists()
    file = files[utils.create_options(
        "\nChoose the list you would like to remove items from: ", files)]
    items = utils.open_file(file)
    idx = utils.create_options(
        "\nChoose the item you would like to delete\nTo end enter '*'", items)

    remove_these = []
    while True:
        remove_these.append(items[idx].strip())
        if input() == '*':
            file = open(f"lists/{file}.txt", "w")
            for item in items:
                if item.strip("\n") not in remove_these:
                    file.write(f"{item}")
            file.close()
            break


def update_list():
    files = view_lists()
    choice = utils.create_options(
        "\nChoose the list you would like to add items to: ", files)
    print("Your list already has the following items on it: ")
    utils.print_list(utils.open_file(files[choice]))
    list_items = add_items()
    utils.save_list(files[choice], list_items)
    print("Your list has been saved")


def add_items():
    list_items = []
    print("\nEnter the items you would like to add to your list: ")
    print("To complete and save your list enter '*'")
    while True:
        item = input()
        if item == '*':
            return list_items
        else:
            list_items.append(item)


def is_available(list_name):
    while True:
        if list_name in utils.read_files(r"lists"):
            print("I'm sorry, that list name is already taken.")
            print(
                "Please enter another list name or enter '*' to return to the main menu.")
            list_name = input()

            if list_name == '*':
                return False
        else:
            return True


def create_list():
    print("\nEnter a name for your list: ")
    list_name = input()
    if is_available(list_name):
        list_items = add_items()
        print("Would you like to save your list? [y/n]")
        if utils.getAns(input(), ['y', 'n']) == 'y':
            utils.save_list(list_name, list_items)
            print("Your list has been saved")
            return
        else:
            print(
                "\nBy not entering a list name you have chosen not to save your list.")
            print("Are you sure? [y/n]")
            if utils.getAns(input(), ['y', 'n']) == "y":
                return


def open_list():
    files = utils.read_files(r"lists")
    choice = utils.create_options(
        "\nChoose the list you would like to read", files)
    contents = utils.open_file(files[choice])
    utils.print_list(contents)


def view_lists():
    print("\nThe lists available are: ")
    files = utils.read_files(r"lists")
    utils.print_list(files)
    return list(files)


def main():
    while True:
        choice = utils.create_options("\nWhat would you like to do?",
                                      ["Create list", "Delete list", "View lists", "Read list",
                                       "Add list items", "Delete list items", "Quit"])
        options = [create_list, delete_list, view_lists, open_list,
                   update_list, delete_items, sys.exit]
        options[choice]()


if __name__ == "__main__":
    main()
