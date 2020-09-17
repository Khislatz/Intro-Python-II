# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, player_name, curr_room):
        self.player_name = player_name
        self.curr_room = curr_room
        self.items = []

    def __str__(self):
        return f"name: {self.player_name}, room: {self.curr_room}, items: {self.items}"