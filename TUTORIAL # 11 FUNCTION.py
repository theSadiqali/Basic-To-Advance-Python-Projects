print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 11 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("                                       TODAY TOPICS IS FUNCTION")
#Function
#What is Function?
#In python a Function is a group related statements that performs a specfics task.
"""
A function is a block of reusable code that performs a specific task.
It takes inputs, processes them, and produces outputs. 
Just like give input....  ( input  ---> Process ---> Output ) 
Parts of a function:

Function name: It's a unique identifier for the function.
Parameters (arguments): These are the inputs the function receives to perform its task.
Body: It contains the code that defines what the function does.
Return statement: It specifies the output of the function.
Creating a function:

Use the def keyword followed by the function name and parentheses ( ).
Define parameters inside the parentheses if the function needs input.
"""
#For Example:
print("\n\nFor Example:\n")
# Now sadiq is a function
def sadiq(x):  #indentation 
    y1 = x - 8
    y2 = x + 8
    y3 = x * 8
    y4 = x / 8
    y5 = x % 8
    y6 = x // 8
    print(f"If you make the above operations with {x}, the results will be {y1}, {y2},{y3}, {y4},{y5}, {y6}")   
    return y1,y2,y3,y4,y5,y6
#Here we have to run the function or proess it
sadiq(5)
#x = 5

#simple function example 
print("\n\nSimple Example 2\n")
def add():
    a = 2
    b = 1
    c = a + b
    print(f"Sum equal to {c}")
add() 

#Help function 
#Actually you can use help using help functin
#help(sadiq)
#Help on function process in module __main__:

print("\n\nCall the function again and again OR with another Number:\n")
sadiq(1)

#Function with multiple parameters
#Define a function with multiple elements 
print("\n\nMultiple Parameter\n")
def mult(x,y):
    z = 2*x + 5*y + 45
    return z
output = mult(3.14,1.618) #Actually you can yield the output by assigning to a variable
print(output)
print(mult(3.14,1.618)) #you can obtain the result directly 
mult(3.14,1.618) #This is also another version

print("\n\nSimple example Multiple parameter\n")
def add_numbers(a,b):
    result = a + b
    return result
# calling the function and passing arguments
sum_result = add_numbers(1,2)
print(sum_result)#Output 3

#Variable 
#the input for a function is called a formal parameter 
#A variable that is decleared inside a function is called a local variable 
#the parameter only exists within the function (i.e the point where the function start and stops)
#A fucntion that is decleared outside a function is known as global variable 
#And its value is accessible and modifiable throughout the program 
print('\n\nVariable\n')
global_var = 10
def my_variable():
    #local variable 
    local_variable = 20
    print("Inside the function: ")
    print("Local Variable: ", local_variable)
    print("Global Variable: ", global_var) # Accessing the global variable 

# Acessing the global varibale outside the function 
print("Outside the function (before function call):")
print("Global variable: ", global_var)

# Calling the function
my_variable()
#now access the local variable outside the function
#print( "Outside the function: ", local_variable ) # This line result in error
 
# NameError: name 'local_variable' is not defined

#Without return statement, the function returns None 
#define a function with and without return statement 

print("\n\nWithout return statement, the function returns None\n")
# Define a function with and without return 
def msg1():
    print("Hello, World!")
def msg2():
    print("Hello!, Sadiq!")
    return None 
msg1()
msg2()
#Now Printing a function after a call indicates a None is the default return statement.
#See the following prontings what functions returns are 
print(msg1())
print(msg2())

#Concatetantion of two strings 
#define a function 
print('\n\nConcatetantion of two strings \n')
def strings(x,y):
    print(x,y)
    return x + y 
# Testing the function 'strings' (x,y)
strings('Hello','Sadiq!')

#Simplicity of functions
# Here is the following code 

print("\n\nSimplicity of functions: \n")
x = 2.7
y = 0.5

equation = x*y + x+y - 37
if equation > 0:
    equation = 6
else: equation = 37

equation
print(equation)

# AND we can write them as a function 

def function (x,y):
    print("\n\nSimplicity of functions: Inside the Code \n")
    x = 2.7
    y = 0.5

    equation = x*y + x+y - 37
    if equation > 0:
        equation = 6
    else: equation = 37

    equation
    print(equation)
    
function(x,y)

#Predefined function 
print("\n\nPredefined functions: like print(), sum(), len(), min(), max(),input()")

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(sum(numbers))
print(len(numbers))
#practice the remainings

#Using conditions and loop in functions 
#define a function including conditions if/else
print("\n\nUsing condition & loops \n")
def fermentation(microorganism, substrate, product,activity):
    print(microorganism, substrate, product, activity)
    if activity < 1000:
        return f"The fermentation process was unsuccessful with the {product} activity of {activity} U/ml from {substrate}"
    else:
        return f"The fermentation process was successful with the {product} activity of {activity} U/ml from {substrate}"
result1 = fermentation("Aspergillus niger",'molasses','insulinase',1800)
print(result1)
print("")
result2 = fermentation('Aspergillus niger','molasses','insulinase', 785)
print(result2)
    
#Bio problem 

#now loop 
print("\n\nLoop: \n")
def fermentation(context):
    for parameters in context:
        print(parameters)
context = ['Stirred-tank bioreactor', '30`C temperature ', '200 rpm agitation speed', '1vvm aeration', '1% (v/v) inoculr']
fermentation(context)

#simple Example 
print("\n\nSimple Example:\n")
def simple1(example1):
    for parameters in example1:
        print(parameters)
example1 = [1,2,3,4,5,6]

simple1(example1)

#Now 
# Recursive Functions
print('\n\nRecursive Function\n')
#Calculating the factorial of a certain number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial (number - 1)
print('the value is', factorial(6))

#nested function 
print("\n\nNested Function\n")
def added_num(num1):
    def incremented_num(num1):
        num1 = num1 + 1 
        return num1
    num2 = incremented_num(num1)
    print(num1,'------->>>',num2)
added_num(25)
#Dont worry i will upload the code on my github 

#NonLocal Function 
#define a function regarding nonlocal function
print("\n\nNonlocal Function:\n") 
def print_year():
    year = 1994
    def print_current_year():
        nonlocal year
        year  += 30  # Actually we are not specying non local here 
        print('Current year is ', year)
    print_current_year()
print_year()


#Thank you soo much for watching this video 
#i will upload a small project soon about function 
#And i will upload a code on my github 
#please like and subscribe my channel 
 