print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 21 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m Generator in Python\033[0m  ")

# What is a Generator?
# A generator in Python is a special type of iterator, allowing you to iterate over a potentially infinite sequence of items without creating the entire sequence in memory at once. It's useful when dealing with large datasets or when you want to generate values on-the-fly.

# How to create a Generator?
# You can create a generator using a function with the yield keyword. Here is a simple example.
print("\n\nExample\n")
def simple_generator():
    yield 1 
    yield 2 
    yield 3
    
# Creating a generator objects 
gen = simple_generator()

# Iterating over the generator 
for value in gen:
    print(value)
    
# This generator function 'simple_generator', yields values 1,2 and 3. when you iterate over the generator using a for loop, it will produce these values once at a time.

# Yield vs Return:
# return statement terminates the function and returns a value.
# yield statement pauses the function's state and returns a value to the caller but allows the function to resume its state when called again.
# Lazy Evaluation:
# Generators use lazy evaluation, meaning they generate values on-the-fly and only when needed. This is memory-efficient, especially when dealing with large datasets.
# Let me show you something (pic) so you can easily understang. 
# Now you know

# Example:
print("\n\nInfinte Generator: \n")
def infinite_generator():
    num = 1 
    while True:
        yield num
        num  += 1
        
    # Using the generator
gen_inf = infinite_generator()

for _ in range(5):
    print(next(gen_inf))
    
# This generator will keep yielding numbers infinitely. The next() function is used to get the next value from the generator.

# Generator Expression
print("\n\nGenerator Expression\n")

# You can also create generator using generator expression, which are similar to list comprehension but use parenthesis "()" instead of square brackets "[]".

gen_expr = (x ** 2 for x in range (5))

for value in gen_expr:
    print("x value power 2: ",value)
# This example creates a generator expression that yields the square of numbers from 0 t 4
# Generators are a powerful feature in Python for efficient and memory-friendly iteration. They are particularly useful in scenarios where you're working with large datasets or need to generate values on-the-fly.

# Lets do some basic and good example:
# example 1
print("\n\nExample 1: \n")

def function():
    for i in range(20):
        if i%2==0:
            yield i 
nlis = []
for i in function():
    nlis.append(i)
print(nlis)

# example 2
print("\n\nExample 2: \n")

def function():
    for i in range(50):
        if i%4==0:
            yield i 
nlis = []
for i in function():
    nlis.append(i)
print(nlis)

print("\n\nExmaple 3: \n")
def message():
    msg_once = 'Hello, Sadiq!'
    yield msg_once
    
    msg_two = 'Hi Python!'
    yield msg_two
    
    msg_three = 'Python is the most powerful programming language!'
    yield msg_three

result = message()
print(next(result))
print(next(result))
print(next(result))

print("\n\nExmaple 4: \n")

special_num = [0.577,1.618,2.718,3.14,6,37,1729]

list_comprehension = [i*3 for i in special_num] # This is alist comprehension
generator_exp = (i*3 for i in special_num) # This is generator expression

print(list_comprehension)
print(generator_exp)
# In this example, the list comprehension will return the list of cube of elements. whereas the generator expression will return the refernce of the calculated value.
# Rather than this application, the function next() can be used on the generator object.

# Exmaple 5
print("\n\nExample 5:\n")

special_num = [0.577,1.618,2.718,3.14,6,37,1729]

generator_exp = (i*3 for i in special_num) # This is generator expression

nums_lis = []
nums_lis.append(next(generator_exp))
nums_lis.append(next(generator_exp))
nums_lis.append(next(generator_exp))
nums_lis.append(next(generator_exp))
nums_lis.append(next(generator_exp))
nums_lis.append(next(generator_exp))
nums_lis.append(next(generator_exp))
print(nums_lis)

# Example 6

print("\n\nExample 6\n")
def mult_table(n):
    for i in range(0,11):
        yield n*i
        i+=1
        
mult_table_list = []
for i in mult_table(20):
    mult_table_list.append(i)
print(mult_table_list)

# Exmple 7
print("\n\nExample 7\n")
def generator(a):
    for i in range(a):
        yield i
        
gen = generator(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) # After 6 StopIteration  

# Example 8
print("\n\nExample 8\n")
def square_num(num):
    for i in range(num):
        yield i**i

generator = square_num(6)

# Using while loop 
while True:
    try:
        print(f"The number using while loop is {next(generator)}")
    except StopIteration:
        break
    # Using for loop
nlis = []
for square in square_num(6):
    nlis.append(square)
print(f"The number using for loop are {nlis}")

# Using generator comprehension
square = (i**i for i in range(square))
square_lis = []
square_lis.append(next(square))
square_lis.append(next(square))
square_lis.append(next(square))
square_lis.append(next(square))
square_lis.append(next(square))
square_lis.append(next(square))
print(f"The numbers using generator comprehension are {square_lis}")

import math
num1= sum (i**i for i in range(6))
print(num1)


# last example 
print("\n\nExmaple 9\n")
def fibonacci(num):
    a,b = 0,1
    for _ in range(num):
        a,b = b, a+b
        yield a 

def square(num):
    for i in num:
        yield i**2

print(sum(square(fibonacci(5))))

# Thank you soo much for watching the last video of python tutorial 
# I will upload some project from basic to advance in python 
# Most importantly you can check the code from github (thesadiqali) link in the description
# Please like and subscribe for upcomming tutorial in python and machine learning and management etc 
# BYE BYE 