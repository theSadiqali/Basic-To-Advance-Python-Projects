print("                                   #=========================#")
print("                                   #    PYTHON Tutorial # 18 #")
print("                                   #-------------------------#")
print("                                   #        YOUTUBE          #")
print("                                   #   thesadiqali channel   #")
print("                                   # =====================   #") 
print("                                   #   PYTHON Tutorial       #")
print("                                   #   BASIC TO ADVANCE      #")
print("                                   #=========================#")
                                    
print("\033[1;31;40m Math Module Functions in Python\033[0m  ")
# Python math module is defined as the most famous mathematical function, which includes trignometry functions, representation functions, logarthamic functions etc
# Furthermore it also defines two mathematical constants i.e Pie and Euler number etc 
# Introduction to the Math Module:
# The math module in Python provides a set of mathematical functions for performing various mathematical operations. To use these functions, you need to import the math module.
import math
# Once imported, you can access various mathematical functions availble in the module.
# Example 1 Basic Arithematic Operations 
print("\n\nExample 1 Basic Arithematic Operations \n")
# Additions
print("Additions: ",math.fsum([1,2]),"Subtraction: ",math.prod([2,3]))
#help(math) # It will give you more infor about math

# acos() fucntion
# Return the arc cosine (measured in radians) of x
# The result is between 0 and pi
# The parameter must be a double value between -1 and 1.
print ("\n\nAcos function\n")
nlis = []
nlis.append(math.acos(1))
nlis.append(math.acos(-1))
print(nlis)

# acosh() Function
# It is a built in method defined under the math module to calculate the hyperbolic arc cosine of the given parameter in radians.
# For example, if x is passed as an acosh function (acosh(x)) parameter, it returns the hyperbolic arc consine value 
print("\n\nacosh() function: ", math.acosh(1729))

print("asin() function: ",math.asin(1)) # It return the arc sine (measureed in radins) of x.
# THe result is between -pi/2 and pi/2

print("asih() function: ", math.asinh(1729)) # Actually its return inverse hyperbolic sine of x.

print("atan() function: ", "positive infinite: ",math.atan(math.inf),"Negative infinite: ",math.atan(math.inf))
# Return the arc tangent ( measured in radins ) of x
# THe result is between -pi/2 and pi/2 

print("atan2() function: ",math.atan2(1729,37)," ",math.atan2(1729,-37))
# Return the arc tangent (measured in radians) of y/x
# unlike atan (y/x) the sign of both x and y are considered .

# atanh() function
print("atanh() function: ",math.atanh(-0.9999)," ",math.atanh(0))
# Return the inverse hyperbolic tangent of x.

# ceil() function
print(f"ceil() Function: \nThe nearest integer greater then pi number is {math.ceil(math.pi)}  ") # pi 3.14

# Comb() Function
# Number of ways to chose k items from n item without repition and without order.
# Evalutes to n!(k!*(n-k)!) when k<=n and evalutes to zero when k>n.
# Also called the binomial coefficient because it is equivalent to the coeffiencient of k-th term in polynimial expansion of the expression (1+x)**n.
# Raises Type Error if either of the arguments are not integers. 
# Raises Value Error if either of the arguments are negative.

print("\n\ncomb() Function\n")
print(f"The combination of 6 with 2 is {math.comb(6,2)}")
# lets do that with pi number
#print(f"The combination of 6 with pi is {math.comb(6,3.14)}") # Type Error

# copysign() function

print("\n\ncopy() Function\n")
# Return the float of the vlaue of the first parameter and the sign of the second parameter.
print(f"The copysign of these two numbers 3.14 adn 2.718 is: {math.copysign(-3.14,2.718)}")

# cos() Function
# Return the cosine function of x (measured in radians)
print("\ncos() function: cos(0)",math.cos(90))

# cosh() Function
# Return the hyperbolic cosine of x
print("\ncosh() function: cos(0)",math.cosh(1))

# degrees() function
print("\ndegree() function: pi/2: ",math.degrees(math.pi/2))

# dist() fucntion
# Return the Eulidean distance between two opints p and q.
# Hint Both input must have the same dimension.
# The points should be specified as sequence (or iterables ) of cordinates.
print("\ndist() Function: dist 30 and 60: \n",math.dist([30],[60]),"\n", math.dist([0.577,1.618],[3.14,2.718]))
x = [0.577,1.618,2.718]
y = [6,28,37]
print(math.dist(x,y))

# erf() Function
# Error function at x 
# This method accepts a value between - inf and + inf and return a value between -1 and +1 
nlis = []
print("\n\nerf() Function\n")
nlis.append(math.erf(math.inf))
nlis.append(math.erf(math.pi))
nlis.append(math.erf(math.e))
nlis.append(math.erf(math.tau))
nlis.append(math.erf(0))
nlis.append(math.erf(6))
nlis.append(math.erf(1.618))
nlis.append(math.erf(0.577))
nlis.append(math.erf(-math.inf))
print(nlis)

