
class Pokemon:
    def __init__(self,name,type1,type2,level):
        self.name=name
        self.type1=type1
        self.type2=type2
        self.level=level
        self.attacks=[]
        self.stats={}
        self.current_hp=0
        self.current_status=0

class Attack:
    def __init__(self,name,attack_type,category,power,accuracity,pp):
        self.name=name
        self.attack_type=attack_type
        self.category=category
        self.power=power
        self.accuracity=accuracity
        self.pp=pp

class Battle:
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2
        self.corrent_turn=0

    def is_finished(self):
        print("a")
        self.pokemon1.current_hp=20
        self.pokemon2.current_hp=20
        return self.pokemon1.current_hp<=0 or self.pokemon2.current_hp<=0

    def do_attack(self):
        command1=None
        command2=None
        command1=input("What should "+str(self.pokemon1.name)+" do? ").lower().split(" ")
        command2=input("What should "+str(self.pokemon2.name)+" do? ").lower().split(" ")
        
        #while not (len(command1)==2 and len(command2)==2 and command1[0]=="attack" and command2=="attack"):
        while not len(command1)==2 :
            print("Wrong command!!")
            command1.clear()
            command2.clear()
            command1=input("What should "+str(self.pokemon1.name)+" do? ").lower().split(" ")
            command2=input("What should "+str(self.pokemon2.name)+" do? ").lower().split(" ")
        #print(command1)