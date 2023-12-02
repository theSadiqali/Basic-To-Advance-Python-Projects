                                    #=========================#
                                    #    PYTHON Tutorial # 7  #
                                    #-------------------------#
                                    #        YOUTUBE          #
                                    #   thesadiqali channel   #
                                    #  ====================== # 
                                    #   PYTHON Tutorial       #
                                    #   BASIC TO ADVANCE      #
                                    #=========================#
#TODAY TOPICS Sets
"""A set in Python is like a collection of items in a bag, but in this bag, each item is unique (there are no duplicates) and there's no specific order to how they are arranged.."""
#Definition: A set in Python is a collection of unique and unordered elements.
#Creation: Sets are created using curly braces {} or the set() function.
#Uniqueness: Sets do not allow duplicate elements; each element appears only once.
#Order: Sets do not maintain the order of elements as they are unordered.
#Actually set is one of built in data types in python used to store collection of data  including list, tuples and dictionary.

#Different Sets
#UNION , INTERSECTION, DIFFERENCE AND SYMMETRIC DIFFERENCE 
#empty sets
print("EMPTY SETS:\n")
set1 = {}
print(f"Empty sets Value: {set1}") # As you can see {} empty braces denotes the empty dictionary, not empty set 
print(type(set1))

set2 = set() # to take empty set without elements, use set() function without any items
print(f"Empty sets Value: {set2}")
print(type(set2))
#Lets convert list to set
#take a list
print("\n\nCONVERTING LIST TO A SET: \n")
lis = ["sadiq ali",12,2023, "Hello", True,False,2024] #Now its a list
lis
#Now convert a list into a set
set3 = set(lis)
print(f"Converted list: {set3}")
print(f"Check Type: {type(lis)}")  #Its a list 
print(f"Check the converted one Type: {type(set3)}") #Its a set

#Set Operation 
#take a set
print("\n\nSet OPeration\n")
print("Add function")
set3.add("Hi python coders!")
print(f"set3: {set3}")
#Update function 
#to add multiple element into the sets 
print("\nUPDATE ELEMENT: \n")
set4 = {2,3,4,5}
print(set4)
set4.update({6,7,8,9,1})
print(f"Updated Sets: {set4}")

#remove function
print("\nREMOVE FUNCTION: ")
#to remove an elemenet from the set .remove we use
set4.remove(4)
#set4.remove(1,2,3,4) # TypeError: set.remove() takes exactly one argument (4 given)
print(f"After removing: {set4}")

#now lets talk about discard function
#actually it leave the set unchanged if the element to be deleted is not available in the set 
print("\n\n Discard function\n")
print(set4.discard(3.11))
print(f"Show the result to prove:  {2 in set4} ")

#logic operation in sets 
#take two sets
print("\n\nSET OPERATION\n")
num_1 = set (["thesadiqali!",123,"Hellothesadiqali",1,2,3])
num_2 = set ([789,1122,True,False,2024,"dec",1,2,3])
#now printing two sets
print(f"printing the sets {num_1 , num_2}")
#Now lets do the intersection 
intersection  = num_1 & num_2
print(f"print the intersection:  {intersection}")

#difference function 
print("\n\nDifference function \n")
print(f"print Num 1 Set: {num_1} \nPrint Num 2 Set: {num_2}")
#to find difference between two sets 
print("Here is the Difference: ",num_1 - num_2 )
num_3 = {1,2,3}
num_4 = {2} #Set comparision 
print("\n\nSet comparision\n")
print("Num3 and Num4 Sets comparision: ",num_3 > num_4)
#you can do the rest

#Union Function 
#Actually it correspond to all the element in both sets 
print("\n\nUnion set function: ",num_3.union(num_4))

#issuperset() and subset() functions 
#To control if a set is superset or subset 
#just like this 
print(f"\n\n1,2,3 is Subset: {set([1.1,2.2]).issubset(num_3)}")
#just like this fo the superset

#now coming to min(), max() and sum() functions
print("\n\nmin(), max() and sum() functions")
A = [1,1,2,2,3,3,4,4,5,5,6,6]
B = {1,1,2,2,3,3,4,4,5,5,6,6}
print("\n\nMINIMUM AND MAX AND SUM\n The minimum function of A is",min(A))
print("\n\nMINIMUM AND MAX AND SUM\n The minimum function of B is",min(B))

print("\n\nMINIMUM AND MAX AND SUM\n The maximum function of A is",max(A))
print("\n\nMINIMUM AND MAX AND SUM\n The maxiimum function of B is",max(B))
print("The sum of A is: ",sum(A))
print("The sum of A is: ",sum(B))

#I will give you the Assignment of copy() function . do some practice with and clear function
#Now lets do the pop function
print("\nPop function")
print("Pop: ",A.pop())
#it removes and returns an arbitrary set elements 
"""Thank you soo much for watching this video 
I will upload on my github 
Do the Assignment""" 










