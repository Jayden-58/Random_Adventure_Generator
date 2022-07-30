'''
READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP  

READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

'''



'''
import random
#S: start
#w: wall
#R: room
#E: end
#u: unknown

# make a 10 by 10 grid


player_rows_position = 1
player_cols_position = 1
player_previous_rows_position = 1
player_previous_cols_position = 1


def make_map():
    map = []
    for rows in range(0, 10, 1):
        map.append([])
        for col in range(0, 10, 1):
            if rows == 0 or rows == 9:  # top and bottom of the map are made into walls
                map[rows].append("w")
            elif col == 0 or col == 9:
                map[rows].append("w")  # sides of the map are made into walls
            elif rows == 1 and col == 1:
                map[rows].append("S")  # the start will always be at (1,1)
            elif rows == 1 and col == 2:  # tile to the right of the start
                # determines if a square will be a room or a wall
                letter = ""
                wall_calculator = random.randint(0, 1)
                if wall_calculator == 1:
                    map[rows].append("R")
                else:
                    map[rows].append("w")
                    # all the squares in the first non wall row (after the start and first square are already assigned)
            elif rows == 1:
                if map[rows][col - 1] == "R":
                    letter = ""
                    wall_calculator = random.randint(0, 1)
                    if wall_calculator == 1:
                        map[rows].append("R")
                    else:
                        map[rows].append("w")
                else:
                    map[rows].append("w")

            elif rows == 2 and col == 1:
                # the tile under the start location reacts to how the tile to the right of the start location gets assigned.
                # if the tile to the right of the start is a wall, the tile under the start MUST be a room.
                if map[1][2] == "w":
                    map[rows].append("R")
                else:
                    letter = ""
                    wall_calculator = random.randint(0, 1)
                    if wall_calculator == 1:
                        map[rows].append("R")
                    else:
                        map[rows].append("w")
            else:
                if map[rows - 1][col] == "R" and map[rows][col - 1] == "R":
                    letter = ""
                    wall_calculator = random.randint(0, 1)
                    if wall_calculator == 1:
                        map[rows].append("R")
                    else:
                        map[rows].append("w")
                elif map[rows - 1][col] == "R" or map[rows][col - 1] == "R":
                    map[rows].append("R")
                else:
                    map[rows].append("w")
    while True:  # finds a random end point for the dungeon
        rows_index = random.randint(0, rows - 1)
        col_index = random.randint(0, col - 1)
        if map[rows_index][col_index] == "R":
            map[rows_index][col_index] = "E"
            break
        else:
            pass
    for row in range(0, 10, 1):
        print(map[row])

    return map

'''
# the map the player will see
def make_player_map():
    player_map = []
    for rows in range(0, 10, 1):
        player_map.append([])
        for col in range(0, 10, 1):
            player_map[rows].append("u")
    for row in range(0, 10, 1):
        print(player_map[row])

'''
map = make_map()

print("")
#make_player_map()

def update_player_position(direction):
    global player_cols_position, player_previous_cols_position, player_rows_position, player_previous_rows_position
    player_previous_rows_position = player_rows_position
    player_previous_cols_position = player_cols_position
    if direction == "north":
        player_rows_position -= 1
    elif direction == "south":
        player_rows_position += 1
    elif direction == "west":
        player_cols_position -= 1
    else:
        player_cols_position += 1
    print("previous: " + str(player_previous_rows_position) +
          ", " + str(player_previous_cols_position))
    print("previous: " + str(player_rows_position) + ", " + str(player_cols_position))

def player_navigation(map):
    player_position = map[player_rows_position][player_cols_position]
    if map[player_rows_position][player_cols_position + 1] == "w":  # east of the player
        pass
    else:
        print("player can go east")
    if map[player_rows_position][player_cols_position - 1] == "w":  # west of the player
        pass
    else:
        print("player can go west")
    if map[player_rows_position + 1][player_cols_position] == "w":  # south of the player
        pass
    else:
        print("player can go south")
    if map[player_rows_position - 1][player_cols_position] == "w":  # north of the player
        pass
    else:
        print("player can go north")
    print(" ")
    valid_choice = False
    
    while valid_choice == False:
        direction_choice = input("Enter the direction You'd like to go (n, s, e, w): ")
        if direction_choice == "n":
            update_player_position("north")
            valid_choice = True
        elif direction_choice == "s":
            update_player_position("south")
            valid_choice = True
        elif direction_choice == "e":
            update_player_position("east")
            valid_choice = True
        elif direction_choice == "w":
            update_player_position("west")
            valid_choice = True
        else:
            print("Invalid Choice")







#player_navigation(map)
'''