"""
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
        self.current_turn=0

    def is_finished(self):
        finished=self.pokemon1.current_hp<=0 or self.pokemon2.current_hp<=0
        if finished:
            print("winner")#TODO:Create winner fuction
        else:
            return finished
       
    def do_attack(self):
        self.pokemon1.current_hp=30
        self.pokemon2.current_hp=30
        print(self.is_finished())
#TODO: no entra en el bucle while no se porque

        while not  self.is_finished:
            self.pokemon1.current_hp=self.pokemon1.current_hp-10
            print(self.pokemon1.current_hp)
        print("really finish")
        print(self.pokemon1.current_hp)

class Command:
    def ask_command(self,pokemon):
        command=None
        command=input("What should "+str(pokemon.name)+" do? ").lower().split(" ")
        #and command[0]=="attack" and int(command[1])>=0 and int(command[1])<=3
        while len(command)!=2 or  command[0]!="attack" or command[1].isnumeric()!=True or int(command[1])<0 or int(command[1])>3:
            print(command[1])
            command.clear()
            command=input("What should "+str(pokemon.name)+" do? ").lower().split(" ")
        return command

    def attack_commands(self,pokemon1,pokemon2):
        command1=self.ask_command(pokemon1)
        command2=self.ask_command(pokemon2)

    def a(self):
        i=True
        while not i:
            print("Dentro")
            i=False
        print("fuera")   

"""