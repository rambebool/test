import random
from rich import print
from rich.panel import Panel

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
            print(f"[bold red][КРИТИЧЕСКИЙ УРОН][/] Прямое попадание в головёшку игроку {defender['name']} [bold red](урон: {critical_damage})[/]")
            defender["hp"] = defender["hp"] - critical_damage
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{defender['name']}: {defender['hp']}[/]")
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{attacker['name']}: {attacker['hp']}[/]")
        elif (critical_damage <= 25):
            print(f"[bold red][КРИТИЧЕСКИЙ УРОН][/] Игрок {defender['name']} получил леща! [bold red](урон: {critical_damage})[/]")
            defender["hp"] = defender["hp"] - critical_damage
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{defender['name']}: {defender['hp']}[/]")
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{attacker['name']}: {attacker['hp']}[/]")
    if (critical_damage_flag == 0):
        shield_damage_flag = random.randint(0, 1)
        if (shield_damage_flag == 0):
            print(f"[bold yellow][БЛОК][/] [bold red]{defender['name']} не смог заблокировать урон![/]")
            defender["hp"] = defender["hp"] - attacker["damage"]
            print(f"{defender['name']} ПОЛУЧИЛ УРОН В РАЗМЕРЕ: {attacker['damage']}")
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{defender['name']}: {defender['hp']}[/]")
            print(f"[green]ЗДОРОВЬЕ[/] [bold magenta]{attacker['name']}: {attacker['hp']}[/]")
        elif (shield_damage_flag == 1):
            print(f"[bold green][БЛОК] [/][bold orange3]{defender['name']} заблокировал урон в размере[/] [bold red]{attacker['damage']}![/]")
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