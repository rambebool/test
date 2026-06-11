import random
import time
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()
import os
import subprocess

# своя логика
from models import struct_player, count_heroes, create_struct_hero, shop_items
from combat import who_is_attacker, attack_hero, tactical_back, who_lose

hero_1 = create_struct_hero()
hero_2 = create_struct_hero()
# count_heroes????????
attacker, defender = who_is_attacker(hero_1, hero_2)
subprocess.run('cls', shell=True)

print(Panel(f"ИМЯ: {attacker['name']}, ХП: {attacker['hp']}, ДАМАГ: {attacker['damage']}, УРОВЕНЬ: {attacker['level']}, ЗОЛОТО: {attacker['gold']}", title="Герой 1"))
print(Panel(f"ИМЯ: {defender['name']}, ХП: {defender['hp']}, ДАМАГ: {defender['damage']}, УРОВЕНЬ: {defender['level']}, ЗОЛОТО: {defender['gold']}", title="Герой 2"))

while(attacker["hp"] > 0 and defender["hp"] > 0):
    #print(f"\n\t[bold red]атакует:[/] [bold magenta]{attacker['name']}[/]\n\t[bold dark_orange]держит удар:[/] [bold magenta]{defender['name']}[/]\n")
    
    print(f"[bold red]{attacker['name']}[/], твоя очередь [bold dark_orange]атаковать героя[/] [bold magenta]{defender['name']}![/]")
    choise = console.input(f"[bold blue]Введите 'АТАКА' или 'НАЗАД'! [bold red](или [bold blue]'МАГАЗ'[/] для доступа в МАГАЗИН): [/]")

    if (choise.lower() == 'магаз'):
        subprocess.run('cls', shell=True)
        shop_items(attacker)


    elif (choise.lower() == 'атака'):
        print(f"\t[bold bright_cyan]Идёт атака...[/]")
        time.sleep(2)
        subprocess.run('cls', shell=True)
        attack_hero(attacker, defender)
        attacker, defender = who_is_attacker(hero_1, hero_2)

    elif(choise.lower() == 'назад'):
        print(f"[red]{attacker['name']} совершает тактическое отступление, в надежде вылечиться или найти золото...[/]")
        time.sleep(2)
        subprocess.run('cls', shell=True)
        tactical_back(attacker)

    elif (choise.lower() == 'выход'):
        subprocess.run('cls', shell=True)
        print(f"Инициирован выход из игры.")
        exit()

who_lose(hero_1, hero_2)