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
    f'На выбор 4 личности какую тебе имплантировать? \n' \
    f'1. Ты сын своего отца...\n' \
    f'2. Ты начал жить в трущебах городских \n' \
    f'3. Ты был батаником в школе-интернате\n' \
    f'4. Вся твоя жизнь кутеж ...\n' \


FINAL = 'Ты нашел "чип 42". С горящими глазами вставляешь его в “Компьютеру”, идет вычислительный процесс. \n\n\n' \
        'Сейчас будет дан ответ жизни, смерти и всего такого. \n\n\n' \
        'Ответ: 42'
FINAL_LOSE = 'Ты так и не узнал ответ на главный вопрос жизни вселенной и всего такого'


intro_warrior = 'Сын отца, стремящийся к идеалам во всем пришедший в Легат, чтобы доказать свою исключительность \n'
intro_robber = 'Сирота и беспризорник, всю жизнь проживший в гетто, пришел в Легат ради личной мести с ' \
               'главарем одной из банд Гетто\n'
intro_geek = 'Воспитанник интерната для одаренных детей, его записали в Легат, т.к. интернатом владеет ' \
             'Легат и другого выбора у него нет \n'
intro_bard = 'Бездельник и кутила, записался в Легат, чтобы избежать платы по игорным долгам. \n'

intro_fight = f'Ты входишь в тренировочную комнату видишь перед собой {dummy_name}' \
              f'Твоя задача разрушить столб быстрее, чем устанешь\n\n'

attack_1_name = 'Сильный удар'
attack_2_name = 'Быстрый удар'

train_win_text = f'{dummy_name} повержен! Поздравляю, да ты герой!\n\n'
train_tired_text = 'У тебя больше нет сил продолжать схватку. Отдохни немного и приходи снова\n'

actions = '“history”, “help”, “train”, “exit”, “stats”'

command_error_text = f'{lieutenant_name}: Я не понимаю, чего ты хочешь, выбери доступную команду или напищи help'
command_help_text = f'Герой, выбери одну из команд {actions} для совершения действия'

"""

GAME

"""
# 5.3
print(LORE)
print(BEGIN_1)

# 5.1
hero_name = input(f'{lieutenant_name}: Легат, назови свое имя: \n>>')
BEGIN_2 = f'{lieutenant_name}: Добро пожаловать {hero_name} на свое первое задание\n' \


print(BEGIN_2)
print(intro_char_choice)

while True:
    inp_char_class = input('Система: Выберете ответ 1, 2, 3 или 4:\n>>')  # 5.2
    if inp_char_class != '1' and inp_char_class != '2' and inp_char_class != '3' and inp_char_class != '4':
        print('Такая личность в системе не обнаружена')
    else:
        break

# 5.2
if inp_char_class == '1':
    print(intro_warrior)
    char_class = 'warrior'
    char_hp = 3000
    char_damage = 30
    char_stamina = 2000
    char_armor = 50

elif inp_char_class == '2':
    print(intro_robber)
    char_class = 'robber'
    char_hp = 2000
    char_damage = 40
    char_stamina = 3000
    char_armor = 25

elif inp_char_class == '3':
    print(intro_geek)
    char_class = 'geek'
    char_hp = 1500
    char_damage = 20
    char_stamina = 4500
    char_armor = 75

elif inp_char_class == '4':
    print(intro_bard)
    char_class = 'bard'
    char_hp = 4500
    char_damage = 10
    char_stamina = 1500
    char_armor = 25


# 5.4
win = 0
print(command_help_text)
while True:
    if win == 1:  # Выход из игры если победил
        break

    action = input('Введи команду: \n>> ')
    if action == 'exit':  # Конец игры. Проигрыш
        break
    # 5.6
    elif action == 'history':
        print(LORE)
    # 5.5
    elif action == 'help':
        print(command_help_text)
    # 6
    elif action == 'stats':
        print(f'{"Name":^15}{"Class":^10}{"HP":^10}{"Damage":^10}{"Stamina":^10}{"Armor":^10}\n'
              f'{hero_name:^15}{char_class:^10}{char_hp:^10}{char_damage:^10}{char_stamina:^10}{char_armor:^10}')
    # 6
    elif action == 'train':
        # 6.1
        hp_enemy_inp = int(input('Введите кол-во жизней противника:\n>> '))
        damage = int(input('Введите силу удара:\n>> '))

        if damage > hp_enemy_inp:
            damage = hp_enemy_inp * 0.25
            print(f'Не корректное значение урона. Новое значение: {damage}')

        stamina_inp = int(input('Введите выносливость:\n>> '))
        if stamina_inp < hp_enemy_inp:
            stamina_inp = hp_enemy_inp * 0.75
            print(f'Не корректное значение урона. Новое значение: {stamina_inp}')

        hp_enemy = hp_enemy_inp  # для вывода в формате Стало / Было жизней
        stamina = stamina_inp

        print(intro_fight)

        while True:  # разные удары
            inp_hit = input(f'Выбери удар: 1 {attack_1_name}, 2 {attack_2_name}: ')
            if inp_hit == '1':
                print(f'{hero_name} делает {attack_1_name}\n')
                hit_damage = damage * 2
                hit_stamina = damage * 3
            elif inp_hit == '2':
                print(f'{hero_name} делает {attack_2_name}\n')
                hit_damage = damage
                hit_stamina = damage
            else:
                print('Ну кто так бьет?')
                hit_damage = 0
                hit_stamina = damage

            hp_enemy -= hit_damage
            stamina -= hit_stamina

            print(f'{hero_name} нанес {hit_damage} урона\n')

            if stamina <= 0:  # Если устал
                print(train_tired_text)
                break

            if hp_enemy <= 0:  # Если жизней осталось 0 то победа
                print(train_win_text)
                win = 1
                break

            # 6
            print(f'{"Name":<20}{"HP":>10}/{"MAX HP":<10}{"Stamina":>10}/{"Max stamina":<10}\n'
                  f'{dummy_name:<20}{hp_enemy:>10}/{hp_enemy_inp:<10}{"-":>10}/{"-":<10}\n'
                  f'{hero_name:<20}{char_hp:>10}/{char_hp:<10}{stamina:>10}/{stamina_inp:<10}\n')

    else:
        print(command_error_text)

if win == 1:
    print(FINAL)
elif win == 0:
    print(FINAL_LOSE)
