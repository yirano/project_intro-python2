from room import Room
from player import Player
# Declare all the rooms

outside = Room("Outside Cave Entrance",
               "North of you, the cave mount beckons", ['sticks', 'leaves'])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['flower', 'lamp'])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(outside)
print(player.current_room)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user = input("Pick a direction: ")

while user != 'q':
    if user in {'n', 's', 'e', 'w'}:
        if hasattr(player.current_room, f'{user}_to'):
            player.current_room = getattr(player.current_room, f'{user}_to')

    ''' Using the following block would require x4
    if user == 'n':
        # check if the curr room has a n_to attr
        if player.current_room.n_is not None:
            # move the player to that room
            player.current_room = player.current_room.n_to
    '''
