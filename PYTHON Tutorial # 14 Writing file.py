print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 14 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("\033[1;37;40m                                   #   thesadiqali channel   #\033[0m")
print("                                   # =====================   #")
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")

print("\033[1;31;40m                                   WRITING FILE IN PYTHON\033[0m")

#Writing file in python 
# To write a text file in python, follow these steps 
# First open the text file for writing ( or appending ) using the open() function.
# Second, Write to the text file using the write() or writelines() method.
# Third close the file using the close() method. 
#*******************************************************
# I will be working on pycharm 
# Only for Write and Read file tutorials.
# TO START, WE USE THE OPEN() FUNCTION TO OPEN A FILE. ITS LIKE OPENING A BOOK YOU WRITE
# BEFORE YOU WRITING SOMETHING IN IT.
# OPEN A FILE IN WRITE MODE
# Open a file in write mode
with open('example2.txt','w') as file:
    file.write("Hello! sadiq ali\n")
    file.write("Hello! thesadiqali\n")
    file.write("Hello! YouTube Channel")

print("Content has been written in file example2")
# I will upload a small project on reading
# Writing file on my channel
# I will upload the code on my Github



