print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 20 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m Decorators in Python\033[0m  ")


# What are Decorators?
# In Python, a decorator is a special type of function that can be used to modify the behavior of another function. Decorators are often used to wrap or modify the functionality of functions without changing their source code directly.

# Decorator provide a simple syntax for calling higher order functions.
# A deorator in python is a function that takes another funciton as its argument, and returns yet another function.
# Decorator can be extremely useful as they allow the extension of an existing funciton, without any modification to the original function source code.
# In fact, there are two type of decorator in python including class decorator and function decorators. 
# In application, decorators are majorily used in creating middle layer in the backend, it performs task like. token authentication, validation, image compression, and many more.

# Creating a decorator:
# Lets create a simple decorator that adds extra functionality to a function:
print("\n\nCreating a decorator\n")
def my_decorator(func):
    def wrapper():
        print("Something is happening before the funciton is called")
        func()
        print("something is happeining after the function is called")
        
    return wrapper
    
@my_decorator
@my_decorator
@my_decorator
def say_hello():
    print("Hello!")
# Calling the decorated function

say_hello()
"""
@hello_decorator
def hi_decorator():
    print("hello")
    
    #Above the code is equal to 

def hi_decorator():
    print("hello")

hi_decorator = hello_decorator(hi_decorator)
"""
import decorator
from decorator import *
import functools
import math

# help(decorator) #Help on function decorator in module decorator

# Function
print("\n\nFunction\n")
def mytext(text):
    print(text)
mytext('Python is a programmin language.')
# In the following funciton, when the code was excuted, it yield the outputs for both functions. 
new_text = mytext
new_text("hello! Sadiq Ali")

print("\n\nMultiplication")

def multiplication(num):
    return num * num
mult = multiplication 

new = mult(3.14)
print(new) # We got that

# Nested\Inner Function
print("\n\nNested\Inner Function")
def mytext():
    print("python is a programming language.")
    def new_text():
        print("Hello, Python!")
    def message():
        print("Hi, Sadiq!")
    new_text()
    message()
mytext()
# In the following function, it is non significant how the child functions are announced. 
# The implementation of the child function does influence on the output.
# These child functions are topically linked with the function mytext(),  Terefore they can be called indivitually.

print("\n\nAddition\n")
def addition(num):
    return num + math.pi
def called_function(func):
    added_number = math.e
    return func(added_number)
print(called_function(addition))

# Functions reverting other functions
print("\n\nFunctions reverting other functions\n")
def msg_func():
    def text():
        return "Python is a programming language!"
    return text
msg = msg_func()
print(msg())

# Define a decorating function
print("\n\nDefine a decorating function\n")
def addition(a,b):
    print(a+b)
def outer_addition(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

Result = outer_addition(addition)
Result(math.pi,math.e)
# In the following example, the function outer_addition that is some voluminous is decorated.

# Rather than above function, python ensures to employ decorator in easy way with the symbol @ called  pie syntax
print("\n\nDecorated\n")
def outer_addition(function):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return function(a,b)
    return inner
@outer_addition #syntax of decorator
def addition(a,b):
    print(a+b)
Result = outer_addition(addition)
Result(math.pi,math.e)

# Reprocessing decorator
# The decorator can be reused by calling that decorator function.

print("\n\nReprocessing decorator\n")

def do_twice(function):
    def wrapper_do_twice():
        function()
        function()
    return wrapper_do_twice

@do_twice
def text():
    print("Python is a programming language.")
text()

# Decorators with Arguments

print("\n\nDecorator with Argument\n")
def do_twice_function(function):
    def wrapper_function(*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper_function
# The function wrapper_function() can admit any number of argument and pass them on the function.
@do_twice_function
def text(programming_language):
    print(f"{programming_language} is a programming language.")
text('Python')

        
    
# Fancy decorators
# @propertymethod
# @staticmethod
# @classmethod
print("\n\nFancy decorator\n")
class Microorganism:
    def __init__(self, name, product) :
        self.name = product
        self.product = product
    @property
    def show(self):
        return self.name + 'produces'+ self.product + 'enzyme'

organism = Microorganism('Aspeergillus niger', 'inulinase')
print(f"Microorgainsm name: {organism.name}")
print(f"Microorganism product: {organism.product}")
print(f"Message: {organism.show}")

# Multiple decorators

def decorator_text_uppercase(func):
    def wrapper():
        function = func()
        text_uppercase = function.upper()
        return text_uppercase
    return wrapper

# using a function
print("\n\nUsing a function\n")
def text():
    return 'Python is the most popular programming language.'

decorate_result = decorator_text_uppercase(text)
print(decorate_result)
# Using a decorator 
@decorator_text_uppercase
def text():
    return 'Python is the most popular programming language.'
print(text())


print("\n\nmultiple\n")
def splitted_text(text):
    def wrapper():
        function = text()
        text_splitting = function.split()
        return text_splitting
    
    return wrapper

@splitted_text
@decorator_text_uppercase #Calling the other decorator 
def text():
    return 'python is the most popular language.'
print(text())

# Arbitrary Arguments
print("\n\nArbitrary Arguments\n")
def arbitrary_argument(func):
    def wrapper(*args, **kwargs):
        print(f"These are positional arguments {args}")
        print(f"These are keyword arguments {kwargs}")
        func(*args)
    return wrapper
# 1 Without arguments decorator
print(__doc__)
@arbitrary_argument
def without_argument():
    print("There is no argument in this decorator. ")

without_argument()
# 2 With positional arguments decorator
print(__doc__)
@arbitrary_argument
def with_position_argument(x1,x2,x3,x4,x5,x6):
    print(x1,x2,x3,x4,x5,x6)
with_position_argument(math.inf,math.tau,math.pi,math.e,math.nan,-math.inf)
# Now let see
print(__doc__)
@arbitrary_argument
# 3 With keyword argument decorator
def with_keyword_argument():
    print("Python and R are my favorite programming languages and keyword arguments.")
with_keyword_argument(language_1 = "python", language_2 = "R")

# Preserving decorators 
print('\n\nPresering Decorator\n')
def preserved_decorator(function):
    def wrapper():
        print("Before calling the function, this is printed.")
        function()
        print("After calling the funciton, this is printed")
    return wrapper

@preserved_decorator
def message():
    #This function prints the msg when its called
    print("Python is the most popular programming language")

message()
print(message.__name__)
print(message.__doc__)
print(message.__class__)
"""
print(message.__module__)
print(message.__code__)
print(message.__closure__)
print(message.__annotions__)
print(message.__dir__)
print(message.__format__)
#AttributeError: 'function' object has no attribute '
    
    """
    
# I think thats it for today, I will upload a code on my github 
# Thank you soo much for watching this video . 
# Next tutorial all about Generator in python 
# please like and subscribe my channel.
# BYE BYE 
