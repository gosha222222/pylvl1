# Задание 1.

while True:
    num = int(input("Введите число\n"))
    if num > 0 and num < 10:
        num = num * num
        print(num)
        break
    else:
        print("Число неверно! Введите число больше 0, но меньше 10")
        continue

# Задание 2.

a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
print(a, b)
a, b = b, a #swap
print(a, b)
