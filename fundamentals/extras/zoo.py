class Animal:
    def __init__(self, name, age, health=10, happiness=10, species=None):
        self.name=name
        self.age=age
        self.health=health
        self.happiness=happiness
        self.species=species
    
    def display_info(self):
        print("*"*13, self.name, "*"*13)
        print("Species: ", self.species)
        print("Health: ", self.health)
        print("Happiness: ", self.happiness)
        return self
    
    def feed(self):
        self.health+=10
        self.happiness+=10
        return self


class Lion(Animal):
    def __init__(self, name, age, is_alpha=False, health=15, happiness=8, species="Lion"):
        super().__init__(name, age, health, happiness, species)
        self.is_alpha=is_alpha
    
    def display_info(self):
        print("*"*13, self.name, "*"*13)
        print("Species: ", self.species)
        print("Health: ", self.health)
        print("Happiness: ", self.happiness)
        print("Alpha: ", self.is_alpha)
        return self

class Tiger(Animal):
    def __init__(self, name, age, health=12, happiness=12, species="Tiger"):
        super().__init__(name, age, health, happiness, species)

class Bear(Animal):
    def __init__(self, name, age, health=15, happiness=6, species="Bear"):
        super().__init__(name, age, health, happiness, species)


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]

    def add_lion(self, name, age, is_alpha=False):
        self.animals.append( Lion(name, age, is_alpha) )
        return self
    
    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age) )
        return self
    
    def add_bear(self, name, age):
        self.animals.append( Bear(name, age) )
        return self
    
    def display_all_info(self):
        for animal in self.animals:
            animal.display_info()
        return self
    
zoo1=Zoo("My Zoo")
zoo1.add_lion("Mufasa", 17, is_alpha=True).add_lion("Simba", 2).add_tiger("Tigger", 2).add_bear("Baloo", 8).display_all_info()