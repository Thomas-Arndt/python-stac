import random

unsorted_list=[]
for n in range(10):
    unsorted_list.append(random.randint(0, 100))
print(unsorted_list)

def selection_sort(rand_list):
    for stepper in range(len(rand_list)):
        min_num=rand_list[stepper]
        min_num_index=stepper
        for searcher in range(stepper, len(rand_list)):
            if rand_list[searcher] < min_num:
                min_num=rand_list[searcher]
                min_num_index=searcher
        rand_list[stepper], rand_list[min_num_index]=rand_list[min_num_index], rand_list[stepper]
    return rand_list

print(selection_sort(unsorted_list))