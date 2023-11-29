                                    #=========================#
                                    #    PYTHON Tutorial #5   #
                                    #-------------------------#
                                    #        YOUTUBE          #
                                    #   thesadiqali channel   #
                                    #  ====================== # 
                                    #   PYTHON Tutorial       #
                                    #   BASIC TO ADVANCE      #
                                    #=========================#
                                    #TODAY TOPICS LISTS
https://www.youtube.com/@Thesadiqali11
#1 lists are Ordered    
#2 lists can contain any arbitrary objects
#3 list elements can be accessed by index 
#4 list can be nested to arbitrary depth
#5 lists are mutable 
#6 lists are dynamic


#indexing
#creating a list
nils = ['sadiq',3,2001]
print(nils)

print()
print(f"positive and negative indexing: \n POSITIVE INDEXING: {nils[0]} \n NEGATIVE INDEXING: {nils[-3]}")
print(f"positive and negative indexing: \n POSITIVE INDEXING: {nils[1]} \n NEGATIVE INDEXING: {nils[-1]}")
print(f"positive and negative indexing: \n POSITIVE INDEXING: {nils[2]} \n NEGATIVE INDEXING: {nils[-2]}")

#WHAT CAN CONTENT A LISTS

#1 STRING
#2 FLOATS
#3 INTEGER 
#4 BOLEAN 
#5 NESTED LIST
#6 NESTED TUPLES 
#7 OTHER DATA STRUCTURE 

#FOR EXAMPLE
print("\n\n EXAMPLE OF CONTENT A LISTS \n")
nilist= ['thesadiqali',3,2001,[1,2,3,4,5,6,7,8,9],('Hello', 'Sadiq',3,2001)]
print(f"nilist: {nilist}")

#list operation 
#now list do this 
print("\n\n LIST OPERATION \n")
#take a list
nlis1 = ['sadiq',3,2001,[1,2,3,4,5,6,7,8,9],("Hello", 'Sadiq',3,2001)]

nlis1
print(len(nlis1))

#slicing of a list 
print("\nSLICING OF A LISTS")
print(nlis1[0:2])
print(nlis1[2:4])

#EXTENDING THE LISTS 

#you know we use extend the function to add new element to the list
#with this function, we add more than one element to the list 
#for example take a list 
print("\n\n EXTENDING THE LIST\n")
nlis2 = ['sadiq', 3,2001,[1,2,3,4,5,6,7,8,9],('Hello','Sadiq',3,2001)]
nlis2.extend(['HELLO SADIQ TO THE WORLD OF PYTHON!', 2023])
nlis2
print(nlis2) 
#AS YOU CAN SEE THE EXTENDING LIST
#NOW APPEND METHOD

#APPEND METHOD 

#AS YOU KNOW ITS DIFFERENT FROM THE EXTEND METHOD.
#WITH APPEND METHOD WE ONLY ADD ONE ELEMENT 

#TAKE A LIST 
print("\n\n APPEND METHOD")
list3 = ['sadiq', 3,2001,[1,2,3,4,5,6,7,8,9],('Hello','Sadiq',3,2001)]
list3.append(['HELLO SADIQ TO THE WORLD OF PYTHON!', 2023])
list3
print(list3)
#just like 
print("\n\n For Example:\n")
list5 = [1,2,3,4,5,6,7,8,9] #start from 1 SORRY FOR THAT 
print(f"len(list5): {len(list5)}")
list5.append(3)
print(f"list5: {list5}")
print(f"list5.count(3){list5.count(3)}")
print(f"list5.index(2){list5.index(2)}")
list5.insert(11,12)
print(f"List 5 after inserting: {list5}")
print(f"max(list5): {max(list5)}")
print(f"min(list5):{max(list5)}")
print(f"sum(list5): {max(list5)}")
#let see , good to go 

#you can also change the element 
#because its mutable
#and also you can delete them with del()
#del
#lets check why its not working 
list6 = ['sadiq',1,2,3]
print(f"list6: {list6}")
del(list6)
#print(f"After deleting the list6: {list6}")

#After that it will show name error is not defined 
#Because its deleted
#now Spliting

