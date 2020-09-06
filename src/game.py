from player import Player
from room import Room


class Game(Player):
    def __init__(self, player_items=[]):
        super().__init__(player_items)

    def handle_items(self, tools):
        pick_drop = input(
            f"You've come across some items. [0] to skip, [1] to gather, [2] to drop: ")
        if pick_drop == str(1):
            picked = input(f'Pick from the following items:{tools}')
            try:
                self.player_add(tools[int(picked)-1])
            except IndexError:
                print(
                    'Such an item does not exist, you have missed the opportunity for it.')
                pass
        elif pick_drop == str(2):
            try:
                if len(self.player_items) == 0:
                    print('There is nothing to drop')
                else:
                    rid = input(
                        f"Pick an item to drop: {self.player_items} >>>")
                    self.player_drop(int(rid)-1)

            except IndexError:
                pass
        if len(self.player_items) > 0:
            print(f'Items in your Backpack:  {self.player_items}\n')
        else:
            print("Your bag is empty")

    def control_direction(self):
        return input("Pick a direction [n, s, e, w]: ")
