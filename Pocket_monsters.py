import random
from Monster import *



class Game:
    def __init__(self):
        self.Monsters = {
            1: Hert,
            2: Hambo,
            3: Cucombo,
            4: Cannabud,
            5: Maurion,
            6: Ghopper,
            7: Mirmina
        }
    
 
    def Battle_loop(self,playermns, enemymnst, turn, x_accuracy):
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
    
                    acc_player_attack = chosen_attack.get("accuracy")
                    ran_num = random.randrange(0, 100)
                    if ran_num >= acc_player_attack:
                        print("you missed")
                        turn = False
                        continue
    
                    if chosen_attack.get("type") == "heal":
                        battle_hp_player += chosen_attack["base_healing"]
    
                        if battle_hp_player > playermns.MaxHP:
                            battle_hp_player = playermns.MaxHP
    
                        print(f"You healed! Your HP is now {battle_hp_player}")
    
                    elif chosen_attack.get("type") == "sleep":
                        enemy_sleep_turns = random.randint(1, 3)
                        print(f"The enemy fell asleep for {enemy_sleep_turns} turns!")
    
                    else:
                        damage = chosen_attack["base_damage"]
    
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
                    if battle_hp_enemy > enemymnst.MaxHP:
                            battle_hp_enemy = enemymnst.MaxHP
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
    
        if battle_hp_player <= 0:
            print("You lost the battle!")
        elif battle_hp_enemy <= 0:
            print("You won the battle!")
    
    def Enemy(self):
        Monster_dict_number = random.randrange(1, 7)
        enemy = self.Monsters[Monster_dict_number]
        # Start_hp = enemy.HP
        # accuracy = 95
    
    def openingmsg(self):
        print(f"\nHello! Welcome to the world of Pocket-Monsters™!\nWe are very excited to welcome you into our demo aplication.\nWell lets get into it, you have 3 options of monster to choose from: ")
        print(f"1. 'Hert'")
        print(f"2. 'Hambo'")
        print(f"3. 'Cucombo'\n")

    def run(self):
        
        x = ""
        Monster_choice = ""
        Monster_name = ""
        First_fight = False
        
        while Monster_choice == "":
            self.openingmsg()
            Monster_choice = int(input("Please enter the number of the monster you would like te receive.\n: "))
            Monster_class = self.Monsters[Monster_choice]
            Monster_name = input(f"hmmm interesting, you chose {Monster_class.__name__}, huh? Not what I expected. But a good choice nonetheless! What would you like to name your new friend?\n:")
            playermns = Monster_class(Monster_name, Monster_choice)
            enemynmr = random.randrange(1, 7)
            enemy_class = self.Monsters[enemynmr]
            enemymnst = enemy_class(f"{enemy_class.__name__}", 2)
            print(f"Now it’s time to have your first fight! We have chosen a random monster for you to battle. Your opponent will be {enemymnst.name}!")
        self.Battle_loop(playermns, enemymnst, True, x)

if __name__ == "__main__":
    game = Game()
    game.run()

 