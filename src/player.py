# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player(Item):
    def __init__(self, current_room, items=[]):
        super().__init__(items)
        self.current_room = current_room

    def __str__(self):
        return f'{self.items}'

    # def append(self, item):
    #     self.items.extend(item)

    # def rid(self):
    #     print(f'DROP THIS')
    #     # self.items.pop(i)

# print(Player('north', ['apple']))
