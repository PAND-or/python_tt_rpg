from dictionaries import *

"""

FUNCTIONS

"""




def say(text, speaker=None):
    if not speaker is None:
        print(f'{speaker}: {text} \n')
    else:
        print(f'{text} \n')


def pause():
    input('Enter to continue>>')


def stats(person):
    strh = f''
    strb = f''
    max_list = []
    skip_list = ['hello_text', 'choice_text']
    for k in person.keys():
        max_key = 'max_' + k
        if max_key in person:
            strh += f'{k:>10} / {max_key:<10}'
            strb += f'{person[k]:>10} / {person[max_key]:<10}'
            max_list.append(max_key)
        elif k not in max_list and k not in skip_list:
            strh += f'{k:^10}'
            strb += f'{person[k]:^10}'
    say(strh + '\n' + strb + '\n')


def help():
    say(command_help_text)


def history():
    say(LORE)


def is_alive(person):
    return person['hp'] > 0


def set_attr(person, **kwargs):
    for k in kwargs:
        person[k] = kwargs[k]


def add_attr(person, **kwargs):
    for k in kwargs:
        person[k] += kwargs[k]


def deny_attr(person, **kwargs):
    for k in kwargs:
        person[k] -= kwargs[k]


def is_end(hero):
    return hero['artifact'] or not is_alive(hero)


def do_restore_stamina(person):
    set_attr(person, stamina=person["max_stamina"])


def is_bored(person):
    if person["stamina"] <= person['damage'] * 2:
        say(f'{person["name"]} очень устал, требуется передышка')
        add_attr(person, stamina=(person['damage'] * 6))
        return True
    else:
        return False




def do_hit(attacker, defender, move, dmg=None, armor=None):
    if dmg is None:
        dmg = attacker['damage']
    if armor is None:
        armor = defender['armor']

    hit = (dmg - armor) if (dmg - armor) > 0 else 0

    deny_attr(defender, hp=hit)
    deny_attr(attacker, stamina=(dmg * 2))

    say(f'{attacker["name"]} делает {move}\nНаносит {hit} урона по {defender["name"]} ({defender["hp"] }/{defender["max_hp"]})')

    return defender['hp'] > 0


def fight(hero, enemy):
    do_restore_stamina(hero)
    do_restore_stamina(enemy)
    while is_alive(hero) and is_alive(enemy):  # 2.6.2 и # 2.6.6
        if not is_bored(hero):
            hero_move = input(f'\nВыбери удар {moves_str}\n>> ')
            hero_move = hero_move if hero_move in dict_move else 'default'
        else:
            hero_move = 'skip'

        enemy_move = 'attack' # TO DO: сделать рандомизатор ударов мобов

        hero_dmg = round(hero['damage'] * dict_move[hero_move]['damage_modificator'])
        hero_armor = round(hero['armor'] * dict_move[hero_move]['armor_modificator'])
        enemy_dmg = round(enemy['damage'] * dict_move[enemy_move]['damage_modificator'])
        enemy_armor = round(enemy['armor'] * dict_move[enemy_move]['armor_modificator'])


        if not do_hit(enemy, hero, dict_move[enemy_move]['name'], enemy_dmg, hero_armor):
            say('\nКак жаль ... тебя убили\n')
            break

        if not do_hit(hero, enemy, dict_move[hero_move]['name'], hero_dmg, enemy_armor):
            get_chest(hero, chest)
            say(f'\nРасправишись с очередным противником {hero["name"]} пошел дальше искать загадочный артефакт\n')
            break


def fight_all(hero, all_enemies):
    hero['win_strike'] = 0
    for enemy in all_enemies:

        say(intro_enemy_fight + enemy["name"])
        stats(enemy)

        fight(hero, enemy)

        if is_alive(hero):
            hero['win_strike'] += 1
        else:
            hero['end_state'] = 'lose'
            break


def start(hero, all_enemies):

    fight_all(hero, all_enemies)
    if is_alive(hero):
        hero['artifact'] = True
        hero['end_state'] = 'win'


