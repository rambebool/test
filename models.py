import random
from rich import print

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
    name = input(f"Введите ИМЯ героя: ")
    gold = 5
    level = 0
    damage = random.randint(1, 10)
    while True:
        try:
            hp = int(input(f"Введите УРОВЕНЬ ЗДОРОВЬЯ героя: "))
        except ValueError:
            print("Ввести можно только числа. Повторите попытку: ")
            continue
        player = struct_player(name, hp, damage, level, gold)
        return player
    
def shop_items(hero):
    print("1. Сапог (+3 к урону) --> [gold]5 золота[/]")
    print("2. Дубина (+5 к урону) --> [gold]10 золота[/]")
    print("3. Перцовый баллончик (+10 к урону) --> [gold]20 золота[/]")

    choise = input("Выберите номер товара: ")

    match choise:
        case "1": 
            if (hero["gold"] >= 5):
                hero["gold"] -= 5
                hero["damage"] = hero["damage"] + 3
                print(f"[bold white]Вы купили 'САПОГ', ваш текущий урон:[/] [bold red]{hero['damage']}[/]")
            else:
                print(f"Недостаточно золота")
        case "2":
            if (hero["gold"] >= 10):
                hero["gold"] = hero["gold"] - 10
                hero["damage"] = hero["damage"] + 5
                print(f"[bold white]Вы купили 'ДУБИНУ', ваш текущий урон:[/] [bold red]{hero['damage']}[/]")
            else:
                print(f"Недостаточно золота")
        case "3":
            if (hero["gold"] >= 20):
                hero["gold"] = hero["gold"] - 20
                hero["damage"] = hero["damage"] + 10
                print(f"[bold white]Вы купили 'ПЕРЦОВЫЙ БАЛЛОНЧИК', ваш текущий урон:[/] [bold red]{hero['damage']}[/]")
            else:
                print(f"Недостаточно золота")
        case "4":
            print(f"Вы вышли из магазина, ничего не купив.")

        case _:
            print(f"Такого товара нет.. вы покинули магазин.")
    return
    


# def random_items()