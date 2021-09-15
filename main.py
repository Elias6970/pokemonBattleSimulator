from assets.pokemon_models import *
from assets.battle_models import *
from assets.pokemon_and_moves import *
from assets.constants import *


pokemon1=Pokemon("Bulbasaur",GRASS,POISON,8)
pokemon1.attacks.append(Attack("Arañazo",NORMAL,PHYSICAL_MOVE,10,100,10))
pokemon1.stats={
        HP:45
}

pokemon2=Pokemon("Ivysaur",GRASS,POISON,15)
pokemon2.attacks.append(Attack("Corte",NORMAL,PHYSICAL_MOVE,10,100,10))
pokemon2.stats={
        HP:60
}
pokemon1.current_hp=20
pokemon2.current_hp=20

b=Battle(pokemon1,pokemon2)
#b.av()
   

commands=Command()
#c.attack_commands(pokemon1,pokemon2)

#---------MAIN LOOP--------------

while 1<12:
        command1=commands.ask_command(pokemon1)
        command2=commands.ask_command(pokemon2)
        b.do_attack(command1,command2)
        b.actual_status()
        if pokemon1.current_hp<=0 or pokemon2.current_hp<=0:
                b.show_winner() 
                break


