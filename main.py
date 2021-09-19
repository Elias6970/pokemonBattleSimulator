from assets.pokemon_models import *
from assets.battle_models import *
from assets.pokemon_and_moves import *
from assets.constants import *

import json
"""
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
"""
#---Crete pokemons---
def set_pokemon(pkm1):
        if pkm1==True:
                pokemon_name=input("Select the first pokemon: ").lower().capitalize()
        else:
                pokemon_name=input("Select the second pokemon: ").lower().capitalize()
        
        
        try:
                with open("db/pokemon.json","r") as file:
                        pokemon_db=json.load(file)
                        pokemon_info=pokemon_db[pokemon_name]
                        file.close()

                if "Type2" in pokemon_info:
                        pokemon=Pokemon(pokemon_name,pokemon_info["Type1"],pokemon_info["Type2"],100)
                else:
                        pokemon=Pokemon(pokemon_name,pokemon_info["Type1"],None,100)

                pokemon.stats={
                       HP: pokemon_info["Stats"]["Hp"],
                       ATTACK: pokemon_info["Stats"]["Attack"],
                       DEFENSE: pokemon_info["Stats"]["Defense"],
                       SPATTACK: pokemon_info["Stats"]["Spattack"],
                       SPDEFENSE: pokemon_info["Stats"]["Spdefense"],
                       SPEED: pokemon_info["Stats"]["Speed"]
                }
                pokemon.current_hp=pokemon.stats[HP]
                return pokemon
        except Exception:
                pass
        
pokemon1=set_pokemon(True)
pokemon2=set_pokemon(False)
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

