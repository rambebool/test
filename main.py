import time
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()

# своя логика
from models import struct_player, create_hero
from combat import who_is_attacker, attack_hero, who_lose

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