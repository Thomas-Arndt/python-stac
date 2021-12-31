import random

unsorted_list=[]
for n in range(10):
    unsorted_list.append(random.randint(0, 100))
print(unsorted_list)


# step through unordered list
# at each step, check if the number to the left is greater than the number to be sorted
# if it is, swap the two numbers, and check to the left again. 
# continue swapping until the number to the left is less than the number to be sorted

def insertion_sort(rand_list):
    for picker in range(1, len(rand_list)):
        stepper=picker
        while(stepper>0 and rand_list[stepper-1]>rand_list[stepper]):
            rand_list[stepper-1], rand_list[stepper]=rand_list[stepper], rand_list[stepper-1]
            stepper-=1
    return rand_list

print(insertion_sort(unsorted_list))