from room import Room
from player import Player
from items import Items

# Term Colors
black = '\033[30m'
red = '\033[31m'
green = '\033[32 m'
yellow = '\033[33 m'
blue = '\033[34 m'
magenta = '\033[35 m'
cyan = '\033[36 m'
white = '\033[37 m'
reset_color = '\033[39 m'

# Declare Items
items = {
    'sword': Items("Sword", "A sword soaked in Vervain"),
    'dagger': Items("Dagger", "A dagger made of White Oak"),
    'elixer': Items("Elixer", "An elixer that heals you instantaneously"),
    'rope': Items("Rope", "A long three-strand rope tied with 8 knots"),
    'flashlight': Items("Flashlight", "A solar powered flashlight"),
    'keychain': Items("Silver Keychain", "What looks like a keychain may be the adventurers best tool. A permanent match-striker")
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", [items["keychain"]]),

    'foyer':    Room("Foyer",
                     "Dim light filters in from the south. \nDusty passages run north and east.", [items["elixer"], items["dagger"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. \nAhead to the north, a light flickers in
the distance, \nbut there is no way across the chasm.""", [items["sword"], items["flashlight"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. \nThe smell of gold permeates the air.""", [items["rope"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! \nSadly, it has already been completely emptied by
earlier adventurers. \nThe only exit is to the south.""", None)
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
name = input(red + "\nWhat shall I call you?: \033[37m")
player = Player(name, room["outside"])

print(f"\n\n\nWhy hello, {player.name}!")

cardinal_direction = ["n", "s", "e", "w"]
verb_support = ["y", "Y", "loot", "take", "keychain", "sword",
                "dagger", "elixer", "rope", "silver keychain", "flashlight"]
drop = ["drop", "leave", "x"]
inventory = "i"

# Write a loop that:
gameIsPlaying = True
while gameIsPlaying:

    # * Prints the current room name

    print(f"\nYou are currently at the: {player.current_room.name}\n",
          f" >>> {player.current_room.description} <<<\n")

    # * Prints the current description (the textwrap module might be useful here).
    if player.current_room != "treasure":
        for i in player.current_room.items:
            print(
                "><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><"

                f"\n\n *** You stumbled onto an item *** \n     {i.name}\n\n"

                "><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")

    user_input_item = input(
        red + f"\n ** Would you like to take this loot? **\n[loot] [take] [y] [n] then [Enter]: \033[37m").lower()
    if user_input_item in verb_support:
        for item in player.current_room.items:
            player.take_item(item)

    elif user_input_item == 'n':
        print("Hope you didn't need that.")

    elif user_input_item in drop:
        player.drop_item(item)

    elif user_input_item == "i":
        player.get_inventory()
 # Player can move
    user_input_direction = input(
        f"\nWhat now, Adventurer {player.name}? \nChoose the direction you want to go...you can always hightail it out of here by typing [q] \033[36m\n[N] [S] [E] [W] then [Enter]: \033[37m").lower()

# If the user enters a cardinal direction, attempt to move to the room there.
# If the user enters a "take" command, add item to player inventory
# If the user enters i display inventory

    if user_input_direction in cardinal_direction:
        player.move(user_input_direction)

    elif user_input_direction == "i":
        player.get_inventory()

    elif user_input_direction in drop:
        player.drop_item(item)

# If the user enters "q", quit the game.
    elif user_input_direction == "q":
        gameIsPlaying = False

# Print an error message if the movement isn't allowed.
    else:
        print("\n Woah there, you must choose a Cardinal Direction. To quit, enter: q")
