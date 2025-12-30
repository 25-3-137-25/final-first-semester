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
        if self.hp > 0:
            return 1
        else:
            return 0


    def yroven(self, someone):
        return ( 60 / (someone.level - self.level))

    def print_info(self):
        print('Имя: {}. Уровень: {}. Сила: {}. ХП: {}. Ловкость: {}. Интеллект: {}.'.format(self.name, self.level, self.strengh, self.hp, self.dexterity, self.iq))

    def take_damage(self, damage):
        self.hp -= damage



class leader(Human):
    def __init__(self, name, dexterity, damage, stiffness, strengh, level = 19, hp = 125, iq = 140):
        super().__init__(name, dexterity, level, strengh, hp, iq, damage)
        self.stiffness = stiffness


    def hand(self, target, damage, strengh, stiffness):
        target.take_damage(self.yroven(target) + (damage + (strengh*0.2) + (stiffness/50)))
        print(f"Персонаж {self.name} ударил кулаком персонажа {target.name}, нанеся {self.yroven(target) + (damage + (strengh*0.2) + (stiffness/50))} урона")

    def butt(self, target, damage, dexterity, stiffness):
        target.take_damage(self.yroven(target) + (damage + (dexterity*0.2) + (stiffness/40)))
        print(f"Персонаж {self.name} толкнул своей пятой точкой персонажа {target.name}, нанеся {self.yroven(target) + (damage + (dexterity*0.2))} урона")



class funny(Human):
    def __init__(self, name, idiocy, damage, dexterity, level = 10, strengh = 1, hp = 88, iq = 1):
        super().__init__(name, level, strengh, hp, dexterity, iq, damage)
        self.idiocy = idiocy


    def papaya(self, target, damage, idiocy):
        target.take_damage(self.yroven(target) + (damage + (idiocy*0.3)))
        print(f"Персонаж {self.name} настолько сильно накричал на персонажа {target.name}, что тот даже получил {self.yroven(target) + (damage + (idiocy*0.3))} урона")

    def licking(self, target, damage, idiocy, dexterity):
        target.take_damage(self.yroven(target) + (damage + (idiocy*0.1) + (dexterity*0.2)))
        print(f"Персонаж {self.name}, достал свой шершавый залежалый язык, вылизал им персонажа {target.name}, тем самым нанёс {self.yroven(target) + (damage + (idiocy*0.1) + (dexterity*0.2))} урона")



class playful(Human):
    def __init__(self, name, playfulness, damage, dexterity, level = 13, strengh = 20, hp = 100, iq = 15):
        super().__init__(name, level, strengh, hp, dexterity, iq, damage)
        self.playfulness = playfulness


    def bobo(self, target, damage, playfulness, strengh):
        target.take_damage(self.yroven(target) + (damage + playfulness*0.6 + strengh*0.1))
        print(f"Персонажу {target.name} сделал бобо {self.name}, нанеся {self.yroven(target) + (damage + playfulness*0.6 + strengh*0.1)} урона")

    def augh(self, target, damage, playfulness):
        target.take_damage(self.yroven(target) + (damage + playfulness*0.8))
        print(f"Персонаж {target.name} закричал АУЧ после удара {self.name}, получив {self.yroven(target) + (damage + playfulness*0.8)} урона")

