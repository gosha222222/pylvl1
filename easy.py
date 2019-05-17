# Генератор 1
massfull = [1, 4, 3, 2, 5, 10]
result_1 = [num * num for num in massfull]
print(result_1)

# Генератор 2
fruits = ['апельсин', 'яблоко', 'киви', 'банан']
another_fruits = ['арбуз', 'киви', 'апельсин', 'маракуйя']
sorted_fruits = list (set (fruits) & set (another_fruits))
print(sorted_fruits)

# Генератор 3
list_1 = [0, 1, 5, 9, 243, -23, -1, -2, 5, 14, 6, 8, 20, 10, 100]
list_2 = [i for i in list_1 if i % 3 == 0 and i >=0 and i % 4 !=0]
print(list_2)

# Понял как делать нормал, банально не успеваю из за долгов и
# основной учебы в универе, к следующему уроку досдам.
