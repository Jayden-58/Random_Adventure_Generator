import random
# determine if a battle will happen WORKING


def encounter_calculator():
    will_fight = False
    number = random.randint(1, 100)
    if number <= 15:
        will_fight = True
    else:
        will_fight = False
    return will_fight


def merchant_encounter_calculator():
    will_appear = False
    number = random.randint(0, 100)
    if number <= 5:
        will_appear = True
    else:
        will_appear = False
    return will_appear

def health_encounter_calculator():
    will_appear = False
    number = random.randint(0, 100)
    if number == 1:
        will_appear = True
    else:
        will_appear = False
    return will_appear

def encounter_builder(monster, weapon):
    player_entrances = ("as you look around the room, a ", "you charge into the room, but a ", "you slowly creep into the room, a ", "you scan the room searching for threats, and a ",
                        "you stumble clumsily into the room, a ", "you crawl into the room on your hands and knees, trying your best to be quiet, but a ", "you kick the door down, and a ", "you ascend the stairs to the next room, suddenly a ", "you walk into the room...'You picked the wrong dungeon, fool!', suddenly a ", "as you walk into the room, you trip and fall. As you try to get up, a ", "you enter the next room. You stop to tie your shoe, but before you can finnish a ")
    player_entrances_index = random.randint(0, len(player_entrances) - 1)
    new_player_entrance = player_entrances[player_entrances_index]

    monster_entrances = (" appeared!", " is standing in the middle of the room, ready to battle!", " came out of nowhere!",
                         " turns around slowly.....", " came from behind you!", " jumps down from above!", " walks into the room...", " appears out of thin air!", " on the floor, wakes up from a peaceful nap!", " catches you by surprize!")
    entrance_index_number = random.randint(0, len(monster_entrances) - 1)
    new_entrance = monster_entrances[entrance_index_number]

    print(new_player_entrance + str(monster) +
          " holding a " + weapon + new_entrance)


def merchant(player_weapon, merchant_weapon):
    print("An old lady is sitting on the floor.")
    print("Hello, I am the dungeon merchant. Lets make a deal....")
    print("I'll trade you this " + merchant_weapon +
          " for your " + player_weapon + ".")
    print("Sounds like a good deal right?")
    print(" ")
    player_answer = input("enter your answer: (yes or no)")
    if player_answer.lower() == "yes" or player_answer.lower() == "y":
        print("hehehe")
        print(" ")
        print("You traded your " + player_weapon +
              " for a " + merchant_weapon + ".")
        return True
    else:
        print("maybe next time then hehehehe")
        print(" ")
        return False