def train(hero, instructor):
    instructor_change = input('Желаете ли поменять дефолтные значения Тренеровочного боя? Y or N:\n>> ').lower()
    if instructor_change == 'y':
        # 1.6.1

        instructor['max_hp'] = int(input('Введите кол-во жизней инструктора:\n>> '))
        instructor['hp'] = instructor['max_hp']
        hero['train_damage'] = int(input('Введите силу удара:\n>> '))

        if hero['train_damage'] > instructor['max_hp']:
            hero['train_damage'] = instructor['max_hp'] * 0.25
            say(f'Не корректное значение урона. Новое значение: {hero["train_damage"]}')

        hero["train_stamina"] = int(input('Введите выносливость:\n>> '))
        if hero["train_stamina"] < instructor['max_hp']:
            hero["train_stamina"] = instructor['max_hp'] * 0.75
            say(f'Не корректное значение урона. Новое значение: {hero["train_stamina"]}')
    else:
        instructor["hp"] = instructor["max_hp"]  # Обнуление жизней
        hero["train_stamina"] = hero["max_stamina"]
        hero["train_damage"] = hero["damage"]

    hero["train_max_stamina"] = hero["train_stamina"]

    say(intro_train_fight)

    while True:  # разные удары
        inp_hit = input(f'Выбери удар: 1 {attack_1_name}, 2 {attack_2_name}: ')
        if inp_hit == '1':
            say(f'{hero["name"]} делает {attack_1_name}\n')
            hit_damage = hero['train_damage'] * 2
            hit_stamina = hero['train_damage'] * 3
        elif inp_hit == '2':
            say(f'{hero["name"]} делает {attack_2_name}\n')
            hit_damage = hero['train_damage']
            hit_stamina = hero['train_damage']
        else:
            print('Ну кто так бьет?')
            hit_damage = 0
            hit_stamina = hero['train_damage']

        instructor["hp"] -= hit_damage
        hero["train_stamina"] -= hit_stamina

        say(f'{hero["name"]} нанес {hit_damage} урона\n')

        if hero["train_stamina"] <= 0:  # Если устал
            say(train_tired_text)
            break

        if instructor['hp'] <= 0:  # Если жизней осталось 0 то победа
            say(train_win_text)
            break

        # 1.6
        print(f'{"Name":<20}{"HP":>10}/{"MAX HP":<10}{"Stamina":>10}/{"Max stamina":<10}\n'
              f'{instructor["name"]:<20}{instructor["hp"]:>10}/{instructor["max_hp"]:<10}'
              f'{instructor["max_stamina"]:>10}/{instructor["max_stamina"]:<10}\n'
              f'{hero["name"]:<20}{hero["hp"]:>10}/{hero["max_hp"]:<10}'
              f'{hero["train_stamina"]:>10}/{hero["train_max_stamina"]:<10}\n')


def get_chest(hero, chest):
    chest_str = '\n'
    for i, v in enumerate(chest):
        chest_str += f'{i}. {v["name"]},\n'

    say(f'Ты обыскиваешь врага и обнаруживаешь {chest_str}')
    chest_inp = input('Что ты возьмешь (or skip)?\n>> ')
    if chest_inp.isdigit():
        if int(chest_inp) >= 0 and int(chest_inp) < len(chest):
            item = chest[int(chest_inp)]
            say(f'Ты взял {item["name"]}\n\n')

            if item['rule'] == 'add':
                hero[item['modificator']] += item['value']
                #add_attr(hero, item["modificator"]=item['value']) не работает так
            elif item['rule'] == 'heal':
                set_attr(hero, max_hp=item['value'])
                #hero["hp"] = hero["max_hp"] * item['value']
            chest.remove(item)
        else:
            say('Долго перебирая варианты ты случайно закрыл сундук')
    else:
        say('Долго перебирая варианты ты случайно закрыл сундук')


def execute(fdict, key):
    arrgs = fdict[key]['args']
    func = fdict[key]['func']
    func(*arrgs)
