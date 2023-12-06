                                    #=========================#
                                    #    PYTHON Tutorial # 9  #
                                    #-------------------------#
                                    #        YOUTUBE          #
                                    #   thesadiqali channel   #
                                    #  ====================== # 
                                    #   PYTHON Tutorial       #
                                    #   BASIC TO ADVANCE      #
                                    #=========================#
#TODAY TOPIC CONDITIONS 
#COMPARISION
#In Python, conditions are used to control the flow of a program based on certain criteria. The primary construct for expressing conditions is the if statement. 
print("CONDITIONS IN PYTHON")
#Comparision operators in python are =, <,>,<=,>=,==,!=

#for example
print("\n\nComparison Operator: ")
a=5
b=1
print(a>b) #greater then
print(a==b) # equal to 
print(a!=b) #not equal to 
print(a<=b) #less then or equal to 
print(a>=b) #greater then or equal to 
#trying if else statement 
print("\n\nIf else statement")
if a == b: # If its true . then run this .
    print("A equal to B")
elif a > b:  # else If its true . then run this .
    print("A is greater then B")
else:   # else run this .
    print("Error")
    
#in condtion statement . indentation matter the most 

#FOR EXAMPLE grading exmple 
#(A 90 and +) , (B 80 + ) , (C 50 + ) , (40 + D) , (39 - F)
print("\n\nExample 1: \n")

num = int(input("Enter a Number: "))
print(f"The entered Marks is: {num} ")
if num >= 90:
    print("Grade is: A")

elif num >= 80:
    print("Grade is: B")

elif num >= 50:
    print("Grade is: C")

elif num >= 40:
    print("Grade is: D")

elif num <= 39:
    print("Grade is: F")

else:
    print("Invalid Number")
 #let see
 
 #logical operator a
 
 #1 and: Return True if both statement are true 
 #2 or: Return True if one statement are true
 #3 not:Reverse the result, returns False if the result is true
 
#example 2

print("\n\nExample 2\n")

x = int(input("ENTER A NUMBER X: "))
y = int(input("ENTER A NUMBER Y: "))
z = int(input("ENTER A NUMBER Z: "))

print(f"the entered numbers for x, y , z are {x}, {y} and {z}")

if x > y and x != z:
    print(f"first statement are true {x}, {y} and {z}")

elif x > y and x != z:
    print(f"2nd statement are true {x}, {y} and {z}")

elif x >= y or x != z:
    print(f"3rd statement are true {x}, {y} and {z}")

elif x == y and x <= z:
    print(f"4th statement are true {x}, {y} and {z}")

elif not x != y:
    print(f"last statement are true {x}, {y} and {z}")

else:
    print("Invalid")
    
#I will upload a basic tutorial with if else in python 
#soon
#Next tutorial all about Loops tutorial # 10 
#thank you soo much for watching this video 
#BYE BYE
