from assets.constants import *
from assets.pokemon_models import *
import random,math,json
#---Crete pokemons---
class Set:
    def set_pokemon(self,pkm1):
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
                
                pokemon.baseStats={
                       HP: pokemon_info["Stats"]["Hp"],
                       ATTACK: pokemon_info["Stats"]["Attack"],
                       DEFENSE: pokemon_info["Stats"]["Defense"],
                       SPATTACK: pokemon_info["Stats"]["Spattack"],
                       SPDEFENSE: pokemon_info["Stats"]["Spdefense"],
                       SPEED: pokemon_info["Stats"]["Speed"]
                } 
                
                pokemon.ivs={
                    HP: random.randrange(0,31), 
                    ATTACK: random.randrange(0,31),
                    DEFENSE: random.randrange(0,31),
                    SPATTACK: random.randrange(0,31),
                    SPDEFENSE: random.randrange(0,31),
                    SPEED: random.randrange(0,31) 
                }
                
                evs=self.set_evs()
                pokemon.evs={
                    HP: int(evs[0]),
                    ATTACK: int(evs[1]),
                    DEFENSE: int(evs[2]),
                    SPATTACK: int(evs[3]),
                    SPDEFENSE: int(evs[4]),
                    SPEED: int(evs[5])  
                } 

                stats_list=self.set_stats(pokemon)
                pokemon.stats={
                       HP: stats_list[0],
                       ATTACK: stats_list[1],
                       DEFENSE: stats_list[2],
                       SPATTACK: stats_list[3],
                       SPDEFENSE: stats_list[4],
                       SPEED: stats_list[5]
                }

                pokemon.current_hp=pokemon.stats[HP]
                return pokemon
            except Exception:
                pass
#evs function
    def set_evs(self):
        answer=input("Would you like to set your Evs?(y/n)").lower()
        total=1000
        if answer=='y':
            while total>510:
                total=0
                try: 
                    hp=int(input(HP+":"))
                    attack=int(input(ATTACK+":"))
                    defense=int(input(DEFENSE+":"))
                    spattack=int(input(SPATTACK+":"))
                    spdefense=int(input(SPDEFENSE+":"))
                    speed=int(input(SPEED+":"))
                    total=hp+attack+defense+spattack+spdefense+speed
                    if total>510:
                        print("Evs can only be equal or less than 510, try it again")
                except:
                    print("Evs are numbers and they can only be equal to 510, we set a random evs for you")
                    hp=6
                    attack=252
                    defense=0
                    spattack=0
                    spdefense=0
                    speed=252
                    evs_list=[hp,attack,defense,spattack,spdefense,speed]
                    return evs_list
            
            evs_list=[hp,attack,defense,spattack,spdefense,speed]
            return evs_list
        
        elif answer=='n':      
            hp=6
            attack=252
            defense=0
            spattack=0
            spdefense=0
            speed=252
            evs_list=[hp,attack,defense,spattack,spdefense,speed]
            return evs_list

#stats function
    def set_stats(self,pokemon:Pokemon):
        hp=math.floor(0.01*(2*int(pokemon.baseStats[HP])+int(pokemon.ivs[HP])+math.floor(0.25*int(pokemon.evs[HP])))*int(pokemon.level))+ int(pokemon.level)+10
        #Añadir naturaleza en vez de un 0.1
        attack=(math.floor(0.01*(2*int(pokemon.baseStats[ATTACK])+int(pokemon.ivs[ATTACK])+math.floor(0.25*int(pokemon.evs[ATTACK])))*int(pokemon.level))+5)
        attack=math.floor(attack+(attack*0.1))
        
        defense=(math.floor(0.01*(2*int(pokemon.baseStats[DEFENSE])+int(pokemon.ivs[DEFENSE])+math.floor(0.25*int(pokemon.evs[DEFENSE])))*int(pokemon.level))+5)
        defense=math.floor(defense+(defense*0.1))
        
        spattack=(math.floor(0.01*(2*int(pokemon.baseStats[SPATTACK])+int(pokemon.ivs[SPATTACK])+math.floor(0.25*int(pokemon.evs[SPATTACK])))*int(pokemon.level))+5)
        spattack=math.floor(spattack+(spattack*0.1))
        
        spdefense=(math.floor(0.01*(2*int(pokemon.baseStats[SPDEFENSE])+int(pokemon.ivs[SPDEFENSE])+math.floor(0.25*int(pokemon.evs[SPDEFENSE])))*int(pokemon.level))+5)
        spdefense=math.floor(spdefense+(spdefense*0.1))
        
        speed=(math.floor(0.01*(2*int(pokemon.baseStats[SPEED])+int(pokemon.ivs[SPEED])+math.floor(0.25*int(pokemon.evs[SPEED])))*int(pokemon.level))+5)
        speed=math.floor(speed+(speed*0.1))

        stats=[hp,attack,defense,spattack,spdefense,speed]
        return stats