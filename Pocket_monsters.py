import random

#atacks
# class Bite:
#     def init(self,name,dmg):
#         base_damage = 7
#         if Bite in class with element:
#             chance to "fire", "water", "grass" + " bite"

#stats
def Stats(self):
    HP = 25 + self.level
    PH_ATTK = 6 + self.level
    EM_ATTK = 3 + self.level
    PH_DEF = 4 + self.level
    EM_DEF = 5 + self.level
    SPD = 6 + self.level

#monsters
class Hert:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 25
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6

class Hamro:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6

class Cannabud:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6

class Cucombo:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6

class Maurion:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6

class Ghopper:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 5
        self.EM_DEF = 2
        self.SPD = 8

class Maurion:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 5
        self.EM_DEF = 4
        self.SPD = 4

class Mirmina:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 23
        self.PH_ATTK = 4
        self.EM_ATTK = 5
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 7



# print(f"{HP}\n{PH_ATTK}\n{EM_ATTK}\n{PH_ATTK}\n{PH_DEF}\n{EM_ATTK}\n{EM_DEF}\n{SPD}")

Lvl_rand = random.randrange(1,10)
Monsters = {
    1 : Hert,
    2 : Hamro
}

#my_pok = Hert(Lvl_rand)

Keuze = int(input("Choose your monster. 1: Hert, 2: Hamster"))

x = input(" Enter your monsters name: ")
Monster = Monsters[Keuze](x, Lvl_rand)
print(Monster.HP)