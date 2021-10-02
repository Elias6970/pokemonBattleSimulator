from assets.constants import SPEED
from assets.pokemon_models import Pokemon


class Do_attack:
    def __init__(self,pokemon1:Pokemon,pokemon2:Pokemon):
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2

    def compute_damage(self,pokemon:Pokemon,attack_number):
        attack=pokemon.attacks[int(attack_number)].power
        


    def do_damage(self,attack_number):
        #Attack order based on speed
        if int(self.pokemon1.stats[SPEED])<int(self.pokemon2.stats[SPEED]):
            self.pokemon1.current_hp=self.pokemon1.current_hp-self.compute_damage(self.pokemon2,attack_number)
            self.pokemon2.current_hp=self.pokemon2.current_hp-self.compute_damage(self.pokemon1,attack_number)
        elif int(self.pokemon1.stats[SPEED])>=int(self.pokemon2.stats[SPEED]):
            self.pokemon2.current_hp=self.pokemon2.current_hp-self.compute_damage(self.pokemon1,attack_number)
            self.pokemon1.current_hp=self.pokemon1.current_hp-self.compute_damage(self.pokemon2,attack_number)
        

