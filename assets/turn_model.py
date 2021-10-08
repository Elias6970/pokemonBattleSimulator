from random import Random, random
from assets.constants import ATTACK, DEFENSE, SPATTACK, SPDEFENSE, SPEED
from assets.pokemon_models import Pokemon
import math, random

class Do_attack:
    def __init__(self):
        self.attackStat=0
        self.defenseStat=0
        self.attackPower=0
        self.attacker_pokemon_lvl=0
        self.critical_damage=1
        self.stab=1
        self.randomPerCent=1
        self.targets=1 #because always moves are going to hit only one enemy pokemon because the battles are 1vs1
   
    # targets   wether   critical   random   stab   type   burn   other
    #   yes       no        yes       yes     yes    no     no      no

    #set the base formula of the damage formula
    def setBaseDamageFormula(self,attackerPokemon:Pokemon,pokemonDefender:Pokemon):
        self.attacker_pokemon_lvl=attackerPokemon.level
        self.attackPower=attackerPokemon.attacks[int(attackerPokemon.current_attack_number)].power
        
        
        Physical=bool
        if attackerPokemon.attacks[int(attackerPokemon.current_attack_number)].category=="Physical":
            self.attackStat=attackerPokemon.stats[ATTACK]
            Physical=True
        elif attackerPokemon.attacks[int(attackerPokemon.current_attack_number)].category=="Special":
            self.attackStat=attackerPokemon.stats[SPATTACK]
            Physical=False
            
        if Physical==True:
            self.defenseStat=pokemonDefender.stats[DEFENSE]
        else:
            self.defenseStat=pokemonDefender.stats[SPDEFENSE]
    
    #set critical damage
    def setCriticalHit(self):
        random_number=random.randrange(1,24)
        if random_number==2:
            self.critical_damage=1.5
        else:
            self.critical_damage=1
    
    #set if the attack is stab or not
    def setStabAttack(self,attackerPokemon:Pokemon,defender_pokemon:Pokemon):
        if attackerPokemon.attacks[int(attackerPokemon.current_attack_number)].attack_type == attackerPokemon.type1 or attackerPokemon.attacks[int(attackerPokemon.current_attack_number)].attack_type == attackerPokemon.type2:
            self.stab=1.5
        else:
            self.stab=1

    def setRandom(self):
        self.randomPerCent=(random.randrange(85,100)/100)

    def setAll(self, attackerPokemon:Pokemon,defenderPokemon:Pokemon):
        self.setBaseDamageFormula(attackerPokemon,defenderPokemon)
        self.setCriticalHit()
        self.setStabAttack(attackerPokemon,defenderPokemon)
        self.setRandom()    
        
    #TODO: no va bien la damage formula. hay que comprobarla
    #calculate the damage formula
    def compute_damage(self):
        base_damage_caused=(((((2*self.attacker_pokemon_lvl)/5)+2)*self.attackPower*((self.attackStat/self.defenseStat)/50))+2)

        damage_caused=math.floor(base_damage_caused*self.targets*self.randomPerCent*self.stab*self.critical_damage)

        return damage_caused
    def do_damage(self, pokemon1:Pokemon,pokemon2:Pokemon):

        #Attack order based on speed
        if int(pokemon1.stats[SPEED])<int(pokemon2.stats[SPEED]):
            self.setAll(pokemon2,pokemon1)
            print(pokemon1.current_hp)
            pokemon1.current_hp=pokemon1.current_hp-self.compute_damage()

        elif int(pokemon1.stats[SPEED])>=int(pokemon2.stats[SPEED]):
            self.setAll(pokemon1,pokemon2)
            pokemon2.current_hp=pokemon2.current_hp-self.compute_damage()
