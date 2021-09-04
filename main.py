"""Текстовая игра про героя и чудовищ."""
import sys
from random import randint, choice

monster_counter = 0
hp = randint(10, 20)
attack = randint(10, 20)


def validate_input(a: str) -> str:
    """Проверяет введенное пользователем число."""
    while a != "1" and a != "2":
        a = input("А может быть все-таки введем 1 или 2? _")
    return a


def battle() -> None:
    """Сражение с монстром."""
    global hp
    global monster_counter
    monster_hp = randint(10, 20)
    monster_attack = randint(1, 5)
    print(
        f"БОЙ! Вы встретили чудовище с {monster_hp} жизнями и с силой удара {monster_attack}"
    )
    n = input("Ваш выбор: 1-атаковать чудовище, 2-убежать _")
    n = validate_input(n)
    if n == "2":
        return
    hp -= monster_attack
    if hp > 0:
        if attack > monster_hp:
            monster_counter += 1
            print(f"Монстр сражен! У вас осталось {hp} жизней")
        else:
            print(f"Монстр вас покусал и сбежал! У вас осталось {hp} жизней")
        return
    else:
        return


def food() -> None:
    """Увеличение жизни с помощью пищи."""
    apple_hp = randint(5, 10)
    print("ЯБЛОЧКО! Время подкрепиться")
    global hp
    hp += apple_hp
    print(
        f"Вы увеличили количество ваших жизней на {apple_hp} и теперь у вас {hp} жизней"
    )
    return


def weapon() -> None:
    """Возможность поменять оружие."""
    sword_attack = randint(10, 20)
    print(f"MEЧ! Вам выпало оружие с силой атаки {sword_attack}")
    n = input("Ваш выбор: 1 - поменять меч, 2 - оставить прежний _")
    n = validate_input(n)
    if n == "2":
        return
    global attack
    attack = sword_attack
    return


def game() -> None:
    """Игра с тремя событиями."""
    events = ["monster", "apple", "sword"]
    print(f"Вы - рыцарь с количеством жизней {hp}, атака меча {attack}")
    while monster_counter < 10 and hp > 0:
        x = choice(events)
        if "monster" in x:
            battle()
        elif "apple" in x:
            food()
        elif "sword" in x:
            weapon()
    if hp <= 0:
        print("ПОРАЖЕНИЕ! Вы убиты, Игра окончена")
    if monster_counter == 10:
        print("ПОБЕДА! Вы сразили 10 монстров")
    sys.exit()
