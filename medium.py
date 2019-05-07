import math
import random

# Задача 1
mass = [2, -5, 8, 9, -25, 25, 4]
new = []
for x in mass:
    if x > 0:
        y = math.sqrt(x)
        if y % int(y) == 0:
            round(y)
            new.append(y)
print(new)

# Задача 2
date = '02.11.2013'
spl = date.split('.')
day = spl[0]
month = spl[1]
year = spl[2]
text = 'года'

if day == '01':
    day = 'первое'
elif day == '02':
    day = 'второе'
elif day == '03':
    day = 'третье'
elif day == '04':
    day = 'четвертое'
elif day == '05':
    day = 'пятое'
elif day == '06':
    day = 'шестое'
elif day == '07':
    day = 'седьмое'
elif day == '08':
    day = 'восьмое'
elif day == '09':
    day = 'девятое'
elif day == '10':
    day = 'десятое'
elif day == '11':
    day = 'одиннадцатое'
elif day == '12':
    day = 'двенадцатое'
elif day == '13':
    day = 'тринадцатое'
elif day == '14':
    day = 'четырнадцатое'
elif day == '15':
    day = 'пятнадцатое'
elif day == '16':
    day = 'шестнадцатое'
elif day == '17':
    day = 'семнадцатое'
elif day == '18':
    day = 'восемнадцатое'
elif day == '19':
    day = 'девятьнадцатое'
elif day == '20':
    day = 'дцадцатое'
elif day == '21':
    day = 'двадцать первое'
elif day == '22':
    day = 'двадцать второе'
elif day == '23':
    day = 'двадцать третье'
elif day == '24':
    day = 'двадцать чертвертое'
elif day == '25':
    day = 'двадцать пятое'
elif day == '26':
    day = 'двадцать шестое'
elif day == '27':
    day = 'двадцать седьмое'
elif day == '28':
    day = 'двадцать восьмое'
elif day == '29':
    day = 'двадцать девятое'
elif day == '30':
    day = 'тридцатое'
elif day == '31':
    day = 'тридцать первое'

day = day.title()

if month == '01':
    month = 'января'
elif month == '02':
    month = 'февраля'
elif month == '03':
    month = 'марта'
elif month == '04':
    month = 'апреля'
elif month == '05':
    month = 'мая'
elif month == '06':
    month = 'июня'
elif month == '07':
    month = 'июля'
elif month == '08':
    month = 'августа'
elif month == '09':
    month = 'сентября'
elif month == '10':
    month = 'октября'
elif month == '11':
    month = 'ноября'
elif month == '12':
    month = 'декабря'


print('{} {} {} {}'.format(day, month, year, text))

# Задача 3

d = []
n = 30
count = 0
while count < n:
    d.append(random.randint(-100, 100))
    count += 1
print(d)

# Задача 4

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst1 = set(lst)
lst1 = list(lst1)
print(lst1)

lst2 = [x for x in lst if not lst.count(x) > 1]
print(lst2)
