# Basic
# 
for i in range(151):
    print(i)

# Multiples of Five
# 
for i in range(5, 1001, 5):
    print(i)

# Counting, the Dojo Way
# 
for i in range(101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That sucker's Huge
# 
total = 0
for i in range(500001):
    if i%2 != 0:
        total+=i
print(total)

# Counting by Fours
# 
total = 0;
for i in range(2018, 0, -4):
    total += i
print(total)

# Flexible Counter
# 
lowNum = 4
highNum = 214
mult = 3
for i in range(lowNum, highNum):
    if i%mult == 0:
        print(i)