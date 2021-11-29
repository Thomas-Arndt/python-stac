# Countdown

def countdown(num):
    for i in range(num, 0, -1):
        print(i)

countdown(10)


# Print and Return

def print_and_return(list):
    print("The printed value is: "+str(list[0]))
    return list[1]

second = print_and_return([1,2])
print("The returned value is: "+str(second))

# First Plus Length

def first_plus_length(list):
    total = list[0] + len(list)
    return total

print("The returned value is: "+ str(first_plus_length([1,2,3,4,5])))

# Values Greater Than the Second

def values_greater_than_the_second(list):
    new_list = []
    count = 0
    if len(list) < 2:
        return False
    else:
        for i in range(len(list)):
            if list[i] > list[1]:
                new_list.append(list[i])
                count+=1
        print(count)
        return new_list

print(values_greater_than_the_second([5,2,3,2,1,4]))
print(values_greater_than_the_second([3]))

# This Length, That Value

def this_length_that_value(size, value):
    arr = []
    for i in range(size):
        arr.append(value)
    return arr

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))