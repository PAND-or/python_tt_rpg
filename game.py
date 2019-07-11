#!/usr/bin/python3
__author__ = "Андрей Петров"

history_text = 'В "Далекой далекой Галактике", на Заурядной планете\n' \
               'во время 5570302377 оборота вокруг одного желтого карлика класса G2V.\n' \
               'В 2377 солнечному циклу по местному цикло-исчислению от рождения Избранного. \n' \
               'В единственно уцелевшем месте совместного проживания особей гуманоидного типа,\n'  \
               'на местном наречии именуемого ”городом Арк-Таун”\n\n' \

hello_text = 'Защитник правопорядка мира и спокойствия последних выживших приступает к своему первому дежурству\n\n' \
             'Его встречает Лейтенант Кардеш\n\n'

lieutenant_name = 'Кардеш'

print(history_text)
input('Press any key to continue\n\n')

print(hello_text)
input('Press any key to continue\n\n')
hero_name = input(f'{lieutenant_name}: Легат, назови свое имя: ')

print(f'{lieutenant_name}: Добро пожаловать {hero_name} на свое первое задание\n')
input('Press any key to continue\n\n')

print(f'{lieutenant_name}: Кстати, совсем забыл как тебя угораздило вступить в Легат?\n')
input('Press any key to continue\n\n')

print(f'{hero_name}: Я ... У меня ...Не совсем помню ... \n'
      f'У меня шизодидное растройство и разные воспоминания о своем прошлом\n'
      f'Я помню одновременно 4 своих "прошлых жизней, какую тебе рассказать?\n'
      f'1. Я сын своего отца...\n'
      f'2. Я начал жить в трущебах городских \n'
      f'3. Я был батаником в школе-интернате\n'
      f'4. Проиграл я значит в очередной раз занятые кредиты ...\n')



while True:
    print('Я ....')
    inp_hero_class = input('Система: Выберете ответ 1, 2, 3 или 4:  ')
    if inp_hero_class == '1':
        print('Сын отца, стремящийся к идеалам во всем пришедший в Легат, чтобы доказать свою исключительность')
        hero_class = 'warrior'
        hp = 3000
        damage = 30
        stamina = 2000
        break
    elif inp_hero_class == '2':
        print('Сирота и беспризорник, всю жизнь проживший в гетто, пришел в Легат ради личной мести с '
              'главарем одной из банд Гетто')
        hero_class = 'robber'
        hp = 2000
        damage = 40
        stamina = 3000
        break
    elif inp_hero_class == '3':
        print('Воспитанник интерната для одаренных детей, его записали в Легат, т.к. интернатом владеет '
              'Легат и другого выбора у него нет ')
        hero_class = 'geek'
        hp = 1500
        damage = 20
        stamina = 4500
        break
    elif inp_hero_class == '4':
        print('Бездельник и кутила, записался в Легат, чтобы избежать платы по игорным долгам. ')
        hero_class = 'bard'
        hp = 4500
        damage = 10
        stamina = 1500
        break
    else:
        print('Пока не определился')

    input('Press any key to continue\n\n')

print(f'{lieutenant_name}: Хе хе хе, отличная история {hero_name}, не расстраивайся, еще найдешь себя\n')
input('Press any key to continue\n\n')

actions_text = '“history”, “help”, “train”, “exit”'

print(f'{lieutenant_name}: Выбери одно из действий {actions_text} или exit чтобы закончить игру\n')
while True:
    print(f'{lieutenant_name}: Чем займешься?\n')
    action = input('Я займусь: ')
    if action == 'exit':
        win = 0
        break
    elif action == 'history':
        print(history_text)
    elif action == 'help':
        print(f'Выбери одну из команд {actions_text}для совершения действия в участке')
    elif action == 'train':
        dummy_hp = 1500
        dummy_name = 'Тренировочный столб'
        train_stamina = stamina
        train_hp = dummy_hp
        print(f'Ты входишь в тренировочную комнату видишь перед собой {dummy_name}'
              f'Твоя задача разрушить столб быстрее, чем устанешь')

        input('Press any key to continue\n\n')
        while True:

            inp_hit = input('Выбери удар: 1 сильный, 2 быстрый: ')
            if inp_hit == '1':
                print(f'{hero_name} делает Сильный удар')
                hit_damage = damage * 4
                hit_stamina = damage * 6
            elif inp_hit == '2':
                print(f'{hero_name} делает быстрый удар')
                hit_damage = damage
                hit_stamina = damage * 2
            else:
                print('Ну кто так бьет?')
                hit_damage = 0
                hit_stamina = damage

            train_hp = train_hp - hit_damage
            train_stamina = train_stamina - hit_stamina

            print(f'{hero_name} нанес {hit_damage} урона')

            if train_hp <= 0:
                print(f'{dummy_name} повержен! Поздравляю, да ты герой!')
                stamina = stamina + 100
                damage = damage + 5
                input('Press any key to continue\n\n')
                break
            elif train_stamina <= 0:
                print(f'Ты слишком устал чтобы продолжать тренировку, попробуй еще раз!')
                input('Press any key to continue\n\n')
                stamina = stamina + 100
                break
            print(f'{dummy_name} HP: {train_hp}/{dummy_hp}')
            print(f'{hero_name} Stamina: {train_stamina}/{stamina} \n\n')

    else:
        print(f'{lieutenant_name}: Я не понимаю, чего ты хочешь, выбери доступную команду или напищи help')

if win == 0:
    print('Ты так и не узнал ответ на главный вопрос жизни вселенной и всего такого')