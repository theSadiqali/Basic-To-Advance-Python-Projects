print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 14 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("\033[1;37;40m                                   #   thesadiqali channel   #\033[0m")
print("                                   # =====================   #")
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")

print("\033[1;31;40m                                   READING FILE IN PYTHON\033[0m")

# Reading Files in python
"""
To read a text file in python, you follow these steps.

1. First, open a text file for reading by using the open() function.
2. Second, read text from the text file using the file read(), readline, or readlines method of the file obejct.
3. Third, close the file using the file close method. this frees up resource and ensures consistency across different python versions.

open(<file>, <mode>)

"""

# Different Method we use
# 1. writeable() --> Returns weather the file can be written to or not.
# 2. readable() --> Returns weather the file steam can be read or not.
# 3. read() --> Returns the file content.
# 4. readline --> Returns a list of line from the file.
# 5. write() --> Writes the specified string to the file.
# 6. writeline() --> Writes a list of strings to the file.
# 7. close() --> Closes the file
# 8. flush() --> Flushes the internal buffer
# 9. seek() --> Change the file position.
# 10. tell() --> Returns the current file.
# 11. truncate --> Resizes the file to a specified.

#Open the file in read mode ( 'r' stands for read )
# Lets start from very basics
# Open in read mode

with open('sadiq.txt', 'r') as file:
    content = file.read()
    print(content)
    #This will print the entire content of the file to the console.
#lets do the reading line by line
#ANd Here we will be using loop

with open('sadiq.txt', 'r') as file:
    line = file.readline()
    for line in line:
        print(line.strip()) # strip() removes the new line characters

with open('sadiq.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()


print("\n\nREADING CERTAIN AMOUNT OF CHARACTER IN THE FILE\n")
with open('sadiq.txt', 'r') as file:
    print(file.read(10))
    print(file.read(20))
    print(file.read(30))
