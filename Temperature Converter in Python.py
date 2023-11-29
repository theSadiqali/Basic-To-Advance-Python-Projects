                                    #=========================#
                                    #     PYTHON PROJECTS     #
                                    #-------------------------#
                                    #        YOUTUBE          #
                                    #   thesadiqali channel   #
                                    #  ====================== # 
                                    #   PYTHON Tutorial       #
                                    #   BASIC TO ADVANCE      #
                                    #=========================#
                       # ============================================== #
                        #          Temperature Converter             #
                        #        1. Celsius to Fahrenheit            #
                        #        2. Celsius to Kelvin                #
                        #        3. Fahrenheit to Celsius            #
                        #        4. Fahrenheit to Kelvin             #
                        #        5. Kelvin to Celsius                #
                        #        6. Kelvin to Fahrenheit             #
                       # ============================================== #
                       
                       
#LETS DO THIS. ITS JUST A BASIC PYTHON PROJECT FOR YOU

#SIMPLE CONVERSION 
#let me tell you one things you can get all of these formulas from my github or google.
#First define celsius to ferhanite
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Second Celsius to Kelvin 
def celsius_to_kelvin(celsius):
    return celsius + 273.15

#Third Fahrenheit to Celsius 
def fahrenheit_to_celisuis(fahrenheit):
    return (fahrenheit - 32)* 5/9

#Fourth Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32)* 5/9 + 273.15

#Fifth Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

#Sixth Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32 #kelvin to fahrenhite

#Now lets define the main function 
def main():
    print("TEMPERATURE CONVERTER: \n")
    print("1. Celsius to Fahrenheit ")
    print("2. Celsius to Kelvin ")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin ")
    print("5. Kelvin to Celsius ")
    print("6. Kelvin to Fahrenheit ")
    #Now we are going to use choice of 6
    print("Choice from 1 to 6\n")
    choice = int(input("Enter your choice: "))
    if choice in range(1,7):
        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius)} ")
            
        elif choice == 2:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Kelvin: {celsius_to_kelvin(celsius)}")
        
        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {fahrenheit_to_celisuis(fahrenheit)}")
            
        elif choice == 4:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {fahrenheit_to_kelvin(fahrenheit)}")
            
        elif choice == 5:
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"Temperature in Celsius: {kelvin_to_celsius(kelvin)}")
            
        elif choice == 6:
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"Temperature in Celsius: {kelvin_to_fahrenheit(kelvin)}")
        else:
            print("Error: Try again OR invalid Choice")   
            #Here we go lets do this. 
            
            
            
if __name__ == "__main__":
    main()
#lets run the program 
#we will do the remaining the same way 
#thank you soo much for watching this video.
