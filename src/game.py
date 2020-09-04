from room import Room


class Game(Room):
    def __init__(self, player, user):
        super().__init__(user)
        self.player = player

    def tools(self, player, user):
        print(f'INSIDE {user}')
        return getattr(self.player.current_room, f'{user}_to').stuff()
