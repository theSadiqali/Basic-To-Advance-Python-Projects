print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 16 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m Arrays in Python\033[0m  ")

# Array is a contianer which can hold a fix number items and these items should be of the same type.
# In Python, an array is a collection of elements, each identified by an index or a key. Python does not have a built-in array data type like some other programming languages; instead, it has lists. Lists are more versatile and can be used as arrays.
# List can be used to form array 
# Element: Each items stored in an array is called an element.
# Index: Each location of an element in an array has a numerical index, which is used to identify the element. 
# Actually Array index begins with 0.
# CREATING AN ARRAY 
print("\nCreating An Array\n")
#Import array or from array import(*).
#(*) means that it covers all features of the array. 
#Import the module
import array as arr
from array import *
# If you want access more information regarding array, you acn excute the following commands 
#help(arr)
# We are going to try this in pycharm 
# Array represent basic values and behave like lists, except the type of object and stores in them is contrained.
# The type is specified at object creating time by using a type code, which is a single character. 

nums = arr.array('d',[0,1,2,3,4,5,6,7,8,9])
# Before that le tme Show you somethings
# Following type codes 
for i in nums:
    print(i)
    
# Accessing 
print("\n\nAccessing\n")
special_nums = arr.array ('d',[0.577,1.618,2.718,3.14,6,37,1729])
print(f"First Element of number is: {special_nums[0]}, called Euler constant")
print(f"First Element of number is: {special_nums[1]}, called Golden ratio")
print(f"First Element of number is: {special_nums[-1]}, called Ramanujan-Hardy number")
       
# Changing or Update 
print("\n\nChanging or Update\n")
nums = arr.array('i',[0,1,1,2,3,5,8,13,21,34])
#Changing the first element of the array 
nums[0]=55
print(nums)
#Changing 2nd to 4th element of the array
nums[1:4]=arr.array('i',[89,144,233,377])
print(nums)

# Deleting 
print("\n\nDeleting\n")
nums = arr.array('i',[0,1,1,2,3,5,8,13,21,34])
#Lets delete the first element of the array 
del nums[0]
print(nums)
#Deleting the 2nd to 4th element of the array 
del nums[1:4]
print(nums)

# Length of the array 
# Special Number 
print("\n\nlength of the Array\n")
special_nums = arr.array ('d',[0.577,1.618,2.718,3.14,6,37,1729])
print(special_nums)
print(f"The length of the array is: {len(special_nums)}")
# Concatenation 

print("\n\nConcatenation \n")
special_nums = arr.array ('d',[0.577,1.618,2.718,3.14,6,37,1729])
fibonacci_nums = arr.array ('d',[1,1,2,3,5,8,13,21,34])
# Fibonacci numbers 

special_fibonacci_nums = arr.array('d')
special_fibonacci_nums = special_nums + fibonacci_nums
print(f"The new array called special fibonacci nums is {special_fibonacci_nums}")

# Creating Id array 
print("\n\nCreating Id Array\n")
mult = 10
one_array = [1]*mult
print(one_array)
print("\n\n")
mult = 10 
nums_array = [i for i in range(mult)]
print(nums_array)
# Addition with the functions insert() and append()
#Using the function insert()
print("\n\nAddition with the functions insert() and append() \n")
fibonacci_nums = arr.array ('d',[1,1,2,3,5,8,13,21,34])
print("Before any addition into fibonacci numbers")
for i in fibonacci_nums:
    print(i,end='')
print()
print("After an element addition into fibonacci numbers")
added_num = fibonacci_nums[-1]+fibonacci_nums[-2]
fibonacci_nums.insert(9,added_num)
for i in fibonacci_nums:
    print(i,end='')
print()
print("After an element addtion into fibonacci number")
added_num = fibonacci_nums[-1] + fibonacci_nums[-2]
fibonacci_nums.insert(10,added_num)
for i in fibonacci_nums:
    print(i,end='')
    
# Removing with the function remove() and pop()
print("\n\nRemoving with the function remove() and pop()\n")
special_nums = arr.array ('d',[0.577,1.618,2.718,3.14,6,37,1729]) # Actually its not necceary to mention the variable every time but we are doing this just for the better understanding of the code.
print('Before removing an element from the array')
for i in special_nums:
    print(i,end='')
    
print()
print("After removing an element from the array")
special_nums.remove(0.577)
for i in special_nums:
    print(i,end='')
print()
# Assignemnt How we can make this using indexing ?
# [0]--- Hint
# Assignment pop() function practice 
print("\n\npop()\n")
print("\n\nRemoving with the function remove() and pop()\n")
special_nums = arr.array ('d',[0.577,1.618,2.718,3.14,6,37,1729]) # Actually its not necceary to mention the variable every time but we are doing this just for the better understanding of the code.
print('Before removing an element from the array')
for i in special_nums:
    print(i,end='')
    
print()
print("After removing last element from the array")
special_nums.pop(6)
for i in special_nums:
    print(i,end='')
print()

# Slicing 
print("\n\n Slicing\n")
special_nums = arr.array('d',[0.577,1.618,2.718,3.14,6,37,1729])
sliced_special_nums = special_nums[1:5] #It returns between index 1 and index 4, not index 5.
print(sliced_special_nums)
# Using for loop 
for i in sliced_special_nums:
    print(i, end=' , ')
    
print("\n\n")    
sliced_special_nums = special_nums[3:] # It will returns 3 and index later 
print(sliced_special_nums)
for i in sliced_special_nums:
    print(i,end=" , ")
    
print("\n\nSearching\n")
# TO make a search in an array, use the function index()
special_nums = arr.array('d',[0.577,1.618,2.718,3.14,6,37,1729])
searched_item = special_nums.index(2.718)
print(f"The searched item euler number 2.718 is present at index {searched_item}.")
# Printing with format 
print("The searched item euler number {} is present at index {}.".format(2.718,searched_item))

# Copying 
# Copying using assignment 
# This process gives the same id number.
print("\n\nCopying\n")
special_nums = arr.array('d',[0.577,1.618,2.718,3.14,6,37,1729])
copied_special_nums = special_nums
print(special_nums,'with the ID number', id(special_nums))
print(copied_special_nums,'with the ID number',id(copied_special_nums))

#Using for loop
for i in special_nums:
    print(i, end= " ")
    
print()
print(f"The ID number of the array special_num is {id(special_nums)}")
for i in copied_special_nums:
    print(i,end=" ")
    
print()
print(f"The ID number of the array copied_special_num is {id(copied_special_nums)}")
# Output Every id are same here 


# Copying Using view()
# This process give the different ID number. 
print("\n\nCopying Using view()\n")
import numpy as np
#Copying the array 
special_nums = np.array([0.577,1.618,2.718,3.14,6,37,1729]) # lets make it easy for you guys 
copied_special_nums = special_nums.view()
print(special_nums,'with the ID number',id(special_nums))
print(copied_special_nums,'with the ID number',id(copied_special_nums))
# Using for loop
for i in special_nums:
    print(i,end=' ')
print()
for i in copied_special_nums:
    print(i,end=' ')
# Different Id number
# Assignment Copying using copy()
# Copying the array 

print("\n\nCopying Using copy()\n")
import numpy as np
#Copying the array 
special_nums = np.array([0.577,1.618,2.718,3.14,6,37,1729]) # lets make it easy for you guys 
copied_special_nums = special_nums.copy()
print(special_nums,'with the ID number',id(special_nums))
print(copied_special_nums,'with the ID number',id(copied_special_nums))
# Using for loop
for i in special_nums:
    print(i,end=' ')
print()
for i in copied_special_nums:
    print(i,end=' ')
    
# I will upload a small project with array as soon as possible 
# You can download the code from my Github 
# Please like and subscribe my channel 
# for today that`s` It 
# BYE BYE 
