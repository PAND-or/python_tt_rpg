#!/usr/bin/python3
__author__ = "Андрей Петров"
from dictionaries_v2 import *
from fynctions_v2 import *

"""

GAME

"""

# 1.5.3
say('LORE')
pause()
say('BEGIN_1')

# 1.5.1
hero_name = sinput('game_input_heroname')

# 2.1
if not hero_name.istitle():
    hero_name = hero_name.capitalize()

say('game_begin_2', hero_name)
pause()
say('intro_char_choice')

while True:
    inp_char_class = sinput('game_input_roles', roles_str)  # 1.5.2
    if inp_char_class in roles:
        hero = roles[inp_char_class]
        say('game_roles_chosen', hero["hello_text"])
        break
    else:
        say('game_roles_errchoise')

hero['name'] = hero_name
say('game_briffing')
say('command_menu_text')

commands = {
    'exit': {
        'func': exit,
        'args': ()
    },
    'history': {
        'func': history,
        'args': ()
    },
    'menu': {
        'func': menu,
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


hero["win_all"] = False

while True:
    #  2.3.2
    if not is_alive(hero) or hero["win_all"]:  # Выход из игры если победил или умер
        break
    action = sinput('game_input_actions').lower()  # 2.4.2
    if action in commands:
        execute(commands, action)
    else:
        say(command_error_text)


# Закос под многовариативность концовок
#  2.3.3
say(FINAL[hero['end_state']])

