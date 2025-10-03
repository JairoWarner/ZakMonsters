import random

def Bite():
    return {"name": "Bite", "base_damage": 7}

def Roll_out():
    return {"name": "Roll_out", "base_damage": 9}

def Erupt():
    return {"name": "Erupt", "base_damage": 11}

def Photosyn():
    return {"name": "Photosyn", "type": "heal", "base_healing": 7}

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

def Battle_loop(playermns, enemymnst, turn, x_accuracy):
    battle_hp_player = playermns.HP
    battle_hp_enemy = enemymnst.HP
    while battle_hp_player > 0 and battle_hp_enemy > 0:
        if turn:
            action = input("Choose your attack:")
            if action.isdigit():
                act_choice = int(action)
                print(f"YOU CHOSE ATTACK {act_choice}")
                print(f"Enemy HP before attack: {battle_hp_enemy}")

                if playermns.attacks[act_choice].get("type") == "heal":
                    battle_hp_player += playermns.attacks[act_choice]["base_healing"]
                    print(f"You healed! Your HP is now {battle_hp_player}")
                else:
                    battle_hp_enemy -= playermns.attacks[act_choice]["base_damage"]
                    print(f"Enemy HP after attack: {battle_hp_enemy}")
            else:
                print("Please only enter a number")
            turn = False
        else:
            enemy_attack = random.choice(enemymnst.attacks)
            if enemy_attack.get("type") == "heal":
                battle_hp_enemy += enemy_attack["base_healing"]
                print(f"Enemy uses {enemy_attack['name']} and heals {enemy_attack['base_healing']} HP!")
                print(f"Enemy HP is now {battle_hp_enemy}")
            else:
                damage = enemy_attack["base_damage"]
                print(f"Enemy uses {enemy_attack['name']} and deals {damage} damage!")
                battle_hp_player -= damage
                print(f"Your HP after enemy attack: {battle_hp_player}")
            turn = True

    if battle_hp_player <= 0:
        print("You lost the battle!")
    elif battle_hp_enemy <= 0:
        print("You won the battle!")


class Hert:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 25
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

class Hambo:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

class Cannabud:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

class Cucombo:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

class Maurion:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 5
        self.EM_DEF = 4
        self.SPD = 4
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

class Ghopper:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 5
        self.EM_DEF = 2
        self.SPD = 8
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

class Mirmina:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 23
        self.PH_ATTK = 4
        self.EM_ATTK = 5
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 7
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Bite(), Photosyn(), Tackle(), Spore()]

def Enemy():
    Monster_dict_number = random.randrange(1, 7)
    enemy = Monsters[Monster_dict_number]
    Start_hp = enemy.HP
    accuracy = 95

def openingmsg():
    print(f"\nHello! Welcome to the world of Pocket-Monsters™!\nWe are very excited to welcome you into our demo aplication.\nWell lets get into it, you have 3 options of monster to choose from: ")
    print(f"1. 'Hert'")
    print(f"2. 'Hamro'")
    print(f"3. 'Cucombo'\n")

Monsters = {
    1: Hert,
    2: Hambo,
    3: Cucombo,
    4: Cannabud,
    5: Maurion,
    6: Ghopper,
    7: Mirmina
}

x = ""
Monster_choice = ""
Monster_name = ""
First_fight = False

for _ in range(1):
    while Monster_choice == "":
        openingmsg()
        Monster_choice = int(input("Please enter the number of the monster you would like te receive.\n: "))
        Monster_class = Monsters[Monster_choice]
        Monster_name = input(f"hmmm interesting, you chose {Monster_class.__name__}, huh? Not what I expected. But a good choice nonetheless! What would you like to name your new friend?\n:")
        playermns = Monster_class(Monster_name, Monster_choice)
        enemynmr = random.randrange(1, 7)
        enemy_class = Monsters[enemynmr]
        enemymnst = enemy_class(f"{enemy_class.__name__}", 2)
        print(f"Now it’s time to have your first fight! We have chosen a random monster for you to battle. Your opponent will be {enemymnst.name}!")
    Battle_loop(playermns, enemymnst, True, x)
