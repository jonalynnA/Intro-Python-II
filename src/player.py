# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(
                self.current_room, f"{direction}_to", self.current_room.items)

        else:
            print(f"\nOpps, you hit a wall, choose another direction")

    def __str__(self):
        return (f"{self.name}")

    def get_inventory(self):
        # Since inventory is a list of objects cannot do x.items musts use for x in i
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(
                    f"\nYou are carrying: \n*{i.name}")
        else:
            print("You have nothing in your inventory.")

    def take_item(self, item):  # Add ability to add item to player inventory
        if item not in self.inventory and item in self.current_room.items:
            self.inventory.append(item)
            for i in self.inventory:
                print(
                    f"\n\n\nITEM: {i.name}\nDESCIPTION: {i.description}\nFYI: Check your inventory at any time[i] then[Enter]<<<"
                    "\nTo ditch something from your loot: [drop][x] then [Enter]")

        elif item not in self.current_room.items:
            print("There is nothing to loot")

        else:
            print("You already grabbed the loot")

    def drop_item(self, item):  # Add ability to drop item from player inventory
        if item in self.inventory:
            self.inventory.remove(item)
            for i in self.inventory:
                print(f"\n You dropped the {i.name}")
                self.get_inventory()

        else:
            print(f"\n You don't have {i.name} in your inventory")
