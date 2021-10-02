from abc import ABC, ABCMeta, abstractmethod


class Attack_strategy(metaclass=ABCMeta):
    @abstractmethod
    def do_attack(self,battle):
        pass
    def now_rains(self):
        pass

class Combat(Attack_strategy):
    def do_attack(self, battle):
        battle.pokemon1.current_hp=battle.pokemon1.current_hp+10
        print(battle.pokemon1.current_hp)
    
    def now_rains(self):
        return super().now_rains()

