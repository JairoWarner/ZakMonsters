import random
from tkinter.font import names


# atacks
# attacks
def Bite():
    return {"name": "Bite", "base_damage": 7}

def Roll_out():
    return {"name": "Roll_out", "base_damage": 7}

def Erupt():
    return {"name": "Erupt", "base_damage": 7}

def Photosyn():
    return {"name": "Photosyn", "base_damage": 7}

def Squirt():
    return {"name": "Squirt", "base_damage": 7}

def Blast():
    return {"name": "Blast", "base_damage": 7}

def Vine_Whip():
    return {"name": "Vine_Whip", "base_damage": 7}

def Inferno_seed():
    return {"name": "Inferno_seed", "base_damage": 7}

def Spore():
    return {"name": "Spore", "base_damage": 7}

def Bubble_mine_field():
    return {"name": "Bubble_mine_field", "base_damage": 7}

def Heat_Up():
    return {"name": "Heat_Up", "base_damage": 7}

def Poison_Plant():
    return {"name": "Poison_Plant", "base_damage": 7}

def Grass_bomb():
    return {"name": "Grass_bomb", "base_damage": 7}

def Big_bubble():
    return {"name": "Big_bubble", "base_damage": 7}

def Vlam_in_de_pan():
    return {"name": "Vlam_in_de_pan", "base_damage": 7}

def Tackle():
    return {"name": "Tackle", "base_damage": 7}

def Gwalk():
    return {"name": "Gwalk", "base_damage": 7}

def Sing():
    return {"name": "Sing", "base_damage": 7}

def Tail_Whip():
    return {"name": "Tail_Whip", "base_damage": 7}

turn = False
def Battle_loop(playermns,enemymnst,turn,x_accuracy):

    battle_hp_player = playermns.HP
    battle_hp_enemy = enemymnst.HP

    while playermns.HP> 0 and enemymnst.hp>0:

        while turn == True:
            action = input(f"Please choose an attack.\n1: Bite\n2: X\n3: Y\n4: Z\n: ")
            if action.isdigit():
                turn = False
                act_choice = int(action)
                print(f"YOU CHOSE ATTACK {act_choice}")
                Hit_chance = random.randrange(0,100)
                if Hit_chance <= x_accuracy:
                    battle_hp_enemy =- playermns.attacks[act_choice]
                    print(battle_hp_enemy)
                else:
                    print("miss")



            else: print("Please only enter a number")


        print("loop gaat door")
        turn == False

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
        return

    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

    def Attacks(self):
        return

class Hambo:

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6

    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

    def Attacks(self):
        return

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
    2 : Hambo,
    3 : Cucombo,
    4 : Cannabud,
    5 : Maurion,
    6 : Ghopper,
    7: Mirmina
}

x=""
Monster_choice = ""
Monster_name = ""
First_fight = False

for _ in range(1):
    while Monster_choice == "":
        openingmsg()
        Monster_choice = int(input("Please enter the number of monster you would like te receive.\n: "))
        Monster_name = input(f"hm {Monsters[Monster_choice]}, huh? Not what I expected. But a good choice nonetheless! What would you like to name your new friend?\n:")

        playermns = Monsters[Monster_choice](Monster_name, Monster_choice)
        enemynmr = random.randrange(1, 7)
        enemymnst = Monsters[enemynmr]("X", 2)
        attack_names = ", ".join([atk["name"] for atk in playermns.attacks])
        test = Hert.attacks


    print(f"Now it’s time to have your first fight! We have chosen a random monster for you to battle. "
          f"Your opponent will be {enemymnst}!")

    print(f"What will be youre first atack?")
    input(f"choose attack:\n{attack_names}")






# Keuze = int(input("Choose your monster. 1: Hert, 2: Hamster"))

# x = input(" Enter your monsters name: ")
# Monster = Monsters[Keuze](x, Lvl_rand)
# print(Monster.HP)