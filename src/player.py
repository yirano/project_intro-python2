# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player(Item):
    def __init__(self, current_room, player_items=[]):
        super().__init__(player_items)
        self.current_room = current_room

    def __str__(self):
        return f'{self.items}'

    # def add(self, item):
    #     self.items.append(item)

    # def drop(self, i):
    #     self.items.pop(i)