# erfc() function
# Copmlementary function at x. 
# This methof accepts a value between -inf and +inf and returns a vlaue between 0 and 2.
nlis = []
print("\n\nerfc() Function\n")
nlis.append(math.erfc(math.inf))
nlis.append(math.erfc(math.pi))
nlis.append(math.erfc(math.e))
nlis.append(math.erfc(math.tau))
nlis.append(math.erfc(0))
nlis.append(math.erfc(6))
nlis.append(math.erfc(1.618))
nlis.append(math.erfc(0.577))
nlis.append(math.erfc(-math.inf))
print(nlis)

# exp() Function 
# The math.exp() method returns # raised to the power of x (Ex).
# E is the base of the natural system of logarithams (approximately 2.718282) and x is the number passed to it.
nlis = []
print("\n\nexp() Function\n")
nlis.append(math.exp(math.inf))
nlis.append(math.exp(math.pi))
nlis.append(math.exp(math.e))
nlis.append(math.exp(math.tau))
nlis.append(math.exp(0))
nlis.append(math.exp(6))
nlis.append(math.exp(1.618))
nlis.append(math.exp(0.577))
nlis.append(math.exp(-math.inf))
print(nlis)

# expm1() function 
# Return exp(x)-1
# This fucntion avoids the loss of precsion involved in the direct evaluation of exp(x)-1 for small x.
nlis = []
print("\n\nexpm1() Function\n")
nlis.append(math.expm1(math.inf))
nlis.append(math.expm1(math.pi))
nlis.append(math.expm1(math.e))
nlis.append(math.expm1(math.tau))
nlis.append(math.expm1(0))
nlis.append(math.expm1(6))
nlis.append(math.expm1(1.618))
nlis.append(math.expm1(0.577))
nlis.append(math.expm1(-math.inf))
print(nlis)

# fabs() Function
# Returns the absolute value of a number
print(f"\nfabs() function: The absolute value of a number -1.618 is {math.fabs(-1.618)}")

# factorial function
# Retrun th factorial value of a number
print('\nfactorial() fucntion: factorial of 6: ', math.factorial(6))
# ValueError: factorial() not defined for negative values

# floor functions:
# Round a number down to the nearest integer.
print("\nfloor() function: of 3.14: ", math.floor(3.14))

# fmod() functions:
# Return th remainder of x/y
print(f"\nfmod() function: of 37,6: {math.fmod(37,6)}")

# frexp() function
# Returns the mantissa and the exponent, of a specified number.
print(f"\nfrexp: of 2.718: {math.frexp(2.718)}")

# fsum function
# Return the sum of all items in any iterable ( tuples, arrays, lists, etc. )
num = [1,2,3,4]
print(f"\nfsum() function: 1,2,3,4: {math.fsum(num)}")

# gamma() function
# Returns the gamma fucntion at x. 
# you can find more informaiton on wikipedia.
# link: https://en.wikipedia.org/wiki/Gamma_function

print(f"\ngamma() function: of 3.14: {math.gamma(3.14)}")

# gcd() function 
# Return the greatest common divisor of two integer 
print(f"\ngcd() function: of 3,10: {math.gcd(3,10)}")

# hypot() function 
# Return the Euclidean norm
# Multidimensional Euclidean distance from the origin to a point.
# Roughly equivalent to sqrt(sum(x**2 for x in cordinates))
# For a two dimesional point (x,y), gives the hypotenuse using the pythagorean theorem sqrt(xx+yy).
print(f"\nhypot() function: of 3,4: {math.hypot(3,4)}")

# isclose function
# It check whether two values are close to each other, or not.
# Returns True if the values are close, otherwise False.
# This method uses a relative or absolute tolerance, to see if the values are close.
# Tip: It uses the following formula to compare the values: abs(a-b) <=max(rel_to * max(abs(a),abs(b)))
print(f"\nisclose() function: of pi and tau: {math.isclose(math.pi, math.tau)}")
print("math.isclose(3.14,3.1400000000000001): ",math.isclose(3.14,3.1400000000000001))

# isfinite() function 
# Return true if x is neither an infinty nor a NaN, and False otherwise.
print("\n\nisfinite() Function\n")
nlis = []

nlis.append(math.isfinite(math.inf))
nlis.append(math.isfinite(math.pi))
nlis.append(math.isfinite(math.e))
nlis.append(math.isfinite(math.tau))
nlis.append(math.isfinite(0))
nlis.append(math.isfinite(6))
nlis.append(math.isfinite(1.618))
nlis.append(math.isfinite(0.577))
nlis.append(math.isfinite(-math.inf))
print(nlis)

# isinf() function
# Return True if x is a positive or negative infinity, and false otherwise ,

print("\n\nisinf() Function\n")
nlis = []

