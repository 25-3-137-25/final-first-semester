import os
import random
# весь этот файлик ответственнен за генерацию и хранение пула артефактов
ARTIFACTS_FILE = "artifacts_pool.txt"

DEFAULT_ARTIFACTS = [
    "Банановый меч",
    "Очки зла",
    "Жвачка хаоса",
    "Каска миньона",
    "Резиновая уточка",
]

def load_artifact_pool():
    # тут я беру пул артефактов и возвращаю список строк артефактов
    # если же нет файла с пулом артефактов, то я создаю его (ниже)
    if not os.path.exists(ARTIFACTS_FILE):
        save_artifact_pool(DEFAULT_ARTIFACTS)
        return DEFAULT_ARTIFACTS[:]
    with open(ARTIFACTS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_artifact_pool(pool): # просто сохранение пула артефактов в файле
    with open(ARTIFACTS_FILE, "w", encoding="utf-8") as f:
        for artifact in pool:
            f.write(artifact + "\n")

def generate_new_artifacts():
    #это уже автогенерация новых артефактов
    new_pool = [
        "Супербанан судьбы",
        "Мегаочко тьмы",
        "Камень папайи",
        "Щит Стюарта",
        "Леденец бессмертия",
    ]
    save_artifact_pool(new_pool)
    return new_pool
