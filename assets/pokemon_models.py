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
