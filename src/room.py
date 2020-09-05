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
            return output + '\n' + 'You have entered from ' + self.s_to.name + '\n'
        elif self.w_to:
            return output + '\n' + 'You have entered from ' + self.w_to.name + '\n'
        elif self.e_to:
            return output + '\n' + 'You have entered from ' + self.e_to.name + '\n'
        elif self.n_to:
            return output + '\n' + 'You have entered from ' + self.n_to.name + '\n'
        return output + stuff

    def stuff(self):
        # return self.items
        output = ''
        n = 1
        for tools in self.items:
            output += f'\n{n}. {tools}'
            n += 1
        return output + '\n>>> '
