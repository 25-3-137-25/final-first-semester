class Human:
    def __init__(self, name, dexterity, level, strengh, hp, iq, damage):
        self.name = name
        self.level = level
        self.strengh = strengh
        self.hp = hp
        self.dexterity = dexterity
        self.iq = iq
        self.damage = damage

    def zhiv(self):
        return self.hp > 0

    def yroven(self, someone):
        diff = someone.level - self.level
        if diff == 0:
            diff = 1
        return 60 / diff

    def print_info(self):
        print(
            f"Имя: {self.name}. Уровень: {self.level}. "
            f"Сила: {self.strengh}. ХП: {self.hp}. "
            f"Ловкость: {self.dexterity}. Интеллект: {self.iq}."
        )

    def take_damage(self, damage):
        self.hp -= damage

    # БАЗОВЫЙ ПОЛИМОРФНЫЙ ИНТЕРФЕЙС (переопределяется в дочерних)
    def attack_menu(self):
        # по умолчанию нет атак, должен быть переопределён
        return {}

    def do_attack(self, choice, target):
        # базовая реализация ничего не делает
        print("Этот персонаж не умеет атаковать так.")
class leader(Human):
    def __init__(self, name, dexterity, damage, stiffness, strengh,
                 level=19, hp=125, iq=140):
        super().__init__(name, dexterity, level, strengh, hp, iq, damage)
        self.stiffness = stiffness

    def hand(self, target):
        dmg = self.yroven(target) + (self.damage + (self.strengh * 0.2) + (self.stiffness / 50))
        target.take_damage(dmg)
        print(f"{self.name} ударил кулаком {target.name}, нанеся {dmg} урона")

    def butt(self, target):
        dmg = self.yroven(target) + (self.damage + (self.dexterity * 0.2) + (self.stiffness / 40))
        target.take_damage(dmg)
        print(f"{self.name} толкнул пятой точкой {target.name}, нанеся {dmg} урона")

    # ПОЛИМОРФНЫЕ МЕТОДЫ
    def attack_menu(self):
        return {
            "1": "Удар кулаком",
            "2": "Удар пятой точкой",
        }

    def do_attack(self, choice, target):
        if choice == "1":
            self.hand(target)
        elif choice == "2":
            self.butt(target)
        else:
            print("Такой атаки нет.")
class funny(Human):
    def __init__(self, name, idiocy, damage, dexterity,
                 level=10, strengh=1, hp=88, iq=1):
        super().__init__(name, dexterity, level, strengh, hp, iq, damage)
        self.idiocy = idiocy

    def papaya(self, target):
        dmg = self.yroven(target) + (self.damage + (self.idiocy * 0.3))
        target.take_damage(dmg)
        print(f"{self.name} накричал на {target.name}, тот получил {dmg} урона")

    def licking(self, target):
        dmg = self.yroven(target) + (self.damage + (self.idiocy * 0.1) + (self.dexterity * 0.2))
        target.take_damage(dmg)
        print(f"{self.name} вылизал {target.name}, нанеся {dmg} урона")

    def attack_menu(self):
        return {
            "1": "Крик ПАПАЙЯ",
            "2": "Вылизывание",
        }

    def do_attack(self, choice, target):
        if choice == "1":
            self.papaya(target)
        elif choice == "2":
            self.licking(target)
        else:
            print("Такой атаки нет.")
class playful(Human):
    def __init__(self, name, playfulness, damage, dexterity,
                 level=13, strengh=20, hp=100, iq=15):
        super().__init__(name, dexterity, level, strengh, hp, iq, damage)
        self.playfulness = playfulness

    def bobo(self, target):
        dmg = self.yroven(target) + (self.damage + self.playfulness * 0.6 + self.strengh * 0.1)
        target.take_damage(dmg)
        print(f"{self.name} сделал бобо {target.name}, нанеся {dmg} урона")

    def augh(self, target):
        dmg = self.yroven(target) + (self.damage + self.playfulness * 0.8)
        target.take_damage(dmg)
        print(f"{self.name} ударил {target.name}, он закричал АУЧ и получил {dmg} урона")

    def attack_menu(self):
        return {
            "1": "Сделать бобо",
            "2": "Сделать ауч",
        }

    def do_attack(self, choice, target):
        if choice == "1":
            self.bobo(target)
        elif choice == "2":
            self.augh(target)
        else:
            print("Такой атаки нет.")
