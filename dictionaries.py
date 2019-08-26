""" TEXTS """
LORE = 'В "Далекой далекой Галактике", на Заурядной планете\n' \
               'во время 5570302377 оборота вокруг одного желтого карлика класса G2V.\n' \
               'В 2377 солнечному циклу по местному цикло-исчислению от рождения Избранного. \n' \
               'В единственно уцелевшем месте совместного проживания особей гуманоидного типа,\n'  \
               'на местном наречии именуемого ”городом Арк-Таун”\n\n' \

BEGIN_1 = 'Защитник правопорядка мира и спокойствия последних выживших приступает к своему первому дежурству\n' \
             'Его встречает Лейтенант Кардеш\n\n'


lieutenant_name = 'Кардеш'
dummy_name = 'Тренировочный столб'


intro_char_choice = f'{lieutenant_name}: Мы всем новичкам в Легате переписываем воспоминания, \n' \
    f'Но у тебя есть возможность выбрать какие именно воспоминания у тебя будут\n'  \
    f'На выбор 4 личности какую тебе имплантировать? \n\n' \

game_input_heroname = f'{lieutenant_name}: Легат, назови свое имя:'
game_begin_2 = 'Добро пожаловать %s на свое первое задание\n'
game_input_roles = 'Система: Выберете ответ %s:'
game_roles_chosen = 'Я .... %s'
game_roles_errchoise = 'Такая личность в системе не обнаружена'
game_input_actions = 'Введи команду:'
game_briffing = 'Ты готов отправиться на свое первое дежурство, твоя оболочка все сделает за тебя. ' \
                'Пишешь ей команду и если оболочка ее знает, она ее выполнит\n'
FINAL = {
    'win': 'Ты нашел "чип 42". С горящими глазами вставляешь его в “Компьютеру”, идет вычислительный процесс. \n\n\n'
           'Сейчас будет дан ответ жизни, смерти и всего такого. \n\n\n'
           'Ответ: 42',
    'exit': 'Жаль, что ты уходишь, ты так и не узнал ответ на главный вопрос жизни вселенной и всего такого',
    'lose': 'Твоей оболочке был нанесен критический урон. Сознание отключилось. \n'
            'Био-оболочку без амуниции и оружия, с выпотрошенные сенсорами доставили назад в Легат. \n'
            'Нейро модуль цел, и ты можешь начать все сначала'
 }

intro_warrior = 'Сын отца, стремящийся к идеалам во всем пришедший в Легат, чтобы доказать свою исключительность \n'
intro_robber = 'Сирота и беспризорник, всю жизнь проживший в гетто, пришел в Легат ради личной мести с ' \
               'главарем одной из банд Гетто\n'
intro_geek = 'Воспитанник интерната для одаренных детей, его записали в Легат, т.к. интернатом владеет ' \
             'Легат и другого выбора у него нет \n'
intro_bard = 'Бездельник и кутила, записался в Легат, чтобы избежать платы по игорным долгам. \n'
choice_warrior = f'Ты сын своего отца...'
choice_robber = f'Ты начал жить в трущебах городских'
choice_geek = f'Ты был ботаником в школе-интернате'
choice_bard = f'Вся твоя жизнь кутеж ...'


intro_train_fight = f'Ты входишь в тренировочную комнату видишь перед собой {dummy_name} \n' \
              f'Твоя задача разрушить столб\n\n'

intro_enemy_fight = f'Блуждая по городу, ты заметил правонарушение! Кто-то высказывает свои мысли\n' \
    f'Ты подходишь к нарушителю, чтобы преподать ему урок.\n' \
    f'Порядок нарушает: %s \n\n'

attack_1_name = 'Сильный удар'
attack_2_name = 'Быстрый удар'

train_win_text = f'{dummy_name} повержен! Поздравляю, да ты герой!\n\n'
train_tired_text = 'У тебя больше нет сил продолжать схватку. Отдохни немного и приходи снова\n'
train_input_def = 'Желаете ли поменять дефолтные значения Тренировочного боя? Y or N'
train_input_hp = 'Введите кол-во жизней инструктора:'
train_input_dmg = 'Введите силу удара:'
train_input_corhp = 'Не корректное значение урона. Новое значение: %s'

actions_text = '\n“history” - Лор игры, \n“menu” - Помощь по командам, \n“train” - Тренировка, ' \
               '\n“exit” - Выход из игры, \n“stats” - Статистика героя, \n“start” - Начало игры'

command_error_text = f'{lieutenant_name}: Я не понимаю, чего ты хочешь, выбери доступную команду или напиши menu'
command_menu_text = f'Герой, выбери одну из команд {actions_text} для совершения действия.'
pause_text = 'Press ENTER to continue'
hit_result = '%s наносит %s урона по %s'
hp_show = '%s: %s'


choice_items_list = 'Ты находишь импланты:\n%s\n'
choice_items_input = 'Введи код модификации'
choice_items_error = 'Ошибка. Модификация с таким кодом не найдена. Отказ в доступе на улучшение'
choice_items_reinput = 'Ошибка. Укажи номер модификации, либо 99 для отказа'
choice_items_empty = 'Оболочка оказалась пустой'

