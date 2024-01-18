print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 15 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m String Operators & Functions in Python\033[0m                                       ")
# In python string is a sequence of characters enclosed in single (') or double (") qoutes. Here how you can declare a string.
print("\n\nFor example\n")
my_string = "Helo, Python!"
print(my_string)
# String Concatenation
#You can combine or concatenate string using th "+" operator

greting = "Hello"
name = "Sadiq"
full_greeting = greting + ", " + name + "!"
print("After Greting",full_greeting)
#let see
#String Repetition:
# Actually you can repeat a string using the "*" operator
word = 'python '
repeated_word = word * 3
print( 'Repeated Word: ',repeated_word )

# String length 
# you can find the length of a string using the len() function
print("\n\nString length\n")
message = "python is fun!, Actually "
print("Message: ", message)
length = len(message)
print("length of a message: ",length)

print("\n\n String Indexing: \n")
# String indexing meaning you can access individual character using their position.
word = 'python'
first_char = word[0]
print("First character: ",first_char)

#String Slicing 
# You can extract a portion  of a string using slicing:
print("\n\nString Slicing\n")
word = "python"
substring = word[1:4]
print(word)
print("Substring:", substring)

# String Function 
#1. upper() and lower()
print("String function")
text = "Hello world"
uppercase_text = text.upper()
lowercase_text = text.lower()
print("Uppercase: ", uppercase_text)
print("Lowercase: ", lowercase_text)
#upper case : HELLO WORLD 
#lower Case: hello world

#2 strip()

# Remove leading and trailing whitespace 
print('\nStrip function\n')
user_input = '        Python       '
cleaned_input = user_input.strip()
print("cleaned input: ", cleaned_input)
# Output will be cleaned input :  python

# 3 Replace()
# Replace a substring with another 
sentence = ' I like python, and sadiq ali youtube channel:'
new_sentence = sentence.replace("sadiq", "the sadiq")
print("New Sentence: ", new_sentence)

# 4 Find()
# Find the index of a substring.
print("\n\nfind function\n")
sentence = "Python is easy to learn "
index = sentence.find("easy")
print("Index of 'easy': ", index)

# Let see

# 5 count()
# Counts occurences of a substring 

print("\n\nCount function\n")
sentence = "python is powerful, very powerful, and python easy. python is fun."
count_python = sentence.count("python")
print("Count of 'Python': ", count_python)
# output '3'

# Actully upper and lower case matter.

# 6 isalpha()
# It return True if all character in the string are alphabets 
# Whites are not considered as alphabets and thus it return False

txt = "Sadiq"
print("\n\nIsalpha function\n")
print(txt.isalpha())
txt = "Sadiq12345"
print(txt.isalpha())
txt = "Sadiq Ali!"
print(txt.isalpha())

# 7 isdecimal() function
# It returns if all the characters in the given string are decimal number 0-9
print("\n\n Isdecimal function\n")
txt = 'thesadiqali'
print(txt.isdecimal())
numbered_txt = '123456789'
print(numbered_txt.isdecimal())

# 8 isdigit()
# This function returns true if all the characters in the string and the unicode characters are digits.
print("\n\nIsdigit funciton\n")
numbered_txt = '123456789'
print(numbered_txt.isdigit())

# 9 isidentifier ()
print("\n\nIsidentifier function\n")
# It returns true if the string is valid identifier on the contrary False
numbered_txt = '123456789'
print(numbered_txt.isidentifier())
variable = 'numbered_txt'
print(variable.isidentifier())

# 10 Isprintable function
#It returns True if all the character in the string are printable feature 
print("\n\nIsprintable function: \n")
txt = "Hello, Sadiq"
print(txt.isprintable())
new_txt = 'Hello,\n Sadiq'
print(new_txt.isprintable())
space = ''
print(space.isprintable())

# isspace () function, islower() lower () function, isupper (), upper() functions,rjust() function, strip (), replace (), partition (), rfind(), rindex(), swapcase()
# Assignment for you guys 

# 11 join function
# It takes all items in an iterable and join them into one strin
# A string must be specified as the seperator.
print('\n\nJoin Function\n')
txt_list = ['Hello', 'Sadiq','Hi', 'Python']
print('#'.join(txt_list))

# 12 ljust function
# It retruns the left justified version of the certain string.
print("\n\nLjustfied Function\n")
txt = 'Sadiq'
txt = txt.ljust(30,'-')
print(txt, 'sadiq is my favorite YouTuber ')

#rjust() function
# It Retuns the right justfied version certain string 

# 13 Istrip 
# It remove the character from the left based on the argument (a string specified the set of the character to be removed)
print("\n\nIstrip Function\n")
txt = '     Hello Sadiq!'
print(txt.lstrip())

# 14 title() function
# This function converts the first character in the given string into upper case.
print("\n\nTitle() function\n")
txt = 'Hello Sadiq, Hi python!'
print(txt.title())

# Reverse String 
# The stride value is equal to -1 if a rever string is wanted to obtain 
print("\n\nReverse Function\n")
txt = "Hello Sadiq ali "
print(txt[::-1])

# in and Not in 
# in returns true when the character or word is in the given string, otherwise False. 
# not in returns False when character or word.

txt = 'Hello, Sadiq!'
print('H' in txt)
print('c' not in txt)


print("Thank you so much for watching this video ")
print("Please like and subscribe my channel")
# I will upload the code on my Github
# Bye Bye 

