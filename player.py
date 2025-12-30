import os
import random  # ← ДОБАВИЛ ЭТОТ ИМПОРТ!
from artifacts import load_artifact_pool, save_artifact_pool, generate_new_artifacts

SAVE_FILE = "save.txt"
USERS_FILE = "users.txt"


class Player:
    def __init__(self, username, artifacts=None, storyline=None):
        self.username = username
        self.artifacts = artifacts or []
        self.storyline = storyline

    def add_artifact(self, artifact):
        if artifact not in self.artifacts:
            self.artifacts.append(artifact)

    def remove_all_artifacts(self):
        self.artifacts = []

    def has_all_artifacts(self):
        pool = load_artifact_pool()
        return sorted(self.artifacts) == sorted(pool)


def register_or_login():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    login, password = line.split(":", 1)
                    users[login.strip()] = password.strip()

    print("1 - Вход")
    print("2 - Регистрация")
    choice = input("Выберите: ").strip()

    if choice == "2":
        login = input("Логин: ").strip()
        password = input("Пароль: ").strip()
        with open(USERS_FILE, "a", encoding="utf-8") as f:
            f.write(f"{login}:{password}\n")
        print("Пользователь создан.")
        return Player(login)

    login = input("Логин: ").strip()
    password = input("Пароль: ").strip()

    if login in users and users[login] == password:
        print("Вход успешен.")
        player = load_game(login)
        if player:
            return player
        return Player(login)
    else:
        print("Ошибка входа. Новый игрок.")
        return Player(login)


def save_game(player, boss_hp):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(f"{player.username}:{player.storyline}:{boss_hp}:")
        for art in player.artifacts:
            f.write(f"{art};")
        f.write("\n")
    print("Сохранено.")


def load_game(username):
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        if not line:
            return None
        parts = line.split(":")
        if len(parts) < 4 or parts[0] != username:
            return None

        storyline = int(parts[1]) if parts[1].isdigit() else None
        boss_hp = int(parts[2])
        artifacts = parts[3].split(";") if parts[3] else []
        artifacts = [a for a in artifacts if a]

        player = Player(username, artifacts, storyline)
        print(f"Загружен прогресс: {len(artifacts)} артефактов")
        return player


def reset_artifacts_to_pool(player):
    pool = load_artifact_pool()
    for a in player.artifacts:
        if a not in pool:
            pool.append(a)
    save_artifact_pool(pool)
    player.remove_all_artifacts()


def give_random_artifact(player):
    pool = load_artifact_pool()
    candidates = [a for a in pool if a not in player.artifacts]
    if not candidates:
        print("Все артефакты собраны! Генерируем новые...")
        new_pool = generate_new_artifacts()
        player.remove_all_artifacts()
        artifact = new_pool[0]
        player.add_artifact(artifact)
        print(f"Новый артефакт: {artifact}")
        return
    artifact = random.choice(candidates)  # ← теперь random определён
    player.add_artifact(artifact)
    print(f"Найден артефакт: {artifact}")