move_empty_room = 'Оглядевшись вокруг, ты не замечаешь ничего необычного'
move_chest_room = 'Войдя в квартал ты находишь чью-то пустую оболочку. Непременно надо достать из нее чипы'
move_enemy_room = 'Ты замечаешь агрессивно настроенного гражданина'

preson_update = 'Ты прокачал свою оболочку, полюбуйся'


"""
DICTIONARIES
"""

#  2.2.1 - 2.2.3
warrior = {
    'hello_text': intro_warrior,
    'choice_text': choice_warrior,
    'role_name': 'warrior',
    'hp': 300,
    'max_hp': 300,
    'damage': 10,
    'armor': 2,
}
robber = {
    'hello_text': intro_robber,
    'choice_text': choice_robber,
    'role_name': 'robber',
    'hp': 200,
    'max_hp': 200,
    'damage': 15,
    'armor': 1,
}
geek = {
    'hello_text': intro_geek,
    'choice_text': choice_geek,
    'role_name': 'geek',
    'hp': 200,
    'max_hp': 200,
    'damage': 7,
    'armor': 5,
}
bard = {
    'hello_text': intro_bard,
    'choice_text': choice_bard,
    'role_name': 'bard',
    'hp': 500,
    'max_hp': 500,
    'damage': 7,
    'armor': 0,
}


roles = {
    'w': warrior,
    'r': robber,
    'g': geek,
    'b': bard,
}

# На случай добавления нового класса или удара, сразу добавлю во все тексты описание этого класса
roles_str = ''
for k, v in roles.items():
    roles_str += f'{k}, '
    intro_char_choice += f'{k}: {v["choice_text"]}  \n'

broken_item_name = ' - полностью разрушен'
good_item_name = ' - в хорошем состоянии'
chest_list = [
    {
        'name': 'Боевой имплант',
        'text': '',
        'min': 1,
        'max': 3,
        'rule': 'add',
        'key': 'damage'
    },
    {
        'name': 'Защитный имплант',
        'text': '',
        'min': 1,
        'max': 3,
        'rule': 'add',
        'key': 'armor'
    },
    {
        'name': 'Станция нанитов',
        'text': ' (увеличение max hp)',
        'min': 10,
        'max': 30,
        'rule': 'add',
        'key': 'max_hp'
    },
    {
        'name': 'Наниты',
        'text': ' (лечение)',
        'min': 10,
        'max': 100,
        'rule': 'restore',
        'key': 'hp'
    }
]


# 2.5.1
all_enemies = [
    {
        'name': 'Вышибала',
        'role_name': 'warrior',
        'hp': 75,
        'max_hp': 75,
        'damage': 2,
        'armor': 5
    },
    {
        'name': 'Гопник',
        'role_name': 'robber',
        'hp': 50,
        'max_hp': 50,
        'damage': 5,
        'armor': 2,
    },
    {
        'name': 'Ботаник',
        'role_name': 'geek',
        'hp': 45,
        'max_hp': 45,
        'damage': 0,
        'armor': 1,
    },
    {
        'name': 'Пьяный дебошир',
        'role_name': 'bard',
        'hp': 150,
        'max_hp': 150,
        'damage': 0,
        'armor': 0,
    },
]

# 2.5.3
instructor = {
    'name': dummy_name,
    'role_name': 'bard',
    'hp': 225,
    'max_hp': 225,
    'damage': 5,
    'armor': 2,
}

TEXTS = {
    'LORE': LORE,
    'BEGIN_1': BEGIN_1,
    'intro_char_choice': intro_char_choice,
    'FINAL': FINAL,
    'intro_warrior': intro_warrior,
    'intro_robber': intro_robber,
    'intro_geek': intro_geek,
    'intro_bard': intro_bard,
    'choice_warrior': choice_warrior,
    'choice_robber': choice_robber,
    'choice_geek': choice_geek,
    'choice_bard': choice_bard,
    'intro_train_fight': intro_train_fight,
    'intro_enemy_fight': intro_enemy_fight,
    'train_win_text': train_win_text,
    'train_tired_text': train_tired_text,
    'actions_text': actions_text,
    'command_error_text': command_error_text,
    'command_menu_text': command_menu_text,
    'hit_result': hit_result,
    'hp_show': hp_show,
    'train_input_def': train_input_def,
    'train_input_hp': train_input_hp,
    'train_input_dmg': train_input_dmg,
    'train_input_corhp': train_input_corhp,
    'pause_text': pause_text,
    'game_input_heroname': game_input_heroname,
    'game_begin_2': game_begin_2,
    'game_input_roles': game_input_roles,
    'game_roles_chosen': game_roles_chosen,
    'game_roles_errchoise': game_roles_errchoise,
    'game_input_actions': game_input_actions,
    'game_briffing': game_briffing,
    'choice_items_list': choice_items_list,
    'choice_items_input': choice_items_input,
    'choice_items_error': choice_items_error,
    'choice_items_reinput': choice_items_reinput,
    'choice_items_empty': choice_items_empty,
    'move_empty_room': move_empty_room,
    'move_chest_room': move_chest_room,
    'move_enemy_room': move_enemy_room,
    'preson_update': preson_update
}