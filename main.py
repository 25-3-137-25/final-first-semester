from species import *
from player import (
    register_or_login, save_game, reset_artifacts_to_pool, give_random_artifact
)
from artifacts import load_artifact_pool, generate_new_artifacts

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


def game_loop(player):
    print(intro)

    if player.storyline is None:
        choose_storyline(player)

    # сюжетные ветки
    if player.storyline == 1 or player.storyline == 2:
        pre_battle(player)
    else:
        print("ЗАЩИТА БАЗЫ:")
        if input("1-Артефакты? (1/другое): ").strip() == "1" and player.artifacts:
            hitler.damage = int(hitler.damage * 0.6)

    minions = {"1": kevin, "2": bob, "3": stuart, "кевин": kevin, "боб": bob, "стюарт": stuart}

    for i, m in enumerate([kevin, bob, stuart], 1):
        print(i);
        m.print_info();
        print()

    while hitler.alive():
        print(f"Босс: {hitler.hp} хп | Артефакты: {player.artifacts}")

        choice = input("Миньон: ").lower().strip()
        if choice not in minions:
            print("Нет такого!");
            continue

        minion = minions[choice]
        if not minion.zhiv():
            print("Мёртв!");
            continue

        # атаки (как в оригинале)
        if minion.name == "Кевин":
            print("1.1-Кулак 1.2-Пятая")
        elif minion.name == "Боб":
            print("2.1-Папайя 2.2-Вылизать")
        else:
            print("3.1-Бобо 3.2-Ауч")

        att = input().strip()

        if att == "1.1":
            minion.hand(hitler, minion.damage, minion.strengh, minion.stiffness)
        elif att == "1.2":
            minion.butt(hitler, minion.damage, minion.dexterity, minion.stiffness)
        elif att == "2.1":
            minion.papaya(hitler, minion.damage, minion.idiocy)
        elif att == "2.2":
            minion.licking(hitler, minion.damage, minion.idiocy, minion.dexterity)
        elif att == "3.1":
            minion.bobo(hitler, stuart.damage, stuart.playfulness, stuart.strengh)
        elif att == "3.2":
            minion.augh(hitler, minion.damage, minion.playfulness)
        else:
            print("Пропуск!"); continue

        if not hitler.alive(): break

        hitler.attacking(minion, hitler.damage)
        print(f"{minion.name}: {minion.hp} хп")

        if input("Сохранить? (y/n): ").lower() == "y":
            save_game(player, hitler.hp)

    print("ПОБЕДА!")
    give_random_artifact(player)

    if player.has_all_artifacts():
        generate_new_artifacts()
        print("НОВЫЕ АРТЕФАКТЫ!")

    if input("Финальное сохранение? (y/n): ").lower() != "y":
        reset_artifacts_to_pool(player)
        print("ПРОГРЕСС СГОРЕЛ!")


if __name__ == "__main__":
    player = register_or_login()
    game_loop(player)
