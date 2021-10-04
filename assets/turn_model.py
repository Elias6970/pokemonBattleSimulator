from assets.constants import ATTACK, SPATTACK, SPEED
from assets.pokemon_models import Pokemon


class Do_attack:
    def __init__(self,pokemon1:Pokemon,pokemon2:Pokemon):
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2

    def compute_damage(self,pokemonAttacker:Pokemon,pokemonDefender:Pokemon,attack_number):
        attackPower=pokemonAttacker.attacks[int(attack_number)].power
        if pokemonAttacker.attacks[int(attack_number)].category=="Physical":
            attackStat=pokemonAttacker.stats[ATTACK]
        elif pokemonAttacker.attacks[int(attack_number)].category=="Special":
            attackStat=pokemonAttacker.stats[SPATTACK]


    def do_damage(self,attack_number):
        #Attack order based on speed
        if int(self.pokemon1.stats[SPEED])<int(self.pokemon2.stats[SPEED]):
            self.pokemon1.current_hp=self.pokemon1.current_hp-self.compute_damage(self.pokemon2,attack_number)
            self.pokemon2.current_hp=self.pokemon2.current_hp-self.compute_damage(self.pokemon1,attack_number)
        elif int(self.pokemon1.stats[SPEED])>=int(self.pokemon2.stats[SPEED]):
            self.pokemon2.current_hp=self.pokemon2.current_hp-self.compute_damage(self.pokemon1,attack_number)
            self.pokemon1.current_hp=self.pokemon1.current_hp-self.compute_damage(self.pokemon2,attack_number)
        

