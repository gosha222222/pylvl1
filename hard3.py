import random

def attack(u1, u2):
    u1["damage"] = random.randint(15, 35)
    u2["damage"] = random.randint(15, 35)
    armor(u1, u2)
    u1["health"] = u1["health"] - u2["damage"]
    u2["health"] = u2["health"] - u1["damage"]
    print(f'У игрока {u1["name"]} осталось {round(u1["health"], 2)} жизней')
    print(f'У игрока {u2["name"]} осталось {round(u2["health"], 2)} жизней\n')

def winner(u1, u2,):
    if u1["health"] > u2["health"]:
        print(f'Победил(а) {u1["name"]}, у него осталось {round(u1["health"], 2)} жизней!')
    else:
        print(f'Победил(а) {u2["name"]}, у него осталось {round(u2["health"], 2)} жизней!')

def armor(u1, u2):
    u1["damage"] = u1["damage"] / u2["armor"]
    u2["damage"] = u2["damage"] / u1["armor"]
    return u1, u2

def write_to(u1, u2):
    file = open('name.txt', 'w', encoding='utf-8')
    str1 = str(u1)
    str2 = str(u2)
    file.write(str1 + "\n" + str2)
    file.close()

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

dmg1 = 0
dmg2 = 0

name1 = input("Игрок 1, введите имя своего персонажа\n")
name2 = input("Игрок 2, введите имя своего персонажа\n")

u1 = {"name":name1, "health":100, "damage":dmg1, "armor":1.2}
u2 = {"name":name2, "health":100, "damage":dmg2, "armor":1.2}

write_to(u1, u2)
i = 0
while u1["health"] > 0 and u2["health"] > 0:
    i += 1
    attack(u1, u2)
winner(u1, u2)
read_from(u1, u2)
