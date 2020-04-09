# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, stash=[]):
        self.name = name
        self.current_room = current_room
        self.stash = stash

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(
                self.current_room, f"{direction}_to", self.current_room.item)

        else:
            print(f"\nOpps, you hit a wall, choose another direction")

    def addItemToPlayer(self, item):  # Add ability to add item to player stash
        item.append(item)

    def looting(self, loot):  # Add ability to loot the item into stash
        loot = loot.split(" ")
        if loot[0] == "take":
            if loot[1] in self.current_room.item:
                self.current_room.item.remove(loot[1])
                self.stash.append(loot[1])
                return print(f"You have looted {loot[1]} into your stash")
            else:
                print("Unable to Loot")
        elif loot[0] == "drop":
            if loot[1] not in self.current_room.item:
                self.stash.remove(loot[1])
                self.current_room.item.append(loot[1])
                return print(f"You have dropped {loot[1]}")
            else:
                print(f"That item is not in your stash ")
