from assets.pokemon_models import *
from assets.battle_models import *
from assets.constants import *
from assets.interfaces import *
from assets.setter import *
from assets.turn_model import Do_attack
from assets.return_pkm_sets import *
"""
s=Save()
s.create_tables()
exit()"""

set=Set()

pokemon1:Pokemon=set.set_pokemon(True)

pokemon2:Pokemon=set.set_pokemon(False)

pokemon1.attacks.append(Attack("Corte",NORMAL,PHYSICAL_MOVE,50,100,10))
pokemon2.attacks.append(Attack("Corte",NORMAL,PHYSICAL_MOVE,50,100,10))

battle=Battle(pokemon1,pokemon2)
commands=Command()
execute_attack=Do_attack()

#---------MAIN LOOP--------------

while 1<12:
        pokemon1.current_attack_number=commands.ask_command(pokemon1)
        pokemon2.current_attack_number=commands.ask_command(pokemon2)

        execute_attack.do_damage(pokemon1,pokemon2)
        battle.actual_status()
        if pokemon1.current_hp<=0 or pokemon2.current_hp<=0:
                battle.show_winner() 
                break

"""
interface=Combat() 
def rain(battle):
        interface.do_attack(battle)

#rain(b)
print(interface)
"""