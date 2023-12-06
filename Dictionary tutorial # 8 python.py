                                    #=========================#
                                    #    PYTHON Tutorial # 8  #
                                    #-------------------------#
                                    #        YOUTUBE          #
                                    #   thesadiqali channel   #
                                    #  ====================== # 
                                    #   PYTHON Tutorial       #
                                    #   BASIC TO ADVANCE      #
                                    #=========================#
#TODAY TOPIC Dictionaries 
#In Python, a dictionary is a built-in data type that represents a collection of key-value pairs. It is also sometimes referred to as an associative array, map, or hash map in other programming languages.

#1 Dictionaries are used to store data values in key value pairs.
#2 A dictionaries is a collection which is ordered. changeble or mutable and do not allow dublicates.
#3 Dictionaries items are ordered, changeble, and does not allow dublicates.
#4 Dictionaries are changeble, meaning that we can change, add or remove items after the dictionary has been created.
#5 Dictionaries cannot have two items with the same key.
#6 A dictionary can nested and can contain another dictionary.

#just like keys and values 
#          'Name'   'Bob'
#          'age'    '22'
#          'job'    'Python Developer'

#JUST LIKE THAT

#Take a sample dictionary
#let me take a simple example for better understanding 
print("DICTIONARY\n")
student = {
    "name": "Sadiq",
    "age": "22",
    "grade": "A",
    "courses": ["Math", "Python", "Statistics", "Intro_AI"]
}

#Now Accessing values
print("Name: ", student["name"])
print("Age: ", student["age"])
print("Grade: ", student["grade"])
print("Courses:", student["courses"])

#modifying values are 
student["age"] = 23
student["courses"].append("History of computer")

#Adding a new key value pair
student["gpa"] = 3.9

#Iterating through key value pairs

print("\n All information:")
for key, value in student.items():
    print(f"{key}:  {value}")
#Don`t worry about for loop. i will teach u that later. 

#Note: As you see that the whole dictionary is enclosed in curly braces {}, each key key is separated from its value by a column ":" and commas are used to separated the items in the dictionary.

#LETS TALK ABOUT KEY FUNCTION

print("\n\nKEY FUNCTION \n")
print(student.keys())

#Value function
print("\n\nVALUE FUNCTION\n")
print(student.values())

#Del function
print("\n\nDELET_E FUNCTION\n")
#del(student)  # NameError: name 'student' is not defined 
#Because student is not defined
#print("After deleting it :", student)


#Verification using is or not in
print("\n\nVerification using is OR is in")
print("courses" in student)
#As you see
print("john " not in student)

#practice 
#Assignement: practice copy function, pop function and pop items function 
#Get function

print("\n\nGET FUNCTION")
print(student.get("courses"))

#iterating dictionary 
#A dictionary can be iterated using the for loop 
print("\n\nIteration \n")
for key in student:
    print(key)
    
#thats it 
#thank you soo much for watching this video. please like and subscribe the channel.
#i will upload a short basic project . related to dictionary 
#after this video 
#NEXT TOPIC CONDITIONS 
#TUTORIAL # 9
