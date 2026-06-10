import os
import subprocess
import time
import random
from rich import print 
from rich.console import Console
console = Console()

def struct_player(name, hp, damage, level, gold):
    player = {
    "name": name,
    "hp": hp,
    "damage": damage,
    "level": level,
    "gold": gold
}
    return player

def create_hero():
    subprocess.run('cls', shell=True)
    name = console.input(f"[bold white]Введите[/] [bold magenta]ИМЯ[/] [bold white]героя:[/] ")
    gold = 5
    level = 0
    damage = random.randint(1, 10)
    hp = 100
    #while True:
       # try:
         #   hp = int(input(f"Введите УРОВЕНЬ ЗДОРОВЬЯ героя: "))
       # except ValueError:
           # print("Ввести можно только числа. Повторите попытку: ")
          #  continue
    player = struct_player(name, hp, damage, level, gold)
    print(f"\t[bold cyan]..персонаж[/] [bold magenta]{name}[/] [bold cyan]создаётся!\n\tЖдите...[/]")
    time.sleep(2)
    return player
    
def shop_items(hero):
    print(f"\n\n\n[bold cyan][МАГАЗИН][/] [bold white]{hero['name']}, ваш баланс:[/] [bold gold1]{hero['gold']}[/]")

    print("1. Сапог (+3 к урону) --> [gold3]5 золота[/]")
    print("2. Дубина (+5 к урону) --> [gold3]10 золота[/]")
    print("3. Перцовый баллончик (+10 к урону) --> [gold3]20 золота[/]")

    choise = console.input(f"[bold cyan][МАГАЗИН][/] [bold white]Выберите номер товара: [/]")

    match choise:
        case "1": 
            if (hero["gold"] >= 5):
                hero["gold"] -= 5
                hero["damage"] = hero["damage"] + 3
                print(f"[bold cyan][МАГАЗИН][/] [bold magenta]{hero['name']}[/], [bold whie]вы купили 'САПОГ', ваш текущий урон:[/] [bold red]{hero['damage']}[/]")
            else:
                print(f"\n\n\n\n[bold cyan][МАГАЗИН][/] [deep_pink2]Недостаточно золота[/]")
        case "2":
            if (hero["gold"] >= 10):
                hero["gold"] = hero["gold"] - 10
                hero["damage"] = hero["damage"] + 5
                print(f"[bold cyan][МАГАЗИН][/] [bold magenta]{hero['name']}[/], [bold whie]вы купили 'ДУБИНУ', ваш текущий урон:[/] [bold red]{hero['damage']}[/]")
            else:
                print(f"\n\n\n\n[bold cyan][МАГАЗИН][/] [deep_pink2]Недостаточно золота[/]")
        case "3":
            if (hero["gold"] >= 20):
                hero["gold"] = hero["gold"] - 20
                hero["damage"] = hero["damage"] + 10
                print(f"[bold cyan][МАГАЗИН][/] [bold magenta]{hero['name']}[/], [bold white]вы купили 'ПЕРЦОВЫЙ БАЛЛОНЧИК', ваш текущий урон:[/] [bold red]{hero['damage']}[/]")
            else:
                print(f"\n\n\n\n[bold cyan][МАГАЗИН][/] [deep_pink2]Недостаточно золота[/]")
        case "4":
            print(f"\n\n\n\n[bold cyan][МАГАЗИН][/] [deep_pink2]Вы вышли из магазина, ничего не купив.[/]")

        case _:
            print(f"\n\n\n\n[bold cyan][МАГАЗИН][/] [deep_pink2]Такого товара нет.. вы покинули магазин.[/]")
    return
    


# def random_items()