#!/usr/bin/python3
__author__ = "Андрей Петров"
from dictionaries import *
from fynctions import *

"""

GAME

"""

# 1.5.3
say(LORE)
pause()
say(BEGIN_1)

# 1.5.1
hero_name = input(f'{lieutenant_name}: Легат, назови свое имя: \n>> ')

# 2.1
if not hero_name.istitle():
    hero_name = hero_name.capitalize()

BEGIN_2 = f'Добро пожаловать {hero_name} на свое первое задание\n'


say(BEGIN_2, lieutenant_name)
pause()
say(intro_char_choice)

while True:
    inp_char_class = input(f'Система: Выберете ответ {roles_str}:\n>> ')  # 1.5.2
    if inp_char_class in roles:
        hero = roles[inp_char_class]
        say(f'Я .... {hero["hello_text"]}', hero_name)
        break
    else:
        say('Такая личность в системе не обнаружена', lieutenant_name)

hero['name'] = hero_name
hero['artifact'] = False

say(command_help_text)

commands = {
    'exit': {
        'func': exit,
        'args': ()
    },
    'history': {
        'func': history,
        'args': ()
    },
    'help': {
        'func': help,
        'args': ()
    },
    'stats': {
        'func': stats,
        'args': (hero, )
    },
    'train': {
        'func': train,
        'args': (hero, instructor)
    },
    'start': {
        'func': start,
        'args': (hero, all_enemies)
    }
}



while True:
    #  2.3.2
    if is_end(hero):  # Выход из игры если победил
        break
    action = input('Введи команду: \n>> ').lower()  # 2.4.2
    if action in commands:
        execute(commands, action)
    else:
        say(command_error_text)


# Закос под многовариативность концовок
#  2.3.3
say(FINAL[hero['end_state']])

