from assets.pokemon_models import *
from assets.battle_models import *
from assets.pokemon_and_moves import *
from assets.constants import *
from assets.interfaces import *
from assets.menu import *
import json

set=Set()
pokemon1=set.set_pokemon(True)
pokemon2=set.set_pokemon(False)
pokemon1.attacks.append(Attack("Corte",NORMAL,PHYSICAL_MOVE,10,100,10))
pokemon2.attacks.append(Attack("Corte",NORMAL,PHYSICAL_MOVE,10,100,10))
b=Battle(pokemon1,pokemon2)
commands=Command()

#---------MAIN LOOP--------------

while 1<12:
        command1=commands.ask_command(pokemon1)
        command2=commands.ask_command(pokemon2)

        b.do_attack(command1,command2)
        b.actual_status()
        if pokemon1.current_hp<=0 or pokemon2.current_hp<=0:
                b.show_winner() 
                break

"""
interface=Combat() 
def rain(battle):
        interface.do_attack(battle)

#rain(b)
print(interface)
"""