nlis.append(math.isinf(math.inf))
nlis.append(math.isinf(math.pi))
nlis.append(math.isinf(math.e))
nlis.append(math.isinf(math.tau))
nlis.append(math.isinf(0))
nlis.append(math.isinf(6))
nlis.append(math.isinf(1.618))
nlis.append(math.isinf(0.577))
nlis.append(math.isinf(-math.inf))
print(nlis)

# isnan() function
# Return True if x is a Nan(not a number), and False other
print("\n\nisnan() Function\n")
nlis = []

nlis.append(math.isnan(float('NaN')))
nlis.append(math.isnan(math.inf))
nlis.append(math.isnan(math.pi))
nlis.append(math.isnan(math.e))
nlis.append(math.isnan(math.tau))
nlis.append(math.isnan(0))
nlis.append(math.isnan(6))
nlis.append(math.isnan(1.618))
nlis.append(math.isnan(0.577))
nlis.append(math.isnan(-math.inf))
print(nlis)

# isqrt() function
# Rounds a square root number downwards to the neares integer.\
print(f"\nisqrt() function: of 4: {math.isqrt(4)}")
# ValueError: isqrt() argument must be nonnegative

# lcm() function
# least common multiple
print(f"\nlcm() function: of (3,5,25): {math.lcm(3,5,25)}")

# ldexp() function
# Returns the inverse of math.frexp() which is x(2poweri) of the given numbers x and i.
print(f"\nldexp() function: 20,4: {math.ldexp(20,4)}")

# lgamma function
# Returns the log gamma value of x 
print(f"\ngamma() function of 6: {math.gamma(6)} and lgamma() function of 6: {math.lgamma(6)} and log() function of 120 of {math.log(120)}")

# Log return the logarithm of x to the given base  log(x, [base=math.e])

# log10() function
# Return the base 10 logarithm of x
print(f"\nlog10() function: of 90: {math.log10(90)} and log1p() function of 90: {math.log1p(90)} and log2() fucntion of 90 {math.log2(90)}")
# Log1p return the natural logarithm of 1+x (base e)

# log2() retrun the base 2 logartihm of x 

# Modf() function
# It return the fractional and integer parts of the certain number. Both the outputs carry the sign of x and are of type float.
print(f"\nmod() funciton of pi: {math.modf(math.pi)}")

# nextafter() function
# return the next floating point value after x towards y.
# if x is equal to y then y is returned.
print(f"\nnextafter() function: of 3.14 and 90 is {math.nextafter(3.14,90)}")

# perm() function 
# Return the number if ways to chose k items from n items with order and without repitition.
print(f"\nperm() function of 6,2 is {math.perm(6,2)} \n\n pow() function of 10,2 is: {math.pow(10,2)}")

# pow() fucntion return the value of x to the power of y


# radians() function 
# convert angle x from degrees to the radians
print(f"\nradians of 180 is {math.radians(180)}")

# remainder() function 
# Difference between x and the closest integer multiple of y.
# Return x -ny where ny is the closest integer multiple of y.
# Return in the case where x is exactly halfway between two multiples of y, the neearest even value of n is issued of n is used. The result is always exact.
print(f"\nremainder of 3.14,2.718 withremainder() function: {math.remainder(3.14,2.718)}")

# sin() function
# Return the sine of x ( measured in radins ).
# Note: To find the sine of degrees, it must first be converted into radins with the math.radins() method.
print(f"\npi with sin() fucntion: {math.sin(math.pi)} \n\nsinh() function of pi: {math.sinh(math.pi)}")
# sinh() it return the hyperbolic sine of x.

# sqrt() function
# Return the square root of x.
print(f"\nsqrt() function: of pi: {math.sqrt(math.pi)}")

# tan() function # return the tangent of x (measured in radians).
print(f"\ntan() function: of 0: {math.tan(0)}\n\ntanh() function of 0: {math.tanh(0)}")
# tanh() Return the hyperbolic tangent of x

# trunc() function
# Truncates the Real x to the nearest integeral toward 0.
# Returns the truncated integer parts of different numbers.
print(f"\ntrunc() function of 0: {math.trunc(0)}")

# ulp() function 
# Return the values of the least significant bit of the float x.
import sys 

print("\n\nulp() Function\n")
nlis = []

nlis.append(math.ulp(-5))
nlis.append(math.ulp(math.inf))
nlis.append(math.ulp(math.pi))
nlis.append(math.ulp(math.e))
nlis.append(math.ulp(math.tau))
nlis.append(math.ulp(0))
nlis.append(math.ulp(6))
nlis.append(math.ulp(1.618))
nlis.append(math.ulp(0.577))
nlis.append(math.ulp(-math.inf))
print(nlis)

# Thank you soo much for watching this video. I will upload some project regarding this topic. 
# Next topic will be list comprehesion in python 
# Most importantly you can download the code from Github
# YouTube thesadiqali 
# Github link in the discription 
# please like and subscribe my channel . BYE BYE 