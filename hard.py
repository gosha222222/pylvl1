name = input("Как вас зовут?\n")
sname = input("Введите вашу фамилию\n")
age = int(input("Введите ваш возраст\n"))
weight = int(input("Введите ваш вес в килограммах\n"))

if age < 30:
    if weight > 50 and weight < 120:
        print(name, sname, "возраст:", age, ", вес:", weight, ", вы в хорошем состоянии!")
    else:
        print(name, sname, "возраст:", age, ", вес:", weight, ", обратитесь к врачу!")

elif age >= 30 and age <= 40:
    if weight > 50 and weight < 120:
        print(name, sname, "возраст:", age, ", вес:", weight, ", вы в хорошем состоянии!")
    else:
        print(name, sname, "возраст:", age, ", вес:", weight, ", начинайте вести правильный образ жизни!")

elif age >= 40 and age <= 80:
    if weight > 50 and weight < 120:
        print(name, sname, "возраст:", age, ", вес:", weight, ", для вашего возраста все хорошо!")
    else:
        print(name, sname, "возраст:", age, ", вес:", weight, ", обратитесь к врачу!")
elif age >= 80:
    if weight > 50 and weight < 120:
        print(name, sname, "возраст:", age, ", вес:", weight, ", спасибо, что живой!")
    else:
        print(name, sname, "возраст:", age, ", вес:", weight, ", необходима срочная госпитализация!")
