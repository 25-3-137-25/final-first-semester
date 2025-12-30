from party import *

class Boss:
    def __init__(self, name, level, hp, damage):
        self.name = name
        self.level = level
        self.hp = hp
        self.damage = damage

    def take_damage(self, damage):
        self.hp -= damage


class vrag(Boss):
    def __init__(self, name, hp, level, damage = 50):
        super().__init__(name, level, hp, damage)

    def attacking(self, cel, damage):
        if 210 <= self.hp <= 310:
            cel.take_damage((damage*2))
            print("Гитлер находится в ПЕРВОЙ ФАЗЕ")
            print(f"Персонаж {cel.name} отхватил по бошке от босса по имени {self.name} и получил {(damage*2)} урона")
        elif 109 <= self.hp <= 209:
            cel.take_damage((damage * 1.5))
            print("Гитлер находится во ВТОРОЙ ФАЗЕ")
            print(f"Персонаж {cel.name} отхватил по бошке от босса по имени {self.name} и получил {(damage * 1.5)} урона")
        elif self.hp < 108:
            cel.take_damage((damage * 1))
            print("Гитлер находится в ТРЕТЬЕЙ ФАЗЕ")
            print(f"Персонаж {cel.name} отхватил по бошке от босса по имени {self.name} и получил {(damage * 1)} урона")

    def alive(self):
        if self.hp > 0:
            return 1
        else:
            return 0