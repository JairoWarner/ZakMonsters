import sys
import os
import json
 
 
def get_attacks():
     
    with open(os.path.join(sys.path[0], "attacks.json")) as attacks_file:
        return json.load(attacks_file)
  