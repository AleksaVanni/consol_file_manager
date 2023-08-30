import sys
from myfunctionals.functions import *
from myfunctionals.victory import get_person_and_question
from myfunctionals.bank import bank_account

while True:
    try:
        print('MЕНЮ:')
        m = '''
            1: "создать файл/папку",
            2: "удалить (файл/папку)",
            3: "копировать (файл/папку)",
            4: "просмотр содержимого рабочей директории",
            5: "сохранить содержимое рабочей директории в файл",
            6: "посмотреть только папки",
            7: "посмотреть только файлы",
            8: "просмотр информации об операционной системе",
            9: "создатель программы",
            10: "играть в викторину",
            11: "мой банковский счет",
            12: "смена рабочей директории (*необязательный пункт)",
            13: "выход"
            '''
        print(m)
        print('--*--' * 7)
        menu_input = int(input('Выберите пункт меню: '))
        print('--*--' * 7)

        path = os.getcwd()

        if menu_input == 1:
            dir_file()  # создать файл или папку
        elif menu_input == 2:
            del_dir_file()  # удалить файл или папку
        elif menu_input == 3:
            my_copy()  # копирова файл или папку
        elif menu_input == 4:
            look_dir(path)  # просмотр содержимого рабочей директории
        elif menu_input == 5:
            save_directory_contents_to_file(path)
            print("Содержимое рабочей директории сохранено в файл 'listdir.txt'")
        elif menu_input == 6:
            print(*(f for f in os.listdir() if not os.path.isfile(f)))  # просмотр только папок
        elif menu_input == 7:
            print(*(f for f in os.listdir() if os.path.isfile(f)))  # просмотр только файлов
        elif menu_input == 8:
            print('Ваша операционная система: ', '***', sys.platform, '***')  # просмотр информации об операционной системе
        elif menu_input == 9:
            print('Создатель этой программы --- @lek$@ndr@ ---')  # создатель программы
        elif menu_input == 10:  # играть в викторину
            rounds = int(input('Сколько раз вы хотите играть?: '))
            for i in range(rounds):
                get_person_and_question()
            print('Пока!')
        elif menu_input == 11:
            bank_account()  # мой банковский счет
        elif menu_input == 12:
            look_getcwd()  # смена рабочей директории
        elif menu_input == 13:  # выход из программы
            my_exit()
        else:
            print("Некорректный ввод. Выберите пункт меню от 1 до 13.")

    except ValueError:
        print("Некорректный ввод. Введите число от 1 до 13.")
