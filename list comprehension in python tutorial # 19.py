print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 19 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m LIst comprehension in Python\033[0m  ")

# What is a List Comprehension?
# A list comprehension is a concise way to create lists in Python. It allows you to construct a new list by specifying the elements you want, along with any conditions or transformations, all in a single line of code.
# list comprehension in python is an easy and compact syntax for creating a list from a string or another list.
# List comprehension is considerably faster than processing a list using the for loop.

# Expression for item in iterable
# Expression: can be any expression and is evaluted once
# Item: Any item from the iterable 
# Iterable: An iterable object (list, tuple, etc )
# Condition: (optional): An optional condition to filter elements.

# Example:
square = []
for num in range(5):
    square.append(num ** 2)
    print(square," Num is: ",num)

print("\n")
# With a list comprehension, you can achieve the same result in a more concise way.
square = [num ** 2 for num in range(5)]
print(square," Num is ", num )

# Adding a Condition 
# Now lets say you want to include only the even squares:
print("\n\nAdding a Condition \n")
even_square = [num ** 2 for num in range(5) if num % 2 == 0]
print(even_square," Num is ", num)

# List comprehension often result in shorter and more readble code.
# Efficieny: They are usually faster than equivalent tradional loops.
# Readiblility: They express the creation of a list in a clear and straight forward manner.

# List comprehension are a powerfull and expressive feature in python.
# Example 
print("\n\nExample\n")
import math
from math import *
#using for loop 
cubic_num = []
for i in range(5):
    i**=3
    cubic_num.append(i)
    
print(cubic_num) 

# Using list comprehension
cubic_num = [i**3 for i in range(5)]
print(cubic_num)

# Using list comprehension
cubic_num = [math.pow(i,3) for i in range(5)]
print(cubic_num)

# Example 2
print("\n\nExample 2\n")
languages = ['python','java','C++','Php']
#using for loop
languages_lis = []
for i in languages:
    if i!= 'C++':
        languages_lis.append(i)
print(languages,"\n",languages_lis)

# Example 3
print("\n\nExample 3\n")
# Using for loop
num_lis = []
for i in range(11):
    if i % 2 == 0:
        num_lis.append('Even')
    else:
        num_lis.append('Odd')
print(f"For Loop: {num_lis}")

# Using list comprehension
num_lis = ['Even' if i%2==0 else 'Odd' for i in range(11)]
print(f"List comprehension: {num_lis}")

# Using lambda function
num_lis = list(map(lambda i:i,['Even' if i%2==0 else 'Odd' for i in range(11)]))
print(f"Lambda: {num_lis}")

# I think That`s alot for today. 
# Thank you soo much for watching this video 
# I will upload the code on my github go and checkout.
# Please like and subscribe my channel.
# Bye Bye 