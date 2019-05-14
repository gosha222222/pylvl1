# Функция 1
def my_person(name, age, city):
    name = name.title()
    result = f'{name}, {age} год(а), проживает в городе {city}'
    return result

# Функция 2
def my_maxnum(a, b, c):
    i = a
    if i < b:
        i = b
    if i < c:
        i = c
    return i

# Функция 2 другое решение, сначала не додумался
# def my_maxnum(a, b, c):
#     return max(a, b, c)

# Функция 3 - попробовал решить так просто, был уверен, что оно не сработает, но оно сработало
def my_max_strlen(*args):
    result = max(args, key = len)
    return result


answer = my_person("Василий", 21, "Москва")
print (answer)
maxnum = my_maxnum(344, 12, -453)
print(maxnum)
maxstrlen = my_max_strlen("Коля", "Петр", "Владимир", "Ян", "Иннокентий")
print (maxstrlen)
