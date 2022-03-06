num1 = 42 #variable declaration, initializing as data type primitive, number
num2 = 2.3 #variable declaration, initializing as  data type primitive, number
boolean = True #variable declaration, initializing as  data type primitive, boolean
string = 'Hello World' #variable declaration, initializing as data type primitive, a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initializing as a composite type, list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initializing as a composite type, dictionary of strings
fruit = ('blueberry', 'strawberry', 'banana')  #variable declaration, initializing as a composite type, tuples of strings
print(type(fruit)) #log statement of an argument in function
print(pizza_toppings[1]) #log statement to access value of a list
pizza_toppings.append('Mushrooms') #add value to a list
print(person['name']) #log statement, access value of a dictionary
person['name'] = 'George' #change value of dictionary
person['eye_color'] = 'blue' #add value of dictionary
print(fruit[2]) #function with a tuple as the argument

if num1 > 45 #conditional if statement
    print("It's greater") #log statement of a string
else: #conditional else statement
    print("It's lower") #log statement of a string

if len(string) < 5: #length check of a string using a conditional if statement 
    print("It's a short word!") #log statement of a string
elif len(string) > 15: #length check of a string using a conditional statment of else if
    print("It's a long word!") #log statement of a string
else: #conditional statement of else
    print("Just right!") #log statement of a string

for x in range(5): #for loop start at the argument
    print(x) #log statement
for x in range(2,5): # for loop start and end at the arguments
    print(x) #log statement
for x in range(2,10,3): #for loop start, increment and stop
    print(x) #log statement
x = 0 #declaration of a number variable
while(x < 5): #while loop stop at a number 
    print(x) #log statement     
    x += 1 #change value of a number variable

pizza_toppings.pop() #function
pizza_toppings.pop(1) #function to add argument of a number 

print(person) #function to access value of a dictionary
person.pop('eye_color') #delete value in a dictionary
print(person) #function to access value of a dictionary

for topping in pizza_toppings: #for loop using a list 
    if topping == 'Pepperoni': #conditional statment using a boolean to compare value
        continue #continue
    print('After 1st if statement') #function to log statement of a string
    if topping == 'Olives': #conditional statement of if using boolean
        break # break

def print_hello_ten_times(): #function
    for num in range(10): #for loop with a stop
        print('Hello') # log statment

print_hello_ten_times() #function return

def print_hello_x_times(x): #function with a parameter
    for num in range(x): #for loop with a stop  
        print('Hello') #log statement of a string

print_hello_x_times(4) #function return with provided argument

def print_hello_x_or_ten_times(x = 10): #function with a parameter
    for num in range(x): #for loop with a stop parameter
        print('Hello') #log statement

print_hello_x_or_ten_times() #function return
print_hello_x_or_ten_times(4) #function return with an argument


"""
Bonus section
"""

# print(num3)
"""- NameError: name <variable name> is not defined"""
# num3 = 72
"""No Error - variable declaration of a number"""
# fruit[0] = 'cranberry'
"""- TypeError: 'tuple' object does not support item assignment"""
# print(person['favorite_team'])
"""- KeyError: 'favorite_team'"""
# print(pizza_toppings[7])
"""- IndexError: list index out of range"""
#   print(boolean)
"""- IndentationError: unexpected indent"""
# fruit.append('raspberry')
"""- AttributeError: 'tuple' object has no attribute 'append'"""
# fruit.pop(1)
"""- AttributeError: 'tuple' object has no attribute 'append'"""