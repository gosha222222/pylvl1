# Задание 1

fruits = ['Груша', 'Киви', 'Банан', 'Яблоко', 'Абрикос', 'Апельсин']

for num, fruit in enumerate (fruits):
    print (str(num) + '.  {:>9}'.format(fruit))

# Задание 2

a = ["a", "b", "c", "d", "e", "f"]
b = ["a", "b", "e", "f"]
for let in a[:]:
    for lett in b[:]:
        if lett == let:
            a.remove(lett)
print ('{}'.format(a))

#Задание 3

a = [1, 5, 7, 4, 6, 7, 9]
b = []

for x in a:
    if x % 2 == 0:
        b.append(x / 4)
    else:
        b.append(x*2)

print(b)
