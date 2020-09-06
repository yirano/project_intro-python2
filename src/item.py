class Item:
    def __init__(self, room_items=[], player_items=[], items=[]):
        self.player_items = player_items
        self.room_items = room_items
        self.items = items

    def __str__(self):
        # return f'{self.items}'
        output = ''
        for tools in self.room_items:
            output += f'\n1. {tools}'
        return output

    def player_add(self, item):
        self.player_items.append(item)

    def player_drop(self, item):
        self.player_items.pop(item)

    def room_add(self, item):
        self.room_items.append(item)

    def room_drop(self, item):
        self.room_items.pop(item)
