#!/usr/bin/python3
__author__ = "Андрей Петров"

""" TEXTS """
LORE = 'В "Далекой далекой Галактике", на Заурядной планете\n' \
               'во время 5570302377 оборота вокруг одного желтого карлика класса G2V.\n' \
               'В 2377 солнечному циклу по местному цикло-исчислению от рождения Избранного. \n' \
               'В единственно уцелевшем месте совместного проживания особей гуманоидного типа,\n'  \
               'на местном наречии именуемого ”городом Арк-Таун”\n\n' \

BEGIN_1 = 'Защитник правопорядка мира и спокойствия последних выживших приступает к своему первому дежурству\n\n' \
             'Его встречает Лейтенант Кардеш\n\n'

lieutenant_name = 'Кардеш'
dummy_name = 'Тренировочный столб'


intro_char_choice = f'{lieutenant_name}: Мы всем новичкам в Легате переписываем воспоминания, \n' \
    f'Но у тебя есть возможность выбрать какие именно воспоминания у тебя будут\n'  \
    f'На выбор 4 личности какую тебе имплантировать? \n\n' \


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
              f'Твоя задача разрушить столб\n\n'

intro_enemy_fight = f'Блуждая по городу, ты заметил правонарушение! Кто-то высказывает свои мысли\n' \
    f'Ты подходишь к нарушителю, чтобы преподать ему урок.\n' \
    f'Порядок нарушает:'

attack_1_name = 'Сильный удар'
attack_2_name = 'Быстрый удар'

train_win_text = f'{dummy_name} повержен! Поздравляю, да ты герой!\n\n'
train_tired_text = 'У тебя больше нет сил продолжать схватку. Отдохни немного и приходи снова\n'

actions_text = '“history”, “menu”, “train”, “exit”'

command_error_text = f'{lieutenant_name}: Я не понимаю, чего ты хочешь, выбери доступную команду или напищи menu'
command_menu_text = f'Герой, выбери одну из команд {actions_text} для совершения действия.'


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

# На случай добавления нового класса или удара, сразу добавлю во все тексты описание этого класса
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



"""
GAME
"""
# 1.5.3
print(LORE)
print(BEGIN_1)

# 1.5.1
hero_name = input(f'{lieutenant_name}: Легат, назови свое имя: \n>> ')

# 2.1
if not hero_name.istitle():
    hero_name = hero_name.capitalize()

BEGIN_2 = f'{lieutenant_name}: Добро пожаловать {hero_name} на свое первое задание\n' \


print(BEGIN_2)
print(intro_char_choice)

while True:
    inp_char_class = input(f'Система: Выберете ответ {roles_str}:\n>> ')  # 1.5.2
    if inp_char_class in roles:
        hero = roles[inp_char_class]
        print(f'Я .... {hero["hello_text"]}')
        break
    else:
        print('Такая личность в системе не обнаружена')


all_win = False
commands = ('exit', 'history', 'menu', 'train', 'start')  # 2.4.1
command_menu_text += '\n `start` - начало игры'  # 2.4.3
print(command_menu_text)

# 1.5.4
while True:
    #  2.3.2
    if all_win is True:  # Выход из игры если победил
        end_state = 'win'
        break
    #  2.3.1
    elif hero["hp"] <= 0:  # Выход из игры, проигрыш
        end_state = 'lose'
        break

    action = input('Введи команду: \n>> ').lower()  # 2.4.2
    if action not in commands:
        print(command_error_text)
    elif action == 'exit':  # Конец игры. Выход
        end_state = 'exit'
        break
    # 1.5.6
    elif action == 'history':
        print(LORE)
    # 1.5.5
    elif action == 'menu':
        print(command_menu_text)
    # 1.6

    elif action == 'start':
        for enemy in all_enemies:  # 2.6.1
            # Условия выхода из цикла перебора врагов
            if hero["hp"] <= 0:  # Если нет здоровья
                print('Убили')
                break

            print(intro_enemy_fight, enemy["name"], '\n')

            # 2.6.4
            print(f'{"Name":^15}{"Role":^10}{"HP":^10}{"Damage":^10}{"Armor":^10}\n'
                  f'{enemy["name"]:^15}{enemy["role_name"]:^10}{enemy["hp"]:^10}{enemy["damage"]:^10}'
                  f'{enemy["armor"]:^10}\n')
            input('\nPress ENTER to continue\n')

            while hero["hp"] > 0 and enemy["hp"] > 0:  # 2.6.2
                hit_hero_damage = hero["damage"] - enemy["armor"]
                hit_enemy_damage = enemy["damage"] - hero["armor"]

                # 2.6.9
                hit_enemy_damage = hit_enemy_damage if hit_enemy_damage >= 0 else 0
                hit_hero_damage = hit_hero_damage if hit_hero_damage >= 0 else 0

                hero["hp"] -= hit_enemy_damage
                enemy["hp"] -= hit_hero_damage

                print(f'{hero_name} наносит {hit_hero_damage} урона по {enemy["name"]}\n'
                      f'{enemy["name"]:<15}{enemy["hp"]:>10}/{enemy["max_hp"]:<10}\n'
                      f'{enemy["name"]} наносит {hit_enemy_damage} урона по {hero_name}\n'  
                      f'{hero_name:<15}{hero["hp"]:>10}/{hero["max_hp"]:<10}\n\n')

                input('\nPress ENTER to continue\n')

        if hero["hp"] > 0:  # Если всех победили
            all_win = True
            print('Всех победил')


    # 1.6
    elif action == 'train':
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

        while True: # удары
            hit_damage = hero['train_damage']
            instructor["hp"] -= hit_damage
            print(f'{hero_name} нанес {hit_damage} урона')
            print(f'{instructor["name"]}: {instructor["hp"]}/{instructor["max_hp"]}\n')
            input('press ENTER to continue\n')

            if instructor['hp'] <= 0:  # Если жизней осталось 0 то победа
                print(train_win_text)
                break



# Закос под многовариативность концовок
#  2.3.3
print(FINAL[end_state])