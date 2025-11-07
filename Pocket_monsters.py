import random

def Bite():
    return {"name": "Bite", "base_damage": 7}

def Roll_out():
    return {"name": "Roll_out", "base_damage": 9}

def Erupt():
    return {"name": "Erupt", "element": "fire", "base_damage": 11}

def Photosyn():
    return {"name": "Photosyn", "type": "heal", "base_healing": 7}

def Squirt():
    return {"name": "Squirt", "element": "water", "base_damage": 7}

def Blast():
    return {"name": "Blast", "element": "fire", "base_damage": 7}

def Vine_Whip():
    return {"name": "Vine_Whip", "element": "grass", "base_damage": 7}

def Inferno_seed():
    return {"name": "Inferno_seed", "element": "fire", "base_damage": 7}

def Spore():
    return {"name": "Spore", "element": "grass", "base_damage": 7}

def Bubble_mine_field():
    return {"name": "Bubble_mine_field", "element": "water", "base_damage": 7}

def Heat_Up():
    return {"name": "Heat_Up", "element": "fire", "base_damage": 7}

def Poison_Plant():
    return {"name": "Poison_Plant", "element": "grass", "base_damage": 7}

def Grass_bomb():
    return {"name": "Grass_bomb", "element": "grass", "base_damage": 7}

def Big_bubble():
    return {"name": "Big_bubble", "element": "water", "base_damage": 7}

def Vlam_in_de_pan():
    return {"name": "Vlam_in_de_pan", "element": "fire", "base_damage": 7}

def Tackle():
    return {"name": "Tackle", "base_damage": 7}

def Gwalk():
    return {"name": "Gwalk", "element": "grass", "base_damage": 7}

def Sing():
    return {"name": "Sing", "type": "sleep", "status_effect": "sleep"}

def Tail_Whip():
    return {"name": "Tail_Whip", "base_damage": 7}

turn = False

def Battle_loop(playermns, enemymnst, turn, x_accuracy):
    battle_hp_player = playermns.HP
    battle_hp_enemy = enemymnst.HP
    battle_speed_player = playermns.SPD
    battle_speed_enemy = enemymnst.SPD

    enemy_sleep_turns = 0

    if battle_speed_player > battle_speed_enemy:
        turn = True
    elif battle_speed_enemy > battle_speed_player:
        turn = False
    else:
        turn = random.choice([True, False])

    while battle_hp_player > 0 and battle_hp_enemy > 0:
        if turn:
            print("\nYour attacks:")
            for i, attack in enumerate(playermns.attacks):
                print(f"{i}: {attack['name']}")

            action = input("\nChoose your attack:")

            if action.isdigit():
                act_choice = int(action)
                if act_choice < 0 or act_choice >= len(playermns.attacks):
                    print("Invalid choice, try again.")
                    continue

                chosen_attack = playermns.attacks[act_choice]
                print(f"YOU CHOSE ATTACK {chosen_attack['name']}")

                if chosen_attack.get("type") == "heal":
                    battle_hp_player += chosen_attack["base_healing"]
                    print(f"You healed! Your HP is now {battle_hp_player}")

                elif chosen_attack.get("type") == "sleep":
                    enemy_sleep_turns = random.randint(1, 3)
                    print(f"The enemy fell asleep for {enemy_sleep_turns} turns!")

                else:
                    # Default damage
                    damage = chosen_attack["base_damage"]

                    # Type effectiveness system
                    if chosen_attack.get("element") == "grass" and enemymnst.type == "water":
                        damage *= 2
                        print("It's super effective!")
                    elif chosen_attack.get("element") == "fire" and enemymnst.type == "grass":
                        damage *= 2
                        print("It's super effective!")
                    elif chosen_attack.get("element") == "water" and enemymnst.type == "fire":
                        damage *= 2
                        print("It's super effective!")
                    elif chosen_attack.get("element") == playermns.type:
                        damage /= 2
                        print("It's not very effective...")

                    print(f"Enemy HP before attack: {battle_hp_enemy}")
                    battle_hp_enemy -= damage
                    print(f"Enemy HP after attack: {battle_hp_enemy}")

            else:
                print("Please only enter a number")
            turn = False


        else:
            if enemy_sleep_turns > 0:
                print(f"The enemy is fast asleep and can't move! ({enemy_sleep_turns} turns left)")
                enemy_sleep_turns -= 1
                turn = True
                continue

            enemy_attack = random.choice(enemymnst.attacks)

            if enemy_attack.get("type") == "heal":
                battle_hp_enemy += enemy_attack["base_healing"]
                print(f"Enemy uses {enemy_attack['name']} and heals {enemy_attack['base_healing']} HP!")
                print(f"Enemy HP is now {battle_hp_enemy}")
            else:
                damage = enemy_attack["base_damage"]

                if enemy_attack.get("element") == "grass" and playermns.type == "water":
                    damage *= 2
                    print("It's super effective!")
                elif enemy_attack.get("element") == "fire" and playermns.type == "grass":
                    damage *= 2
                    print("It's super effective!")
                elif enemy_attack.get("element") == "water" and playermns.type == "fire":
                    damage *= 2
                    print("It's super effective!")
                elif enemy_attack.get("element") == enemymnst.type:
                    damage /= 2
                    print("It's not very effective...")

                print(f"Enemy uses {enemy_attack['name']} and deals {damage} damage!")
                battle_hp_player -= damage
                print(f"Your HP after enemy attack: {battle_hp_player}")

            turn = True
            input("\nPress ENTER to continue...")

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
        self.SPD = 11
        self.type = "grass"
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
    attacks = [Spore(), Photosyn(), Tackle(), Sing()]

class Hambo:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.HP = 30
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 7
        self.type = "water"
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
        self.type = "water"
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
        self.SPD = 4
        self.type = "water"
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
        self.SPD = 7
        self.type = "fire"
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
        self.SPD = 12
        self.type = "grass"
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
        self.SPD = 9
        self.type = "water"
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
    print(f"2. 'Hambo'")
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
