                                    #=========================#
                                    #    PYTHON Tutorial #6   #
                                    #-------------------------#
                                    #        YOUTUBE          #
                                    #   thesadiqali channel   #
                                    #  ====================== # 
                                    #   PYTHON Tutorial       #
                                    #   BASIC TO ADVANCE      #
                                    #=========================#
#TODAY TOPICS TUPLES
#TUPLES are immutable lists and cannot be charged in any way once it is created.
#1 Tuples are defined in the same way as lists.
#2 They are enclosed within parenthesis and not within square braces.
#3 Tuples are ordered, indexed collection of data.
#4 Similar to string indices, the first value in the tuples will have the indexed[0], the second value [1].
#5 Negative indices are counted from the end of the tuples, just like lists.
#6 Tuples also has the same structure where commas seperate the values.
#7 Tuples can store dublicate values.
#8 Tuples allow you to store several data items including string, integer, float in one variable.
#Take the list For Example 
print("TUPLES\n")
tupl = ('Hello!','Sadiq',3,2,True,False,12,[1,2,3],{1,2,3},{'A':3,'B':8},(0,1))
tupl
print(tupl)
print(f"TYPE OF TUPLES: {type(tupl)}")
print(f"LENGTH OF TUPLE: {len(tupl)}")
#let see 
#printing the each value in a tuple using both positive and negative indexing 
print("\n\nPRINTING EACH VALUES\n")
tupl_1 = ('Hello!','Sadiq',3,2,True,False,12,[1,2,3],{1,2,3},{'A':3,'B':8},(0,1))
print(tupl_1[0])
print(tupl_1[1])
print(tupl_1[2])
print(tupl_1[-1])
print(tupl_1[-2])
#let do this 
print("\nType of tuples ")
#lets find the type of these tuples
print(type(tupl_1[0]))
print(type(tupl_1[1]))
print(type(tupl_1[2]))
print(type(tupl_1[-1]))
print(type(tupl_1[-2]))

#CONCENTRATION OF TUPLES 
#TO CONCENTRATE TUPLES + SIGN IS USED 
print("\n\nCONCENTRATION TUPLE\n")
tupl_2 = tupl_1 + ('Concentration tuples',2023,'Dec') #today date 30 nov haha
tupl_2
print(f"Tuple two concentration: \n{tupl_2}")

#REPITION OF A TUPLES 
re_tupl = (1,2,3,4)
repition = re_tupl*2 
print(f"\nRepition Tuple:\n{repition}")
#membership tuples
#as u can see
print(f"2 in Retuples: {2 in re_tupl}")
print(f"5 in Retuples: {5 in re_tupl}")
print(f"5 Not in Retuples: {5 not in re_tupl}")

#membership
print("\nMEMBERSHIP TUPLES")
rep_tup = (1,2,3,4,5)
print(f"1 in tuples: {rep_tup}")
print("\n\n Iteration Tuples\n")
#iteration 
for i in rep_tup:
    print(i)
    
#let see the iteration with for loop , do not woory i will teach you
#about for loop later 

#cmp() function .
#actually it is to compare two tuples and returns TRUE OR FALSE
#JUST LIKE THIS 

print("\n\nCMP() FUNCTION:\n")
def cmp(t1,t2):
    return bool(t1>t2)- bool(t1<t2)
#I will upload the simple tutorial on function SOON
#and i will teach you that later 
def cmp(t3,t4):
    return bool(t3>t4)- bool(t3<t4)
def cmp(t5,t6):
    return bool(t5>t6)- bool(t5<t6)
t1 = (1,3,5) #Here t1 is lower than t2, since the output is -1
t2 = (2,4,6)

t3 =(5,) #Here t3 is higher than t4 since the output is 1
t4 =(4,)

t5 =(3.14,) #Here t5 is equal to t6 since the output is 0
t6 =(3.14,)

