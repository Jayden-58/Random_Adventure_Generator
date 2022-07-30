player_rows_position = 1
player_cols_position = 1
player_previous_rows_position = 1
player_previous_cols_position = 1
player_back_direction = "none"
ending_room = "unset"

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
    '''
    print("previous: " + str(player_previous_rows_position) +
          ", " + str(player_previous_cols_position))
    print("previous: " + str(player_rows_position) + ", " + str(player_cols_position))
    '''

def player_navigation(map):
    can_north = False
    can_south = False
    can_east = False
    can_west = False
    global player_back_direction
    #player_position = map[player_rows_position][player_cols_position]
    if map[player_rows_position][player_cols_position + 1] == "w":  # east of the player
        pass
    else:
        if player_back_direction == "east":
            print("player can go east (back)")
        else:
            print("player can go east")
        can_east = True
    if map[player_rows_position][player_cols_position - 1] == "w":  # west of the player
        pass
    else:
        if player_back_direction == "west":
            print("player can go west (back)")
        else:
            print("player can go west")
        can_west = True
    if map[player_rows_position + 1][player_cols_position] == "w":  # south of the player
        pass
    else:
        if player_back_direction == "south":
            print("player can go south (back)")
        else:
            print("player can go south")
        can_south = True
    if map[player_rows_position - 1][player_cols_position] == "w":  # north of the player
        pass
    else:
        if player_back_direction == "north":
            print("player can go north (back)")
        else:
            print("player can go north")
        can_north = True
    print(" ")
    valid_choice = False
    
    while valid_choice == False:
        direction_choice = input("Enter the direction You'd like to go (n, s, e, w): ")
        if direction_choice == "n" and can_north == True:
            player_back_direction = "south"
            update_player_position("north")
            valid_choice = True
        elif direction_choice == "s" and can_south == True:
            player_back_direction = "north"
            update_player_position("south")
            valid_choice = True
        elif direction_choice == "e" and can_east == True:
            player_back_direction = "west"
            update_player_position("east")
            valid_choice = True
        elif direction_choice == "w" and can_west == True:
            player_back_direction = "east"
            update_player_position("west")
            valid_choice = True
        else:
            print("Invalid Choice")
    
def update_player_map(map, player_map):
    player_map[player_rows_position][player_cols_position] =  "P"  #map[player_rows_position][player_cols_position]
    player_map[player_rows_position - 1][player_cols_position] = map[player_rows_position - 1][player_cols_position]
    player_map[player_rows_position + 1][player_cols_position] = map[player_rows_position + 1][player_cols_position]
    player_map[player_rows_position][player_cols_position - 1] = map[player_rows_position][player_cols_position - 1]
    player_map[player_rows_position][player_cols_position + 1] = map[player_rows_position][player_cols_position + 1]

def check_ending(end_rows, end_cols):
    if player_rows_position == end_rows and player_cols_position == end_cols:
        print("You have successfully reached the end of the dungeon. Along the way you found what you were seeking, but you were lucky to escape with your life")
        print("game over.")
        exit()