import random
import time


class Weapon:
    def __init__(self, name="Unarmed", attack_dice=4):
        self.name=name
        self.attack_dice=attack_dice

    def damage_roll(self):
        damage = Weapon.attack_roll(self.attack_dice)
        return damage

    def __repr__(self):
        return self.name

    @staticmethod
    def attack_roll(attack_dice):
        roll = random.randint(1, attack_dice)
        return roll

class Sword(Weapon):
    def __init__(self, name="Sword", attack_dice = 8):
        super().__init__(name=name, attack_dice=attack_dice)
    

class Mace(Weapon):
    def __init__(self, name="Mace", attack_dice = 12):
        super().__init__(name=name, attack_dice=attack_dice)


# **********************************************


class Character:
    def __init__(self, name, weapon, health=40, armor=12, strength=5):
        self.name=name
        self.weapon=weapon
        self.health=health
        self.armor=armor
        self.strength=strength
    
    def info(self):
        print(f"******{self.name}******")
        print(f"Weapon: {self.weapon.name}")
        print(f"Dice Type: d{self.weapon.attack_dice}")
        print(f"Health: {self.health}")
        print(f"Armor: {self.armor}")
        return self

    def change_health(self, amount):
        self.health += amount
        return self


# **********************************************


class Battle:
    def __init__(self, p1:object, p2:object):
        self.p1=p1
        self.p2=p2

    def game_on(self, state=False):
        self.state=state
        return self

    def set_initiative(self):
        initiative = random.randint(0, 1)
        if initiative == 0:
            self.attacker = self.p1
            self.defender = self.p2
        else:
            self.attacker = self.p2
            self.defender = self.p1
        return self
    
    def swap_role(self):
        temp = self.attacker
        self.attacker = self.defender
        self.defender = temp
        return self
    
    def attack(self):
        print(f"{self.attacker.name} is on the offensive!")
        attack_roll = Battle.dice_roll(20)
        print(f"{self.attacker.name} rolled a {attack_roll}")
        if attack_roll == 1:
            print(f"Crititcal Fail! {self.attacker.name} stumbles and gives {self.defender.name} a free shot..")
            self.attacker.change_health(-self.defender.weapon.damage_roll())
        elif (attack_roll+self.attacker.strength) > self.defender.armor:
            print(f"The roll plus {self.attacker.name}'s strength was greater than {self.defender.name}'s armor of {self.defender.armor}.")
            print(f"{self.attacker.name}'s attack hits!")
            self.defender.change_health(-self.attacker.weapon.damage_roll())
        else:
            print(f"The roll plus {self.attacker.name}'s strength was less than {self.defender.name}'s armor of {self.defender.armor}.")
            print(f"{self.attacker.name}'s attack misses!")
        print("")
        return self

    def declare_winner(self):
        if self.p1.health > 0:
            winner = self.p1.name
        else:
            winner = self.p2.name
        return winner

    def start_battle(self):
        self.game_on(True)
        self.set_initiative()
        while(self.state):
            if(p1.health>0) and (p2.health>0):
                self.attack()
                time.sleep(1)
                self.swap_role()
                time.sleep(1)
            else:
                self.game_on(False)
        print(f"{self.declare_winner()} is the victor!")
        print("")
        self.p1.info()
        print("")
        self.p2.info()

    @staticmethod
    def dice_roll(dice):
        roll = random.randint(1, dice)
        return roll

weapons = [Sword(), Mace(), Weapon()]
# random_weapon = random.choice(weapons)



p1 = Character("Bob", random.choice(weapons))
p2 = Character("Joe", random.choice(weapons))

p1.info()
print("")
p2.info()
print("")
print("Battle Start!")
print("")

battle=Battle(p1, p2)
battle.start_battle()

