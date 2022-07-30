import random


class Weapon:
    def __init__(self, weapon_type, weapon):
        self.weapon_type = weapon_type
        self.weapon = weapon

    def get_action_word(self, weapon_type):
        if weapon_type == "projectile":
            return "shoot"
        elif weapon_type == "swingable":
            return "swing"


def make_weapon_type():
    weapon_types = ("projectile", "swingable")
    weapon_type_index = random.randint(0, len(weapon_types)-1)
    weapon_type = weapon_types[weapon_type_index]
    return weapon_type


def make_weapon(weapon_type):
    if weapon_type == "projectile":
        weapons = ("bow", "flintlock pistol", "crossbow",
                   "double barreled shotgun", "revolver", "slingshot", "rocket launcher", "musket", "alien plasma cannon", "rubber band gun", "nerf blaster", "miniature cannon", "t-shirt cannon", "squirt gun", "sniper rifle", "flare gun", "golden revolver")
    elif weapon_type == "swingable":
        weapons = ("sword", "great sword", "knife", "axe",
                   "battle axe", "war hammer", "dagger", "baseball bat", "golf club", "nunchucks", "chainsaw", "crowbar", "magic wand", "katana", "spear", "short sword", "magic staff", "golden sword")
    weapon_index_number = random.randint(0, len(weapons) - 1)
    new_weapon = weapons[weapon_index_number]
    return new_weapon
