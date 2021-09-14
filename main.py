from assets.models import *
from assets.pokemon_and_moves import *
from assets.constants import *


pokemon1=Pokemon("Bulbasaur","Grass",None,8)
pokemon1.attacks.append(Attack("Arañazo",NORMAL,PHYSICAL_MOVE,20,100,10))
pokemon1.stats={
        HP:45
}
pokemon1.current_hp=20
pokemon2=Pokemon("Ivysaur","Grass",None,15)
pokemon2.attacks.append(Attack("Corte",NORMAL,PHYSICAL_MOVE,10,100,10))
pokemon2.stats={
        HP:60
}
pokemon2.current_hp=20

"""
b=Battle(pokemon1,pokemon2)
print(b.is_finished())
print("d")
"""
pokemon3=Pokemon("Juan",FIRE,WATER,100)
pokemon3.current_hp=20
