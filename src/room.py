# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.curr = ''

    def __str__(self):
        message = f'{self.name}: {self.desc}'
        if self.name == 'Outside Cave Entrance':
            self.curr = 'outside'
        elif self.name == 'Foyer':
            self.curr = 'foyer'
        elif self.name == 'Grand Overlook':
            self.curr = 'overlook'
        elif self.name == 'Narrow Passage':
            self.curr = 'narrow'
        else:
            self.curr = 'treasure'

        return self.curr
