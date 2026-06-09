import random
import time

# .lower
# random.randint
# try, except
# .lower()

def struct_player(name, hp, damage, level):
    player = {
    "name": name,
    "hp": hp,
    "damage": damage,
    "level": level
}
    return player

def create_hero():
    name = input("Введите ИМЯ героя: ")
    damage = random.randint(1, 10)
    while True:
        try:
            hp = int(input("❤️\tВведите УРОВЕНЬ ЗДОРОВЬЯ героя: "))
        except ValueError:
            print("Ввести можно только числа. Повторите попытку: ")
            continue
        level = 0
        player = struct_player(name, hp, damage, level)
        return player
    
def attack_hero(hero1, hero2):
    print(f"⚔️\t^{hero1['name']}^ АТАКОВАЛ ГЕРОЯ ^{hero2['name']}^")
    count_hp = hero2["hp"] - hero1["damage"]
    total_damage = hero1["damage"]
    print(f"💥\t^{hero2['name']}^ ПОЛУЧИЛ УРОН В РАЗМЕРЕ: * {hero1['damage']} *")
    print(f"❤️\tЗДОРОВЬЕ-героя ^{hero2['name']}^: * {count_hp} *")
    return count_hp, total_damage

hero_1 = create_hero()
hero_2 = create_hero()

print("\n\t------[СПИСОК ГЕРОЕВ]------")
print(f"ИМЯ: {hero_1['name']}, ХП: {hero_1['hp']}, ДАМАГ: {hero_1['damage']}, УРОВЕНЬ: {hero_1['level']}")
print(f"ИМЯ: {hero_2['name']}, ХП: {hero_2['hp']}, ДАМАГ: {hero_2['damage']}, УРОВЕНЬ: {hero_2['level']}")
print("\t------[СПИСОК ГЕРОЕВ]------")

is_hero_1_turn = True
is_hero_2_turn = False

while (hero_1["hp"] <= 0):
    choise = input(f"Атаковать героя {hero_2['name']}?\nВведите 'да' или 'нет' > ")
    if (choise.lower() == 'да'):
        print("Идёт атака...")
        time.sleep(5)
        attack_hero(hero_1, hero_2)
    elif (choise.lower() == 'нет'):
        print(f"Вы не атаковали героя.")
        print(f"ХП героя {hero_2['name']}: {hero_2['hp']}")
    else:
        print("Выход из игры.")