from rooms import Room
from players import Player
from items import Item

# Declare all the items

items = {
    'sword': Item('sword').get_item(),
    'coins': Item('coins').get_item(),
    'hammer': Item('hammer').get_item()
}


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


player_name = input("Player name: ").strip()
new_player = Player(player_name, 'outside')
# new_player = Player("Bobby", room['outside'])

new = ['north', 'North', 'east', 'East', 'west', 'West']
nw = ['north', 'North', 'west', 'West']

'north' == 'North'
'south' == 'South'
'east' == 'East'
'west' == 'West'

quit_game = False

def player_items():
    if len(new_player.items) < 1:
        return "There are no items in the inventory."
    elif len(new_player.items) == 1:
        return str(new_player.items[0])
    else:
        return ", ".join(new_player.items)

def room_items():
    if len(room[new_player.curr_room].items) < 1:
        return "There are no items in the room."
    elif len(room[new_player.curr_room].items) == 1:
        return str(room[new_player.curr_room].items)
    else:
        return ", ".join(room[new_player.curr_room].items)

while quit_game != True: 
    print(f'The player {new_player.player_name} is currently (in) {room[new_player.curr_room].room_name}')
    print(f'Room description: {room[new_player.curr_room].description}')
    print(f'The room contains the following items: ' + room_items())

    user_input = input("Please enter North or north, South or south, East or east, and West or west, else q to quit: ").strip()
    # user_input = input("Choose a direction to travel, press q to quit, i for inventory, weapon name to pick up,"
    #             " [drop item_name] to drop item in different room >> ").strip().lower()

    print("\n")
    print("User Input: " + str(user_input.split()))

    # Drop item in whatever room you are in
    if user_input.split()[0] == 'drop' and user_input.split()[1] in new_player.items:
        new_player.items.remove(user_input.split()[1])
        room[new_player.room].items.append(user_input.split()[1])
    elif user_input.split()[0] == 'drop' and user_input.split()[1] not in new_player.items:
        print("The item is not in the inventory")

    # Add item to inventory from current room
    if user_input in room[new_player.curr_room].items:
        room[new_player.curr_room].items.remove(user_input)
        new_player.items.append(user_input)
    elif user_input not in room[new_player.curr_room].items and user_input.split()[0] != "drop":
        print("The item is not in the room")

    # Choose directions:
    if user_input == 'q':
        quit_game = True

    if new_player.curr_room == 'outside' and user_input == ('north' or 'North'):
        new_player.curr_room = 'foyer'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room == 'outside' and user_input != ('north' or 'North'):
        print("The movement isn't allowed, please try again.")
    # From Foyer to Outside
    elif new_player.curr_room == 'foyer' and user_input == ('south' or 'South'):
        new_player.curr_room = 'outside'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    # From Foyer to Overlook
    elif new_player.curr_room == 'foyer' and user_input == ('north' or 'North'):
        new_player.curr_room = 'overlook'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    # From Foyer to Narrow
    elif new_player.curr_room == 'foyer' and user_input == ('east' or 'East'):
        new_player.curr_room = 'narrow'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room == 'foyer' and user_input == ('west' or 'West'):
        print("The movement isn't allowed, please try again.")
    # From Overlook to Foyer
    if new_player.curr_room == 'overlook' and user_input == ('south' or 'South'):
        new_player.curr_room = 'foyer'.s_to
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room == room['overlook'].room_name and user_input in new:
        print("The movement isn't allowed, please try again.")
    # From Narrow to Foyer
    elif new_player.curr_room == 'narrow' and user_input == ('west' or 'West'):
        new_player.curr_room = 'foyer'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    # From Narrow to Treasure
    elif new_player.curr_room == 'narrow' and user_input == ('north' or 'North'):
        new_player.curr_room = 'treasure'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    elif new_player.curr_room == 'narrow' and user_input  in nw:
        print("The movement isn't allowed, please try again.")
    # From Treasure to Narrow
    elif new_player.curr_room == 'treasure' and user_input == ('south' or 'South'):
        new_player.curr_room = 'narrow'
        print(f"Your new current room is {new_player.curr_room}! Please move forward or press q to quit.")
    else:
        print("Invalid option. Please try again.")
        

