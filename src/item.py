class Item:
    def __init__(self, items=[]):
        self.items = items

    def __str__(self):
        # return f'{self.items}'
        output = ''
        for tools in self.items:
            output += f'\n1. {tools}'
        return output
