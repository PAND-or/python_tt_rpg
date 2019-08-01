from dictionaries_v2 import *

"""

FUNCTIONS

"""


def menu():
    print(command_menu_text)


def history():
    print(LORE)


def train(hero, instructor):
    instructor_change = input('Желаете ли поменять дефолтные значения Тренеровочного боя? Y or N:\n>> ').lower()
    if instructor_change == 'y':
        # 1.6.1

        instructor['max_hp'] = int(input('Введите кол-во жизней инструктора:\n>> '))
        instructor['hp'] = instructor['max_hp']
        hero['train_damage'] = int(input('Введите силу удара:\n>> '))

        if hero['train_damage'] > instructor['max_hp']:
            hero['train_damage'] = instructor['max_hp'] * 0.25
            print(f'Не корректное значение урона. Новое значение: {hero["train_damage"]}')

    else:
        instructor["hp"] = instructor["max_hp"]  # Обнуление жизней
        hero["train_damage"] = hero["damage"]

    print(intro_train_fight)

    while True:  # удары
        hit_damage = do_hit(hero["damage"], instructor["armor"])
        instructor["hp"] -= hit_damage
        print(f'{hero["name"]} нанес {hit_damage} урона')
        print(f'{instructor["name"]}: {instructor["hp"]}/{instructor["max_hp"]}\n')
        input('press ENTER to continue\n')

        if instructor['hp'] <= 0:  # Если жизней осталось 0 то победа
            print(train_win_text)
            break


def stats(person):
    for k, v in person.items():
        print(f'{k}: {v}')


def show_hp(person):
    return f'{person["hp"]} / {person["max_hp"]}'


def is_alive(person):
    return person["hp"] > 0


def pause():
    input('\nPress ENTER to continue >>>\n')


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

        print(f'{hero["name"]} наносит {hero_hit} урона по {enemy["name"]}\n'
              f'{enemy["name"]}: {show_hp(enemy)}\n'
              f'{enemy["name"]} наносит {enemy_hit} урона по {hero["name"]}\n'
              f'{hero["name"]}: {show_hp(hero)}\n')

        pause()

    return is_alive(hero)


def fight_all(hero, all_enemies):
    for enemy in all_enemies:
        say(intro_enemy_fight + enemy["name"])
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


def say(text, speaker=None):
    if not speaker is None:
        print(f'{speaker}: {text} \n')
    else:
        print(f'{text} \n')


def execute(fdict, key):
    arrgs = fdict[key]['args']
    func = fdict[key]['func']
    func(*arrgs)
