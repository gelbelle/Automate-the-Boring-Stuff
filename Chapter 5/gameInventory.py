import gameItems


def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for [key, val] in inventory.items():
        print(f"{key}: {val}")
        total_items += val
    print(f"Total number of items: {total_items}")


def add_to_inventory(items, inventory):
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def create_item(item_name):
    match item_name:
        case "dagger":
            return gameItems.Weapon("Basic Dagger", "False", 30, 5, "Piercing")
        case "armour":
            return gameItems.Armour("Armour", False, 50, 30)
        case "arrow":
            return gameItems.Weapon("Basic Arrow", False, 5, 2, "Piercing")
        case "torch":
            return gameItems.Items("Basic Torch", False, 10)
        case "gold coin":
            return gameItems.Treasure("Gold Coin", False, 1)
        case "gem":
            return gameItems.Treasure("Gem", False, 100)


def main():
    inventory = {"rope": 1, "torch": 6,
                 "gold coin": 42, "dagger": 1, "arrow": 12}
    loot = ["gold coin",
            "dagger", "gold coin", "gold coin", "gem"]
    display_inventory(inventory)
    inventory = add_to_inventory(loot, inventory)
    display_inventory(inventory)


if __name__ == "__main__":
    main()
