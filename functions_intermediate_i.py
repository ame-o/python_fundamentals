#1. Update Values in Dictionaries and Lists
#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
from curses import KEY_SELECT


x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
#2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
def iterateDictionary(some_list):
    for i in some_list:
        print(i)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

#3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students)
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
            for dictionary in some_list[i]:
                for key_name in dictionary:
                    print(value in key_name)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(iterateDictionary2('first_name', students))