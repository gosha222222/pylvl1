import os
import sys
import shutil
# print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - дублирует файл")
    print("rm <file_name> - удаляет файл")


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
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    # try:
    shutil.copyfile(dir_name, "less.py")
    print('Файл {} скопирован в файл "less"'.format(dir_name))
    # except FileExistsError:
    #     print('директория {} уже существует'.format(dir_name))

def removefile():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_name)
        print('Файл {} удален'.format(dir_name))
    except FileNotFoundError:
        print('Файла {} не существует'.format(dir_name))

def lsls():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp" : copyfile,
    "rm" : removefile,
    "ls" : lsls
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
