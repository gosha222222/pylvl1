# pylvl1
Geekbrains course base python lang

# Добрый день! У меня вопрос по дз 3 урока, hard, вторая часть. Я записал данные в текстовый файл и они выглядят так: 
{'name': 'dada', 'health': 100, 'damage': 0, 'armor': 1.2}
{'name': 'rere', 'health': 100, 'damage': 0, 'armor': 1.2}
#  Как считать их от туда? Я удаляю знаки и делю по строки на списки таким образом: 
def read_from(u1, u2):
    file = open('name.txt','r', encoding='utf-8')
    i = 0
    while i < 2:
        line = file.readline()
        line = line.replace("'", "")
        line = line.replace(" ", "")
        line = line.replace("{", "")
        line = line.replace("}", "")
        line = line.replace("\n", "")
        line = line.split(',')
        print(line)
        i += 1
 # И получаю на выходе 2 списка вида:
['name:dada', 'health:100', 'damage:0', 'armor:1.2']
['name:rere', 'health:100', 'damage:0', 'armor:1.2']
# Как быть дальше? Идеи вообще кончились, может быть есть способ проще? 
