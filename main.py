import random
import time
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()

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
    
def who_is_attacker(hero1, hero2):
    attacker_flag = random.randint(0, 1)
    if (attacker_flag == 1):
        attacker = hero1
        defender = hero2
    elif (attacker_flag == 0):
        attacker = hero2
        defender = hero1

    return attacker, defender

def attack_hero(attacker, defender):

    critical_damage_flag = random.randint(0, 1)

    if (critical_damage_flag == 1):
        critical_damage = random.randint(20, 30) 

        if (critical_damage >= 26):
            print(f"ВОУ! Прямое попадание в головёшку игрока {defender['name']} в размере {critical_damage}")
            defender["hp"] = defender["hp"] - critical_damage
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{defender['name']}: {defender['hp']}[/]")
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{attacker['name']}: {attacker['hp']}[/]")
        elif (critical_damage <= 25):
            print(f"{defender['name']} получил леща в размере {critical_damage}")
            defender["hp"] = defender["hp"] - critical_damage
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{defender['name']}: {defender['hp']}[/]")
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{attacker['name']}: {attacker['hp']}[/]")
    if (critical_damage_flag == 0):
        print(f"\tКритического удара не случилось.")
        defender["hp"] = defender["hp"] - attacker["damage"]
        print(f"{defender['name']} ПОЛУЧИЛ УРОН В РАЗМЕРЕ: {attacker['damage']}")
        print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{defender['name']}: {defender['hp']}[/]")
        print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{attacker['name']}: {attacker['hp']}[/]")

    return

def who_lose(hero_1, hero_2):
    if (hero_1["hp"] <= 0):
        print(f"ЭТОТ БОЙ ПРОИГРАЛ {hero_1['name']}")
        exit()
    if (hero_2["hp"] <= 0):
        print(f"ЭТОТ БОЙ ПРОИГРАЛ {hero_2['name']}")
        exit()

hero_1 = create_hero()
hero_2 = create_hero()
attacker, defender = who_is_attacker(hero_1, hero_2)

print(Panel(f"ИМЯ: {attacker['name']}, ХП: {attacker['hp']}, ДАМАГ: {attacker['damage']}, УРОВЕНЬ: {attacker['level']}", title="Герой 1"))
print(Panel(f"ИМЯ: {defender['name']}, ХП: {defender['hp']}, ДАМАГ: {defender['damage']}, УРОВЕНЬ: {defender['level']}", title="Герой 2"))

while(attacker["hp"] > 0 and defender["hp"] > 0):
    print(f"\n\t[bold red]атакует:[/] [bold magenta]{attacker['name']}[/]\n\t[bold dark_orange]держит удар:[/] [bold magenta]{defender['name']}[/]\n")
    
    choise = console.input(f"[bold red]{attacker['name']}[/], [bold dark_orange]атаковать героя[/] [bold magenta]{defender['name']}?[/]\n[bold blue]Введите 'да' или 'нет' > [/]")
    if (choise.lower() == 'да'):
        print("Идёт атака...")
        time.sleep(1)
        attack_hero(attacker, defender)
        attacker, defender = who_is_attacker(hero_1, hero_2)
    elif (choise.lower() == 'выход'):
        print(f"Инициирован выход из игры.")
        exit()

who_lose(hero_1, hero_2)