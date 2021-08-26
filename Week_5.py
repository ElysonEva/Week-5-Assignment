# Evangelista, Elyson

loaded_file = False
location_descriptions = {0: "You have quit the game."}
exit_directions = [{"Quit": 0}]
loc = 0


class Room:
    """
    The room class organises the room data to append the room description to global dictionary location_descriptions
    using the room number and room description. The available room exits are appended to global list exit directions as
    dictionaries, having the cardinal direction as keys for the number value.
    """
    def __init__(self, room_info):
        room_dict = {}
        split_info = room_info.split('+')  # setup room data into parts
        self.room_num = split_info[2].split(' ')[1:]
        self.north, self.south, self.east, self.west = self.room_num  # room direction assignment
        room_dict['North'] = int(self.north)  # assignment of room number to exit dict
        room_dict['South'] = int(self.south)
        room_dict['East'] = int(self.east)
        room_dict['West'] = int(self.west.strip('\n'))
        room_dict["Quit"] = 0
        exit_directions.append(room_dict)  # add dict rooms to exit_directions
        self.desc = split_info[1]  # room description
        self.room_num = int(split_info[0].strip(' '))  # room number
        location_descriptions[self.room_num] = self.desc  # reassigns the unique room number with description as dict


def LoadDungeon(user_dungeon_file):
    """
    LoadDungeon function attempts to read a valid .text or .text equivalent file specified in the argument,
    user_dungeon_file. The function checks if valid file has already been loaded through loaded_file,
    if it is true, the function prints an error message. The function attempts to read the file and and pass text to
    Room class. If in case of FileNotFoundError,function prints error message.
    """
    global loaded_file
    if loaded_file is False:
        try:
            read_dungeon_file = open(user_dungeon_file, 'r')
            for lines in read_dungeon_file:
                Room(lines)
            read_dungeon_file.close()
            if len(exit_directions) > 1:
                loaded_file = True
        except FileNotFoundError:
            print('Invalid dungeon file.')
    else:
        print("Dungeon has already been loaded.")


def DungeonGame():
    """
    Function DungeonGame takes user commands to execute commands and navigate through loaded .text files. These commands
    include LoadDungeon. Attempts to load invalid dungeon files print an error message. User commands are used to
    navigate loaded files using cardinal directions, 'North, 'South,'East', and 'West. The user can close valid rooms
    with the 'CloseDoor' command and valid room direction. The user can quit the program with the 'Quit' command. Any
    invalid commands prints an error message but continues the program.
    """
    global loc
    while loc == 0:
        user_input = input('$ ')
        n = user_input.split(' ')
        if n[0] == 'LoadDungeon' and len(n) == 2:
            LoadDungeon(n[1])
            if loaded_file is True:
                loc = 1
            else:
                print('Invalid dungeon file.')
        elif n[0] == 'Quit':
            print(location_descriptions[loc])
            break
        else:
            print("No valid dungeon file entered, please enter dungeon file")
    while loc != 0:
        print(location_descriptions[loc])
        user_input = input('$ ')
        n = user_input.split(' ')
        if n[0] == 'LoadDungeon':  # Dungeon file check
            print("Dungeon already loaded!")
        elif n[0] in exit_directions[loc]:  # valid direction choice
            if exit_directions[loc][n[0]] == 0:
                loc = 0
                print(location_descriptions[loc])
            elif exit_directions[loc][n[0]] == -1:
                print('There is no room in this direction.')
            elif exit_directions[loc][n[0]] < -1:
                print('This room is closed.')
            else:
                loc = exit_directions[loc][n[0]]
        elif n[0] == 'CloseDoor':  # close door command
            if exit_directions[loc][n[1]] < -1:
                print("The door is already closed.")
            elif exit_directions[loc][n[1]] == -1:
                print('There is no room.')
            else:
                exit_directions[loc][n[1]] = -2
                print('The door is now closed.')
        else:  # invalid user input
            print('Invalid input')

