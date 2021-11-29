# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)	# with a comma
print("Hello "+name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", 42)	# with a comma
print("Hello "+str(42))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

print(len(fave_food1))
print(len(fave_food2))
print(len(fave_food1+fave_food2))

print(fave_food1.upper())
print(fave_food1.count("s"))
print(fave_food2.split("i"))
print(fave_food1.islower())

zeroes = ["0", "0", "0", "0", "0"]
joinedstrings = "abc"
joinedempty = ""
print(joinedstrings.join(zeroes))
print(joinedempty.join(zeroes))