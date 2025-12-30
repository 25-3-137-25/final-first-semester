import os
import random

ARTIFACTS_FILE = "artifacts_pool.txt"

DEFAULT_ARTIFACTS = [
    "Банановый меч",
    "Очки зла",
    "Жвачка хаоса",
    "Каска миньона",
    "Резиновая уточка",
]

def load_artifact_pool():
    if not os.path.exists(ARTIFACTS_FILE):
        save_artifact_pool(DEFAULT_ARTIFACTS)
        return DEFAULT_ARTIFACTS[:]
    with open(ARTIFACTS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_artifact_pool(pool):
    with open(ARTIFACTS_FILE, "w", encoding="utf-8") as f:
        for artifact in pool:
            f.write(artifact + "\n")

def generate_new_artifacts():
    new_pool = [
        "Супербанан судьбы",
        "Мегаочко тьмы",
        "Камень папайи",
        "Щит Стюарта",
        "Леденец бессмертия",
    ]
    save_artifact_pool(new_pool)
    return new_pool
