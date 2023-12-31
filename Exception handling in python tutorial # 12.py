print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 12 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m                                   TODAY TOPICS IS Exception Handling in python\033[0m                                       ")
#Exception handling in python 

#Exception:
#An Exception is an event, which occurs during the excution time of a program. which disrupt the normal flow.
#Exception handling in Python allows you to manage and respond to errors that occur during program execution. It helps prevent the program from crashing abruptly by handling unexpected situations or errors gracefully.
#If you have a suspicious code that may raise an exception.

#What are Exceptions?
#Errors in Python: When something goes wrong in Python during program execution, an error occurs. These errors are known as exceptions.

#Basic Structure of Exception Handling:
#Try-Except Block: In Python, you can use a try block to test a block of code for exceptions.
#If an exception occurs within the try block, Python immediately jumps to the matching except block to handle the exception.
#The code within the except block is executed to manage the exception.

#Common Exception:
#Zero Devision Error 
#Name Error
#Value Error 
#IO Error
#EOF Error 
#Indentation Error 

#For Example 
print("\n\nExample 1\n")
try:
    1/0
except ZeroDivisionError:
    print("This Code give Zero division error")

print("1/0")
# Comment
###Traceback (most recent call last):
  ###File "c:\Users\wajah\OneDrive\Desktop\Python\Exception handling in python tutorial # ###12.py", line 42, in <module>
    ###print(1/0)
       ###   ~^~
###ZeroDivisionError: division by zero

#Syntax
"""
try:
    # Code that might raise an exception
    # ...
except ExceptionType:
    # Code to handle the exception
    # ...
else:
    # Optional block executed if no exceptions occur in the try block
    # ...
finally:
    # Optional block, always executed whether an exception occurred or not
    # ...
"""

#And there are two types of exception 
#Two Types of Exception 
#1 Built in Exception
#2 Custom Exception 
"""
Built-in Exceptions: Python provides various built-in exceptions like TypeError, ValueError, ZeroDivisionError, etc.
Custom Exceptions: You can create custom exceptions to handle specific situations in your code by defining new exception classes.
"""

#Example 2
print("\n\nExample 2\n")

try:
    num1 = 1 #int(input("Enter a number: "))
    num2 = 1 #int(input("Enter another number: "))

    result = num1 / num2
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter a valid number.")
    
else:
    print("No exceptions ocurred.")

finally:
    print("Excution completed, regardless of exception.")
#If the user enters non numeric input or zero. the resptive exception will occurs.
#let see

#Benefits of Exception Handling:
"""
Graceful Error Handling: Prevents abrupt program termination.
Controlled Flow: Allows you to control the program flow in case of errors.
Cleanup Actions: Provides a way to perform cleanup actions regardless of exceptions.
Exception handling is a powerful tool in Python that helps you write more robust and reliable code by managing errors effectively.
"""

#lets do some other example 
#Zero Error alreay done

#NameError

print("\n\n \033[1;31;40m NameError\033[0m\n")
try:
    y = "Remove the Comment #. Name Error" #x + 5
except NameError:
    print("This code give a NameError")
print(y)


#Traceback (most recent call last):
  #File "c:\Users\wajah\OneDrive\Desktop\Python\Exception handling in python tutorial # 12.#py", line 116, in <module>
    #print(y)
        #  ^
#NameError: name 'y' is not defined



#Index Error 

print("\n\n\033[1;31;40m Index Error\033[0m\n")

nlis = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729] #chose random numbers

try:
    nlis[10]
except IndexError:
    print("This code give the Index Error.")
print("Remove the below comment # to see the answers about index error ")    
#print(nlis[10])

#This code give the Index Error.
#Traceback (most recent call last):
  #File "c:\Users\wajah\OneDrive\Desktop\Python\Exception handling in python tutorial # 12.#py", line 138, in <module>
    #print(nlis[10])
          #~~~~^^^^
#IndexError: list index out of range


#Now lets do some Multiple except Blocks 
# Try except except etc 
print(" \n\n\033[1;31;40m Multiple Except Blocks \033[0m\n ")
num1 = 2 #float(input("Enter a number:"))
print("The entered value is ",num1)

try:
    num2 = 3 #float( input("Enter a number: ", num2))
    value = num1 / num2 
    print("This process is running with value = ", value)
except ZeroDivisionError:
    print("This Function gives a ZeroDivisionError since a number cannot divide by 0.")
except ValueError:
    print("You should provide a number.")
except:
    print("Something went wrong")

#Raising in Exception 

#Using the raise keyword, the programmer can throw an exception when a certain condition is reached.

print(" \n\n\033[1;31;40m Raising an Exception \033[0m\n ")

num = 1006 #int(input('Enter a number: '))
print("The Entered value is ", num)
try:
    if num > 1000 and num % 2 == 0 or num % 2 != 0:
        raise Exception("Do not allow to the even numbers higher than 1000")
except:
    print("Even or Odd numbers higher than 1000 are not allowed!")
else:
    print("This process is running with value =", num)
    
finally:
    print("the process is completed.")
    

#Assignment:
print(" \n\n\033[1;31;40m Assignment \033[0m\n ")
print("1. Key Error")  #Practice These 
#Alreday discussed. Just like NameError
print("2. Multiple except clauses")   #Practice these 
#Already discussed

#Thank you soo much for waatching this video
#please like and subscribe this channel 
#Thesadiqali
#youtube and instagram and linkdeln 
#I will upload the code on my github 

