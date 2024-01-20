print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 17 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m Lambda Function in Python\033[0m  ")
# A lamda Function is a small anonymous function 
# A lambda function can take any number of arguments, but can only have one expression.
# The expression is evaluted and returned 
# Lambda functions can be used wherever function objects are required.
print("What is Lambda Function in Python?")
# A lambda function in Python is a concise way to create small, anonymous functions. Unlike regular functions defined using the def keyword, lambda functions are created using the lambda keyword. Lambda functions are often used for short-term operations where a full function definition might be overkill.
#Define a function using 'def'
def f(x):
    return x + 6
print('Def: ',f(3.14))

#Define the same function using 'lambda'
print('Lambda',(lambda x: x+6)(3.14))

# Define a function using def keyword 
def f(x,y):
    return x+y
print("the sum of {} and {} is".format(3.14,2.718),f(3.14,2.718))

# Define the same function using lambda
print(f'The sum of pi number and euler number is {(lambda x,y: x+y)(3.14,2.718)}')

# Lets calculate the volume of a cube using def and lambda function.
# But First let me teach you some basic 
# THe basic syntax of lambda function is 
#lambda argument: expression
# Here 'lambda' introduces the function, followed by a list of arguments, a colon, and an expression that is evaluted and returned.
#For example Adding two numbers 
print("\n\nBasic of lambda\n\nAddition\n")
add = lambda x, y: x + y
result = add (5,3)
print('5+8 =',result)
# In this example we create a lambda function called 'add' that take two arguments.
# x and y and return their sum. We then call the lambda function with arguments 5 and 3. 5+3 = 8
# So Output should be 8 . let see 

# Example 2 Squaring a NUmber 
print("\n\nSquaring\n")
square = lambda x: x**2 # For power you have to put **
result = square(4)
print("4 squaring = ",result)

# Here the lambda function square take one argument x and returns the square of x. We call the lambda function with 4 as an argument, and the result is 16

# When to use lambda functions 
# Lambda function are particularly useful in situations where you need a small fucntion for a short period and dont want to formally define a full function using def keyword. THey are commonly used with functions like map, filter and sorted.
# Example 3 Using lambda function with map
print("\n\nUsing lambda with map\n")
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers) # Here we use map to apply the lamda function to each element of the numbers list resulting in a new list of square numbers.

#let see 

# Example 4 
print("\n\nUsing lambda with filter\n")
numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))

print(even_numbers)
# In this example filter is used with a lambda funciton to create a new list containing only the even numbers from the original list.
# Lambda function provide a concise and convenient way to work with functions in python, especially in a situations where a short, one time fucntion is needed. However for more complex functions, its often clearer to use regular function definitions with def keyword. 

# Now calculate volume of a cube with def and lambda 
print("\n\nVolume of a cube with def and lambda \n")
def cube_volume_def(a):
    return a*a*a
print(f"The volume of a cube using the def function is: {cube_volume_def(3.14)}.")

# Lambda function
print(f"The volume of a cube using lambda function is: {(lambda a:a*a*a)(3.14)}.")

# Multiplication table 
print("\n\nMultiplication Table\n")
def mult_table(n):
    return lambda x: x*n
#n = int(input("Enter a number: "))
n = 12
y = mult_table(n)

print(f"The entered number is {n}")
for i in range (11):
    print(("%d x %d = %d" % (n, i, y(i))))
    
# LIst comprehension 
print("\n\nList Comprehension\n")
nums = [lambda a = a:a + 3.14 for a in range(5)]
nlis = []
for num in nums:
    nlis.append(num())
    
print(nlis)
# Lambda function with if else 
print("\n\nLambda function with if else  \n")
#name = (input("Enter Your name: "))
#age = int(input('Enter an age: '))
name = 'Sadiq Ali'
age = 22
print(f"The entered Name is: {name} \nThe entered age is: {age}")
(lambda age: print("Therefore, you can use a vote.") if (age>=18) else print("Therefore You do not use a vote. "))(age)
# Lambda function usage with multiple statements 
print("\n\nLambda function usage with multiple statements\n")
special_nums = [[0.577,1.618,2.718,3.14],[6,28,37,1729]]
special_nums_sorted = lambda a: (sorted(i) for i in a)
print(f"special_nums: {special_nums}\nspecial_nums_sorted: {special_nums_sorted}")
#Get the maximnum of special numbers in the list 
special_nums_max = lambda a, f:[y[len(y)-1]for y in f(a)]
print(f"The maximum of special numbers in each list is { special_nums_max(special_nums,special_nums_sorted)}")

# Lets get the minimum 
# Its Assignment for you guys 
# Get the second maximum of special mnumbers in the list 
special_nums_second_max = lambda a, f:[y[len(y)-2] for y in f(a)]
print(f"The second Max: {special_nums_second_max(special_nums,special_nums_sorted)}")
# Lets do some example 
print("\n\nExample\n")
def func(n):
    return lambda x: x*n
mult_pi_num = func(3.14)
mult_euler_constant = func(0.577)
print(f"The multiplication of euler number and pi number is equal to{mult_pi_num(2.718)}")
print(f"The multiplication of euler number and pi number is equal to{mult_euler_constant(2.718)}")
# Thank you soo much for watching this video 
# Bye Bye 
#please like and subscribe my channel and hit the bell ico for future update or notification
