from species import *
from player import (
    register_or_login, save_game, reset_artifacts_to_pool, give_random_artifact
)
from artifacts import *

intro = (
    "МИР ГАДКИЙ Я. МИНЬОНЫ БЬЮТСЯ СО ЗЛОДЕЯМИ!\n"
    "ОДОЛЕЙТЕ БОССА С ПОМОЩЬЮ 3 БОЙЦОВ.\n"
)


def choose_storyline(player):
    print("ВЫБЕРИТЕ СЮЖЕТ (3 ветки):")
    print("1 - Классика")
    print("2 - Диверсия")
    print("3 - Защита")
    choice = input().strip()
    player.storyline = int(choice) if choice in "123" else 1


def pre_battle(player):
    print("ПЕРЕД БОЕМ:")
    print("1 - Разведка")
    print("2 - Артефакт")
    print("3 - В бой")
    choice = input().strip()
    if choice == "1":
        hitler.damage = int(hitler.damage * 0.7)
        print("Урон босса снижен!")
    elif choice == "2":
        give_random_artifact(player)


def defense_branch(player):
    print("ЗАЩИТА БАЗЫ:")
    choice = input("1-Артефакты? (1/другое): ").strip()
    if choice == "1" and player.artifacts:
        hitler.damage = int(hitler.damage * 0.6)
        print("База укреплена артефактами!")


def game_loop(player):
    print(intro)

    if player.storyline is None:
        choose_storyline(player)

    # 3 сюжетные линии с ветвлениями
    if player.storyline == 1 or player.storyline == 2:
        pre_battle(player)
    elif player.storyline == 3:
        defense_branch(player)

    # СПИСОК МИНЬОНОВ (словарь для выбора)
    minions = {
        "1": kevin,
        "2": bob,
        "3": stuart,
        "кевин": kevin,
        "боб": bob,
        "стюарт": stuart
    }

    # ПОКАЗЫВАЕМ СОСТОЯНИЕ МИНЬОНОВ (полиморфный print_info)
    for i, minion in enumerate([kevin, bob, stuart], 1):
        print(f"{i}:")
        minion.print_info()
        print()

    # ОСНОВНОЙ БОЕВОЙ ЦИКЛ С ПОЛИМОРФИЗМОМ
    while hitler.alive():
        print(f"Босс: {hitler.hp} хп | Артефакты: {player.artifacts}")

        # ВЫБОР МИНЬОНА
        choice = input("Выберите миньона: ").lower().strip()
        if choice not in minions:
            print("Нет такого миньона!")
            continue

        minion = minions[choice]
        if not minion.zhiv():
            print(f"{minion.name} мёртв!")
            continue

        # ПОЛИМОРФНОЕ МЕНЮ АТАК (каждый класс сам знает свои атаки)
        print(f"\n{minion.name} ({minion.hp} хп):")
        menu = minion.attack_menu()
        for key, attack_name in menu.items():
            print(f"  {key} - {attack_name}")

        # ВЫБОР АТАКИ
        attack_choice = input("Атака: ").strip()

        # ПОЛИМОРФНОЕ ВЫПОЛНЕНИЕ АТАКИ (main.py НЕ ЗНАЕТ, КТО КОНКРЕТНО!)
        minion.do_attack(attack_choice, hitler)

        # ПРОВЕРКА ПОБЕДЫ
        if not hitler.alive():
            break

        # ХОД БОССА
        hitler.attacking(minion, hitler.damage)
        print(f"{minion.name}: {minion.hp} хп")

        # СОХРАНЕНИЕ (память игры)
        if input("\nСохранить? (y/n): ").lower() == "y":
            save_game(player, hitler.hp)

    print("🎉 ПОБЕДА! Босс повержен! 🎉")

    # НАГРАДА - АРТЕФАКТ
    give_random_artifact(player)

    # ПРОВЕРКА НА ВСЕ АРТЕФАКТЫ (автогенерация новых)
    if player.has_all_artifacts():
        from artifacts import generate_new_artifacts
        generate_new_artifacts()
        print("🔥 Все артефакты собраны! Сгенерированы НОВЫЕ! 🔥")

    # ФИНАЛЬНОЕ СОХРАНЕНИЕ
    if input("\nФинальное сохранение? (y/n): ").lower() != "y":
        reset_artifacts_to_pool(player)
        print("❌ ПРОГРЕСС СГОРЕЛ! Артефакты вернулись в копилку.")


if __name__ == "__main__":
    player = register_or_login()
    game_loop(player)
