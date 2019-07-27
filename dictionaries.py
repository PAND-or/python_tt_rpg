
""" TEXTS """
LORE = 'В "Далекой далекой Галактике", на Заурядной планете\n' \
               'во время 5570302377 оборота вокруг одного желтого карлика класса G2V.\n' \
               'В 2377 солнечному циклу по местному цикло-исчислению от рождения Избранного. \n' \
               'В единственно уцелевшем месте совместного проживания особей гуманоидного типа,\n'  \
               'на местном наречии именуемого ”городом Арк-Таун”\n' \

BEGIN_1 = 'Защитник правопорядка мира и спокойствия последних выживших приступает к своему первому дежурству\n' \
             'Его встречает Лейтенант Кардеш\n'

lieutenant_name = 'Кардеш'
dummy_name = 'Тренировочный столб'


intro_char_choice = f'{lieutenant_name}: Мы всем новичкам в Легате переписываем воспоминания, \n' \
    f'Но у тебя есть возможность выбрать какие именно воспоминания у тебя будут\n'  \
    f'На выбор 4 личности какую тебе имплантировать? \n' \


FINAL = {
    'win': 'Ты нашел "чип 42". С горящими глазами вставляешь его в “Компьютеру”, идет вычислительный процесс. \n\n\n'
           'Сейчас будет дан ответ жизни, смерти и всего такого. \n\n\n'
           'Ответ: 42',
    'exit': 'Жаль, что ты уходишь, ты так и не узнал ответ на главный вопрос жизни вселенной и всего такого',
    'lose': 'Твоей оболочке был нанесен критический урон. Сознание отключилось. \n'
            'Биооболочку без амуниции и оружия, с выпотрашенными сенсорами доставили назад в Легат. \n'
            'Нейромодуль цел, и ты можешь начать все сначала'
 }

intro_warrior = 'Сын отца, стремящийся к идеалам во всем пришедший в Легат, чтобы доказать свою исключительность \n'
intro_robber = 'Сирота и беспризорник, всю жизнь проживший в гетто, пришел в Легат ради личной мести с ' \
               'главарем одной из банд Гетто\n'
intro_geek = 'Воспитанник интерната для одаренных детей, его записали в Легат, т.к. интернатом владеет ' \
             'Легат и другого выбора у него нет \n'
intro_bard = 'Бездельник и кутила, записался в Легат, чтобы избежать платы по игорным долгам. \n'

intro_train_fight = f'Ты входишь в тренировочную комнату видишь перед собой {dummy_name} \n' \
              f'Твоя задача разрушить столб быстрее, чем устанешь\n\n'

intro_enemy_fight = f'Ты заметил правонарушение! Кто-то высказывает свои мысли\n' \
    f'Ты подходишь к нарушителю, чтобы преподать ему урок.\n' \
    f'Порядок нарушает:'

attack_1_name = 'Сильный удар'
attack_2_name = 'Быстрый удар'

train_win_text = f'{dummy_name} повержен! Поздравляю, да ты герой!\n\n'
train_tired_text = 'У тебя больше нет сил продолжать схватку. Отдохни немного и приходи снова\n'

actions_text = '\n“history” - Лор игры, \n“help” - Помощ по командам, \n“train” - Тренировка, ' \
               '\n“exit” - Выход из игры, \n“stats” - Статистика героя'


command_error_text = f'{lieutenant_name}: Я не понимаю, чего ты хочешь, выбери доступную команду или напищи help'
command_help_text = f'Герой, выбери одну из команд {actions_text} для совершения действия.'

command_help_text += '\n“start” - Начало игры'  # 2.4.3

"""
DICTIONARIES
"""

#  2.2.1 - 2.2.3

warrior = {
    'hello_text': intro_warrior,
    'choice_text': f'Ты сын своего отца...',
    'role_name': 'warrior',
    'hp': 300,
    'max_hp': 300,
    'damage': 15,
    'stamina': 100,
    'max_stamina': 100,
    'armor': 2,
}
robber = {
    'hello_text': intro_robber,
    'choice_text': f'Ты начал жить в трущебах городских',
    'role_name': 'robber',
    'hp': 200,
    'max_hp': 200,
    'damage': 20,
    'stamina': 300,
    'max_stamina': 300,
    'armor': 1,
}
geek = {
    'hello_text': intro_geek,
    'choice_text': f'Ты был батаником в школе-интернате',
    'role_name': 'geek',
    'hp': 200,
    'max_hp': 200,
    'damage': 12,
    'stamina': 200,
    'max_stamina': 200,
    'armor': 5,
}
bard = {
    'hello_text': intro_bard,
    'choice_text': f'Вся твоя жизнь кутеж ..',
    'role_name': 'bard',
    'hp': 500,
    'max_hp': 500,
    'damage': 12,
    'stamina': 100,
    'max_stamina': 100,
    'armor': 0,
}
roles = {
    'w': warrior,
    'r': robber,
    'g': geek,
    'b': bard,
}

# 2.6.8
dict_move = {
    'attack': {
        'armor_modificator': 0.25,
        'damage_modificator': 1.3,
        'name': 'Сильный удар'
    },
    'defense': {
        'armor_modificator': 1.5,
        'damage_modificator': 0.7,
        'name': 'Блок и контратакует'
    },
    'default': {
        'armor_modificator': 1,
        'damage_modificator': 1,
        'name': 'Быстрый удар'
    },
    'skip': {
        'armor_modificator': 1,
        'damage_modificator': 0,
        'name': 'Бессильный удар'
    }
}

chest = [
    {
        'name': 'Дубинка',
        'modificator': 'damage',
        'rule': 'add',
        'value': 3,
    },
    {
        'name': 'Карбоновая броня',
        'modificator': 'armor',
        'rule': 'add',
        'value': 3,
    },
    {
        'name': 'Ремонтные нано-боты',
        'modificator': 'hp',
        'rule': 'heal',
        'value': 1,
    },
]



# На случай добавления нового класса или удара, сразу добавлю во все тексты описание этого класса

moves_str = ''
for k, v in dict_move.items():
    moves_str += f'{k}, '

roles_str = ''
for k, v in roles.items():
    roles_str += f'{k}, '
    intro_char_choice += f'{k}: {v["choice_text"]}  \n'

# 2.5.1
all_enemies = [
    {
        'name': 'Вышибала',
        'role_name': 'warrior',
        'hp': 150,
        'max_hp': 150,
        'damage': 7,
        'stamina': 100,
        'max_stamina': 100,
        'armor': 5
    },
    {
        'name': 'Гопник',
        'role_name': 'robber',
        'hp': 100,
        'max_hp': 100,
        'damage': 10,
        'stamina': 150,
        'max_stamina': 150,
        'armor': 2,
    },
    {
        'name': 'Ботаник',
        'role_name': 'geek',
        'hp': 75,
        'max_hp': 75,
        'damage': 5,
        'stamina': 225,
        'max_stamina': 225,
        'armor': 1,
    },
    {
        'name': 'Пьяный дебошир',
        'role_name': 'bard',
        'hp': 225,
        'max_hp': 225,
        'damage': 2,
        'stamina': 75,
        'max_stamina': 75,
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
    'stamina': 75,
    'max_stamina': 75,
    'armor': 2,
}

