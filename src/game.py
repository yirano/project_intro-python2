from player import Player
from room import Room


class Game(Player):
    def __init__(self, items=[]):
        super().__init__(items)

    def handle_items(self, tools):
        pick_drop = input(
            f"You've come across some items. [0] to skip, [1] to gather, [2] to drop: ")
        if pick_drop == str(1):
            picked = input(f'Pick from the following items:{tools}')
            try:
                self.items.append(tools[int(picked)-1])
                # print(f'Items in your Backpack:  {self.items}\n')
            except IndexError:
                print(
                    'Such an item does not exist, you have missed the opportunity for it.')
                pass
        elif pick_drop == str(2):
            try:
                if len(self.items) == 0:
                    print('There is nothing to drop')
                else:
                    rid = input(f"Pick an item to drop: {self.items} >>>")
                    self.items.pop(int(rid)-1)

            except IndexError:
                pass
        print(f'Items in your Backpack:  {self.items}\n')
