class Item:
    def __init__(self, items=[]):
        self.items = items

    def __str__(self):
        return f'{self.items}'

    def add(self):
        self.items.append('apple')
