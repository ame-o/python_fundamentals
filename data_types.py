# print(type(24))
# print(type(3.9))
# print(type(3j))

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

# print("this is a sample string")

# name = "Zen"
# print("My name is " + name)

# print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# # total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61
# print(total)

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

#old method:
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# x = "hello world"
# print(x.title())
# # output:
# "Hello World"

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# # print(fruits_and_vegetables)
# # salad = 3 * vegetables
# # print(salad)

d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterable = d.keys()
print(iterable)