print(f"Cmp function t1 and t2: {t1,t2}: \n",cmp(t1,t2))
print(f"Cmp function t3 and t4: {t3,t4}:\n", cmp(t3,t4))
print(f"Cmp function t5 and t6: {t5,t6}:\n", cmp(t5,t6))
#lets check

#Minimum function 
print("\n\nPRINT FUNCTION:\n")
print(f"Retuple Value: {re_tupl}")
minimum = min(re_tupl)
print(f"Minimum: {minimum}")

#similar the max() function 
#Tup(seq) function
#It converts a specific sequence to a tuple
print("\nTUPLE(SEQ) FUNCTION\n") 
seq = 'thesadiqali'
sequence =tuple(seq)
print(f"Sequence tuple: {seq}", "\nSequence: ", sequence)

#Slicing
#to obtain a new tuple from the tuple, the slicing method is used.
#obtain a new tuple from index 1 to index 3
print("\n\nSlicing tuple \n")
print(f"Tuple values: {tupl}")
slicing = tupl[1:3]
print(f"After Tuple Slicing 1 to 3: {slicing}")
#let see 
#length function only find the length 
length = len(tupl)
print("length of tuple",length) #just like that 
#is to obtain how many element

#SORTING TUPLE
print("\n\nSORTING TUPLES\n")
#tuples to can be sorted and save as new tuple.
sort_tuple = (1,2,5,6,8,9,0,3)
sort_the_tuple = sorted(sort_tuple)
print(f"Value of tuples: {sort_tuple}\n","After Sorted: ",sort_the_tuple)

#Nested tuple
#Nested tuples in Python refer to tuples that are elements of another tuple. Tuples are immutable, ordered collections, and they can contain other tuples as their elements. 
# Here is an example 
print("\n\nNested Tuples")
nested_tuple = ((1,2,3),('a','b','c'),(4.5,5.5,6.5))
#                0            1             2
#Accesing element in the nested tuples
print(f"Nested_tuple ZERO: {nested_tuple[0]}") # Expecting the output ((1,2,3))
print(f"Nested_tuple ONE AND ZERO: {nested_tuple[1][0]}") #EXPECTING A
print(f"Nested_tuple TWO AND TWO: {nested_tuple[2][2]}") #EXPEXTING OUTPUT 6.5
#LETS SEE
#let me tell u one more thing that tuple are immutable 
#let see
print("\n\nTuple are Immutable")
immu_tupl = (1,2,3,4)
#immu_tupl[1] = 9
#print(f"Immutable tuple: {immu_tupl}") #let see
#TypeError: 'tuple' object does not support item assignment
#type error tuple object does not support item assignment

#Delete a tuple 
#You cannot directly delete individual elements from a tuple, as tuples are immutable. Here is an example 
print("\n\nDelete Tuple")
del_tuple = (0,1,2,3,4,4,4,4,4,4,4,4,5,6,7)
print(f"Tuple before deleting it: {del_tuple}")
#del del_tuple
#print(f"After deleting the tuple: {del_tuple}")
#let see
#NameError: name 'del_tuple' is not defined. Did you mean: 're_tupl'?

#count method 
print("\n\nCount Method\n")
count = del_tuple.count(4)
print(f"Count method: {count}")

#index method 
#actually it return the index of the first occurence of the specified value in a tuple

print("\n\nIndex Method")
print("Index Method 4: ",del_tuple.index(4))
#because it start from zero

#One ELement Tuple
#Creating a one-element tuple requires a trailing comma after the single element. This is necessary to distinguish it from parentheses used for grouping expressions.
print("\n\nOne Element Tuple\n")
one_tuple = (0)
print(f"One element tuple: {one_tuple}")
print(f"Type of One element tuple: {type(one_tuple)}")
#As you can see that the output is integer 
tuple_1 = (0,)
print("Tuple: ",tuple_1)
print("Type of tuple: ",type(tuple_1))
#thank you soo watchong this video 
#for today that`s enough
#next on Sets in python Tutorial # 7
#I will upload the code on github 
