# PART 1

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_list(list_in):
    for i in range(len(list_in)):
        for j in range(len(list_in[i])):
            if list_in[i][j] == 10:
                list_in[i][j] = 15
    
    return list_in

print(update_list(x))

def change_last_name(students):
    students[0]['last_name'] = "Bryant"
    return students

print(change_last_name(students))

def change_sports_directory(directory):
    directory['soccer'][0] = "Andres"
    return directory

print(change_sports_directory(sports_directory))

def change_dictionary_value(dictionary):
    dictionary[0]['y'] = 30
    return dictionary

print(change_dictionary_value(z))


# PART 2

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(input):
    for i in range(len(input)):
        output = ""
        for key in input[i]:
            output += key+" - "+input[i][key]
            if key == "first_name":
                output+= ", "
        print(output)

iterate_dictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# PART 3

def iterate_dictionary_two(key_name, some_list):
    for i in range(len(some_list)):
        for key in some_list[i]:
            if key == key_name:
                print(some_list[i][key])

iterate_dictionary_two("first_name", students)
iterate_dictionary_two("last_name", students)


# PART 4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for key in some_dict:
        length = len(some_dict[key])
        print(str(length)+" "+key)
        for item in some_dict[key]:
            print(item)
        print("")

print_info(dojo)