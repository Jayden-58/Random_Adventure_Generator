import random
end_position_rows = "unset"
end_position_cols = "uset"

def make_map():
    map = []
    global end_position_rows
    global end_position_cols
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
            end_position_rows = rows_index
            end_position_cols = col_index
            break
        else:
            pass

        '''
    for row in range(0, 10, 1):
        print(map[row])
        '''

    return map


# the map the player will see
def make_player_map():
    player_map = []
    for rows in range(0, 10, 1):
        player_map.append([])
        for col in range(0, 10, 1):
            player_map[rows].append("u")
    return player_map
          


class Map:
    def __init__(self, array):
        self.array = array
    def print_map(self):
        for row in range(0, 10, 1):
            print(self.array[row])
        print("  u: unknown")
        print("  w: wall")
        print("  R: room")
        print("  S: start")
        print("  E: exit")
        print("  P: player")
    def get_end_rows(self):
        return end_position_rows
    def get_end_cols(self):
        return end_position_cols


