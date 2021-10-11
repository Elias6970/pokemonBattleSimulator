from assets.constants import SPEED
from assets.pokemon_models import Pokemon


class Command:
    def ask_command(self,pokemon):
        command=None
        command=input("What should "+str(pokemon.name)+" do? ").lower().split(" ")
        
        while len(command)!=2 or  command[0]!="attack" or command[1].isnumeric()!=True or int(command[1])<0 or int(command[1])>3:
            command.clear()
            command=input("What should "+str(pokemon.name)+" do? ").lower().split(" ")
        return command[1]

class Battle:
    def __init__(self,pokemon1:Pokemon,pokemon2:Pokemon):
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2
        self.current_turn=0

    def do_attack(self,pkm1_attack_number,pkm2_attack_number):
        self.pokemon1.current_hp=self.pokemon1.current_hp-self.pokemon2.attacks[int(pkm1_attack_number)].power
        self.pokemon2.current_hp=self.pokemon2.current_hp-self.pokemon1.attacks[int(pkm2_attack_number)].power
        
        self.current_turn=self.current_turn+1

    def actual_status(self):
        if self.pokemon1.current_hp<0:
            self.pokemon1.current_hp=0
        elif self.pokemon2.current_hp<0:
            self.pokemon2.current_hp=0
            
        print(self.pokemon1.name," has ",self.pokemon1.current_hp," HP")
        print(self.pokemon2.name," has ",self.pokemon2.current_hp," HP")
    
    def show_winner(self):
        if self.pokemon1.current_hp<=0 and self.pokemon2.current_hp>0:
            print(self.pokemon2.name+" wins the battle!!!")
        elif self.pokemon2.current_hp<=0 and self.pokemon1.current_hp>0:
            print(self.pokemon1.name+" wins the battle!!!")
        else:
            print("The winner is ")
            if self.pokemon1.stats[SPEED]>self.pokemon2.stats[SPEED]:
                print(self.pokemon1.name,"!!!")
            elif self.pokemon1.stats[SPEED]>self.pokemon2.stats[SPEED]:
                print(self.pokemon2.name,"!!!")
            else:
                print("Draw. Double KO!!!!!")
    