import random
# random monster generator WORKING


def monster_generator():
    monsters = ("warewolf", "skeleton", "gobllin", "centaur", "gargoyle", "ogre", "orc", "pixie", "fairy", "scarecrow", "troll", "wizard", "ghoul", "assassin", "guard", "mage", "gladiator", "giant", "knight", "warrior",
                "vampire", "zombie", "ghost", "elf", "bandit", "theif")
    descriptions = ("tall",  "short", "huge", "tiny", "mystrious",
                    "wild", "brave", "angry", "hungry", "blood thirsty", "confident", "ugly", "strong", "gigantic", "microscopic", "growling", "screaming", "crazy")
    monster_index_number = random.randint(0, len(monsters) - 1)
    description_index_number = random.randint(0, len(descriptions) - 1)
    new_monster = (str(descriptions[description_index_number]
                       ) + " " + str(monsters[monster_index_number]))
    return(new_monster)
