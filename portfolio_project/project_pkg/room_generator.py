import random
# determine walls and details of the room


def room_generator():
    #floors and walls
    walls = ("brick", "stone", "marble", "ice",
             "stone bricks", "volcanic rock", "crystal")
    wall_index_number = random.randint(0, len(walls) - 1)
    new_wall = walls[wall_index_number]
    if new_wall == "brick" or new_wall == "stone bricks":
        floors = ("tile", "stone", "wood", "stone bricks",
                  "cracked stone bricks", "colorful tile", "cracked tile" "bricks")
    elif new_wall == "stone":
        floors = ("stone", "sand", "rocks", "shallow water",
                  "stone, with stalagmites scattered around")
    elif new_wall == "marble":
        floors = ("marble", "cracked marble")
    elif new_wall == "volcanic rock":
        floors = ("volcanic rock", "burnt stone bricks")

    else:
        floors = ("ice", "cold shallow water", "stone", "crystal")
    floor_index_number = random.randint(0, len(floors) - 1)
    new_floor = floors[floor_index_number]
    # decoration
    decorations = ("there is a table in the middle of the room", "the floor is covered with bones", "there is a dead hero on the floor", "blood covers the walls", "there are strange glowing orbs floating around", "small spiders are crawling all over the floor", "you hear strange sounds in the distance", "the floor is covered with torn up paper", "the room is cold", "the room is hot", "there is a small fire in the center of the room",
                   "there is writing in acient text on the walls", "the room is filled with gold and treasure", "this room appears to have once been a prison", "beautiful paintings hang on the wall", "the wall appears to have scratches from a creature with gigantic claws", "there is a table in the center of the room, but it is pushed on its side", "the room smells awful", "a thin layer of mist rises off of the floor", "the floor has acient symbols, seemingly hand-carved centuries ago", "the room is filled with books and scrolls, it appears it was once a library", "the room has a deep hole in the center", "the room is completely dark, except for a the faint glow of a candle...someone has been here recently", "the room has a table with a map and markers of verious territories on it from a war hundreds of years ago", "the room is filled with advanced alian technology. you've never seen anything like it.", "The room is full of rotten loaves of bread. You're slightly confused.", "there are some lizards crawling around on the wall", "this air in room is filled with bubbles", "light comes down from a crack in the cieling")
    decoration_index_number = random.randint(0, len(decorations) - 1)
    new_decoration = decorations[decoration_index_number]
    # putting together the pieces
    print("the walls are " + new_wall + " the floor is " +
          new_floor + ". " + new_decoration)
    print(" ")
