from project_pkg.player_builder import Player, generate_player_motivation, generate_player_health
from project_pkg.weapon_generator import Weapon, make_weapon_type, make_weapon
from project_pkg.map_generator import Map, make_map, make_player_map
from project_pkg.encounter_generator import encounter_calculator, encounter_builder, merchant_encounter_calculator, merchant
from project_pkg.battle_loop import battle_loop
from project_pkg.monster_generator import monster_generator
from project_pkg.player_navigation import player_navigation, update_player_map, check_ending
from project_pkg.room_generator import room_generator
from project_pkg.welcome import welcome

generated_player_health = generate_player_health()
generated_player_motivation = generate_player_motivation()
player = Player(generated_player_health, generated_player_motivation)
weapon_type = make_weapon_type()
player_weapon = Weapon(weapon_type, make_weapon(weapon_type))
map = Map(make_map())
player_map = Map(make_player_map())
in_combat = False

welcome()
player.introduce_player(player_weapon.weapon)
while player.check_alive() == True:
    room_generator()
    check_ending(map.get_end_rows(), map.get_end_cols())
    in_combat = encounter_calculator()
    if in_combat == True:
        generated_monster_weapon_type = make_weapon_type()
        weapon = Weapon(generated_monster_weapon_type,
                        make_weapon(generated_monster_weapon_type))
        monster = str(monster_generator())
        encounter_builder(monster, weapon.weapon)
        player.health = battle_loop(player.health, 100, player_weapon.get_action_word(
            player_weapon.weapon_type), weapon.get_action_word(weapon.weapon_type), monster, player_weapon.weapon, weapon.weapon)
    else:
        merchant_spawn = merchant_encounter_calculator()
        if merchant_spawn == True:
            merchant_weapon_type = make_weapon_type()
            merchant_weapon = Weapon(
                merchant_weapon_type, make_weapon(merchant_weapon_type))
            if merchant(player_weapon.weapon, merchant_weapon.weapon) == True:
                player_weapon = merchant_weapon
    update_player_map(map.array, player_map.array)
    player_map.print_map()
    player_navigation(map.array)
    player.print_health()
