print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 14 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m                                   Classes and Object in Python\033[0m                                       ")

# Python is an Object Oriented programming language.

# An object is simply a collection of data. 

# The def keyword in python, class definitions begin with a class keyword 

# The first string inside the class is called dostring and has a brief description of the class.

# Although not mandatory, this is highly recommended.

#Class
# A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class will have.

# Objects in Python
# Definition: An object is an instance of a class. It's a real-world entity that has  specific characteristics and behaviors defined by its class.
# Creating Objects: Objects are created by using the class name followed by parentheses ( ).
# Attributes: Objects have attributes (variables) that store information.
# Methods: Objects have methods (functions) that perform actions.

#Lets create a class 

print("\033[1m\n\nCreating a Class: \n\033[0m")
class Data:
    num = 3.14
print(Data)


print("\033[1m\n\nCreating an Object: \n\033[0m")

class Data:
    num = 3.14
var = Data()
print(var.num)

#Function init()
print("\033[1m\n\nFunction init(): \n\033[0m")

class Data:
    def __init__(self, euler_number, pi_number, golden_ratio):
        self.euler_number = euler_number
        self.pi_number = pi_number
        self.golden_ratio = golden_ratio
        
val = Data(2.718, 3.14, 1.618)

print(val.euler_number)
print(val.golden_ratio)
print(val.pi_number)
#lets see the output

#Methods 
print("\033[1m\n\nMethod: \n\033[0m")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False # Attribute to track if it is runing 
        
    def start_engine(self):
        self.is_running = True
        print(f"the {self.year} {self.make} {self.model}s engine is started.")
        
    def stop_engine(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} engine is stopped")
        
    def is_car_running(self):
        return self.is_running
    
# Creating an instance of the car class 

my_car = Car("Toyota", "Civic", 2024)

# Calling the methods of car class 

my_car.start_engine()
print("Is the car running?", my_car.is_car_running())

my_car.stop_engine()
print("Is the car running?", my_car.is_car_running())

#Self Parameter 

# The Self parameter is a reference to the current instance of the class, ad is used  to access variable that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
# check the following examples:

#Example:

print("\033[1m\n\nSelf parameter: \n\033[0m")

class Data:
    def __init__(classFirstParameter, euler_number, pi_number, golden_ratio):
        classFirstParameter.euler_number = euler_number
        classFirstParameter.pi_number = pi_number
        classFirstParameter.golden_ratio = golden_ratio
        
    def msg_function(classFirstParameter):
        print("The euler number is: ", classFirstParameter.euler_number)
        print("The golden ratio is: ", classFirstParameter.golden_ratio)
        print("The pi number is : ", classFirstParameter.pi_number)

val = Data(2.718,3.14,1.618)
val.msg_function()

#So Simple 

#Lets draw a Rectangle 

#But first let me teach you constructor first 

#IN python, a constructor is a special method within a class that is automatically called 
#When you create an object (instance) of that class. the constructor methos in python is named __init__().

#So Simple 

#the primary purposed of a constructor is to intiatilize (set up ) the attributes (properties) of an object when it is created.

#Example 
print("\033[1m\n\nSelf Contructor: \n\033[0m")

#lets consider a simple person class with attributes name and age. the __init__() method is used as the constructor to intialize these attributes when an object of the person class is created.

class Person:
    def __init__(self, name, age) :
        self.name = name 
        self.age = age
        
# Creating an instance of the person class (object).
person1 = Person("sadiq", 22)

#Accessing object attributes 
print("Name:", person1.name)
print("age:", person1.age)


#Now lets create or draw a rectangle
"""
#Rectangle
print("\033[1m\n\nDraw Rectangle: \n\033[0m")

class Rectangle(object):
    
    #constructor
    def __init__(self, width, height, color):
        self.width = width
        self.height = height 
        self.color = color
        
    #Method 
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc = self.color))
        plt.axis("scaled")
        plt.show()
        #We will import the library later 

import matplotlib.pyplot as plt
"""
#lets install matplotlib
#pip install matplotlib
#We will do this next time .
#Here we have a library issue right now.
#Lets check does it install 
#Because we are having error that its missing
#Its installed . I will try this later. 

print("\033[1m\n\nDraw Rectangle: \n\033[0m")
print('Please Remove the comment *** in code ')
"""
#Rectangle
import turtle 
class RectangleDrawer:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Drawing a Rectangle")
        self.screen.bgcolor("red")
        
        self.pen = turtle.Turtle()
        self.pen.color("white")
        self.pen.pensize(4)
        
    def draw_rectangle(self, length, width):
        for _ in range(2):
            self.pen.forward(length)
            self.pen.left(90)
            self.pen.forward(width)
            self.pen.left(90)
            
    def draw(self):
        self.draw_rectangle(100, 50) # Change the length and width 
        
    def close_window(self):
        self.screen.bye()
        
# Create an instance of rectangle drawer 

drawer = RectangleDrawer()

#Draw the rectangle
drawer.draw()

# Keep the window open until closed by the user 
drawer.screen.mainloop()
#I Will make a project in OOP soon 
# A small one 
"""

#Data Class 
print("\033[1m\n\nData Class: \n\033[0m")

"""

In python, the concept of data classes and inheritance(child classes) are two distinct 
but related concept. lets explore them with example 

Data class:
Data class in python are a feature introduced in python 3.7 via the dataclasses module.
They provide a convnient way to create classes primarily meant to store data. A data class automatically generates method like '__init__', __repr__ , __eq__ , etc
based on the class attributes

Here is the Example


"""
print("Example\n")

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
# Creating an instance of the point class 

p = Point(3,5)

# Accessing attributes 
print(f"Point cordinated: ({p.x}, {p.y})")


#Thats a data class simple example 

#Child Classes (Inheritance) in python:

print("\033[1m\n\nChild Class: \n\033[0m")

"""
CHild classes (also called subclasses) inherit attributes and methods from their parent class also called chile class. they can add new functionalities  or override existing methods of the parent class.


"""
#Example
print('Example')

class Animal:
    def sound(self):
        return "some generic sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"
# Creating instance of animal and dog classes 
animal = Animal()
dog = Dog()
# Lets Calling the sound methods of both classes 

print(animal.sound()) #output: "some generic sound"
print(dog.sound()) #output: Woof!

#this is the simple example of child class 
#FOr today that`s it 
# I will be making a tutorial. aimple project . in which we will be using super function and child classes and more . 
# For today thats it. 
# Thank you soo much for watching this video 
# please like an subscribe this channel 
# Thesadiqali     `