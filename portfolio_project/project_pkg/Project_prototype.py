'''
READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

READ ME!!! This code is not used in the final version of this project. I included it to show how the project looked becore I started using OOP 

'''


'''
import random


# random monster generator WORKING
def monster_generator():
    monsters = ("warewolf", "skeleton", "gobllin", "centaur", "gargoyle", "ogre", "orc", "pixie", "fairy", "scarecrow", "troll", "wizard", "ghoul", "assassin", "guard", "mage", "gladiator", "giant", "knight", "warrior"
                "vampire", "zombie", "ghost", "elf", "bandit", "theif")
    descriptions = ("tall",  "short", "huge", "tiny", "mystrious",
                    "wild", "brave", "angry", "hungry", "blood thirsty", "confident", "ugly", "strong", "gigantic", "microscopic", "growling", "screaming", "crazy")
    monster_index_number = random.randint(0, len(monsters) - 1)
    description_index_number = random.randint(0, len(descriptions) - 1)
    new_monster = (str(descriptions[description_index_number]
                       ) + " " + str(monsters[monster_index_number]))
    return(new_monster)


# monster enterance generator
def monster_enterance_generator():
    entrances = (" appeared!", " is standing in the middle of the room, ready to battle!", " came out of nowhere!",
                 " turns around slowly.....", " came from behind you!", " jumps down from above!", " walks into the room...", " appears out of thin air!", " on the floor, wakes up from a peaceful nap!", " catches you by surprize!")
    entrance_index_number = random.randint(0, len(entrances) - 1)
    new_entrance = entrances[entrance_index_number]
    return(new_entrance)


# determine if a battle will happen WORKING
def encounter_calculator():
    will_fight = False
    number = random.randint(1, 100)
    if number <= 15:
        will_fight = True
        print("Fight!")
        encounter_builder()
    else:
        will_fight = False
        print("no fight...")


# determine walls and details of the room
def room_generator():
    #floors and walls
    walls = ("brick", "stone", "marble", "ice")
    wall_index_number = random.randint(0, len(walls) - 1)
    new_wall = walls[wall_index_number]
    if new_wall == "brick":
        floors = ("tile", "stone", "wood")
    elif new_wall == "stone":
        floors = ("stone", "sand", "rocks", "shallow water")
    elif new_wall == "marble":
        floors = ("marble", "cracked marble")
    else:
        floors = ("ice", "cold shallow water", "stone")
    floor_index_number = random.randint(0, len(floors) - 1)
    new_floor = floors[floor_index_number]
    # decoration
    decorations = ("there is a table in the middle of the room", "the floor is covered with bones", "there is a dead hero on the floor", "blood covers the walls", "there are strange glowing orbs floating around", "small spiders are crawling all over the floor", "you hear strange voices in the distance", "the floor is covered with torn up paper", "the room is cold", "the room is hot", "there is a small fire in the center of the room",
                   "there is writing in acient text on the walls", "the room is filled with gold and treasure", "this room appears to have once been a prison", "beautiful paintings hang on the wall", "the wall appears to have scratches from a creature with gigantic claws", "there is a table in the center of the room, but it is pushed on its side", "the room smells awful", "a thin layer of mist rises off of the floor", "the floor has acient symbols, seemingly hand-carved centuries ago", "the room is filled with books and scrolls, it appears it was once a library", "the room has a deep hole in the center", "the room is completely dark, except for a the faint glow of a candle...someone has been here recently")
    decoration_index_number = random.randint(0, len(decorations) - 1)
    new_decoration = decorations[decoration_index_number]
    # putting together the pieces
    print(" the walls are " + new_wall + " the floor is " +
          new_floor + ". " + new_decoration)


# it would be cool to do a weapon generator that both the enemies and player can use


def weapon_generator():
    weapon_types = ("projectile", "swingable")
    weapon_type_index = random.randint(0, len(weapon_types)-1)
    weapon_type = weapon_types[weapon_type_index]
    if weapon_type == "projectile":
        weapons = ("bow", "flintlock pistol", "crossbow",
                   "double barreled shotgun", "revolver", "slingshot", "rocket launcher")
        action_word = "shoot"
    elif weapon_type == "swingable":
        weapons = ("sword", "great sword", "axe",
                   "battle axe", "war hammer", "dagger", "baseball bat", "golf club", "nunchucks", "chainsaw",)
        action_word = "swing"
    weapon_index_number = random.randint(0, len(weapons) - 1)
    new_weapon = weapons[weapon_index_number]
    # print(action_word + " " + new_weapon)
    return new_weapon

    # full encounter builder


def encounter_builder():
    player_entrances = ("as you look around the room, a ", "you charge into the room, but a ", "you slowly creep into the room, a ", "you scan the room searching for threats, and a ",
                        "you stumble clumsily into the room, a ", "you crawl into the room on your hands and knees, trying your best to be quiet, but a ", "you kick the door down, and a ", "you ascend the stairs to the next room, suddenly a ", "you walk into the room...'You picked the wrong dungeon, fool!', suddenly a ", "as you walk into the room, you trip and fall. As you try to get up, a ", "you enter the next room. You stop to tie your shoe, but before you can finnish a ")
    player_entrances_index = random.randint(0, len(player_entrances) - 1)
    new_player_entrance = player_entrances[player_entrances_index]
    new_monster = monster_generator()
    new_entrance = monster_enterance_generator()
    new_weapon = weapon_generator()
    print(new_player_entrance + new_monster +
          " holding a " + new_weapon + new_entrance)


# function to make the monster's move
def monster_move():
    new_damage = 0
    damage_calculator = random.randint(0, 100)
    if damage_calculator < 10:
        new_damage = 0
        print("The attack missed: 0 damage.")
    elif damage_calculator >= 95:
        new_damage = 15
        print("The attack was a critical hit: " + str(new_damage) + " damage!")
    else:
        # generates a random number between 1 and 5
        new_damage = random.randint(0, 5)
        print("The attack hit: " + str(new_damage) + " damage.")


def player_move():
    choice = " "
    while choice == " ":
        new_damage = 0
        # maybe ill add charisma.
        choice = input(
            "Select an option: fight, run (previous room), or talk: ")
        if choice == "fight":
            damage_calculator = random.randint(0, 100)
            if damage_calculator < 10:
                new_damage = 0
                print("The attack missed: 0 damage.")
            elif damage_calculator >= 95:
                new_damage = 15
                print("The attack was a critical hit: " +
                      str(new_damage) + " damage!")
            else:
                # generates a random number between 1 and 5
                new_damage = random.randint(1, 5)
                print("The attack hit: " + str(new_damage) + " damage.")
        elif choice == "run":
            # have player travel back to the previous room
            pass  # remove later
        elif choice == "talk":
            # add charisma system
            pass  # remove later
        else:  # makes loop restart if an invalid choice is chosen
            choice = " "


def battle_loop():
    turn = "p"
    enemy_alive = False
    while enemy_alive == True:
        if turn == "p":  # players turn
            player_move()
            turn = "e"

        else:
            monster_move()
            turn = "p"


def player_builder():
    # generate motivation
    player_motivations = ("glory", "gold", "revenge", "power", "wisdom", "tresure", "enlightenment", "to revover a family heirloom", "to be the best explorer in the world",
                          "to destroy anything in your path", "to learn about acient beings who used to live here", "a powerful potion to heal your sick daughter", "a fun experience")
    player_motivation_index = random.randint(0, len(player_motivations) - 1)
    new_player_motivation = player_motivations[player_motivation_index]
    print("You entered the dungeon seeking " + new_player_motivation + ".")
    # generate health
    new_player_health = random.randint(100, 200)
    print("your health is: " + str(new_player_health))
    player_weapon = weapon_generator()
    print("you brought your trusty " + player_weapon + ".")


# player_builder()
# room_generator()
# encounter_calculator()
# weapon_generator()
# player_move()
'''