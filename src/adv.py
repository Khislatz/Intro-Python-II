from room import Room
from player import Player
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

new_player = Player("Bobby", room['outside'])

new = ['north', 'North', 'east', 'East', 'west', 'West']
nw = ['north', 'North', 'west', 'West']

'north' == 'North'
'south' == 'South'
'east' == 'East'
'west' == 'West'

quit_game = False

while quit_game != True: 
    print(f'{new_player.name} is in {new_player.curr_room}')
    print(f'{new_player.curr_room.description}')

    user_input = input("Please enter North or north, South or south, East or east, and West or west, else q to quit: ")
    

    if user_input == 'q':
            quit_game = True
    elif new_player.curr_room.name == room['outside'].name and user_input == ('north' or 'North'):
        new_player.curr_room = room['foyer']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room.name == room['outside'].name and user_input != ('north' or 'North'):
        print("The movement isn't allowed, please try again.")
    # From Foyer to Outside
    elif new_player.curr_room.name == room['foyer'].name and user_input == ('south' or 'South'):
        new_player.curr_room = room['outside']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    # From Foyer to Overlook
    elif new_player.curr_room.name == room['foyer'].name and user_input == ('north' or 'North'):
        new_player.curr_room = room['overlook']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    # From Foyer to Narrow
    elif new_player.curr_room.name == room['foyer'].name and user_input == ('east' or 'East'):
        new_player.curr_room = room['narrow']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room.name == room['foyer'].name and user_input == ('west' or 'West'):
        print("The movement isn't allowed, please try again.")
    # From Overlook to Foyer
    elif new_player.curr_room.name == room['overlook'].name and user_input == ('south' or 'South'):
        new_player.curr_room = room['foyer']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room.name == room['overlook'].name and user_input in new:
        print("The movement isn't allowed, please try again.")
    # From Narrow to Foyer
    elif new_player.curr_room.name == room['narrow'].name and user_input == ('west' or 'West'):
        new_player.curr_room = room['foyer']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    # From Narrow to Treasure
    elif new_player.curr_room.name == room['narrow'].name and user_input == ('north' or 'North'):
        new_player.curr_room = room['treasure']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room.name == room['narrow'].name and user_input  in nw:
        print("The movement isn't allowed, please try again.")
    # From Treasure to Narrow
    elif new_player.curr_room.name == room['treasure'].name and user_input == ('south' or 'South'):
        new_player.curr_room = room['narrow']
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    else:
        print("Invalid option. Please try again.")
        

