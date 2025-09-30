import random

#atacks
# class Bite:
#     def init(self,name,dmg):
#         base_damage = 7
#         if Bite in class with element:
#             chance to "fire", "water", "grass" + " bite"

#stats
# def Stats(self):
#     HP = 25 + self.level
#     PH_ATTK = 6 + self.level
#     EM_ATTK = 3 + self.level
#     PH_DEF = 4 + self.level
#     EM_DEF = 5 + self.level
#     SPD = 6 + self.level

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
    
    def Bite(self, PH_ATTK):
        Monsters[enemynmr]("X",2)
        
        return


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

# class Maurion:

#     def __init__(self,name,level):
#         self.name = name
#         self.level = level
#         self.HP = 30
#         self.PH_ATTK = 6
#         self.EM_ATTK = 3
#         self.PH_DEF = 3
#         self.EM_DEF = 5
#         self.SPD = 6

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

# class Enemy:

#     def __init__(self):
#       pass   

#     def enemy():
#         return


def Enemy():
    Monster_dict_number = random.randrange(1,7)
    enemy = Monsters[Monster_dict_number]
    Start_hp = enemy.HP
    accuracy = 95
   
    # while enemy.HP > 0:
    #     choice = random.randrange(0,100)
    #     if turn % 2 != 0:
    #         if enemy.HP > Start_hp// 2 
                



# print(f"{HP}\n{PH_ATTK}\n{EM_ATTK}\n{PH_ATTK}\n{PH_DEF}\n{EM_ATTK}\n{EM_DEF}\n{SPD}")
def openingmsg ():
    print(f"\nHello! Welcome to the world of Pocket-Monsters™!\nWe are very excited to welcome you into our demo aplication.\nWell lets get into it, you have 3 options of monster to choose from: ")
    print(f"Up first 'Hert'")
    print(f"Up second Hamro'")
    print(f"and last but definitly not least,'Cucombo'\n")

   
Monsters = {
    1 : Hert,
    2 : Hamro,
    3 : Cucombo,
    4 : Cannabud,
    5 : Maurion,
    6 : Ghopper,
    7: Mirmina
}

x=""
Monster_choice = ""
Monster_name = ""
while x != "Quit":
   while Monster_choice == "":
        openingmsg()
        #hier kan een while loop om te checken of er een int word meegegeven
        Monster_choice = int(input("Please enter the number op monster you would like te receive.\n: "))
        Monster_name = input(f"hm {Monsters[Monster_choice]}, huh? not what i excpected. but a good choice non the less! what would you like to name your new friend?\n:")

   playermns = Monsters[Monster_choice](Monster_name,Monster_choice)
   enemynmr = random.randrange(1,7)
   enemymnst = Monsters[enemynmr]("X",2)
   print(f"Now its time to have your first fight! we have chocen a random monster for you to battle. your opponent will be {enemymnst}!")
   







# Keuze = int(input("Choose your monster. 1: Hert, 2: Hamster"))

# x = input(" Enter your monsters name: ")
# Monster = Monsters[Keuze](x, Lvl_rand)
# print(Monster.HP)