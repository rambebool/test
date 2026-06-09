import random

def struct_player(name, hp, damage, level):
    player = {
    "name": name,
    "hp": hp,
    "damage": damage,
    "level": level
}
    return player

def create_hero():
    name = input(f"Введите ИМЯ героя: ")
    level = 0
    damage = random.randint(1, 10)
    while True:
        try:
            hp = int(input(f"Введите УРОВЕНЬ ЗДОРОВЬЯ героя: "))
        except ValueError:
            print("Ввести можно только числа. Повторите попытку: ")
            continue
        player = struct_player(name, hp, damage, level)
        return player