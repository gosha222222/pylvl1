# Задание 1.
a = 5
b = "good"
name = input("Как вас зовут?\n")
age = int(input("Сколько вам лет?\n"))
print("Через 5 лет вам будет ", age + a , " лет")
print("Приятно познакомиться, ", name, "you ", b)

# Задание 2.
num = int(input("Введите число\n"))
a = num + 2
print(a)

# Задание 3.
ageage = int(input("Сколько вам лет?\n")) #из-за задания создал новую переменную и спросил заново
if ageage >= 18:
    print("Доступ разрешен!")
else:
    print("Извините, пользование данным ресурсом только с 18 лет!")
