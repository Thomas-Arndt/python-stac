num1 = 42 # integer variable declaration
num2 = 2.3 # float variable declaration
boolean = True # boolean variable declaration
string = 'Hello World' # string variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary variable declaration
fruit = ('blueberry', 'strawberry', 'banana') # tuple variable declaration
print(type(fruit)) # log statement, function with argument
print(pizza_toppings[1]) # log statement, list access value
pizza_toppings.append('Mushrooms') # dictionary add value
print(person['name']) # log statement, list access value
person['name'] = 'George' # list change value
person['eye_color'] = 'blue' # list change value
print(fruit[2]) # log statement, list access value

if num1 > 45: # conditional if
    print("It's greater") log statement
else: else # conditional else
    print("It's lower") # log statement

if len(string) < 5: # conditional if, length check
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if, length check
    print("It's a long word!") # log statement
else: # conditional else
    print("Just right!") # log statement

for x in range(5): # for loop start 0, stop 4, increment 1
    print(x) # log statement
for x in range(2,5): # for loop start 2, stop 4, increment 1
    print(x) # log statement
for x in range(2,10,3): # for loop start 2, stop 9, increment 3
    print(x) # log statement
x = 0 # integer variable declaration
while(x < 5): # while loop start x=0, stop x=4, increment 1
    print(x) # log statement
    x += 1 # integer variable declaration

pizza_toppings.pop() # access and delete last value in list
pizza_toppings.pop(1) # access and delete second value in list

print(person) # log statement
person.pop('eye_color') # access and remove eye_color from dictionary
print(person) # log statement

for topping in pizza_toppings: # for loop start 0, stop 2, increment 1
    if topping == 'Pepperoni': # conditional if
        continue # for loop continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if
        break # for loop break

def print_hello_ten_times(): # define function
    for num in range(10): # for loop start 0, stop 9, increment 1
        print('Hello') # log statement

print_hello_ten_times() # call function

def print_hello_x_times(x): # define function with parameter
    for num in range(x): # for loop start 0, stop x-1, increment 1
        print('Hello') # log statement

print_hello_x_times(4) # call function with argument

def print_hello_x_or_ten_times(x = 10): # define function with argument with default value
    for num in range(x): # for loop start 0, stop 9, increment 1
        print('Hello') # log statement

print_hello_x_or_ten_times() # call function using default parameter
print_hello_x_or_ten_times(4) # call function overriding default parameter with argument


"""  Multi-line comment
Bonus section
"""  #End multi-line comment

# print(num3)	NameError: name <num3> is not defined
# num3 = 72	Variable declaration
# fruit[0] = 'cranberry'	TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])	KeyError: 'favorite_team'
# print(pizza_toppings[7])	IndexError: list index out of range
#   print(boolean)	IndentationError: unexpected indent
# fruit.append('raspberry')	AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)	AttributeError: 'tuple' object has not attribute 'pop'
