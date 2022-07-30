import random
# function to make the monster's move


def monster_move(action_word, monster, weapon):
    new_damage = 0
    damage_calculator = random.randint(0, 100)
    if damage_calculator < 10:
        new_damage = 0
        print("The " + monster + " " + action_word + "s their " + weapon + ".")
        print("The attack missed: 0 damage.")
    elif damage_calculator >= 95:
        new_damage = 15
        print("The " + monster + " " + action_word + "s their " + weapon + ".")
        print("The attack was a critical hit: " + str(new_damage) + " damage!")
    else:
        # generates a random number between 1 and 5
        new_damage = random.randint(1, 10)
        print("The " + monster + " " + action_word + "s their " + weapon + ".")
        print("The attack hit: " + str(new_damage) + " damage.")
    return(new_damage)


def player_move(action_word, weapon):
    choice = " "
    while choice == " ":
        new_damage = 0
        choice = input("Select an option: fight (f), talk (t)")
        if choice == "fight" or choice.lower() == "f":
            damage_calculator = random.randint(0, 100)
            if damage_calculator < 10:
                new_damage = 0
                print("you " + action_word + " your " + weapon + ".")
                print("The attack missed: 0 damage.")
            elif damage_calculator >= 95:
                new_damage = 45
                print("you " + action_word + " your " + weapon + ".")
                print("The attack was a critical hit: " +
                      str(new_damage) + " damage!")
            else:
                # generates a random number between 1 and 5
                new_damage = random.randint(1, 30)
                print("you " + action_word + " your " + weapon + ".")
                print("The attack hit: " + str(new_damage) + " damage.")
        elif choice == "talk" or choice.lower() == "t":
            fight_over_check = charisma()
            print(" ")
            if fight_over_check == True:
                return -1
            else:
                pass
            pass  # remove later
        else:  # makes loop restart if an invalid choice is chosen
            choice = " "
    return(new_damage)


def battle_loop(player_health, monster_health, player_action_word, monster_action_word, monster, player_weapon, monster_weapon):
    turn = "p"
    enemy_alive = True
    player_alive = True
    while enemy_alive == True and player_alive == True:
        if turn == "p":  # players turn
            damage = player_move(player_action_word, player_weapon)
            if damage == -1: #charisma option makes the damage -1
                break
            else:
                monster_health -= damage
                if monster_health <= 0:
                    enemy_alive = False
                    print("you won the battle")
                else:
                    turn = "e"

        else:
            player_health -= monster_move(monster_action_word,
                                          monster, monster_weapon)
            if player_health <= 0:
                player_alive = False
                print("You died.")
                exit()
            else:
                turn = "p"
    return player_health


def charisma():
    possible_type_of_conversation = ("question", "agreement", "disagreement")
    type_of_conversation_index = random.randint(
        0, len(possible_type_of_conversation) - 1)
    conversation_type = possible_type_of_conversation[type_of_conversation_index]
    if conversation_type == "question":
        possible_question_intro = ("...fine, Maybe we can see if we find common ground. If we do, I'll let you walk out of here alive.", "If you want to get past me, you must pass a test...", "In order to pass, I'll need to ask you a question.", "what?...You're trying to talk your way out of this fight?...Hmmm Lets see...",
                                   "I'll ask you once...", "this issue has been on my mind for a long time. If we agree I'll let you go free.", "lets see if you're like me...", "...This is new, No one's ever tried to talk their way out of a fight with me before...")
        possible_queston_intro_index = random.randint(
            0, len(possible_question_intro) - 1)
        question_intro = possible_question_intro[possible_queston_intro_index]
        print(question_intro)
        possible_questions = ("do you like the king's new policies?",
                              "Do you like pizza with pineapple on it?", "is water wet?", "Do you like the beach more than the mountains?", "are you a friend of the king?", "do you like cats more than dogs?", "do you believe that monsters and humans can live peacefully together?", "do you play the flute?", "have you learned any magic?", "will you marry me?", "were you ever a royal soldier?", "do you like brussell sprouts?", "do you prefer the nighttime over the daytime?", "do you like to watch golf?", "were you ever a theif?", "do you fight with honor?", "would you steal gold from the royal bank?", "do you prefer to travel on foot rather than on horseback?", "is this the krusty krab?", "have you ever stopped to look at the stars while out on your travels?", "do you have pets?", "is your favorlte color pink?")
        possible_questions_index = random.randint(
            0, len(possible_questions) - 1)
        question = possible_questions[possible_questions_index]
        print(question)
        possible_answers = ("yes", "no")
        possible_answer_index = random.randint(0, len(possible_answers) - 1)
        answer = possible_answers[possible_answer_index]
        player_answer = input("Enter your answer. (yes or no): ")
        if player_answer.lower() == "y":
            player_answer = "yes"
        elif player_answer == "n":
            player_answer = "no"
        if str(player_answer) == answer:
            possible_good_results = ("I'm glad we are on the same page, go on ahead.",
                                     "you and I are more alike than I thought. I apopogize for almost killing you")
            possible_good_result_index = random.randint(
                0, len(possible_good_results) - 1)
            good_result = possible_good_results[possible_good_result_index]
            print(good_result)
            return True
        else:
            possible_bad_results = ("...Then I have no choice...", "In that case, prepare to die!", "You monster.", ".........", "I'll need to destroy you then",
                                    "you have disrespected me. Prepare to suffer the consequences.", "I thought maybe we could come to an agreement....I was incorrect")
            possible_bad_result_index = random.randint(
                0, len(possible_bad_results) - 1)
            bad_result = possible_bad_results[possible_bad_result_index]
            print(bad_result)
            return False
    elif conversation_type == "agreement":
        possible_agreements = ("I didn't really want to fight you anyways.", "I'm more scared of you than you are of me, please, let me go!",
                               "Wow...you actually tried to talk to me instead of trying to fight me. You have my respect, and I'll stay out of your way.", "...aww man, I thought this would be more fun! Ok, go on ahead.")
        possible_agreement_index = random.randint(
            0, len(possible_agreements) - 1)
        agreement = possible_agreements[possible_agreement_index]
        print(agreement)
        return True
    else:
        possible_disagreements = ("I never back down from a fight!", "Sorry pal, but this is a fight.", "I'll make you sorry you ever came to this dungeon!",
                                  "I cannot let you pass.", "don't talk me out of killing you!", "I remember what you did 3 years ago...now you must pay...")
        possible_disagreement_index = random.randint(
            0, len(possible_disagreements) - 1)
        disagreement = possible_disagreements[possible_disagreement_index]
        print(disagreement)
        return False
