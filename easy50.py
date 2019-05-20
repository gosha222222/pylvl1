import os
import sys
from shutil import copyfile

def my_chdir():
    dirr = input(
        "Введите название папки, в которую хотите перейти:\nЧто бы вернуться на одну папку вверх введите '..'(Две точки без кавычек)\n")
    try:
        os.chdir(dirr)
        print("Переход успешно выполнен!")
        res = 0
    except FileNotFoundError:
        print("Указанная директория не существует!")
        res = 0

def my_listdir():
    print(os.listdir())
    print("Содержимое папки выведено успешно!\n")
    res = 0

def my_deldir():
    dell = input("Введите название папки, которую хотите удалить:\n")
    try:
        os.rmdir(dell)
        print("Папка успешно удалена!\n")
        res = 0
    except FileNotFoundError:
        print("Папка не существует!\n")
        res = 0
    except PermissionError:
        print("В данный момент папка занята другим процессом. Закройте программы, которые могут ее использовать и повторите попытку!\n")
        res = 0

def my_crdir():
    creat = input("Введите название папки, которую хотите создать:\n")
    try:
        os.mkdir(creat)
        print("Папка успешно создана!\n")
        res = 0
    except FileExistsError:
        print("Папка уже существует!\n")
        res = 0

if __name__ == '__main__':
    import os
    import sys
    from shutil import copyfile

    # Задача 1
    folders = ("dir_1", "dir_2", "dir_3", "dir_4",
               "dir_5", "dir_6", "dir_7", "dir_8", "dir_9")

    for folder in folders:
        os.mkdir(folder)
    for folder in folders:
       os.rmdir(folder)

    # Задача 2
    for direct in os.listdir():
        if os.path.isdir(direct) == True:
            print(direct)

    # Задача 3
        copyfile("easy5.py", "copy_easy5.py")
