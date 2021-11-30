class Pet:
    def __init__(self, name, tricks, sound, health=10, energy=10):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound+"! "+self.sound+"! "+self.sound+"!")

class Dog(Pet):
    def __init__(self, name, tricks, sound, type="dog"):
        super().__init__(name, tricks, sound)
        self.type = type

class Cat(Pet):
    def __init__(self, name, tricks, sound, type="cat"):
        super().__init__(name, tricks, sound)
        self.type = type