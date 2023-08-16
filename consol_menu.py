import os
import shutil
import sys
from myfunctionals.functions import *
from myfunctionals.victory import get_person_and_question
from myfunctionals.bank import bank_account
while True:
    print('MЕНЮ:')
    m = '''\t1: "создать файл/папку",                                     
    2: "удалить (файл/папку)",                                          
    3: "копировать (файл/папку)",                                      
    4: "просмотр содержимого рабочей директории",                       
    5: "посмотреть только папки",
    6: "посмотреть только файлы",
    7: "просмотр информации об операционной системе",
    8: "создатель программы",
    9: "играть в викторину",
    10: "мой банковский счет",
    11: "смена рабочей директории (*необязательный пункт)",
    12: "выход"'''

    print(m)
    print('--*--' * 7)
    menu_input = int(input('Выберите пункт меню: '))
    print(list(m.split('\n'))[menu_input - 1])

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
        print(*(f for f in os.listdir() if not os.path.isfile(f)))  # просмотр только папок
    elif menu_input == 6:
        print(*(f for f in os.listdir() if os.path.isfile(f)))  # просмотр только файлов
    elif menu_input == 7:
        print('Ваша операционная система: ', '***', sys.platform, '***')  # просмотр информации об операционной системе
    elif menu_input == 8:
        print('Создатель этой программы --- @lek$@ndr@ ---')  # создатель программы

    elif menu_input == 9:  # играть в викторину
        rounds = int(input('Сколько раз вы хотите играть?: '))
        for i in range(rounds):
            get_person_and_question()
        print('Пока!')

    elif menu_input == 10:
        bank_account()  # мой банковский счет



    elif menu_input == 11:
        look_getcwd()  # смена рабочей директории


    elif menu_input == 12:  # выход из программы
        my_exit()
