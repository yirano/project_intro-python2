# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room(Item):
    def __init__(self, name, description, items=[]):
        super().__init__(items)
        self.name = name
        self.description = description
        self.s_to = None
        self.w_to = None
        self.n_to = None
        self.e_to = None

    def __str__(self):
        output = f'{self.name}: {self.description}\n'
        stuff = f'{self.items}'
        if self.s_to:
            output += 'To the south is: ' + self.s_to.name + '\n'
        elif self.w_to:
            output += 'To the west is: ' + self.w_to.name + '\n'
        elif self.e_to:
            output += 'To the east is: ' + self.e_to.name + '\n'
        elif self.n_to:
            output += 'To the north is: ' + self.n_to.name + '\n'
        return output + stuff

    def stuff(self):
        # print(f'STUFF: {user}')
        return f'Items to choose: {self.items}'
