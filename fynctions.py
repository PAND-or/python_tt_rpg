from dictionaries import *
import random

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


def map_generate(cells, enemies):
    values = [i for i in range(0, len(enemies))]  # генерация доступных значений
    values.extend(['_', '$'])

    my_map = [random.choice(values) for _i in range(0, cells)]  # рандомная генерация врагов
    my_map[0] = '@'  # первая ячейка - наш герой
    return my_map


def show_map(my_map):
    print('___'*25)
    print(my_map)
    print('___' * 25)

def move(my_map, hero, all_enemies):
    start_cell = len(my_map)
    for i, cell in enumerate(my_map):
        if not is_alive(hero):  # больше не ходим по комнатам если умер
            break
        if cell == '@':  # на случай, если запускать будем не сначала
            start_cell = i
            continue
        if i < start_cell:  #ничего не делаем с ячейкой, пропускаем
            continue

        if cell == '_':
            say('move_empty_room')
        elif cell == '$':
            say('move_chest_room')
            chose_from_chest(hero)
        elif isinstance(cell, int):
            #say('move_enemy_room')
            fight(hero, all_enemies[cell])

        my_map[i] = '@'  # тут был "Вася"
        my_map[i - 1] = '_' # комната зачищена
        show_map(my_map)
    return is_alive(hero)


def use_item(item, person):
    k = item['value']
    if item['rule'] == 'add':
        person[k] += random.randint(item['min'], item['max'])
    elif item['rule'] == 'restore':
        k_max = 'max_' + k
        if k_max in person:
            new_value = int(person[k] + ((person[k_max] * random.randint(item['min'], item['max'])/ 100)))
            if new_value > person[k_max]:  #Что-бы не хилило больше 100%
                person[k] = person[k_max]
            else:
                person[k] = new_value


def chose_from_chest(person):
    items_count = random.randint(1, 3)
    items_list = random.sample(chest_list, items_count)

    choice_items_str = f''
    for i, v in enumerate(items_list):
        choice_items_str += f'{i}: {v["text"]} \n'

    say('choice_items_list', choice_items_str)
    inp = sinput('choice_items_input')

    if len(inp) > 0 and inp.isdigit():
        if 0 <= int(inp) < len(items_list):
            use_item(items_list[inp], person)
        else:
            say('choice_items_error')
    else:
        say('choice_items_error')


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


def roll_dice():
    return random.randint(1, 6)


def roll_master_dice():
    return random.randint(1, 20)


def do_hit(dmg, armor):
    dmg += roll_dice()
    if dmg > armor:
        return dmg - armor
    else:
        return 0


def critical_hit(dmg, armor):
    dice = roll_master_dice()
    if 2 < dice < 19:
        return do_hit(dmg, armor)
    elif dice >=19:
        hit = 0
        for _ in range(3):
            hit += do_hit(dmg, armor)
        return hit
    else:
        return 0


def fight(hero, enemy):
    say('intro_enemy_fight', enemy["name"])
    stats(enemy)
    pause()
    while is_alive(hero) and is_alive(enemy):
        enemy_hit = critical_hit(enemy["damage"], hero["armor"])
        hero_hit = critical_hit(hero["damage"], enemy["armor"])

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
    my_map = map_generate(20, all_enemies)
    show_map(my_map)
    move(my_map, hero, all_enemies)
    #fight_all(hero, all_enemies)

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

