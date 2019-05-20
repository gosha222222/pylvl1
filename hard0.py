# Смена директории работает только если в пути нет пробелов и еще какой - нибудь шляпы.
# Все остальное работает.

import os
import sys
import shutil

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - дублирует файл")
    print("rm <file_name> - удаляет файл")
    print("ls - выведет полный путь текущей директории")
    print("cd <path> - поменяет текущую директорию на указанную")
    print("ping - pong :)))")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def ping():
    print("pong")

def copyfile():
    if os.path.isfile(dir_name):
        dir_name_mass = dir_name.split('.')
        exten = dir_name_mass[-1]
        dir_name_mass.pop()
        dir_name_str = ''.join(dir_name_mass)
        newfile = dir_name_str + "_1." + exten
        shutil.copyfile(dir_name, newfile)
        print('Файл {} продублирован в файл {}'.format(dir_name, newfile))
    else:
        print("Возникли проблемы. Введите название ФАЙЛА с расширением. Например, photo.jpg")

def removefile():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    res = input(f"Вы действтвительно хотите удалить файл {dir_name}? Y/N\n")
    if res == "y" or res == "Y":
        try:
            os.remove(dir_name)
            print('Файл {} удален'.format(dir_name))
        except FileNotFoundError:
            print('Файла {} не существует'.format(dir_name))
    else:
        print("Ничего не было удалено")

def lsls():
    print(os.getcwd())

def chchdir():
    os.chdir(dir_name)
    print(os.getcwd())
do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp" : copyfile,
    "rm" : removefile,
    "ls" : lsls,
    "cd" : chchdir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
