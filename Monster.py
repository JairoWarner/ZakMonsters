import sys
import os
import json

class Player:
    def __init__(self):
        self.all_attacks = None
        self.get_attacks()
        
    def get_attacks(self):
        if self.all_attacks is None:
            with open(os.path.join(sys.path[0], "attacks.json")) as attacks_file:
                self.all_attacks = json.load(attacks_file)
        return self.all_attacks

 
class Hert(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 25
        self.MaxHP = self.HP
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 11
        self.type = "grass"
 
        self.attacks = [
            self.all_attacks["SPORE"],
            self.all_attacks["photosynthesis"],
            self.all_attacks["TACKLE"],
            self.all_attacks["Sing"]
        ]    
 
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
 
   
 
 
class Hambo(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 30
        self.MaxHP = self.HP
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 7
        self.type = "water"
 
        self.attacks = [
            self.all_attacks["BITE"],
            self.all_attacks["photosynthesis"],
            self.all_attacks["TACKLE"],
            self.all_attacks["SPORE"]
        ]    
 
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
 
   
 
 
class Cannabud(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 30
        self.MaxHP = self.HP
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 6
        self.type = "water"

        self.attacks = [
            self.all_attacks["BITE"],
            self.all_attacks["photosynthesis"],
            self.all_attacks["TACKLE"],
            self.all_attacks["SPORE"]
        ]
 
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
 
 
 
 
class Cucombo(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 30
        self.MaxHP = self.HP
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 4
        self.type = "water"
 
        self.attacks = [
            self.all_attacks["BITE"],
            self.all_attacks["photosynthesis"],
            self.all_attacks["TACKLE"],
            self.all_attacks["SPORE"]
        ]
    
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
 
 
 
class Maurion(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 30
        self.MaxHP = self.HP
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 5
        self.EM_DEF = 4
        self.SPD = 7
        self.type = "water"
   
        self.attacks = [
            self.all_attacks["BITE"],
            self.all_attacks["photosynthesis"],
            self.all_attacks["TACKLE"],
            self.all_attacks["SPORE"]
        ]
   
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
 
 
 
 
class Ghopper(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 30
        self.MaxHP = self.HP
        self.PH_ATTK = 6
        self.EM_ATTK = 3
        self.PH_DEF = 5
        self.EM_DEF = 2
        self.SPD = 12
        self.type = "grass"
    
        self.attacks = [
            self.all_attacks["BITE"],
            self.all_attacks["photosynthesis"],
            self.all_attacks["TACKLE"],
            self.all_attacks["SPORE"]
        ]
 
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"
 
   
 
 
class Mirmina(Player):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.HP = 23
        self.MaxHP = self.HP
        self.PH_ATTK = 4
        self.EM_ATTK = 5
        self.PH_DEF = 3
        self.EM_DEF = 5
        self.SPD = 9
        self.type = "water"
 
        self.attacks = [
        self.all_attacks["BITE"],
        self.all_attacks["photosynthesis"],
        self.all_attacks["TACKLE"],
        self.all_attacks["SPORE"]
        ]
 
    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} (Lvl {self.level})"