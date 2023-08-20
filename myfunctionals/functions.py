import os


def dir_file():
    fp = input('Создать файл (f) или папку (p): ')
    if fp == 'p':
        name_p = input('Введите имя новой папки: ')
        if not os.path.exists(name_p):  # проверка на существование
            os.mkdir(name_p)  # создать папку
            print(f'Папка {name_p} успешно создана')
        else:
            print(f'Папка с именем "{name_p}" уже существует')

    elif fp == 'f':
        name_f = input('Введите имя нового файла: ')
        if not os.path.exists(name_f):  # проверка на существование
            with open(name_f, 'w') as f:  # создать файл
                f.close()
            print(f'Файл {name_f} успешно создан')
        else:
            print(f'Файл с именем "{name_f}" уже существует')


def del_dir_file():
    pf = input('Удалить папку (p), удалить файл (f): ')
    if pf == 'p':
        name_to_delete = input('Введите имя папки (пустой) для её удаления: ')
        if not os.path.exists(name_to_delete):  # проверка на существование
            print(f"Ошибка, папки с именем \"{name_to_delete}\" не существует")
        else:
            os.rmdir(name_to_delete)  # удалить папку
            print(f"Папка {name_to_delete} успешно удалена")
    elif pf == 'f':
        name_to_delete = input('Введите имя файла для его удаления: ')
        if not os.path.exists(name_to_delete):
            print(f"Ошибка, файла с именем \"{name_to_delete}\" не существует")
        else:
            os.remove(name_to_delete)
            print(f"Файл {name_to_delete} успешно удален")


def my_copy():
    import shutil

    pf = input('Копировать папку (p), копировать файл (f): ')
    if pf == 'p':
        n_copy = input("Введите имя папки для которой нужно создать копию: ")
        if not os.path.exists(n_copy) or not os.path.isdir(n_copy):
            print("Ошибка, такой папки не найдено")
        else:
            new_copy = input("Введите имя для копии папки: ")
            shutil.copytree(n_copy, new_copy)  # создание копии
            print(f"Папка \"{n_copy}\" успешно скопирована в \"{new_copy}\"")

    elif pf == 'f':
        n_copy = input("Введите имя документа для которой нужно создать копию: ")
        if not os.path.exists(n_copy):  # проверка на существование
            print(f"Ошибка, {n_copy} файла не найдено")
        else:
            new_copy = input("Введите имя для копии файла: ")
            shutil.copy(n_copy, new_copy)  # создание копии
            print(f'Копия документа {n_copy} успешно создана под именем {new_copy}')


def look_dir(path):
    print(os.listdir(path))  # просмотр содержимого рабочей директории


def save_directory_contents_to_file(path):
    files = []
    dirs = []

    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
        else:
            dirs.append(item)

    with open('listdir.txt', 'w') as f:
        f.write('files: ' + ', '.join(files) + '\n')
        f.write('dirs: ' + ', '.join(dirs))


def look_getcwd():
    print(f'Текущая рабочая директория: {os.getcwd()}')
    new_dir = input('Введите путь к новой рабочей директории: ')
    if os.path.exists(new_dir):  # Проверка на существование директории
        os.chdir(new_dir)  # Смена рабочей директории
        print(f'Новая рабочая директория: {os.getcwd()}')
    else:
        print(f'Директория "{new_dir}" не существует')


def my_exit():
    import sys
    sys.exit("Выход из программы")
