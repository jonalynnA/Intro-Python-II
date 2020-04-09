from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", ["keychain"]),

    'foyer':    Room("Foyer",
                     "Dim light filters in from the south. \nDusty passages run north and east.", ["elixer", "dagger"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. \nAhead to the north, a light flickers in
the distance, \nbut there is no way across the chasm.""", ["sword", "flashlight"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. \nThe smell of gold permeates the air.""", ["rope"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! \nSadly, it has already been completely emptied by
earlier adventurers. \nThe only exit is to the south."""),
}

# Declare Items
items = {
    'sword': Items("Sword", "A sword soaked in Vervain"),
    'dagger': Items("Dagger", "A dagger made of White Oak"),
    'elixer': Items("Elixer", "An elixer that heals you instantaneously"),
    'rope': Items("Rope", "A long three-strand rope tied with 8 knots"),
    'flashlight': Items("Flashlight", "A solar powered flashlight"),
    'keychain': Items("Silver Keychain", "What looks like a keychain may be the adventurers best tool: A permanent match-striker")
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

#print("Room north to 'Outside' : ")
# print(room['outside'].n_to.name)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("\nWhat shall I call you?: ")
player = Player(name, room["outside"])
stash = "s"
print(f"\nWhy hello, {player.name}!")


# Write a loop that:
gameIsPlaying = True
while gameIsPlaying:
    # * Prints the current room name
    print(f"\nYou are currently at the: \n{player.current_room.name}\n")

# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.current_room.description}",
          f"\n{player.current_room.item}")

    # * Waits for user input and decides what to do.
    userInput = input(
        f"\nWhat now, Adventurer {player.name}? \nChoose the direction you want to go...you can always hightail it out of here by typing [q]\n[N] [S] [E] [W] then [Enter]: ")

# If the user enters a cardinal direction, attempt to move to the room there.
    cardinal_direction = ["N", "S", "E", "W", "n", "s", "e", "w"]
    if userInput in cardinal_direction:
        player.move(userInput)

# If the user enters "take item" adds item to their stash
    elif userInput in stash:
        print(player.stash)

    elif userInput not in cardinal_direction:
        player.looting(userInput)

# If the user enters "q", quit the game.
    elif userInput == "q":
        gameIsPlaying = False


# Print an error message if the movement isn't allowed.
    else:
        print("\n Woah there, you must choose a Cardinal Direction. To quit, enter: q")