#SPLITING
print("\n\nSPLITING\n")
#conversion using spliting
spli = 'sadiq ali is making a tutorial right now'
print(f"spli.split(): {spli.split()}")

#Now basic operation 

#OPERATIONS
print("\n\nBASIC OPERATION\n")
oper = ['a','b','c','hello','sadiq'] 
oper2 = [1,2,3,4,5,6,7,8,9]
print(f"operation: {oper}")
print(f"operation2: {oper2}")
print(f"operation: len(oper): {len(oper)}")
print(f"operation2: len(oper2): {len(oper2)}")
print(f"operation + operation 2: {oper + oper2}")
#loop
print("\nFor loop")
for i in oper:
    print(i)
for i in oper2:
    print(i)
print(11 in oper)
#lets see
print(4 in oper2)
#you can do lots of things . just like copy the list with copy keyword or clone the list with clone keyword or concentrate the list 

#INPUT FUNCTION 
print("\n\nINPUT FUNCTION:\n")
list7 = input("Enter a list or string: ") # it is a little bit different from the list    
print(f"sadiq: {list7}")

#Evalute function 
#the function serves the aim of converting a string into int or float 
print("\n\n EXPRESSION\n")
expression = '11+2'
total = eval(expression)
print(f"Sum of the expression is: {expression} ")
print(f"Sum of the expression after eval: {total}")

#Format function 
#this function helps to format the output prited on the screen good and attractive look 
#Example 
print("\n\nFormat Function\n")
a = float(input('Enter the pi Number: '))
b = float(input('Enter the golden ratio: '))  #intendation matter the most 
totals = a+b
print("Sum of {} and {} is {}.".format(a,b,totals))
#let see 
#As you can see 

#Now
#COMPARISION OPERATOR AND LOGICAL OPERATOR AND IDENTITY OPERATOR 
print("\n\nComparision Operator\n")
var = 1
var2 = 2
var3 = 3
print(f"var: {var}")
print(f"var2: {var2}")
print(f"var<var2: {var<var2}")
#Etc

#home work logical operators
#just like this 
print(f"\nLOGICAL OPERATOR:\nvar<var2 and var3>var: {var<var2 and var3>var}")

#ASSIGNMENT operator 
#=, ==, +=,-=,/=,%=,%=,|=,//=,&=,>>=,<<= etc
#are employed to evalute a value to a variable
print("\n\nASSIGNMENT operator \n") 
x = 3.14
x+=5
print(x)

#IDENTITY OPERATORS 
#THE OPERATOR IS OR IS NOT ARE EMPLOYED TO CONTROL IF THE OPERANDS OR OBJECTS TO THE LEFT AND RIGHT OF THESE OPERATORS ARE REFERRING TO A VALUE STORED IN THE SAME MEOMERY LOCATION AND RETURN TRUE OR FALSE 
#EXAMPLE 
print("\n\nIDENTITY OPERATOR\n")
a1 = 3.14
b1 = 1.618
print(a is b) #FALSE
print(a is not b) #TRUE
msg1 = "hello sadiq ali"
msg2 = "hello python!"
print(msg1 is msg2) #FALSE
#let see 

#MEMBERSHIP OPERATORS
#ACTUALLY THESE OPERATORS INCLUSION IN AND NOT IN ARE EMPLYED TO CHECK . IF THE CERTAIN VALUE IS AVAILBLE IN THE SEQUENCE OF VALUE AND RETURN TRUE OR FALSE 
#TAKE A LIST LETS DO THIS 
print("\n\nMEMBERSHIP OPERATOR\n")
LIS = ['sadiq', 3,2001,[1,2,3,4],('Hello','Sadiq',3,2001)]
print(5 in LIS) #FALSE
print(LIS)
print(4 not in LIS) #TRUE
print(LIS)

#ETC
#I THINK FOR TODAY THATS IT. 
#WE WILL COVER TUPLES IN NEXT TUTORAL #6
#THANK YOU SOO MUCH FOR WATCHING THIS VIDEO 
#I WILL UPLOAD THE CODE ON GITHUB
#BYE
