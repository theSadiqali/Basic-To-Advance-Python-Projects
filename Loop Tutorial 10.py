print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 10 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("                                       TODAY TOPICS LOOPS")

#In Python, loops are used to repeatedly execute a block of code. There are two main types of loops in Python: for loops and while loops.
#For Loops:
#A for loop is used for iterating over a sequence (that is either a list, tuple, dictionary, set, or string).
print( "\n\n\033[1mLoop\033[0m")
print("\n\nFor Loop:\n")
names = "sadiq","ali","sadiq ali","thesadiqali"
print("Names:\n")
for name in names:
    print(f"Names: \033[1m{name}\033[0m")
fruits = "mango","orange","banana"
print("\nFruits: \n")
for fruit in fruits:
    print(f"fruits: \033[1m{fruit}\033[0m")
    
#numbers
print("\nNumbers:\n")
for i in range(1,20):
    print(f"Numbers counting from 1 to 20:\033[1m {i}\033[0m")


#Example 1:
#lets draw a traingle 
print("\n\nExample Triangle:")
height = 10
#As you know range function. it is helpful to think of the range object in ordered list. Actually the range function returns a sequence of numbers, starting from 1 to 10. 0 to .... 10. or by default, and the increment by 1 or by default and ends at aspecified number.
for i in range (1, height+1):
    print("*"*i)

#Checking the range Function
print("\n\nChecking the Range Function: ")
#lets take one more list
for i in range(-8,5):
    print(f"Range Function: \033[1m{i}\033[0m")

#While Loop
#Now lets Start While loop 
print("\n\nWhile Loop:\n")
#A while loop is used to repeatedly execute a block of code as long as a condition is true.

count = 1
while count <= 10:
    print(f"Count: \033[1m{count}\033[0m")
    count +=1 
    #Addition and calculation
#sometimes we use true or false. ( bolean ) 
#just like run until its get false or true 

#Nested Loop 
print("\n\nNested Loop\n")
print("\n\nExample 2\n ")
#num = int(input("Enter a number: "))
num = 10
print(f"The entered number is: {num}")
#Two ways. You can do this also i, j = 0,0
i = 0
j = 0
for i in range(0,num):
    print()
    for j in range(0, i+1): #nested 
        print("0",end='')

#now else and for statement 

print("\n\nFor - Else Statement: \n")

for i in range(1,10):
    print("\n",i,end='')
else:
    print("\nThese are numbers from 1 to 10.")
#continue statement in for loop
print("\n\nContinue Statement") #same as the above . but at the end we use continue
num2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in num2:
    if i ==11:
        continue  #It will jump here 
    print(i)
    #it will jump on 11 

#continue statement in for loop
print("\n\nBreak Statement") #same as the above . but at the end we use continue
num3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in num3:
    if i ==11:
        break  #It will break here 
    print(i)
    #it will break on 11 
    
#NOw we will do the While 
#While Else Statement
print("\n\nWhile Else Statement\n")
index = 0
while index <=5:
    print(index,end='') #Same as above
    index+=1
else:
    print("\nIt give us the between 0 and 5")
    
#Assignment:
#Practice Continue in while loop 
print("\n\nBreak in While loop\n")
i = 0
while i<=5:
    print(i)
    i+=1
    if i ==3:
        break
    #Just like that. Do the Continue While Loop

#I will upload a small basic project. 
#Thank you soo much for watching this video 
#Bye Bye
#Code on Github
#Thesadiqali channel Youtube
