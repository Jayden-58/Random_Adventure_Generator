import random


class Player:
    def __init__(self, health, motivation):
        self.health = health
        self.motivation = motivation

    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def introduce_player(self,  weapon):
        print("You entered the dungeon seeking " + str(self.motivation) + ".")
        print("your health is: " + str(self.health) + ".")
        print("you brought your trusty " + weapon + ".")

    def print_health(self):
        print("your health is: " + str(self.health))


def generate_player_motivation():
    player_motivations = ("glory", "gold", "revenge", "power", "wisdom", "...nothing. You are here by mistake", "tresure", "enlightenment", "to revover a family heirloom", "to be the best explorer in the world",
                          "to destroy anything in your path", "to learn about acient beings who used to live here", "a powerful potion to heal your sick daughter", "a fun experience", "....to veiw some guy's python project....    ;)", "true power", "a story to tell your friends", "a bounty placed on a monster who is said to live here...")
    player_motivation_index = random.randint(0, len(player_motivations) - 1)
    new_player_motivation = player_motivations[player_motivation_index]
    return new_player_motivation


def generate_player_health():
    new_player_health = random.randint(100, 200)
    return new_player_health
