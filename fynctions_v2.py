from dictionaries_v2 import *

"""

FUNCTIONS

"""


def menu():
    say('command_menu_text')


def history():
    say('LORE')


def train(hero, instructor):
    instructor_change = sinput('train_input_def').lower()
    if instructor_change == 'y':
        # 1.6.1

        instructor['max_hp'] = int(sinput('train_input_hp'))
        instructor['hp'] = instructor['max_hp']
        hero['train_damage'] = int(sinput('train_input_dmg'))

        if hero['train_damage'] > instructor['max_hp']:
            hero['train_damage'] = instructor['max_hp'] * 0.25
            say('train_input_corhp', hero["train_damage"])

    else:
        instructor["hp"] = instructor["max_hp"]  # Обнуление жизней
        hero["train_damage"] = hero["damage"]

    say('intro_train_fight')

    while True:  # удары
        hit_damage = do_hit(hero["damage"], instructor["armor"])
        instructor["hp"] -= hit_damage

        say('hit_result', hero["name"], hit_damage, instructor["name"])
        say('hp_show', instructor["name"], show_hp(instructor))

        pause()

        if instructor['hp'] <= 0:  # Если жизней осталось 0 то победа
            say('train_win_text')
            break


def stats(person):
    skip_list = ['hello_text', 'win_all', 'choice_text', 'name']
    for k, v in person.items():
        if k not in skip_list:
            print(f'{k}: {v}')


def show_hp(person):
    return f'{person["hp"]} / {person["max_hp"]}'


def is_alive(person):
    return person["hp"] > 0


def pause():
    sinput('pause_text')


def do_hit(dmg, armor):
    if dmg > armor:
        return dmg - armor
    else:
        return 0


def fight(hero, enemy):
    while is_alive(hero) and is_alive(enemy):
        enemy_hit = do_hit(enemy["damage"], hero["armor"])
        hero_hit = do_hit(hero["damage"], enemy["armor"])
        hero["hp"] -= enemy_hit
        enemy["hp"] -= hero_hit

        say('hit_result', hero["name"], hero_hit, enemy["name"])
        say('hp_show', enemy["name"], show_hp(enemy))
        say('hit_result', enemy["name"], enemy_hit, hero["name"])
        say('hp_show', hero["name"], show_hp(hero))

        pause()

    return is_alive(hero)


def fight_all(hero, all_enemies):
    for enemy in all_enemies:
        say('intro_enemy_fight', enemy["name"])
        stats(enemy)
        pause()
        fight(hero, enemy)

        if not is_alive(hero):
            break
    return is_alive(hero)


def start(hero, all_enemies):
    fight_all(hero, all_enemies)

    if is_alive(hero):
        hero["win_all"] = True
        hero['end_state'] = 'win'
    else:
        hero['end_state'] = 'lose'


def say(key, *args):
    if key in TEXTS:
        if args:
            print(TEXTS[key] % args)
        else:
            print(TEXTS[key])
    else:
        print(key)


def sinput(key, *args):
    say(key, *args)
    return input('>> ')


def execute(fdict, key):
    arrgs = fdict[key]['args']
    func = fdict[key]['func']
    func(*arrgs)
