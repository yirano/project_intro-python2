from player import Player


class Game(Player):
    def __init__(self, items=[]):
        super().__init__(items)

    def handle_items(self, tools):
        output = ''
        pick_drop = input(
            f"You've come across some items. [0] to skip, [1] to gather: ")
        if pick_drop == str(1):
            tools = input(f'Pick from the following items:{tools}')
            try:
                self.player.append(
                    {self.player.current_room.items[int(tools)-1]})
                print(f'Items in your Backpack:  {self.player.items}\n')
            except IndexError:
                print(
                    'Such an item does not exist, you have missed the opportunity for it.')
                pass
