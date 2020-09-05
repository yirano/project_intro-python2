from room import Room
from player import Player
from game import Game
# Declare all the rooms

outside = Room("Outside Cave Entrance",
               "North of you, the cave mount beckons", ['sticks', 'leaves'])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['flower', 'lamp'])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['sword', 'ax'])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['skull', 'hammer'])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['gold', 'forbidden treasure'])


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


# def handle_items():
#     pick_drop = input(
#         f"You've come across some items. [0] to skip, [1] to gather: ")
#     if pick_drop == str(1):
#         tools = input(f'Pick from the following items:{stuff}')
#         try:
#             player.append({player.current_room.items[int(tools)-1]})
#             print(f'Items in your Backpack:  {player.items}\n')
#         except IndexError:
#             print(
#                 'Such an item does not exist, you have missed the opportunity for it.')
#             pass
#     else:
#         pass

player = Player(outside)
game = Game()
print(player.current_room)

while True:
    # try:
    user = input("Pick a direction [n, s, e, w]: ")

    if user in {'n', 's', 'e', 'w'}:
        if hasattr(player.current_room, f'{user}_to'):
            player.current_room = getattr(
                player.current_room, f'{user}_to')
            tools = player.current_room.stuff()
    print(f'\n{player.current_room}\n')
    Game.handle_items(tools)

    # except AttributeError:
    #     print("\nYou've just fallen into the pit of hell.")
    #     break
