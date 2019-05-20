import os
import sys
import easy5

print("Что вы хотите сделать?")
print("1. Перейти в папку")
print("2. Просмотреть содержимое текущей папки")
print("3. Удалить папку")
print("4. Создать папку")
print("5. Выйти из программы")

## TODO: Пофиксить костыль с res = 0
res = 0

while True:
    try:
        res = int(input("Введите цифру выбранного действия:\n"))
    except ValueError:
        pass

    if res == 1:
        easy5.my_chdir()
        res = 0
    elif res == 2:
        easy5.my_listdir()
        res = 0
    elif res == 3:
        easy5.my_deldir()
        res = 0
    elif res == 4:
        easy5.my_crdir()
        res = 0
    elif res == 5:
        print("Пока-пока!")
        res = 0
        break
    else:
        print("Такой команды не существует! Введите цифру от 1 до 5\n")
        res = 0
