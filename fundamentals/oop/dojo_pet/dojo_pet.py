import ninja
import pet

ninja1 = ninja.Ninja("Thomas", "Arndt", "Scooby-Snacks", "Anything Edible", pet.Dog("Scooby-Doo", "Teeth Chattering", "Woof"))
ninja2 = ninja.Ninja("Another", "Person", "Sardines", "Ground Chicken", pet.Cat("Spots", "Purring", "Meow"))


print(ninja1.first_name+" "+ninja1.last_name+"'s pet "+ninja1.pet.name+"'s Health is "+str(ninja1.pet.health)+" and its energy is "+str(ninja1.pet.energy))
ninja1.feed().walk().bathe()
print(ninja1.first_name+" "+ninja1.last_name+"'s pet "+ninja1.pet.name+"'s Health is "+str(ninja1.pet.health)+" and its energy is "+str(ninja1.pet.energy))
print(ninja1.pet.name+" is a "+ninja1.pet.type+" with the rest of its traits inherited from the Pet class")
print(ninja2.first_name+" "+ninja2.last_name+"'s pet "+ninja2.pet.name+"'s Health is "+str(ninja2.pet.health)+" and its energy is "+str(ninja2.pet.energy))
ninja2.feed().walk().feed().bathe()
print(ninja2.first_name+" "+ninja2.last_name+"'s pet "+ninja2.pet.name+"'s Health is "+str(ninja2.pet.health)+" and its energy is "+str(ninja2.pet.energy))
print(ninja2.pet.name+" is a "+ninja2.pet.type+" with the rest of its traits inherited from the Pet class")
