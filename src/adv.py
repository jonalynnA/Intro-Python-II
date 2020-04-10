from room import Room
from player import Player
from items import Items

# Declare Items
items = {
    'sword': Items("Sword", "A sword soaked in Vervain"),
    'dagger': Items("Dagger", "A dagger made of White Oak"),
    'elixer': Items("Elixer", "An elixer that heals you instantaneously"),
    'rope': Items("Rope", "A long three-strand rope tied with 8 knots"),
    'flashlight': Items("Flashlight", "A solar powered flashlight"),
    'keychain': Items("Silver Keychain", "What looks like a keychain may be the adventurers best tool: A permanent match-striker")
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", items=["keychain"]),

    'foyer':    Room("Foyer",
                     "Dim light filters in from the south. \nDusty passages run north and east.", items=["elixer", "dagger"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. \nAhead to the north, a light flickers in
the distance, \nbut there is no way across the chasm.""", items=["sword", "flashlight"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. \nThe smell of gold permeates the air.""", items=["rope"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! \nSadly, it has already been completely emptied by
earlier adventurers. \nThe only exit is to the south.""", items=None)
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("\nWhat shall I call you?: ")
player = Player(name, room["outside"])

print(f"\nWhy hello, {player.name}!")

cardinal_direction = ["N", "S", "E", "W", "n", "s", "e", "w"]
verb_support = ["y", "n", "Y", "N", "loot", "take"]
inventory = "i"

# Write a loop that:
gameIsPlaying = True
while gameIsPlaying:

    # * Prints the current room name
    print(f"\nYou are currently at the: {player.current_room.name}")

    # * Prints the current description (the textwrap module might be useful here).
    print(f">>> {player.current_room.description} <<<\n",
          f"\n *** There's some loot *** \n    {player.current_room.items}")

    user_input_item = input(
        f"\n ** Would you like to take this loot? **\n[loot] [take] [y] [n] then [Enter]: ")
    if user_input_item in verb_support:
        player.take_item(player.current_room.items)

    elif user_input_item == 'n':
        print("Hope you didn't need that.")

    elif user_input_item == "i":
        player.get_inventory
 # Player can move
    user_input_direction = input(
        f"\nWhat now, Adventurer {player.name}? \nChoose the direction you want to go...you can always hightail it out of here by typing [q]\n[N] [S] [E] [W] then [Enter]: ")

# If the user enters a cardinal direction, attempt to move to the room there.
# If the user enters a "take" command, add item to player inventory
# If the user enters i display inventory

    if user_input_direction in cardinal_direction:
        player.move(user_input_direction)

    elif user_input_item == "i":
        player.get_inventory

# If the user enters "q", quit the game.
    elif user_input_direction == "q":
        gameIsPlaying = False

# Print an error message if the movement isn't allowed.
    else:
        print("\n Woah there, you must choose a Cardinal Direction. To quit, enter: q")
