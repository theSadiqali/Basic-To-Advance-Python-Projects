print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 13 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m                                   Built-in Function in Python\033[0m                                       ")
#Built in functions in python 
# Python has several functions that are readily availble for use. These functions are called built in functions. You can find more information about built in function on Google Or on my Github.
print("\n\n\033[1;31;40m A \033[0m\n")
print("\033[32mabs()\nall()\nany()\nascii()\033[0m")


print("\n\n\033[1;31;40m B \033[0m\n")
print("\033[32mbin()\nbool()\nbreakpoint()\nbytearray()\nbytes()\033[0m")

print("\n\n\033[1;31;40m C \033[0m\n")
print("\033[32mcallable()\nchr()\nclassmethod()\ncompile()\ncomplex()\033[0m")

print("\n\n\033[1;31;40m D \033[0m\n")
print("\033[32mdelattr()\ndict()\ndir()\ndivmod()\033[0m")

print("\n\n\033[1;31;40m E \033[0m\n")
print("\033[32menumerate()\neval()\nexec()\033[0m")

print("\n\n\033[1;31;40m F \033[0m\n")
print("\033[32mfilter()\nfloat()\nformat()\nfrozenset()\033[0m")

print("\n\n\033[1;31;40m G \033[0m\n")
print("\033[32mgetattr()\nglobals()\033[0m")

print("\n\n\033[1;31;40m H \033[0m\n")
print("\033[32mhasattr()\nhash()\nhelp()\nhex()\033[0m")

print("\n\n\033[1;31;40m I \033[0m\n")
print("\033[32mid()\ninput()\nint()\nisinstance()\nissubclass()\niter()\033[0m")

print("\n\n\033[1;31;40m L \033[0m\n")
print("\033[32mlen()\nlist()\nlocals()\033[0m")

print("\n\n\033[1;31;40m M \033[0m\n")
print("\033[32mmap()\nmax()\nmemoryview()\nmin()\033[0m")

print("\n\n\033[1;31;40m N \033[0m\n")
print("\033[32mnext()\033[0m")

print("\n\n\033[1;31;40m O \033[0m\n")
print("\033[32mobject()\noct()\nopen()\nord()\033[0m")

print("\n\n\033[1;31;40m P \033[0m\n")
print("\033[32mpow()\nprint()\nproperty()\033[0m")

print("\n\n\033[1;31;40m R \033[0m\n")
print("\033[32mrange()\nrepr()\nreversed()\nround()\033[0m")

print("\n\n\033[1;31;40m S \033[0m\n")
print("\033[32mset()\nsetattr()\nslice()\nsorted()\nstaticmethod()\nstr()\nsum()\nsuper()\033[0m")

print("\n\n\033[1;31;40m T \033[0m\n")
print("\033[32mtuple()\ntype()\033[0m")

print("\n\n\033[1;31;40m V \033[0m\n")
print("\033[32mvars()\033[0m")

print("\n\n\033[1;31;40m Z \033[0m\n")
print("\033[32mzip()\033[0m")

print("\n\n\033[1;31;40m _ \033[0m\n")
print("\033[32m__import__()\033[0m")


#I will upload these on my github 
# Dont woory for the code and built in function 

# I Will do some of them 
# The remaining. DO as Assignment 

#abs()
# Return the absolute value of a number.

print("\n\nabs()\n")

num1 = 2#int(input("Enter the number 1: "))
print("The entered number is", num1)
num2 = 3#float(input("Enter the number 2: "))
print("The entered number is", num2)
print("The absolute value of the first number is.", abs(num1))
print("The absolute number of the second number is ", abs(num2))
print("THe differnece between the two number is ", abs(num1-num2))

print("\n\nall()\n")
print("Return True if all elements in passes.\n")
nlis1 = [0.577,1.618,3.14,6.28,6,28,37,1729] #pick some random numbers
print(nlis1) 
print(all(nlis1))
nlis1.append(0) # Add 0 to the end of the list
print(nlis1,'Add 0 to the end of the list')
nlis1.append(False) # Add false to the end of the list

print(nlis1, 'Add false to the end of the list')
print(all(nlis1))

nlis1.clear()
print(nlis1, "Clear function")
print(all(nlis1))


#Bin()
# Returns the binary representation of a specified integer 
print("\n\nbin()\n")
num = 100
print(f"The entered number is: {num}")
print(f"The binary representation of {num} is {bin(num)}")

# 2. input()
#Purpose: Accepts input from the user through the console.


print("\n\nInput()\n")
inp = 1#int(input('Enter the Number:'))
print(inp)
print("Remve the Hash # and 1")

#len()
#Purpose: Returns the length (number of items) of an object.
print("\n\nLength Function\n")
lis = [1,2,3,4,5,6,7,8] # List . Random Numbers 
print("list: ",lis)
print(len(lis))

#bytes()
#Returns a btyes object 

print("\n\nbytes\n")
msg = 'Hello, Python!'
new_msg = bytes(msg, 'utf-8')
print(new_msg)


#char()
#It return a character from the specified Unicode code.
print("\n\nChr\n")
print(chr(1))
print(chr(2))
print(chr(3))
print(chr(4))
print(chr(66))

#Assignment . Pratice the remaining Built in function. 
# and I will also upload a complete code on my github 
# thesadiqali
#CHannel
#LIke and subscribe 

#Lets do one more 

#dict()
#It returns dictionary (Array)

print("\n\nDict()\n")
name = dict()
print(name)
dictionary = dict(euler_constant = 0.577, euler_number = 2.71, golden_ratio = 1.618)
print(dictionary)

#Its not necessary to practice everything every week but do it once in python.
#Once in a lifetime
#All of the built in function 
#thank you soo much for watching this video 
 
