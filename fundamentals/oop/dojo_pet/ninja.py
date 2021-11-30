
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(self.pet.name+" was walked...")
        self.pet.play()
        return self
    
    def feed(self):
        print(self.pet.name+" was fed "+self.pet_food+"...")
        self.pet.eat()
        return self

    def bathe(self):
        print(self.pet.name+" was bathed and it made some noise...")
        self.pet.noise()
        return self